from django.urls import path
from app10 import views
app_name="app10"


urlpatterns = [
    path('builtin/',views.builtin,name="biltin"),
]
