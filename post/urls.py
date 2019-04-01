from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('tag/', views.tag_list),
    path('tag/<int:pk>', views.tag_list),
    path('post/', views.post_list),
    path('post/<int:pk>', views.post_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)
