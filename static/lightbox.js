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

function openLightbox(event) {
    if (event.buttons !== 0) {
        return;
    }

    // if the browser issues both click and touch events, ignore
    // the later one:
    if (event.timeStamp - lightboxTime < 100) {
        return;
    }
    lightboxTime = event.timeStamp;

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
    fakeFig.style['background-color'] = '#f0f0f0';
    figure.parentNode.insertBefore(fakeFig, figure);
    // activate lightbox
    figure.classList.add('lightbox');
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
        image.style['left'] = `${image.offsetLeft + event.movementX}px`;
        image.style['top'] = `${image.offsetTop + event.movementY}px`;
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
    let zoomFactor = imageRect.width / window.innerWidth;
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


// these function implements a poor-man's 'onclick' for touch events:
function handleTouchStart(event) {
    if (event.touches.length == 1 && touchCoordinate.length == 0) {
        // remember where the touch started:
        touchCoordinate = [event.touches[0].screenX, event.touches[0].screenY];
    }
}

function handleTouchMove(event) {
    // if the cursor moves too much during the touch, it's not a click:
    if (event.touches.length == 1 && touchCoordinate.length == 2) {
        if ((Math.abs(event.touches[0].screenX - touchCoordinate[0]) > 10) ||
            (Math.abs(event.touches[0].screenY - touchCoordinate[1]) > 10)) {
            touchCoordinate = [];
        }
    // if more than one finger touches the screen, it's not a click:
    } else if (event.touches.length != 1) {
        touchCoordinate = [];
    }
}

function handleTouchEnd(event) {
    // if touchCoordinate still exists at touch end, it's a click:
    if (touchCoordinate.length == 2) {
        // if the browser issues both click and touch events, ignore
        // the later one:
        if (event.timeStamp - lightboxTime < 100) {
            return;
        }
        lightboxTime = event.timeStamp;

        let image = event.target;
        let figure = image.parentNode;
        if (figure.classList.contains('lightbox')) {
            exitLightbox(figure, image);
        } else {
            enterLightbox(figure, image);
        }
        touchCoordinate = [];
    }
}

function handleTouchCancel(event) {
    // if the touch is cancelled, it's not a click:
    touchCoordinate = [];
}

window.addEventListener('DOMContentLoaded', (event) => {
    var figures = document.getElementsByTagName('figure');
    for (let figure of figures) {
        let images = figure.querySelectorAll('img');
        for (let image of images) {
            image.onclick = openLightbox;
            // This is a workaround for image.ontap = opanLightbox:
            image.addEventListener("touchstart", handleTouchStart);
            image.addEventListener("touchend", handleTouchEnd);
            image.addEventListener("touchmove", handleTouchMove);
            image.addEventListener("touchcancel", handleTouchCancel);
        }
    }});
