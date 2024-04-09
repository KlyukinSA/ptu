DO $$
DECLARE
    row_data RECORD;
    start_time TIMESTAMP;
    end_time TIMESTAMP;
    access_time INTERVAL;
    row_size_bytes INT;
    dummy_variable TEXT;
BEGIN
    FOR row_data IN SELECT roles_name, pg_column_size(roles_name) as size_v FROM actor ORDER BY size_v LOOP
        start_time := clock_timestamp();
        dummy_variable := row_data.roles_name->'roles'->0->>'year';
        end_time := clock_timestamp();
         
        access_time := end_time - start_time;
        row_size_bytes := row_data.size_v;

        insert into access_time (time, row_size) values (access_time, row_size_bytes);
    END LOOP;
END $$;
