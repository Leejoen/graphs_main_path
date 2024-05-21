from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('params', views.params, name='params'),
    path('visual', views.visual, name='visual'),
    path('upd_name/<int:pk>', views.UpdName.as_view(), name='upd_name'),
    path('upd_name/visual', views.visual, name='visual'),
    path('edges/<int:pk>', views.CreateEdges.as_view(), name='edges'),
    path('edges/visual', views.visual, name='visual')
]