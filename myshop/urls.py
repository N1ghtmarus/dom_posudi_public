from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('api/v1/', include('api_v1.urls', namespace='api_v1')),
    path('', include('shop.urls', namespace='shop')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
        )
