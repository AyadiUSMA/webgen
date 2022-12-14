from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
# Create your views here.


# Create your views here.
def index(request):
    """View function for home page of site."""


    num_visits = request.session.get('num_visits',0)
    request.session['num_visits']= num_visits +1
    context = {
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
