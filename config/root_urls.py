from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path("users", include(("apps.users.urls", "api-users"))),
    path("boards", include(("apps.boards.urls", "api-boards"))),
]

from config.settings.swagger.setup import SwaggerSetup  # noqa

urlpatterns = SwaggerSetup.do_urls(urlpatterns)

# Static/Media File Root (CSS, JavaScript, Images)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
