from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from itertools import chain
import json

from .models import Dialog, Message
from utilisateur.models import Utilisateur
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
    id_offre = body['id_offre']
    id_demande = body['id_demande']
    id_sender = body['id_user']
    text = body ['message']

    sender = Utilisateur.objects.get(id=id_sender)

    m = Message(dialog=getDialogFromIds(id_offre,id_demande), sender=sender, text=message)
    m.save()
    ## NOTIFIER l'utilisateur 2 qu'un message a été reçue


## Returns all messages of a dialog as a Json file
#
@csrf_exempt
def getDialog(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    id_offre = body['id_offre']
    id_demande = body['id_demande']

    dialog = getDialogFromIds(id_offre,id_demande)
    messages = dialog.message_set.all().order_by('timestamp') # getting messages corresponding to the dialog and ordering them

    messages_text = []# the text of the message_set
    messages_sender = [] # the person who sent the message

    for message in messages:
        messages_text += message.text
        messages_sender += message.sender.username

    data =  { 'messages_text' : messages_text, 'messages_sender' : messages_sender}

    return JsonResponse(data)

## Returns last message given id_demande and id_offre
#
def getlastmessage(id_demande, id_offre):
    dialog = getDialogFromIds(id_offre,id_demande)
    messages = dialog.message_set.all().order_by('timestamp') # getting messages corresponding to the dialog and ordering them

    if (len(messages)==0):
        return " "
    else:
        return messages[len(messages)-1].text

@csrf_exempt
def getLastMessage(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    id_offre = body['id_offre']
    id_demande = body['id_demande']

    data = {'last-message' : getlastmessage(id_demande, id_offre)}

    return JsonResponse(data)

@csrf_exempt
def newDialog(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    id_offre = body['id_offre']
    id_demande = body['id_demande']

    d = Dialog(owner=id_offre, opponent=id_demande)
    d.save()

## Returns all the name of the people who had a dialog with user and the last message
#
@csrf_exempt
def allDialogUser(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    id_user = body['id_user']

    dialogs_info = []

    user = Utilisateur.objects.get(id=id_user)
    offres = Offre.objects.filter(recruteur=user) # Getting the offers user has a dialog with
    demandes = Demande.objects.filter(demandeur=user) # Getting the demandes user has a dialog with

    for offre in offres:
        dialogs_info += alldialoguser(offre.id, True)

    for demande in demandes:
        dialogs_info += alldialoguser(demande.id, False)

    data = {'dialogs' : dialogs_info}
    return JsonResponse(data)

def alldialoguser(idd, is_offre):
    dialogs_info = []

    if (is_offre):
        dialogs = Dialog.objects.filter(owner=idd) # request by 'owner'
        for dialog in dialogs:
            id_demande = dialog.opponent.id
            opponent = dialog.opponent.demandeur.username
            last_message = getlastmessage(id_demande, idd)
            dialogs_info += [[idd, id_demande, opponent, last_message]]
    else:
        dialogs = Dialog.objects.filter(opponent=idd) # request by 'opponent'
        for dialog in dialogs:
            id_offre = dialog.owner.id
            owner = dialog.owner.recruteur.username
            last_message = getlastmessage(id_offre, idd)
            dialogs_info += [[id_offre, idd, owner, last_message]]

    return dialogs_info


def index(request):
    return JsonResponse({'success': "OK"})
