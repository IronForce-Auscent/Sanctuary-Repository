import base64
import sqlite3

connection = sqlite3.connect("primary.db")
cursor = connection.cursor()

accounts = [
    {
        "name": "Ryo Soikutsu",
        "description": "DCM013",
        "status": "w8BIcjkXUXnFK4ZxA1gJBaOVXQpbail6",
        "type": "SANC{5q1_v4cCiN3_In73cTi0n}"
    },
    {
        "name": "Mikaela Katsuragi",
        "description": "FD1262",
        "status": "AxKc3eDzozz8sb1UtevZNWLOn2jiDq6U",
        "type": "user"
    },
    {
        "name": "Runa Satoru",
        "description": "GC1262",
        "status": "JkdB2if81lnEYGEFR93WkCWWBnPWPnLv",
        "type": "user"
    }
]

cursor.execute("DROP TABLE IF EXISTS accounts")
cursor.execute("CREATE TABLE IF NOT EXISTS accounts (id INTEGER PRIMARY KEY, name TEXT, staffID TEXT, status TEXT, type TEXT)")
for account in accounts:
    name, description, status, type = account.values()
    cursor.execute("INSERT INTO accounts (name, staffID, status, type) VALUES (?, ?, ?, ?)", (name, description, status , type))

projects = [
    {
        "name": "FTL Travel",
        "description": "Development of faster-than-light (FTL) warp and sub-lightspeed engines",
        "status": "Complete"
    },
    {
        "name": "Black Hole Energy Manipulation",
        "description": "Manipulation of black hole physics to produce massive quantities of energy",
        "status": "In Progress"
    },
    {
        "name": "Astral Network",
        "description": "Deployment of interstellar travel routes ('Astral Network') between systems and galaxies",
        "status": "Complete"
    },
    {
        "name": "Hyper-Advanced Automated Intrusion Detection System (HAAIDS)",
        "description": "Development of automated IDS for protection of Foundation networks",
        "status": "In Progress"
    },
    {
        "name": "Veil Network",
        "description": "Deployment of Veil Network stations and probes in deep space and wormholes",
        "status": "Complete"
    }
]

cursor.execute("DROP TABLE IF EXISTS projects")
cursor.execute("CREATE TABLE IF NOT EXISTS projects (id INTEGER PRIMARY KEY, name TEXT, description TEXT, status TEXT)")
for account in accounts:
    name, description, status = account.values()
    cursor.execute("INSERT INTO accounts (name, description, status) VALUES (?, ?, ?, ?)", (name, description, status))
    

connection.commit()
connection.close()
