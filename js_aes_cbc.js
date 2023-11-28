//For starting,  need to install package
//npm install crypto


const { createCipheriv, createDecipheriv } = require('crypto');

class AESCipher {
    constructor(key) {
        this.key = Buffer.from(key, 'hex');
    }

    encrypt(data) {
        const iv = Buffer.alloc(16);
        const cipher = createCipheriv('aes-128-cbc', this.key, iv);
        const encrypted = cipher.update(Buffer.from(data, 'hex'));
        const finalBuffer = Buffer.concat([encrypted, cipher.final()]);
        return finalBuffer.toString('hex');
    }

    decrypt(data) {
        const iv = Buffer.alloc(16);
        const decipher = createDecipheriv('aes-128-cbc', this.key, iv);
        const decrypted = decipher.update(Buffer.from(data, 'hex'));
        const finalBuffer = Buffer.concat([decrypted, decipher.final()]);
        return finalBuffer.toString('hex');
    }
}

const ver = process.argv[2];
const key = process.argv[3];
const txt = process.argv[4];

if (ver === 'encrypt') {
    const val = new AESCipher(key).encrypt(txt);
    console.log(val);
} else {
    const val = new AESCipher(key).decrypt(txt);
    console.log(val);
}

