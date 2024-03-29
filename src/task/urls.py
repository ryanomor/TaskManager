from django.conf.urls import url, include
from task import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it
router = DefaultRouter(trailing_slash=False)
router.register(r'tasks', views.TaskItemViewSet)

# The API URLs are now determined automatically by the router
urlpatterns = [
    url(r'^', include(router.urls)),
]
