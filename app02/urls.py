from django.urls import path
from . import views
from .views import home, produtos, contatos

app_name = 'app02'

urlpatterns = [
    path('',views.home, name='home'),
    path('produtos/', views.produtos, name='produtos'),
    path('contatos/', views.contatos,name='contatos'),

]
                                                             