from django.urls import path
from .views import RecipesList, RecipesDetail, RecipesUpload, RecipesAdd

urlpatterns = [
    path('recipes/list', RecipesList.as_view(), name='recipes-list'),
    path('recipe/<int:pk>', RecipesDetail.as_view(), name='recipe'),
    path('recipe/add', RecipesAdd.as_view(), name='recipe-add'),
    path('recipe/pk/add_image',
        RecipesUpload.as_view(), name='recipe-upload-image')
]

app_name = 'ledger'

