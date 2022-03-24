from django.test import TestCase
from .models import ArticleModel
from django.utils import timezone
from datetime import datetime


# Create your tests here.
class ArticleTest(TestCase):
    def test_article_created_success(self):
        ArticleModel.objects.create(title="test article", category="test category", author="test author",
                                    content="test content", created_at=datetime.now(tz=timezone.utc))
        article = ArticleModel.objects.get(title="test article")
        self.assertEqual(article.category, 'test category')


class BlogPagesTest(TestCase):
    def test_home_page_content(self):
        res = self.client.get("/blog/")
        self.assertEqual(res.content, b"Welcome get to my blog!")
        