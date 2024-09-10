from django.db import models

# Create your models here.

class Setor(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    status = models.CharField(max_length=50)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    usuarios = models.ManyToManyField(Usuario)
    imagem = models.ImageField(upload_to='medias/', blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo