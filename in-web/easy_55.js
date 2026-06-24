const CryptoJS = require("crypto-js");

const KEY = "aiding6666666666";

/**
 * 使用 AES-ECB 解密 challenge55 接口返回的密文。
 *
 * @param {string} str 接口返回的 result 字段密文。
 * @returns {string} 解密后的 JSON 字符串。
 */
function aesDecrypt(str) {
    // KEY 转成 Utf8 字节
    const key = CryptoJS.enc.Utf8.parse(KEY);

    const decrypted = CryptoJS.AES.decrypt(str, key, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7,
    });

    return decrypted.toString(CryptoJS.enc.Utf8);
}

const encrypted = process.argv[2];

if (!encrypted) {
    console.error("缺少待解密的 result 参数");
    process.exit(1);
}

console.log(aesDecrypt(encrypted));
