from django.conf.urls import url

from .views import TourDetailView, TourListView

urlpatterns = [
    url(r'^tournee/(?P<slug>[\w-]+)/$', TourDetailView.as_view(), name='tour-detail'),
    url(r'^$', TourListView.as_view(), name='tour-list'),
]
