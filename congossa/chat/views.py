from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from itertools import chain
import json

from .models import Dialog, Message
from offre.models import Offre, Demande

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

##
# Returns last message given id_demande and id_offre
def getlastmessage(id_demande, id_offre):
    dialog = getDialogFromIds(id_offre,id_demande)
    messages = dialog.message_set.all().order_by('timestamp') # getting messages corresponding to the dialog and ordering them
    return messages[len(messages)-1].text

@csrf_exempt
def getLastMessage(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    idoffre = body['id_offre']
    iddemande = body['id_demande']

    data = {'last-message' : getlastmessage(id_demande, id_offre)}

    return JsonResponse(data)

@csrf_exempt
def newDialog(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    idoffre = body['id_offre']
    iddemande = body['id_demande']

    d = Dialog(owner=idoffre, opponent=iddemande)
    d.save()

## Returns all the name of the people who had a dialog with user and the last message
#
@csrf_exempt
def allDialogUser(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    id_user = body['id_user']

    dialogs_info = []
    user = Utilisateur.objects.filter(id=id_user)
    id_offre = Offre.objects.filter(recruteur=user) # Getting the offers user has a dialog with
    is_offre = [True for i in range(len(id_offre))]

    id_offre += Demande.objects.filter(demandeur=user) # Getting the demandes user has a dialog with
    is_offre += [False for i in range(len(len(id_offre)-len(id_offre)))]

    for i in range(len(id_offre)):
        dialogs_info += alldialoguser(id_offre[i], is_offre[i])

    data = {'dialogs' : dialogs_info}
    return JsonResponse(data)

def alldialoguser(id_offre, is_offre):
    dialogs_info = []

    if (is_offre):
        dialogs = Dialog.objects.filter(owner=idoffre) # request by 'owner'
        for d in dialogs:
            iddemande = d.opponent.id
            opponent = d.opponent.demandeur.username
            last_message = getlastmessage(iddemande,idoffre)
            dialogs_info += [[opponent, last_message]]

    if (not(is_offre)):
        dialogs = Dialog.objects.filter(opponent=idoffre) # request by 'opponent'
        for d in dialogs:
            iddemande = d.owner.id
            owner = d.owner.recruteur.username
            last_message = getlastmessage(iddemande,idoffre)
            dialogs_info += [[owner, last_message]]

    return dialogs_info


def index(request):
    return JsonResponse({'success': "OK"})
