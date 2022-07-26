"""crudder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from manualupload import views
from excelsheetupload import views as views2

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('formpage/', views.form_name_view, name='form_name'),
    path('excelpage/', views.excel_upload_view, name="excel_upload"),
    # path('students/', views.getStudents),
    path('students/:rollno', views.getStudent),
    path('viewform/', views.viewform, name="view_form"),
    path('delete/<int:id>/', views.deleteData, name="delete_data"),
    path('<int:id>/', views.updateData, name="update_data")
]
