from django.test import TestCase
from .models import FAQ

class FAQModelTest(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(question="Who is Django?", answer="Django is a guitarist .")

    def test_translation(self):
        self.assertTrue(self.faq.question_hi)
        self.assertTrue(self.faq.question_bn)
