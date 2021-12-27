from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView

from cards.models import Card


def index(request):
    cards = Card.objects.all()
    context = {
        'cards': cards,
    }
    return render(request, 'cards/index.html', context=context)


class CardsListView(ListView):
    model = Card


# def cards_list(request):
#     cards = Card.objects.all()
#     context = {
#         'cards': cards,
#     }
#     return render(request, 'cards/card_list.html', context=context)


# def card_details(request, card_id):
#     cards = Card.objects.all()
#     card = get_object_or_404(Card, pk=card_id)
#     context = {
#         'card': card,
#         'cards': cards,
#
#     }
#     return render(request, 'cards/card_detail.html', context=context)
#


class CardDetailView(DetailView):
    model = Card
