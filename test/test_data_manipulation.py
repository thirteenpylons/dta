from ..data_manipulation import Email



def test_extract_first_name():
    first_name = Email("first.last@email.com").extract_first_name()
    assert first_name == "First"