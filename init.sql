CREATE TABLE IF NOT EXISTS raw_data (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    symbol VARCHAR(10) NOT NULL,
    current_price NUMERIC NOT NULL,
    market_cap NUMERIC,
    total_supply NUMERIC,
    high_24h NUMERIC,
    low_24h NUMERIC,
    ath NUMERIC,
    ath_date TIMESTAMP,
    atl NUMERIC,
    atl_date TIMESTAMP,
    last_updated TIMESTAMP NOT NULL,
    save_timestamp TIMESTAMP NOT NULL
);
