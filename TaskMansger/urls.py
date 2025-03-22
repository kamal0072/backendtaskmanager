from django.contrib import admin
from django.urls import path, include
from task import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tasks', views.TaskViewSet )

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('api/', include(router.urls)),
]
