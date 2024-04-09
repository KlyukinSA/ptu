
actors.list.txt это 2 670 000 записей, 1,3G

обработка actors.list.txt в main.py у меня это 9 минут. на выходе 2,8G



```sh
cd python-database-parser
python main.py
psql lab32
```

```sql
CREATE TABLE actor (
    id BIGSERIAL PRIMARY KEY,
    actor_name VARCHAR(255),
    roles_name JSONB
);

\copy actor(actor_name, roles_name) FROM 'output.txt' WITH DELIMITER E'\t' ESCAPE '\' CSV

-- COPY 2673783

select * from actor limit 3;

--   3 | Homo $     | {"roles": [{"year": 1986, "title": "Nykytaiteen museo", "credit": "25", "character name": "Himself"}, {"year": 1985, "title": "Suuri illusioni", "credit": "22", "character name": "Guests"}]}
```

# Запросы

## Количество серий, в которых снимался каждый актер, в порядке убывания

```sql
SELECT DISTINCT id, actor_name, COUNT(*) as series_amount
FROM (
    SELECT id, actor_name, jsonb_array_elements(roles_name -> 'roles') as role
    FROM actor LIMIT 1000
) AS actor_role
WHERE actor_role.role ? 'series_name'
GROUP BY id, actor_name 
order by series_amount desc;
```

## Продолжительность карьеры каждого актера

```sql
select id, actor_name,
    (MAX((actor_role.role->>'year')::int) - MIN((actor_role.role->>'year')::int) + 1) as career 
from (
    select id, actor_name, jsonb_array_elements(roles_name -> 'roles') as role from actor limit 100
) as actor_role
group by id, actor_name;
```

## Актеры, которые иглали Chorus'а в The Emancipation of Anemone

SELECT actor_name FROM actor
WHERE roles_name @> '{"roles" : [{"title": "The Emancipation of Anemone", "character name": "Chorus"}]}'::jsonb;


SELECT actor_name FROM actor WHERE roles_name @> '{"roles" : [{"title": "La huella del doctor Ernesto Guevara", "character name": "Himself"}]}'::jsonb;
 Carlos 'Calica' Ferrer

## Годы съемок, начиная с 2000

SELECT year from (
    SELECT jsonb_path_query("roles_name", '$.roles[*].year') as year from actor
) as temp WHERE year::integer > 2000 limit 5;


## Записи, уходящие в toast

SELECT id, pg_column_size(roles_name) FROM actor WHERE pg_column_size(roles_name) > 2048
ORDER BY pg_column_size(roles_name) DESC;

SELECT count(*) FROM actor WHERE pg_column_size(roles_name) > 2048;

## Год второй роли 11-го актера всеми способами

```
lab32=# select roles_name->'roles'->1->'year' from actor where id = 11;
 ?column? 
----------
 2011

lab32=# select roles_name['roles'][1]['year'] from actor where id = 11;
 roles_name 
------------
 2011

lab32=# select jsonb_path_query("roles_name", '$.roles[1].year') as year from actor where id = 11;
 year 
------
 2011
```

# Время доступа
```
create table access_time(time INTERVAL, row_size INT);
psql lab32 -f measure.sql
python3 show_measures.py
```

# Изменение year у первой роли

```sql
SELECT id, MAX(JSON_ARRAY_LENGTH((roles_name -> 'roles')::json)) as len
FROM actor 
GROUP BY id
ORDER BY len DESC
LIMIT 5
```

```sql
SELECT id
 FROM actor
 WHERE JSON_ARRAY_LENGTH((roles_name -> 'roles')::json) = 1
 LIMIT 1
```

```sql
SELECT pg_database_size('lab32');
```
```sql
UPDATE actor
SET roles_name = jsonb_set(
    roles_name,
    '{roles, 0, year}',
    to_jsonb(2000)::jsonb
)
WHERE id = 2418373;
```
