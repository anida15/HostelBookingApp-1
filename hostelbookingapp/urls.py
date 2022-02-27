from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('vendors/', include('vendors.urls')),
    path('payment/', include('payment.urls')),
    path('rooms/', include('rooms.urls')),
    path('booking/', include('booking.urls')),
  
]
