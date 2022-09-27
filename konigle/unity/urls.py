from django.urls import path, include
from .views import StoreTemplateViews, UnityEmailList, EmailLeadsListViews
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'api'

router = routers.DefaultRouter()

urlpatterns = [
    path('', StoreTemplateViews.as_view(), name='store'),
    path('', include(router.urls)),
    path('leads/', UnityEmailList.as_view(), name='leads'),
    path('email-leads/', EmailLeadsListViews.as_view(), name='email_leads'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
