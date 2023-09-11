from django.contrib import admin
from django.forms import BaseInlineFormSet

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_count = sum(form.cleaned_data['is_main'] for form in self.forms if form.cleaned_data)
        if main_count == 0:
            raise ValidationError('Должен быть один основной тег.')
        elif main_count > 1:
            raise ValidationError('Может быть только один основной тег.')
        super().clean()

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]

admin.site.register(Tag)