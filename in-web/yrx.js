// 重写push方法
_push = Array.prototype.push
Array.prototype.push = function () {
    console.log("这里是hook的" , arguments)
    return _push.apply(this,arguments)
}

// hook eval
_eval = eval;
function eval (){
    if(arguments[0].indexOf('debugger') !== -1){
        return _eval.apply(this,'')
    }
    return _eval.apply(this,arguments)
}

// hook cookie
(function () {
    'use strict';
    var cookie_cache = document.cookie;
    Object.defineProperty(document, 'cookie', {
        get: function () {
            return cookie_cache;
        },
        set: function (val) {
            console.log('Setting cookie', val);
            // 填写cookie名
            if (val.indexOf('cookie名') != -1) {
                debugger;
            }
            var cookie = val.split(";")[0];
            var ncookie = cookie.split("=");
            var flag = false;
            var cache = cookie_cache.split("; ");
            cache = cache.map(function (a) {
                if (a.split("=")[0] === ncookie[0]) {
                    flag = true;
                    return cookie;
                }
                return a;
            })
            cookie_cache = cache.join("; ");
            if (!flag) {
                cookie_cache += cookie + "; ";
            }
            return cookie_cache;
        }
    });
})();