from rest_framework.routers import DefaultRouter
from .views import DiagnosticViewSet

router = DefaultRouter()
router.register(r'', DiagnosticViewSet)

urlpatterns = router.urls
