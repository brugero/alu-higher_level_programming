-- Script to create the table second_table and add multiple rows
-- The database name will be passed as an argument to the mysql command

-- The following line is a comment and will not be executed by MySQL
-- It shows how the script might be called from the command line:
-- mysql -u <your_username> -p <your_database_name> < path/to/this_script.sql

-- Create the table second_table if it doesn't exist
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Add multiple rows to the second_table
INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
