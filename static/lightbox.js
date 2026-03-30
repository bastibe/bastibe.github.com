let isDragging = false;
let wasDragged = false;
let touchCoordinate = [];
let lightboxTime = undefined;


document.addEventListener('keyup', e => {
    let lightboxImage = document.querySelector('figure.lightbox img.lightbox');
    if (e.key === 'Escape' && lightboxImage) {
        let figure = lightboxImage.parentNode;
        exitLightbox(figure, lightboxImage);
    }
});


function lightboxFigureClickCallback(event) {
    // if the browser issues both click and touch events, ignore
    // the later one:
    if (event.timeStamp - lightboxTime < 300) {
        return;
    }
    lightboxTime = event.timeStamp;

    let figure = event.target;

    event.stopImmediatePropagation();
    if (figure.classList.contains('lightbox')) {
        // don't exit if we came here from a drag
        if (wasDragged === true) {
            wasDragged = false;
            return;
        }
        exitLightbox(figure);
    }
}

function lightboxImgClickCallback(event) {
    // if the browser issues both click and touch events, ignore
    // the later one:
    if (event.timeStamp - lightboxTime < 300) {
        return;
    }
    lightboxTime = event.timeStamp;

    let image = event.target;
    let figure = image.parentNode;

    event.stopImmediatePropagation();
    if (figure.classList.contains('lightbox')) {
        // don't exit if we came here from a drag
        if (wasDragged === true) {
            wasDragged = false;
            return;
        }
    } else {
        // reset dragging state
        wasDragged = false;
        enterLightbox(figure, image);
    }
}


function enterLightbox(figure, image) {
    // save all image state
    for (let img of figure.getElementsByTagName('img')) {
      img.originalStyleWidth = img.style['width'];
      img.originalStyleHeight = img.style['height'];
      img.originalWidth = img.width;
      img.originalHeight = img.height;
      if (img != image) {
        img.style['visibility'] = 'hidden';
      }
    }
    // fix body in place so it doesn't scroll when the lightbox is
    // moved by touch
    document.body.style['top'] = `${-window.scrollY}px`;
    document.body.style['width'] = `${window.innerWidth}px`;
    document.body.style['position'] = 'fixed';
    // add fake figure as a placeholder while lightbox is showing to
    // prevent relayout
    let fakeFig = document.createElement('figure');
    fakeFig.id = 'fakefig';
    fakeFig.style['width'] = `${figure.offsetWidth}px`;
    fakeFig.style['height'] = `${figure.offsetHeight}px`;
    fakeFig.style['background-color'] = '#c0c0c0';
    fakeFig.style['opacity'] = 0.5;
    fakeFig.style['position'] = figure.style['position'];
    fakeFig.style['float'] = figure.style['float'];
    fakeFig.style['display'] = figure.style['display'];
    figure.parentNode.insertBefore(fakeFig, figure);
    // activate lightbox
    figure.classList.add('lightbox');
    figure.originalWide = figure.classList.contains('wide-figure');
    figure.classList.remove('wide-figure');
    image.classList.add('lightbox');
    let aspectRatio = image.naturalWidth / image.naturalHeight;
    let screenAspectRatio = window.innerWidth / window.innerHeight;
    if (aspectRatio > screenAspectRatio) {
      image.style['width'] = `${window.innerWidth*0.9}px`;
      image.style['height'] = `${window.innerWidth*0.9/aspectRatio}px`;
    } else {
      image.style['height'] = `${window.innerHeight*0.9}px`;
      image.style['width'] = `${window.innerHeight*0.9*aspectRatio}px`;
    }
    image.style['max-width'] = 'none';
    image.style['max-height'] = 'none';
    image.setAttribute('draggable', false);
    image.addEventListener('wheel', lightboxScrollCallback);
    image.addEventListener('mousedown', lightboxMouseDownCallback);
    image.addEventListener('mousemove', lightboxMouseMoveCallback);
    image.addEventListener('mouseup', lightboxMouseUpCallback);
    // replace thumbnail with full-resolution image (if necessary):
    if (image.src.includes('thumb')) {
        image.src = image.src.replace('thumb.', '');
        // reposition to center once image is loaded (it will move
        // because its size changes)
        image.onload = e => {
            image.style['left'] = `${(window.innerWidth-image.offsetWidth)/2}px`;
            image.style['top'] = `${(window.innerHeight-image.offsetHeight)/2}px`;
            image.onload = undefined;
        }
    }
    // set initial image position to center:
    image.style['left'] = `${(window.innerWidth-image.offsetWidth)/2}px`;
    image.style['top'] = `${(window.innerHeight-image.offsetHeight)/2}px`;
    // hide all other images in this figure:
    for (let otherImage of figure.querySelectorAll('img:not(.lightbox)')) {
        otherImage.style['visibility'] = 'hidden';
    }
}


