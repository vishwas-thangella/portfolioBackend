from django.urls import path
from myapp.views import Home,Projects,About,Contact
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('api/',Home,name="Home"),
    path('api/projects',Projects,name="Projects"),
    path('api/about',About,name="About"),
    path('api/contact',Contact,name="Contact")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)