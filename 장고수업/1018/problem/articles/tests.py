from rest_framework.test import APITestCase
from django.urls import reverse

from django.contrib.auth import get_user_model
import csv

problems = [0] * 10
score = 0

class ArticlesTest(APITestCase):
    def tearDown(self):
        global score, problems
        if hasattr(self, '_outcome'):  # Python 3.4+
            result = self.defaultTestResult()  # these 2 methods have no side effects
            self._feedErrorsToResult(result, self._outcome.errors)
        else:  # Python 3.2 - 3.3 or 3.0 - 3.1 and 2.7
            result = getattr(self, '_outcomeForDoCleanups', self._resultForDoCleanups)
        error = self.list2reason(result.errors)
        failure = self.list2reason(result.failures)
        ok = not error and not failure

        # demo:   report short info immediately (not important)
        if not ok:
            print("="*12,'fail',"="*12)
        else:
            print("="*30)
            score += int(self.id()[-2:])
            problems[int(self.id()[-5:-3])] = int(self.id()[-2:])
            
        print(self.id().split('.')[-1])
        print(score)
        print(problems)

    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]
    
    # 1-1-get : 15
    def test_articles_list_00_15(self):
        # #create
        from articles.models import Article
        Article.objects.create(title="first", content="first")
        Article.objects.create(title="last", content="last")

        response = self.client.get(reverse('articles:article_list'))
        self.assertEqual(Article.objects.order_by('-id')[0].title, response.data[-1]['title'])

    # 1-2-post : 15
    def test_articles_create_post_01_15(self):
        from articles.models import Article
        Article.objects.create(title="test", content="test")
        article = Article.objects.last()

        valid_reservation_data = {
            'title': 'test',
            'content': 'test'
        }
        response = self.client.post(reverse('articles:article_list'), valid_reservation_data)
        self.assertEqual(201, response.status_code)

        new_article = Article.objects.last()
        self.assertNotEqual(article, new_article)

    # 2-1-get : 10
    def test_articles_detail_get_02_10(self):
        # create
        from articles.models import Article
        Article.objects.create(title="first", content="first")

        response = self.client.get(reverse('articles:article_detail', args=[1]))
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get(reverse('articles:article_detail', args=[100]))
        self.assertEqual(response.status_code, 404)
    
    # 2-2-delete : 10
    def test_articles_detail_delete_03_10(self):
        # create
        from articles.models import Article
        Article.objects.create(title="first", content="first")

        response = self.client.delete(reverse('articles:article_detail', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['delete'], '1')

        response = self.client.delete(reverse('articles:article_detail', args=[100]))
        self.assertEqual(response.status_code, 404)
    
    # 2-3-put : 10
    def test_articles_detail_put_04_10(self):
        # create
        from articles.models import Article
        Article.objects.create(title="first", content="first")

        valid_reservation_data = {
            'title': 'test',
            'content': 'test'
        }
        response = self.client.put(reverse('articles:article_detail', args=[1]), valid_reservation_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'test')

        response = self.client.put(reverse('articles:article_detail', args=[100]), valid_reservation_data)
        self.assertEqual(response.status_code, 404)

class CommentTest(APITestCase):
    def tearDown(self):
        global score, problems
        if hasattr(self, '_outcome'):  # Python 3.4+
            result = self.defaultTestResult()  # these 2 methods have no side effects
            self._feedErrorsToResult(result, self._outcome.errors)
        else:  # Python 3.2 - 3.3 or 3.0 - 3.1 and 2.7
            result = getattr(self, '_outcomeForDoCleanups', self._resultForDoCleanups)
        error = self.list2reason(result.errors)
        failure = self.list2reason(result.failures)
        ok = not error and not failure

        # demo:   report short info immediately (not important)
        print()
        
        if not ok:
            print("="*12,'fail',"="*12)
        else:
            print("="*30)
            score += int(self.id()[-2:])
            problems[int(self.id()[-5:-3])] = int(self.id()[-2:])
        print(self.id().split('.')[-1])
        print(score)
        print(problems)


    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]

    # 3-1-serializer : 10
    def test_comment_serializer_05_10(self):
        # create
        from articles.models import Article, Comment
        r1 = Article.objects.create(title="article", content="test")
        c1 = Comment.objects.create(content="comment", article=r1)
        
        response = self.client.get(reverse('articles:comment_list'))
        self.assertEqual(r1.pk, response.data[-1]['article'])

    # 3-2-get : 05
    def test_comment_list_get_06_10(self):
        # create
        from articles.models import Article, Comment
        r1 = Article.objects.create(title="article", content="test")
        Comment.objects.create(content="comment", article=r1)
        
        response = self.client.get(reverse('articles:comment_list'))
        self.assertEqual(Comment.objects.order_by('-id')[0].content, response.data[-1]['content'])


    # 4-post : 05
    def test_comment_create_post_07_05(self):
        from articles.models import Article, Comment
        r1 = Article.objects.create(title="article", content="test")
        c1 = Comment.objects.create(content="comment", article=r1)
        comment = Comment.objects.last()

        valid_reservation_data = {
            'content': 'test',
        }
        response = self.client.post(reverse('articles:comment_create', args=[1]), valid_reservation_data)
        self.assertEqual(201, response.status_code)

        new_comment = Comment.objects.last()
        self.assertNotEqual(comment, new_comment)


    # 5-1-get : 05
    def test_comment_detail_get_08_05(self):
        # create
        from articles.models import Article, Comment
        r1 = Article.objects.create(title="article", content="first")
        Comment.objects.create(content="comment", article=r1)

        response = self.client.get(reverse('articles:comment_detail', args=[1]))
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get(reverse('articles:comment_detail', args=[100]))
        self.assertEqual(response.status_code, 404)
    
    # 5-2-delete : 05
    def test_comment_detail_delete_09_05(self):
        # create
        from articles.models import Article, Comment
        r1 = Article.objects.create(title="article", content="first")
        Comment.objects.create(content="comment", article=r1)

        response = self.client.delete(reverse('articles:comment_detail', args=[1]))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data['delete'], '1')

        response = self.client.delete(reverse('articles:comment_detail', args=[100]))
        self.assertEqual(response.status_code, 404)
    
    # 6-1-comment-count : 05
    def test_articles_comment_count_10_05(self):
        # create
        from articles.models import Article, Comment
        r1 = Article.objects.create(title="article", content="first")
        Comment.objects.create(content="comment", article=r1)

        response = self.client.get(reverse('articles:article_detail', args=[1]))
        self.assertEqual(response.data['comment_count'], 1)
        
        