from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from itertools import chain

from .models import Dialog, Message

## Returns dialog object if given two ids : one for 'offre' the other for 'demande'
#
@csrf_exempt
def getDialogFromIds(id_offre, id_demande):
    owner = Offre.objects.get(id=id_offre)
    opponent = Demande.objects.get(id=id_demande)
    dialog = Dialog.objects.get(owner=owner, opponent=opponent)

    return dialog


## Add a message to the database when one is sent
#
@csrf_exempt
def addMessage(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    idoffre = body['id_offre']
    iddemande = body['id_demande']
    sender = request.user;

    m = Message(dialog=getDialogFromIds(id_offre,id_demande), sender=sender, text=message)
    m.save()
    ## NOTIFIER l'utilisateur 2 qu'un message a été reçue


## Returns all messages of a dialog as a Json file
#
@csrf_exempt
def getDialog(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    idoffre = body['id_offre']
    iddemande = body['id_demande']

    dialog = getDialogFromIds(id_offre,id_demande)
    messages = dialog.message_set.all().order_by('timestamp') # getting messages corresponding to the dialog and ordering them
    data =  { 'messages' : messages}

    return JsonResponse(data)

@csrf_exempt
def getLastMessage(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    idoffre = body['id_offre']
    iddemande = body['id_demande']

    dialog = getDialogFromIds(id_offre,id_demande)
    messages = dialog.message_set.all().order_by('timestamp') # getting messages corresponding to the dialog and ordering them
    data = {'last-message' : messages[0]}

    return JsonResponse(data)

@csrf_exempt
def newDialog(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    idoffre = body['id_offre']
    iddemande = body['id_demande']

    d = Dialog(owner=idoffre, opponent=iddemande)
    d.save()

## Returns all the name of the people who had a dialog with user
#
@csrf_exempt
def allDialogUser(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    idoffre = body['id_offre']
    dialogs_list = []

    dialogs1 = Dialog.objects.filter(owner=id_offre)
    for d in dialogs1:
        dialogs_list+=[d.opponent.demandeur.username]

    dialogs2 = Dialog.objects.filter(opponent=id_offre)
    for d in dialogs2:
        dialogs_list+=[d.owner.recruteur.username]

    data = {'dialogs' : dialogs_list}
    return JsonResponse(data)


def index(request):
    return JsonResponse({'success': "OK"})
