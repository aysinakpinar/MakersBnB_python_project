DROP TABLE IF EXISTS spaces;
DROP TABLE IF EXISTS user_details;


-- Then, we recreate them
-- Create or update the database
CREATE TABLE IF NOT EXISTS "user_details" (
    user_id SERIAL PRIMARY KEY,
    user_username VARCHAR(50) NOT NULL UNIQUE,
    user_password_hash VARCHAR(255) NOT NULL,
    user_email VARCHAR(100) NOT NULL UNIQUE,
    user_role VARCHAR(50) NOT NULL,
    user_created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS "spaces" (
    space_id SERIAL PRIMARY KEY,
    space_name VARCHAR(100) NOT NULL,
    space_address VARCHAR(255) NOT NULL,
    space_description TEXT,
    space_price NUMERIC(10, 2) NOT NULL,
    space_lister_id INT NOT NULL,
    space_active VARCHAR(50) DEFAULT 'Available',
    space_created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    space_updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_space_lister FOREIGN KEY (space_lister_id) REFERENCES "user_details" (user_id) ON DELETE CASCADE
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO user_details (user_username, user_password_hash, user_email, user_role)
VALUES ('john_doe', '$2a$12$X5qvZad9iXsT1fnjFvjqNuESs0U6hKFH3w55dPAdIu5G75E0Q2iK', 'john.doe@example.com', 'user');
INSERT INTO user_details (user_username, user_password_hash, user_email, user_role)
VALUES ('alice_smith', '$2a$12$8dbW8ZCqzJjzDwFJ7tLg/d6N7OrC6Eczw8w0YhS6nVppGKmjNNO5q', 'alice.smith@example.com', 'host');
INSERT INTO user_details (user_username, user_password_hash, user_email, user_role)
VALUES ('bob_jones', '$2a$12$R6vsG0.r1tJHGmRzR5lFdL/29KQmdErfuLrD9k2l3TKHqS7zEy/oq', 'bob.jones@example.com', 'user');
INSERT INTO user_details (user_username, user_password_hash, user_email, user_role)
VALUES ('susan_lee', '$2a$12$w.mgVZy3cFdyU5NoVJ7gsdkjfN1OAxY4h./RHKZIM6aP2L5ouAA9S', 'susan.lee@example.com', 'host');
INSERT INTO user_details (user_username, user_password_hash, user_email, user_role)
VALUES ('mike_brown', '$2a$12$kjJovGn1Uvc5sg6me5RgI4C/zmfuWo8u3.IJajDkzjRkj0ZK5L6y6', 'mike.brown@example.com', 'user');


INSERT INTO spaces (space_name, space_address, space_description, space_price, space_lister_id, space_active)
VALUES ('Downtown Loft', '123 Main St, Manchester, Greater Manchester, United Kingdom', 'A stylish 2-bedroom loft in the heart of downtown.', 450, 1, 'Available');
INSERT INTO spaces (space_name, space_address, space_description, space_price, space_lister_id, space_active)
VALUES ('Seaside Villa', '456 Ocean Ave, Brighton, East Sussex, United Kingdom', 'A luxurious seaside villa with an infinity pool and ocean views.', 850, 2, 'Unavailable');
INSERT INTO spaces (space_name, space_address, space_description, space_price, space_lister_id, space_active)
VALUES ('Mountain Retreat', '789 Alpine Rd, Snowdonia, Gwynedd, Wales, United Kingdom', 'A cozy cabin retreat perfect for a weekend getaway.', 1000, 3, 'Requested');
INSERT INTO spaces (space_name, space_address, space_description, space_price, space_lister_id, space_active)
VALUES ('City Penthouse', '101 Skyline Blvd, London, Greater London, United Kingdom', 'A modern penthouse with panoramic city views and top-tier amenities.', 900, 4, 'Available');
INSERT INTO spaces (space_name, space_address, space_description, space_price, space_lister_id, space_active)
VALUES ('Suburban House', '202 Maple Dr, Birmingham, West Midlands, United Kingdom', 'A spacious 4-bedroom family home with a large backyard and garage.', 600, 5, 'Unavailable');
INSERT INTO spaces (space_name, space_address, space_description, space_price, space_lister_id, space_active)
VALUES ('Urban Studio', '78 High St, Manchester, Greater Manchester, United Kingdom', 'A chic and compact studio apartment in the city center, ideal for young professionals.', 200, 1, 'Available');
INSERT INTO spaces (space_name, space_address, space_description, space_price, space_lister_id, space_active)
VALUES ('Riverside Cottage', '34 River Rd, Oxford, Oxfordshire, United Kingdom', 'A quaint cottage by the river with a peaceful garden and walking trails.', 300, 1, 'Requested');
INSERT INTO spaces (space_name, space_address, space_description, space_price, space_lister_id, space_active)
VALUES ('Country Estate', '543 Greenfield Rd, Surrey, South East England, United Kingdom', 'An expansive 5-bedroom estate with private gardens, a pool, and a tennis court.', 150, 1, 'Available');
INSERT INTO spaces (space_name, space_address, space_description, space_price, space_lister_id, space_active)
VALUES ('Lochside Lodge', '123 Loch Rd, Inverness, Scotland, United Kingdom', 'A serene lodge overlooking a loch, perfect for nature lovers and outdoor enthusiasts.', 200, 1, 'Unavailable');
INSERT INTO spaces (space_name, space_address, space_description, space_price, space_lister_id, space_active)
VALUES ('Downtown Condo', '56 Park Ave, Edinburgh, Scotland, United Kingdom', 'A modern 2-bedroom condominium with great views and close proximity to shops and restaurants.', 300, 1, 'Available');