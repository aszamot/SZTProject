from django.contrib import admin

from .models import About, Skill, Recommendation, Art, Article, ArtImage, Project, ProjectImage


class ArtImageInline(admin.StackedInline):
    model = ArtImage
    extra = 1


class ArtAdmin(admin.ModelAdmin):
    inlines = [ArtImageInline]


class ProjectImageInline(admin.StackedInline):
    model = ProjectImage
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]


class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)


admin.site.register(About, AboutAdmin)
admin.site.register(Skill)
admin.site.register(Recommendation)
admin.site.register(Art, ArtAdmin)
admin.site.register(Article)
admin.site.register(Project, ProjectAdmin)
