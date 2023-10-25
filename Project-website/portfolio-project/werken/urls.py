from django.urls import path, include
from . import views

urlpatterns = [
 path('<int:werken_id>', views.detail, name='detail'),
] 