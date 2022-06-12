from app.views import *
from rest_framework import routers
from django.urls import path

router = routers.DefaultRouter()
router.register(r'news', NewsView, basename='news')
router.register(r'murojat', MurojatView, basename='murojat')
router.register(r'yuridik', YuridikView, basename='yuridik')

urlpatterns = router.urls

# urlpatterns += [
#     path('news/', NewsView.as_view(), name='news'),
# ]