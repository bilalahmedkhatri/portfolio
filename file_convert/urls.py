from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ViewConvertFile, download_file, front


urlpatterns = [
    path('demo/image-to-doc/', ViewConvertFile.as_view(), name="file_to_doc"),
    path('demo/image-to-<int:id>', download_file, name="downloadfile"),
    path('', front, name="front"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

