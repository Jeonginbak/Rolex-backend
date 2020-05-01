import json
from django.http import JsonResponse, HttpResponse 
from django.views import View
from django.db.models import Q 
                
from .models import Category, Collection, Product, MiddleImage, Feature, Detail
from .models import Size, Material, Bezel, Bracelet, Dial
from .models import BezelFind, BraceletFind, DialFind

class DetailView(View):

    def metadata(self, data, product):
        data["metadata"] = {
            "category"      : product.category.name,
            "collection"    : product.collection.name,
            "is_oyster"     : product.detail.is_oyster,
            "size"          : product.detail.size.diameter,
            "material"      : product.detail.material.name,
            "watch_image"   : product.header_watch,
            "bg_image"      : product.header_background,
            "price"         : product.detail.price,
            "product_id"    : product.id
        } 
        return data

    def main_features(self, data, product):
        data["main_features"] = {
            "thumbnail_image"   : product.middle_image.thumbnail_url,
            "click_image"       : product.middle_image.image_url,
            "title"             : product.middle_image.title,
            "sub_title"         : product.middle_image.sub_title,
            "description"       : product.middle_image.description
        }
        return data

    def sub_features(self, data, features, p_id):   
        title_list  = []
        sub_list    = []
        small_img   = []
        large_img   = []
        for num in range(0,len(features)):
            f = Feature.objects.filter(product_id=p_id)[num]
            title_list.append(f.title)
            sub_list.append(f.sub_title)
            small_img.append(f.thumbnail_url)
            large_img.append(f.image_url)

        data["sub_features"] = {
                'title'       : title_list[:len(features)],
                'sub_title'   : sub_list[:len(features)],
                'thumbnail'   : small_img[:len(features)],
                'click_image' : large_img[:len(features)]
        }
        return data

    def get(self, request, product_id):
        try:		
            if Product.objects.filter(id=product_id).exists():
                product  = Product.objects.get(id=product_id)
                features = Feature.objects.filter(product_id=product_id)
                data = dict()

                self.metadata(data, product)
                data["description"] = {
                    "first_paragraph"  : product.description,
                    "second_paragraph" : product.sub_description
                }
                self.main_features(data, product)
                self.sub_features(data, features, product)

                return JsonResponse( {'product':data}, status=200 )
            return JsonResponse({'message': 'PRODUCT_DOES_NOT_EXIST'}, status = 404)
        except KeyError:
            return HttpResponse(status=404)
        except TypeError:
            return HttpResponse(status=500)


