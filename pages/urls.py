from django.urls import path
from pages.views import index, view1, view2, view3

urlpatterns = [
    path('', index, name='index'),
    path('view1/', view1, name='view1'),
    path('view2/', view2, name='view2'),
    path('view3/', view3, name='view3'),
]
