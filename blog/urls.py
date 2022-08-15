from django.contrib import admin
from django.urls import re_path
from django.urls import path
#from .views import TestView
from . import views
#from .views import FriendList
#from .views import FriendDetail


urlpatterns = [
    path('',views.Login,name='Login'),
    path('Logout',views.Logout,name="Logout"),
    path('Logout2/<str:name>',views.Logout2,name="Logout2"),
    path('ADC',views.ADC,name="ADC"),
    path('editADC2/<str:name>',views.editADC2,name="editADC2"),
    path('ADC2/<str:name>',views.ADC2,name="ADC2"),
    path('PDI2/<str:name>',views.PDI2,name="PDI2"),
    path('PDI',views.PDI,name="PDI"),
    path('RH',views.RH,name="RH"),
    path('ES',views.ES,name="ES"),
    path('MBO22RH',views.MBO22RH,name="MBO22RH"),
    path('MBO22DL',views.MBO22DL,name="MBO22DL"),
    path('ADC22DL',views.ADC22DL,name="ADC22DL"),
    path('ADC22ESTA',views.ADC22ESTA,name="ADC22ESTA"),
    path('PDI22RH',views.PDI22RH,name="PDI22RH"),
    path('ADC22RHA',views.ADC22RHA,name="ADC22RHA"),
    path('upload',views.upload,name="upload"),
    path('upMBO',views.upMBO,name="upMBO"),
    path('upADC',views.upADC,name="upADC"),
    path('upPDI',views.upPDI,name="upPDI"),
    path('upCE',views.upCE,name="upCE"),
    path('listAE',views.listAE,name="listAE"),
    path('listMBO',views.listMBO,name="listMBO"),
    path('listADC',views.listADC,name="listADC"),
    path('listPDI',views.listPDI,name="listPDI"),

#    path('upload',views.uploadview.as_view(),name="upload"),
    #path('PDI22',views.PDI22,name="PDI22"),

    #path('Logout/<int:num>',views.Logout,name="Logout"),
#    path('register',views.AccountRegistration.as_view(), name='register'),
    #path("home/<int:num>",views.home,name="home"),
    path("edit4/<int:num>",views.edit4,name="edit4"),
    path("edit3/<int:num>",views.edit3,name="edit3"),
    path("edit2/<int:num>",views.edit2,name="edit2"),
    path("edit/<int:num>",views.edit,name="edit"),
    path("editADC/<int:num>",views.editADC,name="editADC"),
    path("editPDI/<int:num>",views.editPDI,name="editPDI"),
    path("home",views.home,name="home"),
    path("homeA",views.homeA,name="homeA"),
    path("homeB",views.homeB,name="homeB"),
    path("homeC",views.homeC,name="homeC"),
#    path('',views.index,name='index'),
    #path('test/', test.form),
    #path('test/', test.post),
    #path('test/', test.get),
    #path('next', views.next, name='next'),
]