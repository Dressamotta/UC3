from django.contrib import admin

from django.urls import path

from app01.views import home,produtos,contatos

irlpatterns = [

  path('admin/',admin.site.urls)
  path(home,name='home'),
       path('produtos/',produtos,name='produtos'),
       path(contato/',contatos,name=contatos')
]
       

