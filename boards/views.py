from django.shortcuts import render
from boards.models import Board
from boards.serializers import BoardSerializer
from rest_framework import viewsets

# Create your views here.

def hello_view(request):
    return render(request, 'MessageBoard.html', {
        'data': "Hello Django ",
    })

def getAllMessage(request):
    message_list = Board.objects.all()
    return render(request, 'MessageBoard.html', {
        'message_list': message_list
    })

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
