from django.conf.urls import include, url
from users import views

urlpatterns = (#'',esto estando dentro de otra url con inclue da error str
    url(r'user/$', views.IndexView.as_view(), name="index"),
)
