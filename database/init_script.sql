CREATE TABLE IF NOT EXISTS sources (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
    
);

CREATE TABLE IF NOT EXISTS urls (
    id SERIAL PRIMARY KEY,
    value TEXT NOT NULL,
    inserted_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    source_id INTEGER NOT NULL,
    FOREIGN KEY (source_id) REFERENCES sources (id)
);

CREATE TABLE IF NOT EXISTS ip_addresses (
    id SERIAL PRIMARY KEY,
    value TEXT NOT NULL,
    inserted_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    source_id INTEGER NOT NULL,
    FOREIGN KEY (source_id) REFERENCES sources (id)
);