from django.test import TestCase
from django.urls import reverse
from .models import Post, Comment


class BlogTests(TestCase):
    """
    Tests to check that the blog page exists at the correct URL, uses 
    the correct view and uses the correct template. I also check that
    when a comment is added the details match what is stored in the database.
    """

    def setUp(self):
        Post.objects.create(
            title='My Title', summary='Test summary', body='Test body')
        Comment.objects.create(author='Bob', text='Test comment')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/blog/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('blog'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('blog'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'blog.html')

    def test_comment(self):
        new_comment = Comment.objects.get(id=1)
        self.assertEqual(str(new_comment.author), 'Bob')
        self.assertEqual(str(new_comment.text), 'Test comment')
