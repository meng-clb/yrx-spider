setTimeout = function(){};
window = {}
window.addEventListener = '1'

document = {}
document.addEventListener = function (a, b, c) {
    b();
}

document.createElement = function () {
    return {
        innerHTML: "<a href='/'>_1H</a>",
        firstChild: {
            href: 'https://www.python-spider.com/'
        }
    }
}

__jscode

function decode(){
    return document.cookie
}

// console.log(decode())