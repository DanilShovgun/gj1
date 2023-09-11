from django.db import models
from django.core.exceptions import ValidationError

class Tag(models.Model):
    name = models.CharField(max_length=50)

class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='article_images/')
    tags = models.ManyToManyField(Tag, through='Scope')

    class Meta:
        ordering = ['title']

class Scope(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField()
    
    def clean(self):
        main_scopes = Scope.objects.filter(article=self.article, is_main=True)
        if self.is_main:
            if main_scopes.exists():
                raise ValidationError('Основной тег уже существует.')
        elif not self.is_main and not main_scopes.exists():
            raise ValidationError('Должен быть один основной тег.')