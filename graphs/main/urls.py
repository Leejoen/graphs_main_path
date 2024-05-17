from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('params', views.params, name='params'),
    path('visual', views.visual, name='visual'),
    path('param/<int:pk>', views.Param.as_view(), name='param')
]