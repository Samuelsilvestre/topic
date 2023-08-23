from django.db import models
from django.contrib.auth.models import User

class Base(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now_add = True)

    class Meta:
        abstract = True

class Topic(Base):
    title = models.CharField(max_length = 25, blank = True, null = True)
    text = models.TextField()

    def __str__(self) -> str:
        return f'{self.title}'
    
    class Meta:
        db_table = 'Topic'
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'
        ordering = ['created']

