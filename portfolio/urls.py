from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# for static file on server
from django.conf.urls import url
from django.views.static import serve


urlpatterns = [
    # remove debug error
    # url(r'^media/(?P<path>.*)$', serve,
    #     {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('api-portfolio/', include('portfolio_api.urls')),
    path('', include('file_convert.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
