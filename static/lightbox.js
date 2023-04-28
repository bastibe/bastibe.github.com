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


function lightboxClickCallback(event) {
    // if the browser issues both click and touch events, ignore
    // the later one:
    if (event.timeStamp - lightboxTime < 300) {
        return;
    }
    lightboxTime = event.timeStamp;

    let figure, image
    if (event.target.tagName == "FIGURE") {
        figure = event.target;
        image = figure.getElementsByTagName('img')[0];
    } else if (event.target.tagName == "IMG") {
        image = event.target;
        figure = image.parentNode;
    }

    event.stopImmediatePropagation();
    if (figure.classList.contains('lightbox')) {
        // don't exit if we came here from a drag
        if (wasDragged === true) {
            wasDragged = false;
            return;
        }
        exitLightbox(figure, image);
    } else {
        // reset dragging state
        wasDragged = false;
        enterLightbox(figure, image);
    }
}


function enterLightbox(figure, image) {
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
    image.classList.add('lightbox');
    image.style['max-width'] = '90%';
    image.style['max-height'] = '90%';
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


function exitLightbox(figure, image) {
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
    image.classList.remove('lightbox');
    image.style['max-width'] = '';
    image.style['max-height'] = '';
    image.style['top'] = '';
    image.style['left'] = '';
    image.removeEventListener('wheel', lightboxScrollCallback);
    image.removeEventListener('mousedown', lightboxMouseDownCallback);
    image.removeEventListener('mousemove', lightboxMouseMoveCallback);
    image.removeEventListener('mouseup', lightboxMouseUpCallback);
    image.setAttribute('draggable', true);
    // unhide all images in this figure:
    for (let otherImage of figure.querySelectorAll('img')) {
        otherImage.style['visibility'] = '';
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
    let image = event.target; // relative position on image:
    let imageRect = image.getBoundingClientRect();
    let imageX = (event.clientX-imageRect.left)/imageRect.width;
    let imageY = (event.clientY-imageRect.top)/imageRect.height;

    // zoom in:
    let zoomFactor = Math.max(imageRect.width / window.innerWidth,
                              imageRect.height / window.innerHeight);
    zoomFactor /= 1.0 - event.wheelDeltaY / 360;
    zoomFactor = Math.min(Math.max(zoomFactor, 0.9), 5);
    image.style['max-width'] = `${zoomFactor*100}%`;
    image.style['max-height'] = `${zoomFactor*100}%`;

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
        figure.addEventListener("click", lightboxClickCallback);
        let images = figure.querySelectorAll('img');
        for (let image of images) {
            image.addEventListener("click", lightboxClickCallback);
        }
    }});
