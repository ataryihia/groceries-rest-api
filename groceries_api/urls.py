from django.urls import path, include

from rest_framework.routers import DefaultRouter
from groceries_api import views

router = DefaultRouter()
router.register('groceries', views.GroceriesViewSet,basename='groceriesModel')
router.register('profile', views.UserProfileViewSet,basename='profileModel')

urlpatterns = [
    path('login',views.UserLoginApiView.as_view()),
    path('', include(router.urls)),

]
