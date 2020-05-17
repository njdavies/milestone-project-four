from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

class SignUpPageTests(TestCase):
    """
    Tests to check that the signup page exists and returns an HTTP 200 status code, 
    uses the correct url name in the view and uses the correct template. I also
    test that when a new user is created the details match what is stored in the
    database.
    """
    username = 'bob'
    email = 'newuser@email.com'

    def test_signup_page_status_code(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
                         [0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
