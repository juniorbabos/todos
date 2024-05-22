from django.db import models
from datetime import date


class Todo(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=100, null=False, blank=False)
    created_at = models.DateField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(verbose_name= "Data de entrega", null=False, blank=False)
    finished_at = models.DateField(null=True)
    #tarefa = models.CharField(verbose_name="Tarefa", max_length=100, null=False, blank=False)

    class Meta:
        #ordenar - para ser contrario
        ordering = ["deadline"]

    def mark_has_complete(self):
        if not self.finished_at:
            self.finished_at = date.today()
            self.save()