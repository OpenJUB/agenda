from django.shortcuts import render

from .models import AgendaItem


def index(request):
    if request.method == 'POST' and request.POST.get('addItem'):
        itemText = request.POST.get('addItem', '')
        if itemText != '':
            newItem = AgendaItem.objects.create(text=itemText)
            newItem.save()
    aItems = list(AgendaItem.objects.all())
    return render(request, 'index.html', {'agendaItems': aItems})
