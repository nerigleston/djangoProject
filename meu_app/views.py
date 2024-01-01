from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Dado
from .forms import DadoForm
from django.http import HttpResponse
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from elasticsearch.exceptions import NotFoundError

es = Elasticsearch(['http://localhost:9200'])


def manipular_dados(request):
    dados = Dado.objects.all()
    form = DadoForm()

    if request.method == 'POST':
        form = DadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manipular_dados')

    return render(request, 'meu_app/manipular_dados.html', {'dados': dados, 'form': form})


def export_to_elasticsearch(request):
    dados = Dado.objects.all()

    actions = [
        {
            "_op_type": "index",
            "_index": "meu_app_index",
            "_source": {
                'nome': dado.nome,
                'idade': dado.idade,
            }
        }
        for dado in dados
    ]

    bulk(es, actions)

    response_data = {
        'message': 'Dado exportado com sucesso para o Elasticsearch!'}
    return JsonResponse(response_data)


def retrieve_data_from_elasticsearch(request):
    search_query = {
        "query": {
            "match_all": {}
        }
    }

    try:
        results = es.search(index='meu_app_index', body=search_query)
    except NotFoundError:
        results = {'hits': {'hits': []}}

    hits = results.get('hits', {}).get('hits', [])

    data_from_elasticsearch = []
    for hit in hits:
        source = hit.get('_source', {})
        nome = source.get('nome', '')
        idade = source.get('idade', 0)
        entry_id = hit.get('_id')
        data_from_elasticsearch.append(
            {'nome': nome, 'idade': idade, 'id': entry_id})

    return render(request, 'meu_app/retrieve_data_from_elasticsearch.html', {'data_from_elasticsearch': data_from_elasticsearch})


def remover_dado(request, dado_id):
    dado = Dado.objects.get(id=dado_id)
    dado.delete()
    return redirect('manipular_dados')


def remover_dado_elastic(request, document_id):
    try:
        response = es.delete(index='meu_app_index',
                             doc_type='_doc', id=document_id)

        if response.get('result') == 'deleted':
            return JsonResponse({'success': True, 'message': 'Documento removido do Elasticsearch com sucesso.'})
        else:
            return JsonResponse({'success': False, 'message': 'Falha ao remover o documento do Elasticsearch.'})

    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Falha ao remover o documento do Elasticsearch. Erro: {str(e)}'})
