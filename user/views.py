import json
import bcrypt
import jwt

from django.http    import JsonResponse, HttpResponse
from django.views   import View

from .models        import User
from rolex.settings import SECRET_KEY


class SignUp(View):
    def post(self, request):
        data = json.loads(request.body)
        User(
            name=data['name']
            password=bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode(),
        ).save()
        return HttpResponse(status=200)


class LogIn(View):
    def post(self, request):
        data = json.loads
        try:
            if User.objects.filter(name=data['name']).exists():
                user = User.objects.get(name=data['name'])

                if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                    token = jwt.encode({'id':user.id}, SECRET_KEY, algorithm='HS256')
                    return JsonResponse({'access_token':token.decode('utf-8')}, status=200)
                return HttpResponse(status=401)
        except KeyError:
            return JsonResponse({'users':'INVALID'}, status=401)