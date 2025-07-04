from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===

# // Exercise and challenge

# Test-drive a GET /albums route that connects with an AlbumRepository
def test_get_albums(page, test_web_address, db_connection): 
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    div_tag = page.locator("div")
    expect(div_tag).to_have_text([
        "Title: Doolittle\nReleased: 1989",
        "Title: Surfer Rosa\nReleased: 1988"
    ])
    
# Test-drive and implement a route that returns the HTML content for a single album.
def test_get_single_album(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums/1")
    h1_tag = page.locator("h1")
    p_tag = page.locator("p")
    expect(h1_tag).to_have_text("Doolittle")
    expect(p_tag).to_have_text("Release year: 1989\nArtist: Pixies")
    
# Test-drive a GET /artists route that connects with an ArtistRepository
def test_get_artists(page, test_web_address, db_connection): 
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    div_tag = page.locator("div")
    expect(div_tag).to_have_text([
        "Name: Pixies",
        "Name: ABBA",
        "Name: Taylor Swift",
        "Name: Nina Simone"
    ])
    
# Test-drive and implement a route that returns the HTML content for a single artist.
def test_get_single_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists/1")
    h1_tag = page.locator("h1")
    p_tag = page.locator("p")
    expect(h1_tag).to_have_text("Pixies")
    expect(p_tag).to_have_text("Genre: Rock")
    
#  Create a new album- POST request
def test_create_album(db_connection, page, test_web_address):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Add a new album")
    page.fill("input[name=title]", "OK, Computer")
    page.fill("input[name=release_year]", "1997")
    page.click("text=Create Album")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("OK, Computer")
    
def test_validate_album(db_connection, page, test_web_address):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Add a new album")
    page.click("text=Create Album")
    errors_tag = page.locator(".errors")
    expect(errors_tag).to_have_text(
        "Your submission contains errors: " \
        "Title must not be blank, "
        "Release year must be a number" \
    )
    
#  Create a new artist- POST request
def test_create_artist(db_connection, page, test_web_address):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text=Add a new artist")
    page.fill("input[name=name]", "Blue")
    page.fill("input[name=genre]", "Pop")
    page.click("text=Create Artist")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Blue")
    
def test_validate_artist(db_connection, page, test_web_address):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text=Add a new artist")
    page.click("text=Create Artist")
    errors_tag = page.locator(".errors")
    expect(errors_tag).to_have_text(
        "Your submission contains errors: " \
        "Name must not be blank, "
        "Genre must not be blank" \
    )



