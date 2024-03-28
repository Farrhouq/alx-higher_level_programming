ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert all tables within the database to UTF-8
SELECT 
    CONCAT('ALTER TABLE `', table_name, '` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;') AS stmt
FROM 
    information_schema.tables
WHERE 
    table_schema = 'hbtn_0c_0' AND table_type = 'BASE TABLE';
