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

def update_book(request.pk=pk):
    guest = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        return render(request, 'task_update.html', {'task': task, 'statuses': STATUS_CHOICES})
    elif request.method == "POST":
        task.title = request.POST.get('title')
        task.status = request.POST.get('status')
        task.deadline = request.POST.get('deadline')
        task.description = request.POST.get('description')
        if not task.deadline:
            task.deadline = None
        task.save()
        return redirect('index', pk=guestbooks.pk)