// ПЕРЕМЕННЫЕ
let rightPosition = 0;
let imgBlockPosition = 0;
let direction = 'right'
let hit = false
let jump = false
let timer = null
let x = 0
let halfWidth = window.screen.width / 2

let canvas = window.document.querySelector('#canvas');
let jumpBlock = window.document.querySelector('#jump-block');
let hitBlock = window.document.querySelector('#hit-block');
let fsBtn = window.document.querySelector('#fsBtn');
let heroImg = window.document.querySelector('#hero-img');
let imgBlock = window.document.querySelector('#img-block');

hitBlock.style.top = `${window.screen.height / 2 - 144 / 2}px`
jumpBlock.style.top = `${window.screen.height / 2 - 144 / 2}px`

heroImg.onclick = (event) => {
    event.preventDefault()
}
fsBtn.onclick = () => {
    if (window.document.fullscreen) {
        fsBtn.src = 'assets/img/fullscreen.png'
        window.document.exitFullscreen()
    } else {
        fsBtn.src = 'assets/img/cancel.png'
        canvas.requestFullscreen()
    }
}
jumpBlock.onclick = () => jump = true
hitBlock.onclick = () => hit = true
// ФУНКЦИИ
const rightHandler = () => {
    heroImg.style.transform = 'scale(-1,1)'
    rightPosition++
    imgBlockPosition++
    if (rightPosition > 5) rightPosition = 0
    heroImg.style.left = `-${rightPosition * 288}px`
    heroImg.style.top = '-576px'
    imgBlock.style.left = `${imgBlockPosition * 20}px`
}

const leftHandler = () => {
    heroImg.style.transform = 'scale(1,1)'
    rightPosition++
    imgBlockPosition--
    if (rightPosition > 5) rightPosition = 0
    heroImg.style.left = `-${rightPosition * 288}px`
    heroImg.style.top = '-576px'
    imgBlock.style.left = `${imgBlockPosition * 20}px`
}

const standHandler = () => {
    switch (direction) {
        case 'right': {
            heroImg.style.transform = 'scale(-1,1)'
            if (rightPosition > 4) rightPosition = 1
            break;
        }
        case 'left': {
            heroImg.style.transform = 'scale(1,1)'
            if (rightPosition > 3) rightPosition = 0
            break;
        }
        default:
            break
    }

    rightPosition++
    heroImg.style.left = `-${rightPosition * 288}px`
    heroImg.style.top = '0'
}

const hitHandler = () => {
    switch (direction) {
        case 'right': {
            heroImg.style.transform = 'scale(-1,1)'
            if (rightPosition > 4) {
                rightPosition = 0
                hit = false
            }
            break;
        }
        case 'left': {
            heroImg.style.transform = 'scale(1,1)'
            if (rightPosition > 3) {
                rightPosition = 0
                hit = false
            }
            break;
        }
        default:
            break
    }

    rightPosition++
    heroImg.style.left = `-${rightPosition * 288}px`
    heroImg.style.top = '-864px'
}

const jumpHandler = () => {
    switch (direction) {
        case 'right': {
            heroImg.style.transform = 'scale(-1,1)'
            if (rightPosition > 4) {
                rightPosition = 0
                jump = false
            }
            break;
        }
        case 'left': {
            heroImg.style.transform = 'scale(1,1)'
            if (rightPosition > 3) {
                rightPosition = 0
                jump = false
            }
            break;
        }
        default:
            break
    }

    rightPosition++
    heroImg.style.left = `-${rightPosition * 288}px`
    heroImg.style.top = '-288px'
}

// ОБРАБОТЧИКИ СОБЫТИЙ
const onTouchStart = (event) => {
    clearInterval(timer)
    x = event.type === 'mousedown' ? event.screenX : event.touches[0].screenX
    timer = setInterval(() => {
        if (x > halfWidth) {
            direction = 'right'
            rightHandler()
        } else {
            direction = 'left'
            leftHandler()
        }
    }, 130)
}

const onTouchEnd = (event) => {
    clearInterval(timer)
    lifeCycle()
}

window.onmousedown = (event) => onTouchStart(event)
window.ontouchstart = (event) => onTouchStart(event)
window.onmouseup = (event) => onTouchEnd(event)
window.ontouchend = (event) => onTouchEnd(event)

const lifeCycle = () => {
    timer = setInterval(() => {
        if (hit) {
            hitHandler()
        } else if (jump) {
            jumpHandler()
        } else {
            standHandler()
        }
    }, 150)
}

const start = () => {
    lifeCycle()
}

start()