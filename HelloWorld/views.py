from django.http import HttpResponse

# Create your views here.

def index(request):
    print("req: " ,request)

    return HttpResponse("hey you")


def bye(request):
    return HttpResponse("mesghere",status = 204)