from django.urls import path
from upload_file import views

# from pl_dc_pro.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
# from django.conf.urls.static import static
urlpatterns = [
    # path('', views.index, name = 'index'),
    # path('', views.index, name='upload_file'),
    path('insert_file', views.insert_file, name='insert_file'),
]
# DataFlair
# if DEBUG:
#     urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
#     urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)
