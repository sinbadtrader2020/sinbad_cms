
from django.urls import include, path
from . import views
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'blogs', views.BlogViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/api/', include(router.urls)),
    path('admin/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls, name='admin'),

]




