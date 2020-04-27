import jwt

from django.http        import JsonResponse

from .models            import User
from rolex.settings     import SECRET_KEY # 장고의 SECRET_KEY를 이용


def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        # 헤더에 있는 Authorization 정보를 가져온다.
        token = request.headers.get('Authorization', None)

        # 만약 Authorization 정보가 없으면 에러코드 발생
        if token == None:
            return JsonResponse({"error_code": "INVALID_LOGIN"}, status=401)
        
        # jwt로 토큰 생성
        d_token = jwt.decode(token, SECRET_KEY, algorithms='HS256')
        # 가져온 토큰에서 id 추출
        user = User.objects.get(id=d_token['id'])
        request.user = user
        return func(self, request, *args, **kwargs)
    return wrapper