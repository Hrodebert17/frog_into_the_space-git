import sqlite3

print("importing sql")

print("connecting the database")
connection = sqlite3.connect("Game_database.db")

print("Creating the cursor:")
cursor = connection.cursor()

print("creating the tables if they dont exists")

# noinspection PyBroadException
try:
    cursor.execute("""CREATE TABLE player_stats(
                    LEVEL_REACHED INT,
                    UNLOCKED_LVL INT,
                    ID text
                    )""")
    print("created player stats datapack")
    print("setting all the player stats to default")
    cursor.execute("INSERT INTO player_stats (LEVEL_REACHED,UNLOCKED_LVL,ID) \
                   VALUES (1,1,'local')")
    connection.commit()


except:
    print("no need to create any database")

