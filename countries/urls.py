from django.conf.urls import url
from countries import views

urlpatterns=[
    url(r'^api/countries$',views.views.countries_list),
    url(r'^api/countries/(?P<pk>[0-9]+)$',views.countries_detail)
]

