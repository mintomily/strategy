from django.urls import path
from . import views

app_name = 'strapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path ('bulletin/', views.BulletinView.as_view(), name='bulletin'),

    path ('bulletinform/', views.BulletinFormView.as_view(), name='bulletin_form'),

    path('character-detail/<int:pk>',
         views.DetailView.as_view(),
         name = 'character_detail'),

    path('character/<str:category>',
         views.CategoryView.as_view(),
         name = 'character_cat'),

    path('characterform/', views.CharacterFormView.as_view(), name='character_form'),

    path('character_done/',
         views.CharacterSuccessView.as_view(),
         name='character_done'),

    path('contact/', views.ContactView.as_view(), name='contact'),

    path('character/<int:pk>/delete/',
         views.CharacterDeleteView.as_view(),
         name = 'character_delete'),
]