from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from itertools import chain

from .models import Dialog, Message

## Returns dialog object if given two user ids
#
@csrf_exempt
def getDialogFromIds(login1, login2):
    user1 = get_object_or_404(Utilisateur,username=login1)
    user2 = get_object_or_404(Utilisateur,username=login2)
    dialog = get_object_or_404(Dialog, owner=login1, opponent=login2)

    return dialog


## Add a message to the database when one is sent
#
@csrf_exempt
def addMessage(request):
    user1 = get_object_or_404(Utilisateur,username=login1)
    m = Message(dialog=getDialogFromIds(login1,login2), sender=user1, text=message)
    m.save()
    ## NOTIFIER l'utilisateur 2 qu'un message a été reçue


## Returns all messages of a dialog as a Json file
#
@csrf_exempt
def getDialog(request):
    dialog = getDialogFromIds(login1,login2)
    messages = dialog.message_set.all().order_by('timestamp') # getting messages corresponding to the dialog and ordering them
    data =  { 'messages' : messages}

    return JsonResponse(data)

@csrf_exempt
def getLastMessage(request):
    dialog = getDialogFromIds(login1,login2)
    messages = dialog.message_set.all().order_by('timestamp') # getting messages corresponding to the dialog and ordering them
    data = {'last-message' : messages[0]}

    return JsonResponse(data)

@csrf_exempt
def newDialog(request):
    user1 = get_object_or_404(Utilisateur,username=login1)
    user2 = get_object_or_404(Utilisateur,username=login2)
    d = Dialog(owner=user1, opponent=user2)
    d.save()

## Returns all the name of the people who had a dialog with user
#
@csrf_exempt
def allDialogUser(request):
    dialogs_list = []
    user = request.user;

    dialogs1 = Dialog.objects.filter(owner=user)
    for d in dialogs1:
        dialogs_list+=[d.opponent.username]

    dialogs2 = Dialog.objects.filter(opponent=user)
    for d in dialogs2:
        dialogs_list+=[d.opponent.username]

    data = {'dialogs' : dialogs_list}
    return JsonResponse(data)


def index(request):
    return JsonResponse({'success': "OK"})
