from posixpath import basename
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
#router.register(r'co', views.COTObjectList.as_view(), basename="COTOjbect")
#router.register(r'co/<pk>', views.COTObjectDetail.as_view(), basename="COTOjbect")
router.register(r'tf', views.CPTransformViewSet)
router.register(r'icon', views.IconViewSet)
router.register(r'iconSet', views.IconSetViewSet)

urlpatterns = [
    path("co/<uid>", views.COTObjectDetail.as_view()),
    path("tf/<cot_uid>", views.CPTransformDetail.as_view(), name="tf_detail"),
    path("tf/", views.CPTransformList.as_view()),
    path("co/", views.COTObjectList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
