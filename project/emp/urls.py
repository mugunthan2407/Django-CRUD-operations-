from django.urls import path,URLPattern
from emp import views
from django.contrib import admin

urlpatterns=[
    path('admin/',admin.site.urls),
    path('',views.show),
    path('show',views.show),
    path('emp',views.emp),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.destroy),
]