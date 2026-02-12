# Decompiled from: fs_image/cactiotpad/crypto.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

_hashlib = uhashlib
_hashlib = hashlib
_os = uos
_os = os
_binascii = ubinascii
_binascii = binascii
_cryptolib = ucryptolib
_cryptolib = None
_sha256 = <func_0>
_rand_bytes = <func_1>
_hex_to_bytes = <func_2>
_bytes_to_hex = <func_3>
_b64encode = <func_4>
_b64decode = <func_5>
generate_symkey1 = <func_6>
_validate_symkey1 = <func_7>
_ordered_symkeys = <func_8>
derive_symkey2 = <func_9>
derive_session_hash_and_key = <func_10>
_pkcs7_pad = (16)
_pkcs7_unpad = (16)
encrypt_message = <func_13>
decrypt_message = <func_14>
1 = _hashlib
return 1
return 0
return 0
return 'utf-8'
return 'utf-8'
1 = 0
return 'utf-8'
return 'utf-8'
return _bytes_to_hex(_rand_bytes(4))
4 = (2, 0)
5 = (3, 1)
6 = (5, 4)
7 = (4, 5)
return 7(1)
4 = _ordered_symkeys(0, 1, 2, 3)
return None(8)
5 = _ordered_symkeys(0, 1, 3, 4)
6 = _hex_to_bytes(2)
7 = _sha256(6)
8 = _bytes_to_hex(7)
9 = None(16)
return (8, 9)
2 = 1
return [2](2)
2 = -1
return 2
2 = _hex_to_bytes(0)
3 = _rand_bytes(16)
4 = 3
5 = 1('utf-8')
6 = 5
return 3(6)
2 = _hex_to_bytes(0)
3 = _b64decode(1)
4 = 16
5 = 4
6 = None
return 'utf-8'