import pytest
from lib.artist_parameters_validator import ArtistParametersValidator

def test_is_valid():
    validator = ArtistParametersValidator("Blue", "Pop")
    assert validator.is_valid() == True
    
def test_is_not_valid_with_no_name():
    validator_1 = ArtistParametersValidator(None, "Pop")
    assert validator_1.is_valid() == False
    validator_2 = ArtistParametersValidator("", "Pop")
    assert validator_2.is_valid() == False
    
def test_is_not_valid_with_no_genre():
    validator_1 = ArtistParametersValidator("Blue", "")
    assert validator_1.is_valid() == False
    validator_2 = ArtistParametersValidator("Blue", None)
    assert validator_2.is_valid() == False
    
def test_errors():
    validator_1 = ArtistParametersValidator("", "")
    assert validator_1.generate_errors() == [
        "Name must not be blank",
        "Genre must not be blank"
    ]
    validator_2 = ArtistParametersValidator("Blue", "")
    assert validator_2.generate_errors() == [
        "Genre must not be blank"
    ]
    validator_3 = ArtistParametersValidator("", "Pop")
    assert validator_3.generate_errors() == [
        "Name must not be blank"
    ]
    
def test_get_valid_name_if_name_valid():
    validator = ArtistParametersValidator("Blue", "Pop")
    assert validator.get_valid_name() == "Blue"
    
def test_get_valid_name_refuses_if_invalid():
    validator = ArtistParametersValidator("", "Pop")
    with pytest.raises(Exception) as err:
        validator.get_valid_name()
    assert str(err.value) == "Cannot get valid name"
    
def test_get_valid_genre_if_genre_valid():
    validator = ArtistParametersValidator("Blue", "Pop")
    assert validator.get_valid_genre() == "Pop"
    
def test_get_valid_genre_refuses_if_invalid():
    validator = ArtistParametersValidator("Blue", "")
    with pytest.raises(Exception) as err:
        validator.get_valid_genre()
    assert str(err.value) == "Cannot get valid genre"