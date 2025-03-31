-- Script to list all records of the table second_table
-- of the specified database where name is not NULL.
-- Results should display the score and the name (in this order).
-- Records should be listed by descending score.
-- The database name will be passed as an argument to the mysql command.

-- The following line is a comment and will not be executed by MySQL.
-- It shows how the script might be called from the command line:
-- mysql -u <your_username> -p <your_database_name> < path/to/this_script.sql

-- Select score and name from second_table,
-- where name is not NULL, ordered by score descending.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
