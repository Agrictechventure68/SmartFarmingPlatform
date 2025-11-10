from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h2>✅ Agri_Empower Backend is Live!</h2><p>Deployment successful on Render.</p>")

urlpatterns = [
    path('', home),  # 👈 Root routqe (now returns a success message)
    path('admin/', admin.site.urls),
    path('farmers/', include('farmers.urls')),
    path('curriculum/', include('curriculum.urls')),
    path('diagnostic/', include('diagnostic.urls')),
    path('ecommerce/', include('ecommerce.urls')),
]