class ConfigView(View):
    def basic_info(self, data, product, watch_id):
        data['collection']  = product.collection.name
        data['is_oyster']   = Detail.objects.get(id=watch_id).is_oyster
        data['diameter']    = Detail.objects.get(id=watch_id).size.diameter
        data['price']       = Detail.objects.get(id=watch_id).price
        data['watch_image'] = product.header_watch
        data['product_id']  = Detail.objects.get(id=watch_id).id

    def get(self, request, option=None):
        size_opt     = request.GET.get('size', None)
        material_opt = request.GET.get('material', None)
        bezel_opt    = request.GET.get('bezel', None)
        bracelet_opt = request.GET.get('bracelet', None)

        try:
            if option == 'model':
                sizes = [ Product.objects.get(id=1), Product.objects.get(id=105) ]
                
                option_list = []
                for s in sizes:
                    data = {}
                    product            = s
                    watch_id           = s.id
                    data['background'] = s.header_background
                    self.basic_info(data, product, watch_id)
                    option_list.append(data)

                return JsonResponse({'model_data': option_list}, status = 200)

            if option == 'material':
                get_material = list(BezelFind.objects.filter(size__diameter=size_opt))
                for m in get_material:
                    if '다이아몬드' in m.material.name:
                        get_material.remove(m)
                for m in get_material:
                    if '다이아몬드' in m.material.name:
                        get_material.remove(m)

                option_list = []
                for g in get_material:
                    data = {}
                    data['material_url']  = g.material.image_url
                    data['material_name'] = g.material.name
                    watch_id              = Detail.objects.filter(size__diameter=size_opt, material_id=g.material.id).first().id
                    product               = Product.objects.get(id=watch_id)
                    self.basic_info(data, product, watch_id)
                    option_list.append(data)
                return JsonResponse({'material_data' : option_list}, status = 200)

            if option == 'bezel':
                if material_opt == '플래티넘':
                    plus_diamond = material_opt + '과 다이아몬드'
                    bezel_id = [3,2]
                else:
                    plus_diamond = material_opt +'와 다이아몬드'
                    bezel_id = [1,2]

                basic   = Detail.objects.filter(size__diameter=size_opt, material__name=material_opt)
                diamond = Detail.objects.filter(size__diameter=size_opt, material__name=plus_diamond)

                option_list = []
                data = {}
                watch_id = basic.first().id
                product = Product.objects.get(id=watch_id)
                self.basic_info(data, product, watch_id)

                data['bezel_url'] = BezelFind.objects.filter(size__diameter=size_opt, material__name=material_opt, bezel_id=bezel_id[0])[0].image_url
                option_list.append(data)

                data = {}
                watch_id = diamond.first().id
                product = Product.objects.get(id=watch_id)
                self.basic_info(data, product, watch_id)

                data['bezel_url'] = BezelFind.objects.filter(size__diameter=size_opt, material__name=plus_diamond, bezel_id=bezel_id[1])[0].image_url
                option_list.append(data)

                return JsonResponse({'bezel_data':option_list}, status = 200)
            
            if option == 'bracelet':
                get_bracelet = BraceletFind.objects.filter(size__diameter=size_opt, material__name=material_opt, bezel__name=bezel_opt)

                option_list = []
                for b in get_bracelet:
                    data = {}
                    data['bracelet_url'] = b.image_url
                    watch_id = Detail.objects.filter(size__diameter=size_opt, material__name=material_opt, bracelet_id=b.bracelet.id).first().id
                    product = Product.objects.get(id=watch_id)
                    self.basic_info(data, product, watch_id)
                    option_list.append(data)
                return JsonResponse({'bracelet_data' : option_list}, status = 200)

            if option == 'dial':
                get_dial = DialFind.objects.filter(size__diameter=size_opt, material__name=material_opt)

                option_list = []
                for d in get_dial:
                    data = {}
                    data['dial_url'] = d.image_url
                    watch_id = Detail.objects.filter(size__diameter=size_opt, material__name=material_opt, dial__name=d.dial.name).first().id
                    product = Product.objects.get(id=watch_id)
                    self.basic_info(data, product, watch_id)
                    option_list.append(data)
                return JsonResponse({'dial_data' : option_list}, status =200)

        except KeyError:
            return HttpResponse(status=404)
        except TypeError:
            return HttpResponse(status=500)

class ListView(View):
    def get(self, request):
        size_filter     = request.GET.getlist('diameter', None)
        material_filter = request.GET.getlist('material', None)
        bezel_filter    = request.GET.getlist('bezel', None)
        bracelet_filter = request.GET.getlist('bracelet', None)
        dial_filter     = request.GET.getlist('dial', None)
        page            = request.GET.get('page', None)
        limit           = request.GET.get('limit', None)
    
        page = int(page)
        limit = int(limit)
        end_page = page * limit

        watch_filter = {
            'detail__size__diameter__in' : size_filter,
            'detail__material__name__in' : material_filter,
            'detail__bezel__name__in'    : bezel_filter,
            'detail__bracelet__name__in' : bracelet_filter,
            'detail__dial__name__in'     : dial_filter
        }

        if size_filter == []:
            del(watch_filter['detail__size__diameter__in'])

        if material_filter == []:
            del(watch_filter['detail__material__name__in'])

        if bezel_filter == []:
            del(watch_filter['detail__bezel__name__in'])

        if bracelet_filter == []:
            del(watch_filter['detail__bracelet__name__in'])

        if dial_filter == []:
            del(watch_filter['detail__dial__name__in'])

        if Product.objects.filter(**watch_filter):
           products = Product.objects.filter(**watch_filter)
    
           data_attribute = [
                {
                'id'           : product.id,
                'collection'   : product.collection.name,
                'oyster'       : product.detail.is_oyster,
                'diameter'     : product.detail.size.diameter,
                'material'     : product.detail.material.name,
                'image'        : product.header_watch
                } for product in products[end_page-limit:end_page] 
           ]
           return JsonResponse({'products': data_attribute}, status = 200)

        return JsonResponse({'message':'NO_PRODUCT'}, status = 400)


