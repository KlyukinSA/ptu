date >> open-text.txt 

Уже установлен пакет gnupg самой новой версии

# создание ключей
```
sysadmin@deb10-1:~/infsec/lab2$ gpg --gen-key
gpg (GnuPG) 2.2.27; Copyright (C) 2021 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

gpg: создан щит с ключами '/home/sysadmin/.gnupg/pubring.kbx'
Замечание: "gpg --full-generate-key" вызывает полнофункциональный диалог создания ключа.

GnuPG должен составить идентификатор пользователя для идентификации ключа.

Ваше полное имя: Клюкин Степан Александрович
Адрес электронной почты: klyukin.sa@edu.spbstu.ru
Используется таблица символов 'utf-8'.
Вы выбрали следующий идентификатор пользователя:
    "Клюкин Степан Александрович <klyukin.sa@edu.spbstu.ru>"

Сменить (N)Имя, (E)Адрес; (O)Принять/(Q)Выход? o
Необходимо получить много случайных чисел. Желательно, чтобы Вы
в процессе генерации выполняли какие-то другие действия (печать
на клавиатуре, движения мыши, обращения к дискам); это даст генератору
случайных чисел больше возможностей получить достаточное количество энтропии.
Необходимо получить много случайных чисел. Желательно, чтобы Вы
в процессе генерации выполняли какие-то другие действия (печать
на клавиатуре, движения мыши, обращения к дискам); это даст генератору
случайных чисел больше возможностей получить достаточное количество энтропии.
fdds aa gpg: /home/sysadmin/.gnupg/trustdb.gpg: создана таблица доверия
gpg: ключ 3B025E54C29EC8FE помечен как абсолютно доверенный
gpg: создан каталог '/home/sysadmin/.gnupg/openpgp-revocs.d'
gpg: сертификат отзыва записан в '/home/sysadmin/.gnupg/openpgp-revocs.d/29EC26D5034AC87B599E65583B025E54C29EC8FE.rev'.
открытый и секретный ключи созданы и подписаны.

pub   rsa3072 2024-10-25 [SC] [   годен до: 2026-10-25]
      29EC26D5034AC87B599E65583B025E54C29EC8FE
uid                      Клюкин Степан Александрович <klyukin.sa@edu.spbstu.ru>
sub   rsa3072 2024-10-25 [E] [   годен до: 2026-10-25]
```
# список ключей
```
sysadmin@deb10-1:~/infsec/lab2$ gpg --list-secret-keys
gpg: проверка таблицы доверия
gpg: marginals needed: 3  completes needed: 1  trust model: pgp
gpg: глубина: 0  достоверных:   1  подписанных:   0  доверие: 0-, 0q, 0n, 0m, 0f, 1u
gpg: срок следующей проверки таблицы доверия 2026-10-25
/home/sysadmin/.gnupg/pubring.kbx
---------------------------------
sec   rsa3072 2024-10-25 [SC] [   годен до: 2026-10-25]
      29EC26D5034AC87B599E65583B025E54C29EC8FE
uid         [  абсолютно ] Клюкин Степан Александрович <klyukin.sa@edu.spbstu.ru>
ssb   rsa3072 2024-10-25 [E] [   годен до: 2026-10-25]

sysadmin@deb10-1:~/infsec/lab2$ gpg --list-keys
/home/sysadmin/.gnupg/pubring.kbx
---------------------------------
pub   rsa3072 2024-10-25 [SC] [   годен до: 2026-10-25]
      29EC26D5034AC87B599E65583B025E54C29EC8FE
uid         [  абсолютно ] Клюкин Степан Александрович <klyukin.sa@edu.spbstu.ru>
sub   rsa3072 2024-10-25 [E] [   годен до: 2026-10-25]
```
# 1.4.2. Задание 3. Выполнение экспорта публичного ключа
```
gpg --output pubkey.asc --armor --export 29EC26D5034AC87B599E65583B025E54C29EC8FE
```
# Импорт открытого ключа
```
sysadmin@deb10-1:~/infsec/lab2$ gpg --import 874A9D18.asc 
gpg: ключ DB9729FF874A9D18: импортирован открытый ключ "Egor S. Orlov (Infsec course at HSSE) <egor.orlov@avalon.ru>"
gpg: Всего обработано: 1
gpg:                  импортировано: 1

sysadmin@deb10-1:~/infsec/lab2$ gpg --list-keys
/home/sysadmin/.gnupg/pubring.kbx
---------------------------------
pub   rsa3072 2024-10-25 [SC] [   годен до: 2026-10-25]
      29EC26D5034AC87B599E65583B025E54C29EC8FE
uid         [  абсолютно ] Клюкин Степан Александрович <klyukin.sa@edu.spbstu.ru>
sub   rsa3072 2024-10-25 [E] [   годен до: 2026-10-25]

pub   rsa2048 2021-09-29 [SC]
      24B39968DF98CB8509378B6ADB9729FF874A9D18
uid         [ неизвестно ] Egor S. Orlov (Infsec course at HSSE) <egor.orlov@avalon.ru>
sub   rsa2048 2021-09-29 [E]

sysadmin@deb10-1:~/infsec/lab2$ gpg --edit-key egor.orlov@avalon.ru
gpg (GnuPG) 2.2.27; Copyright (C) 2021 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

pub  rsa2048/DB9729FF874A9D18
          создан: 2021-09-29     годен до: никогда     назначение: SC  
     доверие: неизвестно достоверность: неизвестно
sub  rsa2048/D61AB33E33A0A0F0
          создан: 2021-09-29     годен до: никогда     назначение: E   
[ неизвестно ] (1). Egor S. Orlov (Infsec course at HSSE) <egor.orlov@avalon.ru>

gpg> sign

pub  rsa2048/DB9729FF874A9D18
          создан: 2021-09-29     годен до: никогда     назначение: SC  
     доверие: неизвестно достоверность: неизвестно
 Отпечаток первичного ключа: 24B3 9968 DF98 CB85 0937  8B6A DB97 29FF 874A 9D18

     Egor S. Orlov (Infsec course at HSSE) <egor.orlov@avalon.ru>

Вы уверены, что хотите подписать этот ключ
своим ключом "Клюкин Степан Александрович <klyukin.sa@edu.spbstu.ru>" (3B025E54C29EC8FE)?

Действительно подписать? (y/N) y

gpg> q
Сохранить изменения? (y/N) y

sysadmin@deb10-1:~/infsec/lab2$ gpg --list-keys
gpg: проверка таблицы доверия
gpg: marginals needed: 3  completes needed: 1  trust model: pgp
gpg: глубина: 0  достоверных:   1  подписанных:   1  доверие: 0-, 0q, 0n, 0m, 0f, 1u
gpg: глубина: 1  достоверных:   1  подписанных:   0  доверие: 1-, 0q, 0n, 0m, 0f, 0u
gpg: срок следующей проверки таблицы доверия 2026-10-25
/home/sysadmin/.gnupg/pubring.kbx
---------------------------------
pub   rsa3072 2024-10-25 [SC] [   годен до: 2026-10-25]
      29EC26D5034AC87B599E65583B025E54C29EC8FE
uid         [  абсолютно ] Клюкин Степан Александрович <klyukin.sa@edu.spbstu.ru>
sub   rsa3072 2024-10-25 [E] [   годен до: 2026-10-25]

pub   rsa2048 2021-09-29 [SC]
      24B39968DF98CB8509378B6ADB9729FF874A9D18
uid         [   полное   ] Egor S. Orlov (Infsec course at HSSE) <egor.orlov@avalon.ru>
sub   rsa2048 2021-09-29 [E]
```
# 1.5.1. Задание 5. Выполните шифрование файла средствами GPG
```
sysadmin@deb10-1:~/infsec/lab2$ gpg -a -r CFA7225F6AD88CAA67BF1ED07009D30C37A788D3 -o close-text.asc -e open-text.txt
```
#  1.6.1. Создание отсоединенной подписи
```
sysadmin@deb10-1:~/infsec/lab2$ gpg --sign --detach-sign --default-key CFA7225F6AD88CAA67BF1ED07009D30C37A788D3 --armor open-text.txt 
```
