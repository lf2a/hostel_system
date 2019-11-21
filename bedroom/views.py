# django library
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator

# django local
from core.models import Booking
from .models import Bedroom, BedroomImage
from hostel.settings import NUM_OF_ELEMENTS


def bedrooms(request):
    '''Buscando quartos disponiveis

    render:
        list: envia para o template uma lista contendo os quartos que não estão reservados
    '''
    bedroom = Bedroom.objects.all()
    booking = Booking.objects.all()

    available_rooms = []
    for b in booking:
        available_rooms.append(b.bedroom)

    available_rooms = set(bedroom).difference(set(available_rooms))

    data = []
    for r in available_rooms:
        images = BedroomImage.objects.filter(bedroom__id=r.id)

        data.append({
            'id': r.id,
            'number': r.number,
            'floor': r.floor,
            'bathroom': r.bathroom,
            'bed': r.bed,
            'daily': r.daily,
            'images': images,
        })

    paginator = Paginator(data, NUM_OF_ELEMENTS)

    page = request.GET.get('p')
    rooms = paginator.get_page(page)

    return render(
        request=request,
        template_name='bedrooms.html',
        context={
            'data': rooms
        }
    )


def bedroom(request, id):
    '''Mostrar informações do quarto

    render:
        dict: retorna as informações do quarto para serem acopladas no template
    '''
    data = {}

    bedroom = get_object_or_404(Bedroom, id=id)
    images = get_list_or_404(BedroomImage, bedroom__id=bedroom.id)

    try:
        data = {
            'id': bedroom.id,
            'number': bedroom.number,
            'floor': bedroom.floor,
            'bathroom': bedroom.bathroom,
            'bed': bedroom.bed,
            'daily': bedroom.daily,
            'images': images,
        }

    except NameError:
        data = {
            'id': '',
            'number': '',
            'floor': '',
            'bathroom': '',
            'bed': '',
            'daily': '',
            'images': '',
        }

    return render(
        request=request,
        template_name='bedroom.html',
        context=data
    )
