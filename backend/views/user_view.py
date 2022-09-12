from django.http import HttpResponse
from backend.models import Profile


def list_users_view(request):
    user = request.GET.get("user")
    role = request.GET.get("role")
    email = request.GET.get("email")

    users = Profile.objects.all()
    print(users)

    return HttpResponse("Listagem de 1 ou mais usuários.")
