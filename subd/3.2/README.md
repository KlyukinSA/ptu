
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

# Время доступа
```
create table access_time(time INTERVAL, row_size INT);
psql lab32 -f measure.sql
python3 show_measures.py
```
