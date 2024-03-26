INSERT INTO retail_center(type, address) VALUES
('Grocery', '123 Main St.'),
('Clothing', '456 Elm St.'),
('Electronics', '789 Oak St.'),
('Home goods', '321 Maple Ave.'),
('Pet supplies', '654 Birch Rd.'),
('Sporting goods', '987 Pine St.'),
('Beauty products', '246 Cedar Dr.'),
('Toys and games', '135 Walnut St.'),
('Office supplies', '864 Cherry Ln.'),
('Books and music', '579 Spruce St');

select * from fill_shipped_item(1000000);

select * from fill_transportation_event(10);

select * from fill_item_transportation(20000000);
