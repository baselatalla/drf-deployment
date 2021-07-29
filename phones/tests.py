from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Phone

# Create your tests here.
class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='testcompany', password='password')
        test_user.save()

        test_post = Phone.objects.create(
            rating = 9,
            company = test_user,
            name = 'test_phone',
            specifications = 'test_description'
        )
        test_post.save()

    def test_blog_content(self):
        phone = Phone.objects.get(id=1)
        actual_company = str(phone.company)
        actual_name = str(phone.name)
        actual_specifications = str(phone.specifications)
        self.assertEqual(actual_company, 'testcompany')
        self.assertEqual(actual_name, 'test_phone')
        self.assertEqual(actual_specifications, 'test_description')
