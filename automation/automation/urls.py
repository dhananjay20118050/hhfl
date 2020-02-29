from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from RPAPanel import views

router = DefaultRouter()
router.register(r'apps', views.AppViewSet)
router.register(r'node', views.NodeViewSet)
router.register(r'hubs', views.HubViewSet)
router.register(r'appdatacapturetracking', views.TrackingViewSet)
router.register(r'UpdatedataViewSet', views.TimelineViewSet)
router.register(r'getfiledata', views.FileDdataViewSet)
router.register(r'errortracking', views.ErrorViewSet)

admin.site.site_header = "Wipro Bank Portal"
admin.site.site_title = "Wipro Bank Portal"
admin.site.index_title = "Wipro Bank Portal"

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', admin.site.urls),

    url(r'^appdata/(?P<appid>\d+)/$', views.pagedata),
    # Node
    path('edit/<int:id>', views.edit),

    # Hubs
    url(r'^hubs/', views.indexhub),
    path('createhub/', views.addhub, name='createhub'),
    path('edithubs/<int:id>', views.edithubs),


    # Process
    url(r'^process/', views.indexprocess),
    path('createprocess/', views.addprocess, name='createprocess'),

    # master app link
    url(r'^apps/', views.indexapps),
    path('createapps/', views.addapps, name='createapps'),
    path('editapps/<int:id>', views.editapps),

    # Process
    url('datacapture/startDataCapture', views.startDataCapture),
    url('datacapture/exportData', views.exportData),
    url(r'^datacapture/', views.indexdatacapture),
    url(r'^api/', include(router.urls)),

    path('upload_file', include('upload_file.urls')),

]
