CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    level INT,
    type VARCHAR(255),
    category VARCHAR(255),
    rarity_value FLOAT NOT NULL,
    weight FLOAT,
    value INT
);