from django.urls import path
from . import views

app_name = 'camos_app'

urlpatterns = [
    path('', views.home, name="home"),
    path('client_login', views.client_login, name="client_login"),
    path('supplier_login', views.supplier_login, name="supplier_login"),
    path('client_regist', views.client_regist, name="client_regist"),
    path('supplier_regist', views.supplier_regist, name="supplier_regist"),
    path('client_login', views.client_login, name="client_login"),
    path('supplier_login', views.supplier_login, name="supplier_login"),
    path('client_home', views.client_home, name="client_home"),
    path('supplier_home', views.supplier_home, name="supplier_home"),
    path('client_job_list', views.client_job_list, name="client_job_list"),
    path('client_job_detail/<int:id>', views.client_job_detail, name="client_job_detail"),
    path('client_job_create', views.client_job_create, name="client_job_create"),
    path('supplier_job_list', views.supplier_job_list, name="supplier_job_list"),
    path('supplier_job_map', views.supplier_job_map, name="supplier_job_map"),
    path('supplier_job_detail/<int:id>', views.supplier_job_detail, name="supplier_job_detail"),
    path('supplier_person_create/<int:id>', views.supplier_person_create, name="supplier_person_create"),
    path('client_worker_list', views.client_worker_list, name='client_worker_list'),
    path('client_worker_detail/<int:id>', views.client_worker_detail, name='client_worker_detail'),
    path('supplier_worker_list', views.supplier_worker_list, name="supplier_worker_list"),
    path('client_settings', views.client_settings, name="client_settings"),
    path('supplier_settings', views.supplier_settings, name="supplier_settings"),
    path('user_logout', views.user_logout, name='user_logout'),
]