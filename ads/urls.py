from django.urls import path
from ads import views
from ads.models import Category, Ad


urlpatterns = [
    path('', views.index_ads),

    # списковые
    path('cat/', views.Cats_List_View.as_view()),
    path('ad/', views.Ads_List_View.as_view()),
    path('selection/', views.Selection_List_View.as_view()),
    # детальные
    path('cat/<int:pk>/', views.Cats_Detail_View.as_view()),
    path('ad/<int:pk>/', views.Ads_Detail_View.as_view()),
    path('selection/<int:pk>/', views.Selection_Retrieve_View.as_view()),
    # создание
    path('cat/create/', views.Cats_Create_View.as_view()),
    path('ad/create/', views.Ads_Create_View.as_view()),
    path('selection/create/', views.Selection_Create_View.as_view()),
    # изменение
    path('cat/<int:pk>/update/', views.Cats_Update_View.as_view()),
    path('ad/<int:pk>/update/', views.Ads_Update_View.as_view()),
    path('selection/<int:pk>/update/', views.Selection_Update_View.as_view()),
    # удаление
    path('cat/<int:pk>/delete/', views.Cats_Delete_View.as_view()),
    path('ad/<int:pk>/delete/', views.Ads_Delete_View.as_view()),
    path('selection/<int:pk>/delete/', views.Selection_Delete_View.as_view()),
    # работа с картинками
    path('ad/<int:pk>/image/', views.Ads_Image_View.as_view()),

]
