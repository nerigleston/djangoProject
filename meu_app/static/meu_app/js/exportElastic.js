function exportToElasticsearch(url) {
  fetch(url, {
      method: 'GET',
      headers: {
          'Content-Type': 'application/json',
      },
  })
  .then(response => response.json())
  .then(data => {
    alert(data.message);
  })
  .catch(error => {
    console.error('Erro ao exportar dados para o Elasticsearch:', error);
    alert('Erro ao exportar dados para o Elasticsearch.');
  });
}
document.getElementById('export-link').addEventListener('click', function (event) {
  event.preventDefault();
  exportToElasticsearch(this.href);
});

