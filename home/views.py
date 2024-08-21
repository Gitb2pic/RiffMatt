from django.http import HttpResponse

# Create your views here.

def credit(request):
    content = 'Nicky.\nAlex Dev.'
    return HttpResponse(content, content_type="text/plain")
