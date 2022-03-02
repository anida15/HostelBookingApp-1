from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('vendors/', include('vendors.urls')),
    path('payment/', include('payment.urls')),
    path('rooms/', include('rooms.urls')),
    path('booking/', include('booking.urls')),
  
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
