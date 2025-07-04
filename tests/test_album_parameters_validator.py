import pytest
from lib.album_parameters_validator import AlbumParametersValidator

def test_is_valid():
    validator = AlbumParametersValidator("a title", "2025")
    assert validator.is_valid() == True
    
def test_is_not_valid_with_no_title():
    validator_1 = AlbumParametersValidator(None, "2025")
    assert validator_1.is_valid() == False
    validator_2 = AlbumParametersValidator("", "2025")
    assert validator_2.is_valid() == False
    
def test_is_not_valid_with_no_release_year():
    validator_1 = AlbumParametersValidator("title b", "")
    assert validator_1.is_valid() == False
    validator_2 = AlbumParametersValidator("title k", None)
    assert validator_2.is_valid() == False
    validator_3 = AlbumParametersValidator("title k", 'cat')
    assert validator_3.is_valid() == False
    
def test_errors():
    validator_1 = AlbumParametersValidator("", "")
    assert validator_1.generate_errors() == [
        "Title must not be blank",
        "Release year must be a number"
    ]
    validator_2 = AlbumParametersValidator("Title", "")
    assert validator_2.generate_errors() == [
        "Release year must be a number"
    ]
    validator_3 = AlbumParametersValidator("", "1990")
    assert validator_3.generate_errors() == [
        "Title must not be blank"
    ]
    
def test_get_valid_title_if_title_valid():
    validator = AlbumParametersValidator("title", "2025")
    assert validator.get_valid_title() == "title"
    
def test_get_valid_title_refuses_if_invalid():
    validator = AlbumParametersValidator("", "2025")
    with pytest.raises(Exception) as err:
        validator.get_valid_title()
    assert str(err.value) == "Cannot get valid title"
    
def test_get_valid_release_year_if_release_year_valid():
    validator = AlbumParametersValidator("title", "2025")
    assert validator.get_valid_release_year() == 2025
    
def test_get_valid_release_year_refuses_if_invalid():
    validator = AlbumParametersValidator("title", "")
    with pytest.raises(Exception) as err:
        validator.get_valid_release_year()
    assert str(err.value) == "Cannot get valid release year"