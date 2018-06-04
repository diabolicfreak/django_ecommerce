from django.conf.urls import url, include
from products.views import ProductDetailSlugView, ProductListView, ProductDetailView, ProductFeaturedListView, ProductFeaturedDetailView

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
    # url(r'^(?P<pk>\d+)/$', ProductDetailView.ass_view()),
    # url(r'^featured/$', ProductFeaturedListView.as_view()),
    # url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),
]