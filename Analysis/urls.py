from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = 'analysis_home'),
    path('calculating', views.please_wait, name = 'please_wait'),
    path('database', views.database, name = 'database'),
    path('getObject/<int:id>', views.getObject, name = 'getObject'),
    path('results/<int:id>', views.results, name = 'results')
]
