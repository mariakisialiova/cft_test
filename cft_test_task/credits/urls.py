from django.urls import path
from . import views

urlpatterns = [
    path(
        "contracts/<int:contract_id>/",
        views.get_unique_manufacturer_ids_view,
        name="get_unique_manufacturer_ids",
    ),
]
