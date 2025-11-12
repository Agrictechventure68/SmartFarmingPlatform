from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse(
        "<h2>✅ Agri_Empower Backend is Live!</h2>"
        "<p>Deployment successful on Render.</p>"
        "<p>Available apis:</p>"
        "<ul>"
        "<li>/api/farmers/</li>"
        "<li>/api/curriculum/</li>"
        "<li>/api/diagnostic/</li>"
        "<li>/api/ecommerce/</li>"
        "</ul>"
    )

urlpatterns = [
    path('', home),  # Root route
    path('admin/', admin.site.urls),

# 👇 Updated api routes
    path('api/farmers/', include('farmers.urls')),
    path('api/curriculum/', include('curriculum.urls')),
    path('api/diagnostic/', include('diagnostic.urls')),
    path('api/ecommerce/', include('ecommerce.urls')),
]