function exitLightbox(figure) {
    // release body
    let scrollY = parseInt(document.body.style['top']);
    document.body.style['top'] = '';
    document.body.style['position'] = '';
    document.body.style['width'] = '';
    window.scrollTo(0, -scrollY);
    // remove fake figure
    let fakeFig = document.getElementById('fakefig');
    fakeFig.remove();
    // disable lightbox
    figure.classList.remove('lightbox');
    if (figure.originalWide) {
      figure.classList.add('wide-figure');
    }
    // reset images
    for (let img of figure.getElementsByTagName('img')) {
        img.classList.remove('lightbox');
        img.style['top'] = '';
        img.style['left'] = '';
        img.style['width'] = img.originalStyleWidth;
        img.style['height'] = img.originalStyleHeight;
        img.width = img.originalWidth;
        img.height = img.originalHeight;
        img.style['visibility'] = '';
        img.removeEventListener('wheel', lightboxScrollCallback);
        img.removeEventListener('mousedown', lightboxMouseDownCallback);
        img.removeEventListener('mousemove', lightboxMouseMoveCallback);
        img.removeEventListener('mouseup', lightboxMouseUpCallback);
        img.setAttribute('draggable', true);
    }
}

function lightboxMouseDownCallback(event) {
    isDragging = true;
}

function lightboxMouseMoveCallback(event) {
    if (isDragging === true) {
        let image = event.target;
        image.style['left'] = `${image.offsetLeft + event.movementX}px`;
        image.style['top'] = `${image.offsetTop + event.movementY}px`;
        moveImageIntoBorders(image);
        // prevent closing of figure:
        if (event.movementX != 0 || event.movementY != 0) {
            wasDragged = true;
        }
    }
}


function lightboxMouseUpCallback(event) {
    isDragging = false;
}


function lightboxScrollCallback(event) {
    let image = event.target;
    let imageRect = image.getBoundingClientRect();

    // remember relative cursor position on image, for later:
    let imageX = (event.clientX - imageRect.left) / imageRect.width;
    let imageY = (event.clientY - imageRect.top) / imageRect.height;

    // zoom:
    let zoomFactor = 1.0 + event.wheelDeltaY / 360;
    let newImageWidth = imageRect.width * zoomFactor;
    let newImageHeight = imageRect.height * zoomFactor;

    // limit zoom in to 400% pixel size:
    if (newImageWidth > image.naturalWidth * 4) {
      newImageWidth = image.naturalWidth * 4;
      newImageHeight = image.naturalHeight * 4;
    }
    // limit zoom out to 10% screen width:
    let aspectRatio = newImageWidth / newImageHeight;
    if (newImageWidth < window.innerWidth * 0.1) {
      newImageWidth = window.innerWidth * 0.1;
      newImageHeight = newImageWidth / aspectRatio;
    } else if (newImageHeight < window.innerHeight * 0.1) {
      newImageHeight = window.innerHeight * 0.1;
      newImageWidth = newImageHeight * aspectRatio;
    }

    image.style['width'] = `${newImageWidth}px`;
    image.style['height'] = `${newImageHeight}px`;

    // pan so the image does not move under cursor:
    let newImageRect = image.getBoundingClientRect();
    let newPositionX = -imageX*newImageRect.width + event.clientX;
    let newPositionY = -imageY*newImageRect.height + event.clientY;
    image.style['left'] = `${newPositionX}px`;
    image.style['top'] = `${newPositionY}px`;

    moveImageIntoBorders(image);

    // do not scroll background
    event.preventDefault();
}


function moveImageIntoBorders(image) {
    // make sure the image stays within the viewport borders:
    imageRect = image.getBoundingClientRect(); // refresh to new coordinates
    if (imageRect.width <= window.innerWidth*0.9) {
        // image fits into figure: prevent edges from leaving figure
        if (imageRect.left < window.innerWidth*0.05) {
            image.style['left'] = `${window.innerWidth*0.05}px`;
        } else if (imageRect.right > window.innerWidth*0.95) {
            image.style['left'] = `${window.innerWidth*0.95-imageRect.width}px`;
        }
    } else {
        // image too big for figure: prevent edges from entering figure
        if (imageRect.left > window.innerWidth*0.05) {
            image.style['left'] = `${window.innerWidth*0.05}px`;
        } else if (imageRect.right < window.innerWidth*0.95) {
            image.style['left'] = `${window.innerWidth*0.95-imageRect.width}px`;
        }
    }
    if (imageRect.height <= window.innerHeight*0.9) {
        // image fits into figure: prevent edges from leaving figure
        if (imageRect.top < window.innerHeight*0.05) {
            image.style['top'] = `${window.innerHeight*0.05}px`;
        } else if (imageRect.bottom > window.innerHeight*0.95) {
            image.style['top'] = `${window.innerHeight*0.95-imageRect.height}px`;
        }
    } else {
        // image too big for figure: prevent edges from entering figure
        if (imageRect.top > window.innerHeight*0.05 ) {
            image.style['top'] = `${window.innerHeight*0.05}px`;
        } else if (imageRect.bottom < window.innerHeight*0.95) {
            image.style['top'] = `${window.innerHeight*0.95-imageRect.height}px`;
        }
    }
}


window.addEventListener('DOMContentLoaded', (event) => {
    var figures = document.getElementsByTagName('figure');
    for (let figure of figures) {
        figure.addEventListener("click", lightboxFigureClickCallback);
        let images = figure.querySelectorAll('img');
        for (let image of images) {
            image.addEventListener("click", lightboxImgClickCallback);
        }
    }});
