from django.db import models


class Dado(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()

    def __str__(self):
        return f"{self.nome} - {self.idade}"

    def get_display_text(self):
        return f"{self.nome} - {self.idade}"


class Meta:
    app_label = 'meu_app'
