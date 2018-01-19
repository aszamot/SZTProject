from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('portfolio/art/<int:art_id>', views.art, name='art'),
    path('portfolio/project/<int:project_id>', views.project, name="project"),
    path('thanks', views.thanks, name="thanks"),
]
