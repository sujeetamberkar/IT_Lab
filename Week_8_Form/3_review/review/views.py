from django.shortcuts import render
from .forms import VoteForm

def vote_book(request):
    # Initialize the vote counts if not already done
    if 'good' not in request.session:
        request.session['good'] = 0
        request.session['satisfactory'] = 0
        request.session['bad'] = 0
    
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            # Increment the vote count for the selected choice
            choice = form.cleaned_data['vote']
            request.session[choice] += 1
            request.session.modified = True  # Make sure the session is saved
            
    else:
        form = VoteForm()

    # Calculate percentages
    total_votes = request.session['good'] + request.session['satisfactory'] + request.session['bad']
    percentages = {
        'good': request.session['good'] / total_votes * 100 if total_votes > 0 else 0,
        'satisfactory': request.session['satisfactory'] / total_votes * 100 if total_votes > 0 else 0,
        'bad': request.session['bad'] / total_votes * 100 if total_votes > 0 else 0,
    }

    return render(request, 'vote.html', {'form': form, 'percentages': percentages})
