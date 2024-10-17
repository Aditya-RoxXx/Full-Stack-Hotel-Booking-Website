from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from . forms import PaymentForm
from . models import Category, Room

def rooms(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    rooms = Room.objects.filter(is_booked=False)

    if category_id:
        rooms = rooms.filter(category_id=category_id)

    if query:
        rooms = rooms.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    return render(request, 'bookings/rooms.html', {
        'rooms': rooms,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })

def detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    related_rooms = Room.objects.filter(category=room.category, is_booked=False).exclude(pk=pk)[0:3]

    return render(request, 'bookings/detail.html', {
        'room': room,
        'related_rooms': related_rooms
    })


@login_required
def payment(request, room_id):
    room = get_object_or_404(Room, pk=room_id)

    if request.method == 'POST':
        form = PaymentForm(request.POST)

        if form.is_valid():
            payment = form.save(commit=False)
            payment.room = room
            payment.user = request.user
            payment.save()

            room.is_booked = True
            room.save()

            print("Form is valid, payment processed, and room status updated.")
            return redirect('bookings:detail', pk=room.id)
        else:
            print(form.errors)
    else:
        form = PaymentForm()

    return render(request, 'bookings/form.html', {
        'form': form,
        'title': 'Payment',
    })

@login_required
def delete(request, pk):
    room = get_object_or_404(Room, pk=pk, rented_by=request.user)
    room.delete()

    return redirect('core:index')