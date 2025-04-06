from django.shortcuts import render
from .forms import RespuestaForm
from . import procesador  # importa tu archivo

def index(request):
    if request.method == 'POST':
        form = RespuestaForm(request.POST)
        if form.is_valid():
            respuesta = form.save()

            # Llamar al analizador de texto con la descripción ingresada
            resultados = procesador.procesar_respuesta(
                respuesta.seguro,
                respuesta.problema
            )

            return render(request, 'gracias.html', {
                'resultados': resultados,
                'nombre_seguro': respuesta.seguro,
                'descripcion': respuesta.problema,
            })
    else:
        form = RespuestaForm()
    return render(request, 'index.html', {'form': form})
