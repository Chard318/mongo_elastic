from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

'''
from django.conf.urls import url, include
from rest_framework import routers
from shellfish.expertfinder import views

router = routers.DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)
'''

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('expertfinder.urls'))
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)