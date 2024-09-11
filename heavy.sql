-- Drop the Users table if it exists
DROP TABLE IF EXISTS Sandwiches;

-- Create the Users table
CREATE TABLE IF NOT EXISTS Sandwiches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL,
    blog TEXT NOT NULL UNIQUE,
    author TEXT,
    thumbnail TEXT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Added timestamp for record creation
);
