from lib.models.magazine import Magazine

def test_magazine_can_be_saved_and_retrieved():
    magazine = Magazine(name="Nature Monthly", category="Science")
    magazine.save()

    fetched = Magazine.find_by_id(magazine.id)
    assert fetched.name == "Nature Monthly"
    assert fetched.category == "Science"
