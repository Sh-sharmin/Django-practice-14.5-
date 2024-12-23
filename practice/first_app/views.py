from django.shortcuts import render
from .forms import ExampleForm
# Create your views here.
def home(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            selected_author = form.cleaned_data['author']
            print(f"Selected Author: {selected_author}")
    else:
        form = ExampleForm()
    return render(request, 'home.html', {'form': form})