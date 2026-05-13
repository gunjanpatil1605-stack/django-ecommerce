from django.contrib import admin
from django.urls import path, include

# 📸 Media file support (for images upload)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # 🌐 Core app routes
    path('', include('core.urls')),
]

# 🖼️ Serve media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)