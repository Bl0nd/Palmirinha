from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome  

class Receita(models.Model):

    DIFICULDADES = [('F','Fácil'),('M','Moderado'),('D','Dificil'),]

    nome = models.CharField(max_length=50)
    ingredientes = models.TextField(max_length=2000)
    preparo = models.TextField(max_length=8000)
    dificuldade = models.CharField(max_length=10,choices=DIFICULDADES)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='imagens/', null=True)

    def __str__(self):
        return self.nome  