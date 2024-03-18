"""from django.test import TestCase
from django.urls import reverse
from .models import ShortURL
from .forms import CreateNewShortURL

class CreateShortURLTest(TestCase):
    def setUp(self):
        # Create a ShortURL instance for testing
        self.short_url = ShortURL.objects.create(
            original_url="https://www.example.com",
            short_url="abc123",
            time_data_created="2022-01-01 12:00:00"
        )

    def test_create_short_url_view(self):
        url = reverse('https://esyconnect.com/profile223/')  # Replace 'create_short_url' with your actual URL name
        response = self.client.post(url, {'original_url': 'https://www.example.com'})

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the ShortURL was created in the database
        self.assertTrue(ShortURL.objects.filter(original_url='https://www.example.com').exists())

        # Check if the rendered template is 'urlcreated.html'
        self.assertTemplateUsed(response, 'urlcreated.html')

    # Add more test cases as needed """