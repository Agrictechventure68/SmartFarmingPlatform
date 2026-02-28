from rest_framework.routers import DefaultRouter
from .views import FarmerViewSet

router = DefaultRouter()
router.register(r'', FarmerViewSet, basename='farmer')

urlpatterns = router.urls
 