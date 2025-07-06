from django.contrib import admin
from django.urls import path
from products import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),  # ✅ ADD THIS LINE
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/<int:saree_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:saree_id>/', views.remove_from_cart, name='remove_from_cart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

