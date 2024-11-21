# Задание
Написать на python с помощью hashlib программу которая читает файлы 1.txt - 10.txt из текущей дирекотрии, вычисляет их хуш-сумму с помощью алгоритма sha256, записывает полученные хеш-суммы в текстовый файл HashList.txt, запускает программу FC, заново вычисляет хеш-суммы файлов, сравнивает полученные хеш-суммы со списками HashList.txt и VirusHashList.txt в текущей диктоктории, состоящими из строк хеш-сумм, печатает список хеш-сумм оригинальных, измененных (хеш-сумма отличается от первоначальной в HashList.txt) и зараженных (хеш-сумма находится в VirusHashList.txt) файлов, удаляет зараженные файлы
# Результат
```
sysadmin@deb10-1:~/infsec/lab5$ bash test.sh 
Программа изменяет исходные файлы
Выберите вариант от 1 до 25 (Номер в списке группы)
10
Выполнено
Измененные файлы:
1.txt
3.txt
5.txt
8.txt
Зараженные файлы:
1.txt
3.txt
report.txt
origin hash:
1.txt - 5dedc882b11536c40b6096518e1ed04acc875edc2e21e3a1123d9aeaf04b34a3
2.txt - a8c834a2f880d1ae1f5ad335900eb100c7245b80908887868cbd6fe3f12dff7a
3.txt - 024903b541eee897a9767508d6c663140756a62d80d3d3996e67b400e54cf0c1
4.txt - 1a8d279e1b19dc0a5d9561bac282923a79ac89defac58bb721a3c4c5ff95fb19
5.txt - a2440c1ee8b86ebfe97f43cf6806c63e1af5ad0be86be81c6f7ed7fc6e40538f
6.txt - 3a83d6657f2d53fc11156870d8676c4cdf12ad41b0f9a3d77ff3524348a90d44
7.txt - 572fc7030dc5c69aeaa7c1fd95f1feffc378dd2ffea448f0f4ddcd4ce38ed59e
8.txt - 2ca4dafdfd2094bd48eb80e1d6c6c745a7cb0a965c85410b03d228f2082a1a89
9.txt - 118265b3a3ee259a8dd9643e2f9aac610fb5da9780c37016bfbf823b9804d57f
10.txt - 234de7f5f6512501f7f12b4075fc0d541d77440677e9eab0ad093d270fbd54ad
changed hash:
1.txt - d8df840b6ac5246e0c571df94d2fa285b4fe2763a02bcddca1feccdad3fe420e
3.txt - 60b3564377f52f2bb38a37e61c4cd8f32eac5ac346f7a1ee39a6b34f77d42631
5.txt - 3c12d0b76e66f228360db3a648cad82ef2651d663673873ba7c28299a4f6a00a
8.txt - eeac4a53b9084a49bef95ae586a6f2a21cd466cddb523b7a28e46ef528c02328
infected hash:
1.txt - d8df840b6ac5246e0c571df94d2fa285b4fe2763a02bcddca1feccdad3fe420e
3.txt - 60b3564377f52f2bb38a37e61c4cd8f32eac5ac346f7a1ee39a6b34f77d42631
```
