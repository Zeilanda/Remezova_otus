from django.shortcuts import render, get_object_or_404

# Create your views here.
from cards.models import Card


def index(request):
    return render(request, 'cards/index.html')


def cards_list(request):
    cards = Card.objects.all()
    context = {
        'cards': cards,
    }
    return render(request, 'cards/cards_list.html', context=context)


def card_details(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    context = {
        'card': card,
    }
    return render(request, 'cards/card_details.html', context=context)
#
