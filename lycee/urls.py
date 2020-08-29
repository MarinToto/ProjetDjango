from django.conf.urls import url
from . import views
from .views import StudentCreateView,StudentUpdateView,ParticularCorView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<cursus_id>[0-9]+)$', views.detail, name='detail'),
    # /lycee/student/73
    url(r'^student/(?P<student_id>[0-9]+)$', views.detail_student, name='detail_student'),
    url(r'^student/create/$', StudentCreateView.as_view(), name='create_student'),
    url(r'^student/edit/(?P<pk>\d+)$', StudentUpdateView.as_view(), name='update_student'),
    url(r'^student/call/(?P<cursus_id>\d+)$', views.call_of_roll, name='call_of_roll'),
    url(r'^student/particular_cor/$', ParticularCorView.as_view(), name='particular_cor'), 
]