from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include

router = DefaultRouter()
router.register(r'users', UsersViewSet, basename="users")
router.register(r'profiles', ProfilesViewSet, basename="profiles")
router.register(r'kids', KidsViewSet, basename="kids")
router.register(r'events', EventViewset, basename='events')
router.register(r'messages', MessagesViewSet, basename='messages')
router.register(r'messagelist', MessageListViewSet, basename='messageslist')

# urlpatterns = router.urls
urlpatterns = [
    path('', include(router.urls)),
    path('public', public),
    path('private', private),
    path('fetch-weather/<int:zipcode>', fetch_weather, name='fetch_weather'),
    path('fetch-local-events/', fetch_local_events, name='fetch-local-events'),

]

