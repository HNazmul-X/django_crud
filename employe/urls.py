from django.urls import path
from employe import views

urlpatterns = [
    path("", views.employee_form, name="employee_form"),
    path("list/", views.employee_list, name="employee_list"),
    path("edit/<slug:id>", views.employee_update,name="employee_update"),
    path("/delete/<slug:id>", views.deleteEmployee,name="delete_employe")
]
