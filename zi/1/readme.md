# Исследование_зависимости_криптостойкости_от_длины_ключа

# Вход в систему
логин: `sysadmin`
пароль: `netlab123`

# fcrackzip
fcrackzip - утилита для восстановления/взлома паролей zip-архивов
Может использоваться и как инструмент восстановления данных и
как инструмент злоумышленника.

It is able to crack password protected zip files with brute force or dictionary based attacks, optionally testing with unzip its results. It can also crack cpmask’ed images.

# Подготовка системы
## Наличие установленных программ
```bash
sysadmin@deb10-1:~/Рабочий стол$ which fcrackzip
/usr/bin/fcrackzip
sysadmin@deb10-1:~/Рабочий стол$ which zip
/usr/bin/zip
sysadmin@deb10-1:~/Рабочий стол$ which unzip
/usr/bin/unzip
sysadmin@deb10-1:~/Рабочий стол$ which git
/usr/bin/git
sysadmin@deb10-1:~/Рабочий стол$
```
	`sudo apt update && apt install fcrackzip zip unzip git`
## Получение файлов
Находясь в домашнем каталоге `/home/sysadmin`
`git clone https://github.com/esorlov/infsec/`
`cd infsec/lab1`
```bash
sysadmin@deb10-1:~/infsec/lab1$ pwd
/home/sysadmin/infsec/lab1
sysadmin@deb10-1:~/infsec/lab1$ ls
opentext.txt  report
```
# Задание 1. Создание зашифрованных zip-архивов
Создание зашифрованных ZIP-архивов производится командой `zip -e <archive.zip> <files...>`
Пароль для создания ключа шифрования вводится с клавиатуры

- **Выполните создание из файла opentext.txt зашифрованных архивов в соответствии со следующей таблицей.**

| Имя архива   | содержимое   | длина пароля | пароль |
| ------------ | ------------ | ------------ | ------ |
| archive2.zip | opentext.txt | 2            | ne     |
| archive3.zip | opentext.txt | 3            | net    |
| archive4.zip | opentext.txt | 4            | netl   |
| archive5.zip | opentext.txt | 5            | netla  |
| archive6.zip | opentext.txt | 6            | netlab |
```bash
sysadmin@deb10-1:~/infsec/lab1$ zip -e archive3.zip opentext.txt 
Enter password: 
Verify password: 
  adding: opentext.txt (deflated 40%)
sysadmin@deb10-1:~/infsec/lab1$ zip -e archive4.zip opentext.txt 
Enter password: 
Verify password: 
  adding: opentext.txt (deflated 40%)
sysadmin@deb10-1:~/infsec/lab1$ zip -e archive5.zip opentext.txt 
Enter password: 
Verify password: 
  adding: opentext.txt (deflated 40%)
sysadmin@deb10-1:~/infsec/lab1$ zip -e archive6.zip opentext.txt 
Enter password: 
Verify password: 
  adding: opentext.txt (deflated 40%)
sysadmin@deb10-1:~/infsec/lab1$ ls
archive2.zip  archive3.zip  archive4.zip  archive5.zip  archive6.zip  opentext.txt  report

```
- **Попробуйте открыть один из архивов при помощи неверного пароля. Убедитесь, что это невозможно.**
```bash
sysadmin@deb10-1:~/infsec/lab1$ unzip -P netotparol archive2.zip 
Archive:  archive2.zip
   skipping: opentext.txt            incorrect password

```
- **Убедитесь, что при указании верного пароля от архива возникает предложение перезаписать уже существующий в текущем каталоге файл opentext.txt. Т.е. извлечение файла становится возможным.**
```bash
sysadmin@deb10-1:~/infsec/lab1$ unzip -P ne archive2.zip 
Archive:  archive2.zip
replace opentext.txt? [y]es, [n]o, [A]ll, [N]one, [r]ename: y
  inflating: opentext.txt
```

## Восстановление паролей зашифрованных ZIP-архивов
В этой части задания якобы потерянные пароли от зашифрованных ZIP-архивов будут восстановлены с использованием специальной утилиты fcrackzip.
Fcrackzip пытается восстановить пароль архива методом полного перебора (метод грубой силы).
Ваша задача понять как длина указанного при создании архива пароля, т.е. по сути длина ключа шифрования влияет на время необходимое на осуществление полного перебора (выполнение атаки на криптосистему методом грубой силы).
- **Ознакомьтесь со справкой по команде fcrackzip**
`man fcrackzip`

Для восстановления пароля мы будем использовать следующее сочетание опций
`-vul min-max -c a`

