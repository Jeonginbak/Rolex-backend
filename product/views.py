from django.http import JsonResponse, HttpResponse
from django.views import View
                
from .models import Category, Collection, Product, MiddleImage, Feature, Detail
from .models import Size, Material, Bezel, Bracelet, Dial

class DetailView(View):

    def get_metadata(self, data, product):
        data["metadata"] = {
            "category"      : product.category.name,
            "collection"    : product.collection.name,
            "is_oyster"     : product.detail.is_oyster,
            "size"          : product.detail.size.diameter,
            "material"      : product.detail.material.name,
            "watch_image"   : product.header_watch,
            "bg_image"      : product.header_background,
            "price"         : product.detail.price 
        } 
        return data

    def get_main_features(self, data, product):
        data["main_features"] = {
            "thumbnail_image"   : product.middle_image.thumbnail_url,
            "click_image"       : product.middle_image.image_url,
            "title"             : product.middle_image.title,
            "sub_title"         : product.middle_image.sub_title,
            "description" : product.middle_image.description
        }
        return data

    def get_sub_features(self, data, features, p_id):
        title_list = []
        sub_list = []
        small_img = []
        large_img = []
        feature_len = len(features)

        for num in range(feature_len):
            f = Feature.objects.filter(product_id=p_id)[num]
            title_list.append(f.title)
            sub_list.append(f.sub_title)
            small_img.append(f.thumbnail_url)
            large_img.append(f.image_url)

        data["sub_features"] = {
                'title': title_list[:feature_len],
                'sub_title': sub_list[:feature_len],
                'thumbnail' : small_img[:feature_len],
                'click_image' : large_img[:feature_len]
        }

    def get(self, request, product_id):
        try:		
            if Product.objects.filter(id=product_id).exists():
                product = Product.objects.get(id=product_id)
                features = Feature.objects.filter(product_id=product_id)
                data = dict()

                self.get_metadata(data, product)

                data["description"] = {
                        "first_paragraph" : product.description,
                        "second_paragraph" : product.sub_description
                }

                self.get_main_features(data, product)
                self.get_sub_features(data, features, product_id)
                print(data)
                return JsonResponse( {'product':data}, status=200 )

            return JsonResponse({'message': 'PRODUCT_DOES_NOT_EXIST'}, status = 404)
        except KeyError:
            return HttpResponse(status=404)
        except TypeError:
            return HttpResponse(status=500)

