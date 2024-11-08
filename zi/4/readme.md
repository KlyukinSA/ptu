```
hostname
deb10-1
```

```
sysadmin@deb10-1:~$ openssl req -newkey rsa:4096 -nodes -keyout deb10-1.key -out deb10-1.csr
Generating a RSA private key
...........................................................++++
..++++
writing new private key to 'deb10-1.key'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:RU
State or Province Name (full name) [Some-State]:ru
Locality Name (eg, city) []:SPb
Organization Name (eg, company) [Internet Widgits Pty Ltd]:SPbSTU
Organizational Unit Name (eg, section) []:ICCS
Common Name (e.g. server FQDN or YOUR name) []:deb10-1.spbstu.ru
Email Address []:klyukin.sa@edu.spbstu.ru

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:

sysadmin@deb10-1:~$ openssl req -text -in deb10-1.csr
Certificate Request:
    Data:
        Version: 1 (0x0)
        Subject: C = RU, ST = ru, L = SPb, O = SPbSTU, OU = ICCS, CN = deb10-1.spbstu.ru, emailAddress = klyukin.sa@edu.spbstu.ru ...
```

```
sysadmin@deb10-1:~$ openssl req -newkey rsa:4096 -x509 -keyout ca.key -out ca.crt -days 3654
Generating a RSA private key
.................................................1.............................................2.....................................++++
.....................++++
writing new private key to 'ca.key'
Enter PEM pass phrase:
Verifying - Enter PEM pass phrase:
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:RU
State or Province Name (full name) [Some-State]:ru
Locality Name (eg, city) []:SPb
Organization Name (eg, company) [Internet Widgits Pty Ltd]:SPbSTU
Organizational Unit Name (eg, section) []:ICCS 
Common Name (e.g. server FQDN or YOUR name) []:Infsec Course CA
Email Address []:klyukin.sa@edu.spbstu.ru

sysadmin@deb10-1:~$ openssl x509 -text -in ca.crt 
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            0e:a1:a7:27:cc:62:c1:4b:76:fc:6d:3b:f7:5d:82:37:65:2c:f8:95
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C = RU, ST = ru, L = SPb, O = SPbSTU, OU = ICCS, CN = Infsec Course CA, emailAddress = klyukin.sa@edu.spbstu.ru
        Validity
            Not Before: Nov  8 08:35:25 2024 GMT
            Not After : Nov 10 08:35:25 2034 GMT
        Subject: C = RU, ST = ru, L = SPb, O = SPbSTU, OU = ICCS, CN = Infsec Course CA, emailAddress = klyukin.sa@edu.spbstu.ru ...
```

```
sysadmin@deb10-1:~$ openssl x509 -req -in deb10-1.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out deb10-1.crt
Signature ok
subject=C = RU, ST = ru, L = SPb, O = SPbSTU, OU = ICCS, CN = deb10-1.spbstu.ru, emailAddress = klyukin.sa@edu.spbstu.ru
Getting CA Private Key
Enter pass phrase for ca.key:
```

выкладываем
- deb10-1.csr
- ca.crt
- deb10-1.crt
