from django.contrib import admin
from django.urls import path
from ExpenseTracker import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.dashboard),
    path('add_expense/',views.add_expense)
]
