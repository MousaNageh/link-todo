from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="LINK DEVELOPMENT",
        default_version='v1',
        description="Api For End Users To See Their Tasks.",
        contact=openapi.Contact(email="200moussa200@gmail.com")
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

admin.site.site_header = 'LINK DEVELOPMENT'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include("users.urls")),
    path('api/tasks/', include("tasks.urls")),
    path('', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),
]