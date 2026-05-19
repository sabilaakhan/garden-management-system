
CREATE DATABASE IF NOT EXISTS garden_db;
USE garden_db;
CREATE table users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE gardens (
    garden_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(150) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_gardens_user
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
CREATE INDEX idx_gardens_user_id
ON gardens(user_id);

CREATE TABLE plants (
    plant_id INT AUTO_INCREMENT PRIMARY KEY,
    garden_id INT NOT NULL,
    user_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    species VARCHAR(100) NOT NULL,
    planted_date DATE NOT NULL,
    notes TEXT,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_plants_garden
        FOREIGN KEY (garden_id)
        REFERENCES gardens(garden_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT fk_plants_user
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT chk_plant_name
        CHECK (CHAR_LENGTH(name) >= 2)
);

CREATE INDEX idx_plants_garden_id
ON plants(garden_id);
CREATE INDEX idx_plants_user_id
ON plants(user_id);
CREATE INDEX idx_plants_species
ON plants(species);

CREATE TABLE growth_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    plant_id INT NOT NULL,
    height DECIMAL(5,2) NOT NULL,
    leaf_count INT NOT NULL,
    notes TEXT,
    recorded_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_growthlogs_plant
        FOREIGN KEY (plant_id)
        REFERENCES plants(plant_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
CONSTRAINT chk_height
        CHECK (height >= 0),
CONSTRAINT chk_leaf_count
        CHECK (leaf_count >= 0)
);
CREATE INDEX idx_growthlogs_plant_id
ON growth_logs(plant_id);
CREATE INDEX idx_growthlogs_recorded_at
ON growth_logs(recorded_at);
CREATE TABLE reminders (
    reminder_id INT AUTO_INCREMENT PRIMARY KEY,
    plant_id INT NOT NULL,
    reminder_type VARCHAR(50) NOT NULL,
    due_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_reminders_plant
        FOREIGN KEY (plant_id)
        REFERENCES plants(plant_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT chk_reminder_status
        CHECK (status IN ('Pending', 'Completed', 'Missed'))
);

CREATE INDEX idx_reminders_plant_id
ON reminders(plant_id);
CREATE INDEX idx_reminders_due_date
ON reminders(due_date);

