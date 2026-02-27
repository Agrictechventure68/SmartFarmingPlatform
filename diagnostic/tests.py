from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, DiagnosticEntry

class DiagnosticEntryTestCase(TestCase):
    def setUp(self):
        self.cat = Category.objects.create(name='Crop')
        self.entry = DiagnosticEntry.objects.create(
            category=self.cat,
            name='Tomato Blight',
            symptoms='Leaves yellowing',
            treatment='Fungicide application'
        )

    def test_str_method(self):
        self.assertEqual(str(self.entry), 'Tomato Blight (Crop)')