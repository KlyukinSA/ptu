create table if not exists retail_center (
    id serial primary key,
    type varchar(255),
    address varchar(255)
);
create table if not exists shipped_item (
    item_num serial primary key,
    retail_center_id int references retail_center,
    weight numeric,
    dimension numeric,
    insurance_amt numeric,
    destination varchar(255),
    final_delivery_date date
);
create table if not exists transportation_event (
    seq_number serial primary key,
    type varchar(255),
    delivery_route varchar(255)
);
create table if not exists item_transportation (
    transportation_event_seq_number int references transportation_event,
    shipped_item_item_num int references shipped_item,
    primary key (transportation_event_seq_number, shipped_item_item_num)
);

CREATE or replace function fill_shipped_item(num integer)
returns boolean
AS $$
    import random
    import string
    from datetime import datetime, timedelta
    rv = plpy.execute('SELECT * FROM retail_center')
    street = ["Tverskaya Street", "Nevsky Prospect", "Arbat Street", "Bolshaya Sadovaya Street", "Petrovka Street", "Kuznetsky Most Street", "Leninsky Prospect", "Komsomolsky Prospect", "Novy Arbat Street", "Vozdvizhenka Street", "Kutuzovsky Prospect", "Varvarka Street", "Pokrovka Street", "Gorky Street", "Ostozhenka Street", "Prechistenka Street", "Rozhdestvenka Street", "Solyanka Street", "Kropotkinskaya Street", "Novaya Basmannaya Street", "Yauzsky Boulevard"]
    city = ["Moscow", "St. Petersburg", "Kazan", "Nizhny Novgorod", "Novosibirsk", "Yekaterinburg", "Samara", "Omsk", "Chelyabinsk", "Rostov-on-Don", "Ufa", "Volgograd", "Perm", "Krasnoyarsk", "Voronezh", "Saratov", "Krasnodar", "Tolyatti", "Izhevsk", "Barnaul"]
    plan = plpy.prepare("INSERT INTO shipped_item(retail_center_id, weight, dimension, insurance_amt, destination, final_delivery_date) VALUES($1, $2, $3, $4, $5, $6)", ["int", "numeric(19, 0)", "numeric(19, 0)", "numeric(19, 0)", "varchar(255)", "timestamp"])
    for i in range(0, num):
        retailId = random.randint(1, len(rv))
        weight = random.randint(1, 1000000)
        dimension = random.randint(1, 1000000)
        insuranceAmt = random.randint(1, 10000000)
        destination = city[random.randint(0, len(city) - 1)] + ' ' + str(random.randint(0, 199)) + ' ' + street[random.randint(0, len(street) - 1)] + ' ' + random.choice(string.ascii_letters.upper())
        delta_time = (24 * 3600) * random.randint(1, 365)
        final_delivery_date = datetime.strptime('07/28/2014 18:54:55.099', '%m/%d/%Y %H:%M:%S.%f') + timedelta(seconds=delta_time)
        plpy.execute(plan, [retailId, weight, dimension, insuranceAmt, destination, final_delivery_date])
    return True
$$ LANGUAGE plpython3u;

CREATE or replace function fill_transportation_event(num integer)
returns boolean
AS $$
    import random
    import string
    from datetime import datetime, timedelta
    event_t = ["Overload", "Registration documents", "Waiting sending", "Sending", "Storing", "Order Assembly", "Accounting expectations", "Passport control","Expertise in the FSB", "Arrived", "Sorted"]
    d_route = ["Moscow", "St. Petersburg", "Kazan", "Nizhny Novgorod", "Novosibirsk", "Yekaterinburg", "Samara", "Omsk", "Chelyabinsk", "Rostov-on-Don", "Ufa", "Volgograd", "Perm", "Krasnoyarsk", "Voronezh", "Saratov", "Krasnodar", "Tolyatti", "Izhevsk", "Barnaul"]
    plan = plpy.prepare("INSERT INTO transportation_event(type, delivery_route) VALUES($1, $2)", ["varchar(255)", "varchar(255)"])
    for i in range(0, num):
        ev = event_t[random.randint(0, len(event_t) - 1)]
        route = d_route[random.randint(0, len(d_route) - 1)] + ' ' + d_route[random.randint(0, len(d_route) - 1)] + ' ' + str(random.randint(1, 10000))
        plpy.execute(plan, [ev, route])
    return True
$$ LANGUAGE plpython3u;

CREATE or replace function fill_item_transportation(num integer)
returns boolean
AS $$
    import random
    from datetime import datetime, timedelta
    rv = plpy.execute('SELECT item_num FROM shipped_item order by item_num DESC LIMIT 1')
    rv = rv[0]["item_num"]
    dv = plpy.execute('SELECT seq_number FROM transportation_event order by seq_number DESC LIMIT 1')
    dv = dv[0]["seq_number"]
    plan = plpy.prepare("INSERT INTO item_transportation(transportation_event_seq_number, shipped_item_item_num) VALUES($1, $2)", ["int", "int"])
    for i in range(0, num):
        one = random.randint(1, rv)
        two = random.randint(1, dv)
        try:
            plpy.execute(plan, [two, one])
        except plpy.SPIError:
            continue
    return True
$$ LANGUAGE plpython3u;
