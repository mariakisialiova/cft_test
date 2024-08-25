from django.http import JsonResponse

from credits.models import CreditApplication


def get_unique_manufacturer_ids_view(request, contract_id):
    manufacturer_ids = CreditApplication.objects.filter(
        contract_id=contract_id,
    ).values_list(
        'product__manufacturer_id',
        flat=True,
    ).distinct()

    return JsonResponse(list(manufacturer_ids), safe=False)
