from lib.models.author import Author

def test_author_can_be_saved_and_retrieved():
    author = Author(name="Test Author")
    author.save()

    fetched = Author.find_by_id(author.id)
    assert fetched.name == "Test Author"
