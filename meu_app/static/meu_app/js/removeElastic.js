function removeDadoFromElasticsearch(url) {
  console.log('URL:', url); // Check if the URL is correct
  fetch(url, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  })
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      alert(data.message);
      location.reload();
    } else {
      alert('Erro ao remover documento do Elasticsearch: ' + data.message);
    }
  })
  .catch(error => {
    console.error('Erro ao remover documento do Elasticsearch:', error);
    alert('Erro ao remover documento do Elasticsearch.');
  });
}
document.querySelectorAll('.remove-link').forEach(link => {
  link.addEventListener('click', function (event) {
    event.preventDefault();
    removeDadoFromElasticsearch(this.href);
  });
});
