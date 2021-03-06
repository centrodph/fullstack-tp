"""interview_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from django.views.static import serve
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import settings
from interview.urls import router as interview_router
from candidate.urls import router as candidate_router
from question.urls import router as question_router
from challenge.urls import router as challenge_router

router = routers.DefaultRouter()
router.registry.extend(interview_router.registry)
router.registry.extend(candidate_router.registry)
router.registry.extend(question_router.registry)
router.registry.extend(challenge_router.registry)

schema_view = get_schema_view(
    openapi.Info(
        title="Full stack TP",
        default_version='v1',
        description="API for the Full stack TP",
        contact=openapi.Contact(email="centrodph@gmail.com"),
    ),
    public=True,
)


static_urlpatterns = [
    re_path(r"static/(?P<path>.*)$", serve, {"document_root": "static"}),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
