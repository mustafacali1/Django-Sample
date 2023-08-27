from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import Meeting, Room
from .forms import RoomForm

# region Static Pages
# request => http://127.0.0.1:8000/welcome.html
def welcome(request):
    return render(request,
                  'website/welcome.html',
                  {
                      'message': 'Welcome to the Meeting Planer App',
                      'num_meeting': Meeting.objects.count(),
                      'meetings': Meeting.objects.all()
                  })


# Request => http://127.0.0.1:8000/date
def date(request):
    return HttpResponse(f'This page was served at {str(datetime.now())}')


# request => http://127.0.0.1:8000/about
def about(request):
    return HttpResponse('Copy right Tyson Solution..!')


# endregion


# region Room
def room_list(request):
    return render(request,
                  'rooms/room_list.html',
                  {'rooms': Room.objects.all()})


def room_detail(request, id):
    room = get_object_or_404(Room, pk=id)

    return render(request,
                  'rooms/detail.html',
                  {'room': room})


def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form = RoomForm()

    return render(
        request,
        'room/create.html',
        {'form': form}
    )

# endregion


# region Meetings
def meeting_detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)

    return render(request,
                  'meetings/detail.html',
                  {'meeting': meeting})
# endregion
