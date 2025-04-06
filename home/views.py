from django.shortcuts import render
from .forms import RespuestaForm

def index(request):
    if request.method == 'POST':
        form = RespuestaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'gracias.html')
    else:
        form = RespuestaForm()
    return render(request, 'index.html', {'form': form})
