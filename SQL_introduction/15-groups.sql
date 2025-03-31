-- Script to list the number of records with the same score
-- in the table second_table of the specified database.
-- The result should display:
-- - the score
-- - the number of records for this score with the label number
-- The list should be sorted by the number of records (descending).
-- The database name will be passed as an argument to the mysql command.

-- The following line is a comment and will not be executed by MySQL.
-- It shows how the script might be called from the command line:
-- mysql -u <your_username> -p <your_database_name> < path/to/this_script.sql

-- Group records by score and count the occurrences of each score,
-- then order the results by the count in descending order.
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
