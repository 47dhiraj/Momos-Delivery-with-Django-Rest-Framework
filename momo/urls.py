from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions



from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(                                      # For Swagger UI (openapi)

   openapi.Info(
      title="Momo Delivery Service",
      default_version='v1',
      description="This is a REST API for a Momo Delivery Service",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),

)



urlpatterns = [

    # url for admin panel or dashboard
    path('admin/', admin.site.urls),

    # url for authentication app
    path('auth/',include('authentication.urls')),

    # url for orders app
    path('',include('orders.urls')),


    # djoser le provide gareko Backend JWT Authentication URL
    path('auth/', include('djoser.urls.jwt')),
    # yo mathi ko auth/ url provides the following major endpoint/url:
    # auth//jwt/create/  to obtain JSON Web Token(JWT) i.e login jasto garna ko lagi use huncha.
    # auth/jwt/refresh/  to refresh JSON Web Token i.e refresh token diyera access token get garincha.
    # auth/jwt/verify/   to verify JSON Web Token i.e token lai verify garna paryo vani.
    

    # URL for swagger ui, 
    path('swagger<format>.json|.yaml/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]


