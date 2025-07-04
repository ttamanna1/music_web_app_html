from lib.album import Album

class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection
        
    def all(self):
        rows = self._connection.execute("SELECT * FROM albums")
        albums =[]
        for row in rows:
            album = Album(row['id'], row['title'], row['release_year'], row['artist_id'])
            albums.append(album)
        return albums
    
    def find(self, id):
        rows = self._connection.execute(f"SELECT * FROM albums WHERE id = %s", [id])
        row = rows[0]
        return Album(row['id'], row['title'], row['release_year'], row['artist_id'])
    
    def create(self, album):
        rows = self._connection.execute(
            "INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s) RETURNING id", 
            [album.title, album.release_year, album.artist_id]
        )
        album.id = rows[0]['id']
        return None
    
    def delete(self, id):
        self._connection.execute(
            "DELETE FROM albums WHERE id = %s", 
            [id]
        )
        return None
    