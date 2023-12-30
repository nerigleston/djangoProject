from django.shortcuts import render, redirect
from .models import Dado
from .forms import DadoForm
from django.http import HttpResponse
import csv


def manipular_dados(request):
    dados = Dado.objects.all()
    form = DadoForm()

    if request.method == 'POST':
        form = DadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manipular_dados')

    return render(request, 'meu_app/manipular_dados.html', {'dados': dados, 'form': form})


def export_csv(request):
    dados = Dado.objects.all()
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="exported_data.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(["Nome", "Idade"])

    for dado in dados:
        writer.writerow([dado.nome, dado.idade])

    return response


def remover_dado(request, dado_id):
    dado = Dado.objects.get(id=dado_id)
    dado.delete()
    return redirect('manipular_dados')
