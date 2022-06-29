from django.contrib import admin
from django.urls import re_path
from django.urls import path
#from .views import TestView
from . import views
#from .views import FriendList
#from .views import FriendDetail


urlpatterns = [
    #path('<int:id>/<nickname>/', views.index, name='index'),
#    re_path('get', TestView.as_view(), name='get'),
#    re_path('form', TestView.as_view(), name='form'),
    #re_path('post', TestView.as_view(), name='post'),
    #path('post', views.post, name='post'),
#    re_path('get', TestView.as_view(), name='get'),
#    re_path('result', TestView.as_view(), name='result'),
    #path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('',views.Login,name='Login'),
    path('Logout',views.Logout,name="Logout"),
#    path('Logout2',views.Logout2,name="Logout2"),
    path('Logout2/<str:name>',views.Logout2,name="Logout2"),
#    path('Logout2/<int:num>/<str:name>',views.Logout2,name="Logout2"),
#    path('Logout2/(?P<num>[0-9]+)/(?P<name>[^/]+)\\Z',views.Logout2,name="Logout2"),
    path('G1D/<int:num>',views.G1D,name="G1D"),
    path('G1D2/<str:name>',views.G1D2,name="G1D2"),
    path('G2D2/<str:name>',views.G2D2,name="G2D2"),
    path('G3D2/<str:name>',views.G3D2,name="G3D2"),
    path('G4D2/<str:name>',views.G4D2,name="G4D2"),
    path('G5D2/<str:name>',views.G5D2,name="G5D2"),
    path('G6D2/<str:name>',views.G6D2,name="G6D2"),
    path('G7D2/<str:name>',views.G7D2,name="G7D2"),
    path('G2D/<int:num>',views.G2D,name="G2D"),
    path('G3D/<int:num>',views.G3D,name="G3D"),
    path('G4D/<int:num>',views.G4D,name="G4D"),
    path('G5D/<int:num>',views.G5D,name="G5D"),
    path('G6D/<int:num>',views.G6D,name="G6D"),
    path('G7D/<int:num>',views.G7D,name="G7D"),
    path('E1D/<int:num>',views.E1D,name="E1D"),
    path('E2D/<int:num>',views.E2D,name="E2D"),
    path('E1D2/<str:name>',views.E1D2,name="E1D2"),
    path('E2D2/<str:name>',views.E2D2,name="E2D2"),
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
    path('PDI22RH',views.PDI22RH,name="PDI22RH"),
    path('ADC22RHA',views.ADC22RHA,name="ADC22RHA"),
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