```bash
-v, --verbose
              Each -v makes the program more verbose.
-u, --use-unzip
              Try  to  decompress  the first file by calling unzip with the guessed password. This weeds out false posi‐
              tives when not enough files have been given.
-l, --length min[-max]
              Use an initial password of length min, and check all passwords up to passwords of length max  (including).
              You can omit the max parameter.
-c, --charset characterset-specification
              Select the characters to use in brute-force cracking. Must be one of

                a   include all lowercase characters [a-z]
                A   include all uppercase characters [A-Z]
                1   include the digits [0-9]
                !   include [!:$%&/()=?{[]}+*~#]
                :   the following characters up to the end of the spe-
                    cification string are included in the character set.
                    This way you can include any character except binary
                    null (at least under unix).

              For example, a1:$% selects lowercase characters, digits and the dollar and percent signs.
```
- **Попробуйте восстановить пароль, например для архива archive3.zip, используя следующую команду**
```
fcrackzip -vul 3-3 -c a archive3.zip
```
```bash
sysadmin@deb10-1:~/infsec/lab1$ fcrackzip -vul 3-3 -c a archive3.zip
found file 'opentext.txt', (size cp/uc    278/   447, flags 9, chk 7850)


PASSWORD FOUND!!!!: pw == net
```
# Задание 2. Исследование времени восстановления паролей
Для определения точного времени, необходимого на восстановление пароля от зашифрованного архива мы будем использовать утилиту time.
```shell
sysadmin@deb10-1:~/infsec/lab1$ time fcrackzip -vul 2-2 -c a archive2.zip 
found file 'opentext.txt', (size cp/uc    278/   447, flags 9, chk 7850)


PASSWORD FOUND!!!!: pw == ne

real	0m0,018s
user	0m0,011s
sys	0m0,004s
sysadmin@deb10-1:~/infsec/lab1$ time fcrackzip -vul 3-3 -c a archive3.zip 
found file 'opentext.txt', (size cp/uc    278/   447, flags 9, chk 7850)


PASSWORD FOUND!!!!: pw == net

real	0m0,089s
user	0m0,059s
sys	0m0,017s

```

| K, Длина пароля | T1, Время, мс | T2, Время, мс | T3, Время, мс | T, Среднее время, мс |
| --------------- | ------------- | ------------- | ------------- | -------------------- |
| 2               | 18            | 15            | 17            | 16,66666667          |
| 3               | 89            | 89            | 87            | 88,33333333          |
| 4               | 2201          | 2166          | 2162          | 2176,333333          |
| 5               | 52652         | 52033         | 52490         | 52391,66667          |


# Задание 3. Подсчёт скорости перебора паролей
Сложность перебора (С) оценивается как мощность алфавита (N) возведенной в степень длины пароля (K). Суммарное кол-во символов у всех вариантов пароля. 
$$C=N^K$$
Скорость перебора S - это сложность перебора (С), разделить на время (T)
$$S=\frac{C}{T}=\frac{N^k}{T}$$
Исходя из полученных в предыдущем пункте данных о времени выполнения восстановления пароля *оцените приблизительную скорость перебора* в символах в миллисекунду, выполнив подсчет для различных длин пароля. используйте калькулятор. Мощность алфавита - 26 (символы нижнего регистра, англ).

- Для длин от 2 до 5 среднее время должно быть измерено в Задании 2, а скорость вычислена. Для длин больших 5 необходимо ***оценить предполагаемое время*** на основании ***оценочной скорости перебора***.

Обратите внимание, что скорость перебора должна возрастать по мере увеличения сложности, связано это с тем, что чем выше сложность тем меньше в полученном результате накладных расходов, связанных с выполнением вспомогательного кода, выполнением системных вызовов, ввода-вывода и т.п.

- Используя полученную оценочную скорость перебора (S), оцените предполагаемое время в миллисекундах-секундах-минутах-часах, необходимое для перебора пароля длиной 6-8 символов

| K, Длина пароля | T, Среднее время, мс | S, Скорость перебора (символ/мс) |
| --------------- | -------------------- | -------------------------------- |
| 2               | 16,66666667          | 40,55999999                      |
| 3               | 88,33333333          | 198,9735849                      |
| 4               | 2176,333333          | 209,9751877                      |
| 5               | 52391,66667          | 226,7798823                      |
| 6               | ***1283496,284***    | ***240,683031***                 |
| 7               | ***31548492,48***    | ***254,5861797***                |
| 8               | ***777785343,7***    | ***268,4893284***                |
- Попробуйте изменить мощность словаря, используемого при переборе, убрав ограничение на перебор только по буквам нижнего регистра
```shell
sysadmin@deb10-1:~/infsec/lab1$ time fcrackzip -vul 4-4 archive4.zip
found file 'opentext.txt', (size cp/uc    278/   447, flags 9, chk 7850)
checking pw l5N~                                    

PASSWORD FOUND!!!!: pw == netl

real	0m57,709s
user	0m44,215s
sys	0m12,993s
sysadmin@deb10-1:~/infsec/lab1$ time fcrackzip -vul 4-4 archive4.zip
found file 'opentext.txt', (size cp/uc    278/   447, flags 9, chk 7850)
checking pw l5N~                                    

PASSWORD FOUND!!!!: pw == netl

real	0m58,321s
user	0m44,639s
sys	0m13,192s

```
Мощность словаря была 26 а стала 80. Сложность перебора увеличилась в 89 раз (была 456976, стала 40960000)

После изменения мощности словаря, используемого в переборе, время перебора увеличилось примерно в 2,5 раза.

Скорость перебора с увеличением сложности перебора, как и предполагалось, увеличилась.
Была 209 символов/мс, стала 7528 символов/мс.

# Задание 4. Отчёт по лабораторной
![[lab1-report.2024.09.25-17_16_17.txt]]

