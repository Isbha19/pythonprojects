
from django.urls import path

from todoapp import views

urlpatterns = [
    path('', views.home,name="home"),
    path('delete/<int:taskid>', views.delete,name="delete"),
    path('update/<int:id>/', views.update,name="update"),
    path('cbview/', views.Tasklistview.as_view(), name="cbview"),
    path('cbdetails/<int:pk>/', views.Taskdetailview.as_view(), name="cbdetails"),
    path('cbupdate/<int:pk>/', views.Taskupdateview.as_view(), name="cbupdate"),
    path('cbdelete/<int:pk>/', views.Taskdeleteview.as_view(), name="cbdelete"),

]
