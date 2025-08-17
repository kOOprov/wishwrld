from django.core.validators import FileExtensionValidator
from django.db import models

class Feedback(models.Model):
    name= models.CharField(help_text='имя',max_length=75,default='wishwrld user')
    full_text = models.TextField('текст комментария')
    date= models.DateTimeField('дата публикации')

    def __str__(self):
        return self.full_text

    class Meta:
        verbose_name ='feedback'
        verbose_name_plural ='feedbacks'

class UploadSongs(models.Model):
    autor = models.CharField(max_length=75)
    song_name = models.CharField(max_length=75)
    file = models.FileField(upload_to='uploadsmodel',validators=[FileExtensionValidator(allowed_extensions=['mp3'])])

    def __str__(self):
        return self.song_name

    class Meta:
        verbose_name ='Song'
        verbose_name_plural ='Songs'

class MyPlaylist(models.Model):
    autor = models.CharField(max_length=75)
    song_name = models.CharField(max_length=75)
    file = models.FileField(upload_to='uploadsmodel',validators=[FileExtensionValidator(allowed_extensions=['mp3','mp4','m4a'])])


    def __str__(self):
        return self.song_name

    class Meta:
        verbose_name ='My Playlist Song'
        verbose_name_plural ='My Playlist Songs'