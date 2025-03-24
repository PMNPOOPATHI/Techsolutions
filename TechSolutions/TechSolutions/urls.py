"""
URL configuration for TechSolutions project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from stu_details import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.log_in,name = 'LogIn'),
    path('login/',views.log_in,name = 'LogIn_r'),
    path('student/',views.students_view,  name = 'Details_student'),
    path('student/<str:user>/',views.students_view,  name = 'Details_student_user'),
    path('daily_ac/',views.ac_daily),
    path('view_details/<id>/',views.viewDetails),
    path('update_page/<id>/',views.updatePage),
    path('pay_bill/<id>/',views.billing_page, name='Payment'),
    path('pay_bill/',views.billing_page, name='Payment'),
    path('courses/',views.Courses),
    path('print_bill/',views.print_bill),
    path('print_bill/',views.print_bill),
    path('print_bill/<id>/',views.print_bill,name = 'Print_Bill'),
    path('ac_summary/',views.acc_summary),
    path('logout/',views.log_out),
    path('delete/<id>/',views.delete_data),
    path('add_students/', views.add_students),
    path('by_id/',views.search_by_id),
    path('by_name/<name>/',views.search_by_name),
    path('by_course/<course>/',views.search_by_course),
    path('show_bill/',views.show_bill,name = 'Show_Bill'),
    path('Accounts/',views.acc_summary)
]
