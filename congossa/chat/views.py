from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponse


## Returns dialog object if given two user ids
def getDialogFromIds(login1, login2):
    user1 = get_object_or_404(Utilisateur,username=login1) # récupération de l'objet user1
    user2 = get_object_or_404(Utilisateur,username=login2) # récupération de l'objet user2
    dialog = Dialog(owner=login1, opponent=login2)

    return dialog
    

## Add a message to the database when one is sent   
def addMessage(request):
    user1 = get_object_or_404(Utilisateur,username=login1) # récupération de l'objet user1
    user2 = get_object_or_404(Utilisateur,username=login2) # récupération de l'objet user1
    m = Message(dialog=getDialogFromIds(login1,login2), sender=user, text=message)
    m.save()


## Returns last 30messages of a dialog as a Json file
def getDialog(request):
    dialog = getDialogFromIds(login1,login2)
    messages = dialog.message_set.all().order_by('timestamp') # getting messages corresponding to the dialog and ordering them
    data =  sortMessages(messages)
    return JsonResponse(data)

def getLastMessage(request):
    user = get_object_or_404(Utilisateur,username=login) # récupération de l'objet user

def newDialog():

