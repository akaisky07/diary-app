from django.shortcuts import render, redirect, get_object_or_404
from .models import Entry
from .forms import EntryForm

def home(request):
    entries = Entry.objects.all()
    return render(request, 'home.html', {'entries': entries})

def create_entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EntryForm()
    return render(request, 'create_entry.html', {'form': form})

def delete_entry(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id)
    if request.method == 'POST':
        entry.delete()
        return redirect('home')
    return render(request, 'delete_entry.html', {'entry': entry})

