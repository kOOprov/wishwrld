from django.urls import path
from.import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns =[
    path ('',views.index ,name='mainpage'),
    path ('mabout',views.mabout,name='wishpage'),
    path ('songs/',views.songs,name='songs'),
    path ('albums',views.albums,name='albums'),
    path ('feedback/',views.feedback,name='feedback'),
    path ('ochenvajno',views.ochenvajno,name='ochenvajno'),
    path ('my_playlist', views.my_playlist, name='my_playlist'),
    path('comm_success',views.comm_success, name = 'comm_success'),
    path('create_songs/',views.create_songs, name = 'create_songs'),
    path('search_result/',views.search_result,name='search_result')
] + static (settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
