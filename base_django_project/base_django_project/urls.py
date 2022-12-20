from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fashion-blog', include('fashionblog.urls')),
    path('', include('basic_website.urls'))
    
]
