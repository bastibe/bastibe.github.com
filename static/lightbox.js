let isDragging = false;
let wasDragged = false;

document.addEventListener('keyup', e => {
    let lightboxImage = document.querySelector('figure.lightbox img.lightbox');
    if (e.key === 'Escape' && lightboxImage) {
        let figure = lightboxImage.parentNode;
        exitLightbox(figure, lightboxImage);
    }
});

function openLightbox(event) {
    if (event.buttons !== 0) {
        return;
    }
    let image = event.target;
    let figure = image.parentNode;
    if (wasDragged === true) {
        wasDragged = false;
    } else if (figure.classList.contains('lightbox')) {
        exitLightbox(figure, image);
    } else {
        enterLightbox(figure, image);
    }
}

function enterLightbox(figure, image) {
    figure.classList.add('lightbox');
    // don't scroll background when scrolling figure:
    figure.onwheel = e => { e.preventDefault(); };
    image.classList.add('lightbox');
    image.onwheel = zoomLightbox;
    image.style['max-width'] = '90%';
    image.style['max-height'] = '90%';
    image.addEventListener('mousedown', lightboxMouseDown);
    image.addEventListener('mousemove', lightboxMouseMove);
    image.addEventListener('mouseup', lightboxMouseUp);
    image.setAttribute('draggable', false);
    // set initial image position to center:
    image.style['left'] = `${(window.innerWidth-image.offsetWidth)/2}px`;
    image.style['top'] = `${(window.innerHeight-image.offsetHeight)/2}px`;
    // hide all other images in this figure:
    for (let otherImage of figure.querySelectorAll('img:not(.lightbox)')) {
        otherImage.style['visibility'] = 'hidden';
    }
}

function exitLightbox(figure, image) {
    figure.classList.remove('lightbox');
    figure.onwheel = undefined;
    image.classList.remove('lightbox');
    image.onwheel = undefined;
    image.style['max-width'] = '';
    image.style['max-height'] = '';
    image.style['top'] = '';
    image.style['left'] = '';
    image.removeEventListener('mousedown', lightboxMouseDown);
    image.removeEventListener('mousemove', lightboxMouseMove);
    image.removeEventListener('mouseup', lightboxMouseUp);
    image.setAttribute('draggable', true);
    // unhide all images in this figure:
    for (let otherImage of figure.querySelectorAll('img')) {
        otherImage.style['visibility'] = '';
    }
}

function lightboxMouseDown(event) {
    isDragging = true;
}

function lightboxMouseMove(event) {
    if (isDragging === true) {
        let image = event.target;
        let left = parseFloat(image.style['left']);
        image.style['left'] = `${left + event.movementX}px`;
        let top = parseFloat(image.style['top']);
        image.style['top'] = `${top + event.movementY}px`;
        moveImageIntoBorders(image);
        // prevent closing of figure:
        if (event.movementX != 0 || event.movementY != 0) {
            wasDragged = true;
        }
    }
}

function lightboxMouseUp(event) {
    isDragging = false;
}

function zoomLightbox(event) {
    let image = event.target; // relative position on image:
    let imageRect = image.getBoundingClientRect();
    let imageX = (event.clientX-imageRect.left)/imageRect.width;
    let imageY = (event.clientY-imageRect.top)/imageRect.height;

    // zoom in:
    let zoomFactor = parseFloat(image.style['max-width']) / 100;
    zoomFactor /= 1.0 - event.wheelDeltaY / 360;
    zoomFactor = Math.min(Math.max(zoomFactor, 0.9), 5);
    image.style['max-width'] = `${zoomFactor*100}%`;
    image.style['max-height'] = `${zoomFactor*100}%`;

    // pan so the image does not move under cursor:
    let newPositionX = -imageX*image.offsetWidth + event.clientX;
    let newPositionY = -imageY*image.offsetHeight + event.clientY;
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
        let images = figure.querySelectorAll('img');
        for (let image of images) {
            image.onclick = openLightbox;
        }
    }});
