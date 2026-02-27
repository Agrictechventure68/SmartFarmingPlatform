from django.test import TestCase
from .models import Curriculum

class CurriculumModelTest(TestCase):
    def test_create_curriculum(self):
        c = Curriculum.objects.create(
            title='Tomato Farming',
            description='Learn tomato cultivation',
            duration='2 weeks',
            level='Foundation'
        )
        self.assertEqual(str(c), 'Tomato Farming')