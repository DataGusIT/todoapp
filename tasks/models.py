from django.db import models
from django.urls import reverse

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Baixa'),
        ('medium', 'Média'),
        ('high', 'Alta'),
    ]
    
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(blank=True, verbose_name='Descrição')
    priority = models.CharField(
        max_length=10, 
        choices=PRIORITY_CHOICES, 
        default='medium',
        verbose_name='Prioridade'
    )
    completed = models.BooleanField(default=False, verbose_name='Concluída')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criada em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizada em')
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('task_detail', kwargs={'pk': self.pk})