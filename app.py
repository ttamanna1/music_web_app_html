import os
from flask import Flask, redirect, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist import Artist
from lib.artist_repository import ArtistRepository
from lib.album_parameters_validator import AlbumParametersValidator
from lib.artist_parameters_validator import ArtistParametersValidator


# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/albums', methods=['GET'])
def get_albums():    
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template("albums.html", albums=albums)

@app.route('/albums/<id>', methods=['GET'])
def get_single_album(id):
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    album = album_repository.find(id)
    artist_repository = ArtistRepository(connection)
    artist = artist_repository.find(album.artist_id)
    return render_template("album.html", album=album, artist=artist)

@app.route('/artists', methods=['GET'])
def get_artists():    
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    return render_template("artists.html", artists=artists)

@app.route('/artists/<id>', methods=['GET'])
def get_single_artist(id):
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    artist = artist_repository.find(id)
    return render_template("artist.html", artist=artist)

@app.route('/albums/new_album', methods=['GET'])
def get_new_album():
    return render_template('new_album.html')

@app.route('/albums', methods=['POST'])
def create_album():
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    validator = AlbumParametersValidator(
        request.form['title'],
        request.form['release_year']
    )
    if not validator.is_valid():
        errors = validator.generate_errors()
        return render_template('new_album.html', errors=errors)
    album = Album(None, validator.get_valid_title(), validator.get_valid_release_year(), 1)
    album_repository.create(album)
    return redirect(f"/albums/{album.id}")

@app.route('/artists/new_artist', methods=['GET'])
def get_new_artist():
    return render_template('new_artist.html')

@app.route('/artists', methods=['POST'])
def create_artist():
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    validator = ArtistParametersValidator(
        request.form['name'],
        request.form['genre']
    )
    if not validator.is_valid():
        errors = validator.generate_errors()
        return render_template('new_artist.html', errors=errors)
    artist = Artist(None, validator.get_valid_name(), validator.get_valid_genre())
    artist_repository.create(artist)
    return redirect(f"/artists/{artist.id}")

# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))