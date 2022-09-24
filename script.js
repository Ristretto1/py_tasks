// ПЕРЕМЕННЫЕ
let heroImg = window.document.querySelector('#hero-img');
let imgBlock = window.document.querySelector('#img-block');
let rightPosition = 0;
let imgBlockPosition = 0;

// ФУНКЦИИ
const rightHandler = () => {
    heroImg.style.transform = 'scale(-1,1)'
    rightPosition++
    imgBlockPosition++
    if (rightPosition > 5) rightPosition = 0
    heroImg.style.left = `-${rightPosition * 288}px`
    imgBlock.style.left = `${imgBlockPosition * 20}px`
}

const leftHandler = () => {
    heroImg.style.transform = 'scale(1,1)'
    rightPosition++
    imgBlockPosition--
    if (rightPosition > 5) rightPosition = 0
    heroImg.style.left = `-${rightPosition * 288}px`
    imgBlock.style.left = `${imgBlockPosition * 20}px`
}

// ОБРАБОТЧИКИ СОБЫТИЙ
let timer = null
let x = 0
let halfWidth = window.screen.width / 2
const onTouchStart = (event) => {
    event.preventDefault()
    x = event.type === 'mousedown' ? event.screenX : event.touches[0].screenX

    timer = setInterval(() => {
        (x > halfWidth) ? rightHandler() : leftHandler()
    }, 130)
}

const onTouchEnd = (event) => {
    event.preventDefault()
    clearInterval(timer)
}

window.onmousedown = (event) => onTouchStart(event)
window.ontouchstart = (event) => onTouchStart(event)
window.onmouseup = (event) => onTouchEnd(event)
window.ontouchend = (event) => onTouchEnd(event)