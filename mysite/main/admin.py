from django.contrib import admin
from .models import Curso
from tinymce.widgets import TinyMCE # django-tinymce4-lite
from django.db import models
# Register your models here.


class CursoAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Titulo/Fecha", {"fields": ["curso_titulo", "curso_publicado"]}),
        ("Contenido", {"fields": ["curso_contenido"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


admin.site.register(Curso, CursoAdmin)