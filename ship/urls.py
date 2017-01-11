from django.conf.urls import url
from . import views

app_name = 'ship'

urlpatterns = [
    # /ship/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /ship/departments/
    url(r'^departments$', views.DepartmentView.as_view(), name='departments'),

    # /ship/departments/<department.id>/
    url(r'^departments/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),


    url(r'^records$', views.RecordsView.as_view(), name='records'),

    # /ship/<department.id>/
    # url(r'^(?P<department_id>[0-9]+)/baknaz_team/$', views.baknaz_team, name='baknaz_team'),

    # /ship/
    # url(r'^$', views.records, name='records'),
]
