-- Convert the database to UTF-8

-- For each database:
ALTER DATABASE
    hbtn_0c_0
    CHARACTER SET = utf8mb4
    COLLATE = utf8mb4_unicode_ci;

-- For each table:
ALTER TABLE
    first_table
    CONVERT TO CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

-- For each column:
ALTER TABLE
    first_table
    CHANGE name name
    VARCHAR(256)
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;
