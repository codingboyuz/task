from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny


schema_view = get_schema_view(
    openapi.Info(
        title="Safe Worker API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="<EMAIL>"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[AllowAny],
)

# Add token authentication to Swagger UI
schema_view.get_auth = lambda: [
    openapi.Parameter(
        openapi.IN_HEADER,
        description="JWT Bearer token",
        type=openapi.TYPE_STRING,
        required=True,
    ),
]

urlpatterns = [
    # path('swagger(?P<format>\.json|\.yaml)',schema_view.without_ui(cache_timeout=0),name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]