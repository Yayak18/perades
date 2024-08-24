from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<str:nama_desa>', views.record_perangkat, name='record'),
    path('hapus_perangkat/<str:nama_perangkat>', views.record_perangkat, name='hapus_perangkat'),
]
