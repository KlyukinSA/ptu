SELECT dimension, insurance_amt FROM shipped_item WHERE dimension between 20000 and 25000 and insurance_amt % 21 = 0;

CREATE INDEX shipped_item_dimension_index ON shipped_item(dimension) WHERE insurance_amt % 21 = 0;


SELECT shipped_item.dimension, transportation_event.type FROM shipped_item
JOIN item_transportation ON item_transportation.shipped_item_item_num = shipped_item.item_num
JOIN transportation_event ON transportation_event.seq_number = item_transportation.transportation_event_seq_number
WHERE dimension < 500 and type = 'Waiting sending';

CREATE INDEX shipped_item_dimension_index_without_perscent ON shipped_item(dimension);


select destination from shipped_item where to_tsvector('english', "destination") @@ plainto_tsquery('St. Petersburg Nevsky Prospect');

CREATE INDEX shipped_item_destination_index ON shipped_item USING GIN(to_tsvector('english', destination));
