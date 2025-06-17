from .models import ContactDetail

def contact_detail(request):
    detail = ContactDetail.objects.first()
    return {'contact_detail': detail}
