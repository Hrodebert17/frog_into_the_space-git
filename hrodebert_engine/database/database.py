from hrodebert_engine.database import cursor as cursor
from hrodebert_engine.database import connection as connection


def close_database():
    connection.close()


def get_variable(variable):
    var = connection.execute(f"SELECT {variable} from player_stats")
    result = None
    for row in var:
        result = row[0]
    return result

