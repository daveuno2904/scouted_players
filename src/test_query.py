import sqlite3
import pandas as pd

# Connect and read with pandas
conn = sqlite3.connect("data/scouted_players.db")

# Write an advanced SQL query joining both tables together
query = """
    SELECT 
    p.name, 
    p.current_club, 
    p.eligibility_type, 
    p.cap_tied, 
    s.goals_per90 
    FROM players p
    JOIN stats s ON p.id = s.player_id
"""

df = pd.read_sql_query(query, conn)

conn.close()

print(df)
