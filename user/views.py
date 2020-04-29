import json
import bcrypt
import jwt

from django.http    import JsonResponse, HttpResponse
from django.views   import View

from .models        import User, Like
from .utils         import login_decorator
from product.models import Product, Detail
from rolex.settings import SECRET_KEY


class SignUp(View):
	def post(self, request):
		data = json.loads(request.body)

		try:
			if User.objects.filter(name=data['name']).exists():
				return JsonResponse({'message':'invalid'}, status=401)
			
			User(
				name=data['name'],
				password=bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
			).save()

			return HttpResponse(status=200)

		except KeyError:
			return JsonResponse({'message':'KeyError'}, status=401)


class LogIn(View):
	def post(self, request):
		data = json.loads(request.body)
		try:
			if User.objects.filter(name=data['name']).exists():
				user = User.objects.get(name=data['name'])

				if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
					token = jwt.encode({'id':user.id}, SECRET_KEY, algorithm='HS256')
					return JsonResponse({'access_token': token.decode('utf-8')}, status=200)
				return HttpResponse(status=401)
		except KeyError:
			return JsonResponse({'message':'invalid'}, status=401)


class LikeView(View):
	@login_decorator
	def post(self, request, *args, **kwargs):
		
		data = json.loads(request.body)
		if 'product_id' in data:
			product_id = data['product_id']
			product = Product.objects.filter(id=product_id)
			user = request.user
			
			if Like.objects.filter(user=user.id, product=product_id).exists():
				Like.objects.get(user_id=user.id,product_id=product_id).delete()
			else:		
				Like.objects.create(product_id=product_id, user_id=user.id)
		return HttpResponse(status=200)


class MyLikeListPreview(View):
	@login_decorator
	def get(self, request):
		user = request.user
		like_list = Like.objects.filter(user=user.id)
		data_list = list(like_list)

		for data in data_list:
			collection = Product.objects.get(id=data.product_id).collection.name
			image = Product.objects.get(id=data.product_id).header_watch
			oyster = Detail.objects.get(id=data.product_id).is_oyster
			size = Detail.objects.get(id=data.product_id).size.diameter
			material = Detail.objects.get(id=data.product_id).material.name
		
		result = {
			'collection':collection,
			'image':image,
			'oyster':oyster,
			'size':size,
			'material':material
		}	
		
		return JsonResponse({'product_preview':result}, status=200)
