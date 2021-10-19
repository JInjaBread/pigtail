from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('subject/', include('subject.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
