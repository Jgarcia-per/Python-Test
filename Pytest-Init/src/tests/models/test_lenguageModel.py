# Models
from src.models.lenguageModel import LanguageModel

# Comprobamos que la base de datos no este vacia
def test_get_languages_not_none():
    languages = LanguageModel.get_languages(),
    assert languages != None

# Que tenga elementos
def test_get_languages_has_elements():
    languages = LanguageModel.get_languages(),
    assert len(languages) > 0

# Longitud de esos elementos
def test_get_languages_check_elements_length():
    languages = LanguageModel.get_languages(),
    for language in languages:
        assert len(language) > 0
