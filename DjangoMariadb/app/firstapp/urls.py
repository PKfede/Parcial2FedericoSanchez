from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('states/<int:id>', views.state, name='state'),
    path('states/', views.states, name='states'),
    #path('client/login/', views.movielogin, name='movielogin'),
    path('client/movie/', views.movieclient, name='movieclient'),

    path('', views.paito, name='paito'),
    # ex: /1.0/5/
    path('view/<int:id>/', views.results, name='results'),
    path('client/createsession/', views.createsession, name='createsession'),
    path('client/createpatient/', views.createpatient, name='createpatient'),
    path('client/addclinicalcase/', views.addclinicalcase, name='addclinicalcase'),
    path('client/addclinicalcasenote/', views.addclinicalcasenote, name='addclinicalcasenote'),
    #segundo parcial
    path('login/',views.login,name='login'),
    path('client/movies',views.movies,name='movies'),
    path('generate_password/<str:password>',views.makepassword,name='makepassword'),

    path('vista/',views.vista, name='vista'),
    path('vista/index.html',views.vista, name='vista'),
    path('getJson',views.getJson, name='getJson'),
]
