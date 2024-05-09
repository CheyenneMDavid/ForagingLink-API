from django.urls import path
from .views import PlantInFocusPostList

urlpatterns = [
    path(
        "plant_in_focus_posts/",
        PlantInFocusPostList.as_view(),
        name="plant_in_focus_posts",
    ),
]
