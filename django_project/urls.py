from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("team.urls")),
    path("", include("shop.urls")),
    path("", include("accounts.urls")),
    path("", include("post.urls")),
    path('api/', include('api.urls')),  # api/posts/ and api/comments/
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
