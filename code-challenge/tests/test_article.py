from lib.models.article import Article
from lib.models.author import Author
from lib.models.magazine import Magazine

def test_article_can_be_saved_and_retrieved():
    author = Author(name="Article Author")
    author.save()

    magazine = Magazine(name="Tech Weekly", category="Technology")
    magazine.save()

    article = Article(title="AI Trends", author_id=author.id, magazine_id=magazine.id)
    article.save()

    fetched = Article.find_by_id(article.id)
    assert fetched.title == "AI Trends"
    assert fetched.author_id == author.id
    assert fetched.magazine_id == magazine.id
