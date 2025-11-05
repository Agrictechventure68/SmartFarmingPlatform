from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/farmers/', include('farmers.urls')),
    path('api/curriculum/', include('curriculum.urls')),
    path('api/diagnostic/', include('diagnostic.urls')),
    path('api/ecommerce/', include('ecommerce.urls')),
]