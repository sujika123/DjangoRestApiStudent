from django.urls import path

from demoapp import views

urlpatterns = [

   path('api',views.student_list,name='api'),
   path('api2/<int:id>/',views.student_detail, name='api2'),

]






