CREATE DATABASE new_ayction;
USE new_ayction;

CREATE TABLE auctions (
    auction_id INT AUTO_INCREMENT PRIMARY KEY,
    auction_date DATE,
    auction_time TIME,
    location VARCHAR(255),
    features TEXT
);

CREATE TABLE persons (
    person_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(255),
    date_of_birth DATE,
    address VARCHAR(255),
    phone_number VARCHAR(20),
    buyer_id INT,
    seller_id INT
);

CREATE TABLE items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    auction_id INT,
    lot_number INT,
    start_price DECIMAL(10, 2),
    short_description TEXT,
    sale_price DECIMAL(10, 2),
    seller_id INT,
    buyer_id INT,
    CONSTRAINT fk_auction FOREIGN KEY (auction_id) REFERENCES auctions(auction_id),
    index(seller_id),
    index(buyer_id)
);

INSERT INTO auctions (auction_date, auction_time, location, features)
VALUES
    ('2023-09-19', '12:00:00', 'Kyiv', 'Antiques'),
    ('2023-09-20', '14:30:00', 'Lviv', 'Paintings'),
    ('2023-09-21', '11:45:00', 'Kharkiv', 'Silver and Jewelry'),
    ('2023-09-22', '16:15:00', 'Odessa', 'Furniture and Wood Crafts'),
    ('2023-09-23', '13:30:00', 'Dnipro', 'Ceramics and Porcelain'),
    ('2023-09-24', '15:00:00', 'Zaporizhia', 'Antique Paintings'),
    ('2023-09-25', '14:45:00', 'Lutsk', 'Coins and Banknotes'),
    ('2023-09-26', '12:30:00', 'Ivano-Frankivsk', 'Rare Books'),
    ('2023-09-27', '13:00:00', 'Ternopil', 'Sporting Goods'),
    ('2023-09-28', '11:00:00', 'Rivne', 'Musical Instruments');

INSERT INTO persons (full_name, date_of_birth, address, phone_number, seller_id, buyer_id)
VALUES
    ('Marina Kozlova', '1982-06-25', '567 Pine Street, Kyiv', '+380-44-987-6543', 1, null),
    ('Andriy Pavlenko', '1976-10-12', '234 Forest Street, Lviv', '+380-32-555-1234', 2, null ),
    ('Tetiana Ignatenko', '1989-03-15', '789 Oak Street, Kharkiv', '+380-57-2345-6789', 3, null),
    ('Valentin Sidorov', '1985-09-20', '123 Cherry Street, Odessa', '+380-48-987-5678', 4 , null),
    ('Nadiya Petrenko', '1978-12-05', '456 Linden Street, Dnipro', '+380-56-555-7890', 5, null),
    ('Maxim Zhukov', '1992-04-18', '101 Maple Street, Zaporizhia', '+380-61-1234-5678', 6, null),
    ('Olga Lysenko', '1984-07-30', '888 Chestnut Street, Lviv', '+380-32-777-8888', 7, null),
    ('Oleksiy Zaytsev', '1981-08-18', '777 Horse Chestnut Street, Kyiv', '+380-44-777-1234', 8, null),
    ('Lyudmyla Hryhorova', '1974-11-10', '999 Pine Street, Kharkiv', '+380-57-999-5555', 9, null),
    ('Petro Koval', '1986-02-25', '321 Forest Street, Dnipro', '+380-56-321-9876', 10, null),
    ('Maria Prykhidko', '1985-05-12', '789 Pine Street, New York', '+380-93-843-4982', null, 1),
    ('Mykhailo Wilson', '1980-07-20', '234 Birch Street, London', '+380-66-781-6435', null, 2),
    ('Sarah Lee', '1988-01-15', '567 Maple Street, Paris', '+380-53-736-9752', null, 3),
    ('Olena Kovalenko', '1983-09-30', '123 Main Street, Kyiv', '+380-44-123-4567', null, 4),
    ('Vasyl Petrenko', '1975-12-15', '456 Cherry Street, Lviv', '+380-32-987-6543', null, 5),
    ('Andriy Ivanov', '1990-03-22', '789 Oak Street, Odessa', '+380-48-2345-6789', null, 6),
    ('Yulia Moroz', '1987-04-10', '567 Pine Street, Kharkiv', '+380-57-555-7890', null, 7),
    ('Oleg Sidorov', '1995-11-01', '456 Linden Street, Dnipro', '+380-56-444-8888', null, 8),
    ('Tetiana Marchenko', '1989-07-25', '101 Maple Street, Zaporizhia', '+380-61-777-9999', null, 9),
    ('Ivan Koval', '1983-12-14', '888 Chestnut Street, Lviv', '+380-32-555-1111', null , 10);

INSERT INTO items (auction_id, lot_number, start_price, short_description, sale_price, seller_id, buyer_id)
VALUES
    (1, 1001, 500.00, 'Antique Vase', 750.00, 1, 1),
    (1, 1002, 300.00, 'Painting', 450.00, 2, 2),
    (2, 2001, 150.00, 'Rare Book', 200.00, 3, 3),
    (2, 2002, 400.00, 'Precious Diamond', 600.00, 5, 4),
    (2, 2003, 1500.00, 'One-of-a-Kind Item', 4000.00, 7, 5),
    (3, 3001, 200.00, 'Sculpture', 500.00, 8, 6),
    (3, 3002, 100.00, 'Statuette', 200.00, 8, 7),
    (3, 3003, 700.00, 'Painting "Sunflowers"', 900.00, 6, 8),
    (4, 4001, 1500.00, 'Rare Vintage Car', 1800.00, 4, 10),
    (4, 4002, 300.00, 'Collectible Coin', 350.00, 9, 10);

SELECT * FROM auctions;

SELECT * FROM persons;

SELECT * FROM items;

select * from persons where buyer_id is not null
