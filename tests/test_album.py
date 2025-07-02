from lib.album import Album

def test_constructs_with_fields():
    album = Album(1, 'OK, Computer', 1997, 5)
    assert album.id == 1
    assert album.title == 'OK, Computer'
    assert album.release_year == 1997
    assert album.artist_id == 5
    
def test_equality():
    album1 = Album(1, 'OK, Computer', 1997, 5)
    album2 = Album(1, 'OK, Computer', 1997, 5)
    assert album1 == album2
    
def test_formatting():
    album = Album(1, 'OK, Computer', 1997, 5)
    assert str(album) == 'Album(1, OK, Computer, 1997, 5)'