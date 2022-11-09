from db.run_sql import run_sql
from models.album import Album

def select_all():
    artists = []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Album(row["full_name"], row["id"])
        artists.append(artist)
    return artists