import os
import sqlite3

db_dir = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(db_dir, exist_ok=True)
db_path = os.path.join(db_dir, "scouted_players.db")


conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute(
"""
CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    current_club TEXT,
    league TEXT,
    position TEXT NOT NULL,
    birth_country TEXT,
    eligibility_type TEXT, --e.g "Domestic", "Dual Heritage"
    cap_tied INTEGER -- 0 for No (Eligible), 1 for Yes (Locked to another nation)
)
"""
)

cursor.execute(
"""CREATE TABLE IF NOT EXISTS stats (
    stat_id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER NOT NULL,
    season TEXT NOT NULL,
    minutes_played INTEGER,
    appearances INTEGER,
    goals_per90 REAL,
    assists_per90 REAL,
    interceptions_per90 REAL,
    tackles_per90 REAL, 
    progressions_per90 REAL,
    FOREIGN KEY (player_id) REFERENCES players(player_id)              
)
"""
)

test_players = [
    ("Victor Osimhen", "Galatasaray", "Süper Lig", "Forward", "Nigeria", "Domestic", 1),
    ("Ademola Lookman", "Atletico Madrid", "La Liga", "Forward", "England", "Dual Heritage", 1),
    ("Michael Olise", "Bayern Munich", "Bundesliga", "Midfielder", "France", "Dual Heritage", 1),
    ("Eberechi Eze", "Arsenal", "Premier League", "Midfielder", "England", "Dual Heritage", 1),
    ("Bukayo Saka", "Arsenal", "Premier League", "Midfielder", "England", "Domestic", 1),
    ("Nathan Tella", "Bayer Leverkusen", "Bundesliga", "Forward", "England", "Dual Heritage", 1),
    ("Qudus Akanni", "Remo Stars", "NPFL", "Midfielder", "Nigeria", "Domestic", 0),

]

cursor.execute("DELETE FROM players")  # Clear existing data before inserting new test data
cursor.execute("DELETE FROM stats")  # Clear existing data before inserting new test data

for p in test_players:

    # Insert player
    cursor.execute(
        """
        INSERT INTO players (
            name,
            current_club,
            league,
            position,
            birth_country,
            eligibility_type,
            cap_tied
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        p
    )

    player_id = cursor.lastrowid

    # Insert statistics for this player
    cursor.execute(
        """
        INSERT INTO stats (
            player_id,
            season,
            minutes_played,
            appearances,
            goals_per90,
            assists_per90,
            interceptions_per90,
            tackles_per90,
            progressions_per90
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            player_id,
            "2025/2026",
            1800,
            20,
            0.35,
            0.20,
            1.1,
            2.3,
            4.2
        )
    )

conn.commit()

conn.close()

print(
    f"Database successfully created and seeded at: " f"{os.path.abspath(db_path)}")
