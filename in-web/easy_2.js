const crypto = require("crypto");



function md5 (str) {
    return crypto
        .createHash("md5")
        .update(str)
        .digest("hex");
}


// var c = new Date()['valueOf']();
c = 1587102734000;
token = global['btoa']('aiding_win' +  String(c));
// md = global['btoa']('aiding_win' + Math['round'](c/ 1000));
md = md5(global['btoa']('aiding_win'+ String(Math['round'](c/ 1000))));
console.log(token)
console.log(md)
a = {}
a['add'] = function (d,e){
                return d + e;
            }
cookie = a['add'](a['add'](a['add'](a['add'](a['add'](a['add']('sign=', String(Math['round'](c/ 1000))), '~'), token), '|'), md), '; path=/');
console.log(cookie)