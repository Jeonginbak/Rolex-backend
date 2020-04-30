import json
import bcrypt
import jwt

from django.http    import JsonResponse, HttpResponse
from django.views   import View


from rolex.settings import SECRET_KEY
from .models        import User, Like
from .utils         import login_decorator
from product.models import (
								Product, 
								Detail, 
								MiddleImage, 
								Feature
							)

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
		res = []
		for data in like_list:
			product = Product.objects.get(id=data.product_id)
			detail = Detail.objects.get(id=data.product_id)
			middle = MiddleImage.objects.get(id=data.product_id)
			feature = Feature.objects.get(id=data.product_id)
			data_attribute = {
				'collection':product.collection.name,
				'thumbnail_image':product.header_watch,
				'oyster':detail.is_oyster,
				'size':detail.size.diameter,
				'material':detail.material.name,
			}
			res.append(data_attribute)
		return JsonResponse({'product_preview':res}, status=200)
