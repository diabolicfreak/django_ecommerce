from django.conf.urls import url, include
from django.contrib import admin
from .views import home_page, contact_page, login_page, register_page
from products.views import ProductListView, ProductDetailView, ProductFeaturedListView, ProductFeaturedDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', home_page, name='home'),
    url(r'^contact$', contact_page, name='contact'),
    url(r'^login$', login_page, name='login'),
    url(r'^register$', register_page, name='register'),
    url(r'^products/', include('products.urls', namespace='products'),),
    # url(r'^products$', ProductListView.as_view()),
    # url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    # url(r'^featured/$', ProductFeaturedListView.as_view()),
    # url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),
    url(r'^admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
