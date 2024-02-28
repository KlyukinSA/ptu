CREATE OR REPLACE FUNCTION check_price_range()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.price < 0 THEN
        RAISE EXCEPTION 'Price cannot be negative!';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER check_price_trigger
BEFORE INSERT OR UPDATE ON Tour
FOR EACH ROW
EXECUTE FUNCTION check_price_range();



INSERT INTO Tour (price, place) VALUES (100, 'London'); -- Допустимая вставка
INSERT INTO Tour (price, place) VALUES (-50, 'Paris'); -- Вставка с отрицательной ценой
