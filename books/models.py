from django.db import models
from django.urls import reverse


class Books(models.Model):
    DoesNotExist = None
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    book = models.FileField(upload_to='books/%Y/%m/%d/', verbose_name='книга', blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d', verbose_name='фото', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')

    def get_absolute_url(self):
        return reverse('detail', kwargs={"book_id": self.pk})


    def __str__(self):
        return f'{self.title}- {self.author}'

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

        ordering = ['-created_at']

    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Comment(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, default=None)
    text = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.book}'



