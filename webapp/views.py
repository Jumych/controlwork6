from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Book_Guest
from webapp.error import GuestForm
# Create your views here.


def index_view(request):
    guestbooks = Book_Guest.objects.order_by('-deadline')


    context = {
        'guestbooks': guestbooks
    }
    return render(request, 'index.html', context)


def add_book(request):
    if request.method == "GET":
        form = GuestForm()
        return render(request, 'add_book.html', {'form': form})
    if request.method == "POST":
        form = GuestForm(data=request.POST)
        if form.is_valid():
            f = Book_Guest.objects.create(name=form.cleaned_data['name'], email=form.cleaned_data['email'], description=form.cleaned_data['description'])
            return redirect('index')
        else:
            return render(request, 'add_book.html', {'form', form})


def update_book(request, pk):
    guestbooks = get_object_or_404(Book_Guest, pk=pk)
    if request.method == 'GET':
        form = GuestForm(initial={
            'name': guestbooks.name,
            'email': guestbooks.email,
            'description': guestbooks.description
        })
        return render(request, "update.html", {'form': form})
    elif request.method == 'POST':
        form = GuestForm(data=request.POST)
        if form.is_valid():
            guestbooks.name = form.cleaned_data.get('author')
            guestbooks.email = form.cleaned_data.get('gmail')
            guestbooks.description = form.cleaned_data.get('description')
            guestbooks.save()
            return redirect('index')
        else:
            return render(request, "update.html", {'form': form})


def book_delete(request, pk):
    guest = get_object_or_404(Book_Guest, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'guest': guest})
    elif request.method == 'POST':
        guest.delete()
        return redirect('index')