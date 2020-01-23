from django.conf.urls import url


from .import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^imageview/$', views.ImageView.as_view(), name='imageview'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]