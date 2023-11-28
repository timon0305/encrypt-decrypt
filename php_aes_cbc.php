<?php
// For starting, need to install package
// npm install crypto

class AESCipher {
    private $key;

    public function __construct($key) {
        $this->key = hex2bin($key);
    }

    public function encrypt($data) {
        $iv = str_repeat("\0", 16);
        $cipher = openssl_encrypt(hex2bin($data), 'aes-128-cbc', $this->key, OPENSSL_RAW_DATA, $iv);
        return bin2hex($cipher);
    }

    public function decrypt($data) {
        $iv = str_repeat("\0", 16);
        $decipher = openssl_decrypt(hex2bin($data), 'aes-128-cbc', $this->key, OPENSSL_RAW_DATA, $iv);
        return bin2hex($decipher);
    }
}

$ver = $argv[1];
$key = $argv[2];
$txt = $argv[3];

if ($ver === 'encrypt') {
    $val = (new AESCipher($key))->encrypt($txt);
    echo $val . "\n";
} else {
    $val = (new AESCipher($key))->decrypt($txt);
    echo $val . "\n";
}
?>
