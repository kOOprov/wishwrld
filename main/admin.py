from django.contrib import admin
from .models import Feedback, UploadSongs, MyPlaylist

admin.site.register(Feedback)
admin.site.register (UploadSongs)
admin.site.register (MyPlaylist)