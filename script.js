// ПЕРЕМЕННЫЕ
let heroImg = window.document.querySelector('#hero-img');
let imgBlock = window.document.querySelector('#img-block');
let rightPosition = 0;
let imgBlockPosition = 0;

// ФУНКЦИИ
const rightHandler = () => {
    rightPosition++
    imgBlockPosition++
    if (rightPosition > 5) rightPosition = 0
    heroImg.style.left = `-${rightPosition*288}px`
    imgBlock.style.left = `${imgBlockPosition*20}px`
}

// ОБРАБОТЧИКИ СОБЫТИЙ
let timer = null
const onTouchStart = (event) => {
 timer = setInterval(() => {
     rightHandler()
 }, 130)
}

const onTouchEnd = (event) => {
    clearInterval(timer)
}

window.onmousedown = (event) => onTouchStart
window.ontouchstart = (event) => onTouchStart
window.onmouseup = (event) => onTouchEnd
window.ontouchend = (event) => onTouchEnd