from rest_framework.routers import DefaultRouter
from .views import CurriculumViewSet

router = DefaultRouter()
router.register(r'', CurriculumViewSet)

urlpatterns = router.urls
