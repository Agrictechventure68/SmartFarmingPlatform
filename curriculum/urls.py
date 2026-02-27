from rest_framework.routers import DefaultRouter
from .views import CurriculumViewSet

router.register(r'', CurriculumViewSet, basename='curriculum')