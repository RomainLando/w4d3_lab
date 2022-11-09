from db.run_sql import run_sql
from models.artist import Artist

def select_all():
    artists = []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row["full_name"], row["id"])
        artists.append(artist)
    return artists


def save(artist):
    sql = """
    INSERT INTO artists (full_name) VALUES (%s) RETURNING *
    """
    values = [artist.full_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def delete(id):
    sql = """
    DELETE FROM artists WHERE id = %s
    """
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = """
    DELETE FROM artists 
    """
    run_sql(sql)

def select(id):
    artist = None
    sql = """
    SELECT * FROM artists WHERE id = %s
    """
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        artist = Artist(result["full_name"], result["id"])
    return artist


def update(artist):
    sql = """
    UPDATE artists SET full_name = (%s)
    WHERE id = %s
    """
    values = [artist.full_name, artist.id]
    print(values)
    run_sql(sql, values)




