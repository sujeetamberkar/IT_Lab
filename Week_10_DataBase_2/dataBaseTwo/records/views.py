from django.shortcuts import render, redirect, get_object_or_404
from .models import Human
from .forms import HumanForm

def human_list_update(request):
    humans = Human.objects.all()
    selected_human = None
    form = HumanForm()
    if 'select_human' in request.POST:
        selected_human = Human.objects.get(pk=request.POST.get('human_dropdown'))
        form = HumanForm(instance=selected_human)
    elif 'update_human' in request.POST:
        selected_human = get_object_or_404(Human, pk=request.POST.get('human_id'))
        form = HumanForm(request.POST, instance=selected_human)
        if form.is_valid():
            form.save()
            return redirect('records:human_list_update')
    elif 'delete_human' in request.POST:
        selected_human = get_object_or_404(Human, pk=request.POST.get('human_id'))
        selected_human.delete()
        return redirect('records:human_list_update')
    return render(request, 'records/human_list_update.html', {'humans': humans, 'form': form, 'selected_human': selected_human})

def add_human(request):
    if request.method == 'POST':
        form = HumanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('records:human_list_update')  # Redirect to the listing page which also has update/delete functionality
    else:
        form = HumanForm()
    return render(request, 'records/add_human.html', {'form': form})
