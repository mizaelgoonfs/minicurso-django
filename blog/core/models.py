from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
import unicodedata

# Create your models here.
class Post(models.Model):
    title = models.CharField('Título', max_length=300, blank=False, null=False)
    resume = models.TextField('Resumo', max_length=500, blank=False, null=False, default='')
    content = RichTextField()
    date_published = models.DateTimeField('Data de publicação', auto_now_add=True)
    slug = models.SlugField('Slug', editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        old_string = self.title
        new_string = ''.join(ch for ch in unicodedata.normalize('NFKD', old_string) if not unicodedata.combining(ch))

        self.slug = slugify(new_string, allow_unicode=True)
        filter_slug = Post.objects.filter(slug=self.slug)
        if(filter_slug):
            self.slug += '-1'
        super().save(*args, **kwargs)