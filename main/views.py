import re

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import FeedbackForm, UploadSongsForm
from .models import Feedback, UploadSongs, MyPlaylist
from django.db.models import Q


def index(request):
    return render (request,'main/index.html')
def mabout (request):
    return render(request,'main/mabout.html')
def feedback (request):
    error = ''
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comm_success')
        else:
            error = 'Форма неверно заполнена'
    feedbacks = Feedback.objects.all()
    form = FeedbackForm()
    data = {
        'form':form,
        'feedbacks':feedbacks,
        'error':error
    }
    return render (request,'main/feedback.html', data)
def songs (request):
    error = ''
    if request.method == 'POST':
        form = UploadSongsForm(request.POST, request.FILES)
        if form.is_valid():
            file_upload = UploadSongs(file=form.cleaned_data['file'],
            song_name = form.cleaned_data['song_name']
            )
            file_upload.save()
            return redirect('songs')
        else:
            error = ''
    else:
        form = UploadSongsForm()
    song = UploadSongs.objects.all()
    return render(request, 'main/songs.html', {'form': form, 'song': song, 'error': error})
def albums(request):
    return render(request,'main/albums.html')
def ochenvajno(request):
    return render(request,'main/ochenvajno.html')
def my_playlist(request):
    song = MyPlaylist.objects.all()
    return render(request,'main/my_playlist.html',{'song':song})
def comm_success(request):
    return render (request, 'main/comm_success.html')
def create_songs (request):
    error = ''
    if request.method == 'POST':
        form = UploadSongsForm(request.POST, request.FILES)
        if form.is_valid():
            file_upload = UploadSongs(file=form.cleaned_data['file'],
            song_name = form.cleaned_data['song_name'],
            autor = form.cleaned_data['autor']
            )
            file_upload.save()
            return redirect('songs')
        else:
            error = ''
    else:
        form = UploadSongsForm()
    song = UploadSongs.objects.all()
    return render(request, 'main/create_songs.html', {'form': form, 'song': song, 'error': error})
def search_result(request):
    query = request.GET.get('song_name','')
    if query:
        song = UploadSongs.objects.filter(Q(song_name__iregex=r'^.*' + re.escape(query) + r'.*$')
                                          | Q(autor__iregex=r'^.*' + re.escape(query) + r'.*$'))
        context = {
            'song':song,
            'query':query
        }
        return render(request,'main/search_result.html',context)
    else:
        return HttpResponse('Нет результатов')