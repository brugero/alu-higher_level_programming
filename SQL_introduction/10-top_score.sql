-- Script to list all records of the table second_table
-- of the specified database, ordered by score (top first).
-- Results should display both the score and the name (in this order).
-- The database name will be passed as an argument to the mysql command.

-- The following line is a comment and will not be executed by MySQL.
-- It shows how the script might be called from the command line:
-- mysql -u <your_username> -p <your_database_name> < path/to/this_script.sql

-- Select the score and name from second_table, ordered by score descending.
SELECT score, name FROM second_table ORDER BY score DESC;
