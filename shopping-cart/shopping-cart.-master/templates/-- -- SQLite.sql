-- -- SQLite
-- CREATE TABLE Transactions(
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     user_id INTEGER NOT NULL,
--     name TEXT NOT NULL,
--     shares INTEGER NOT NULL,
--     price NUMERIC NOT NULL,
--     type TEXT NOT NULL,
--     symbol TEXT NOT NULL,
--     time TIMSTAMP DEFAULT CURRENT_TIMESTAMP,
--     FOREIGN KEY(user_id) REFERENCES users(id)  
-- );