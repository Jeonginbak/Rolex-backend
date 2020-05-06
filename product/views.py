import json
from django.http import JsonResponse, HttpResponse 
from django.views import View
                
from .models import Category, Collection, Product, MiddleImage, Feature, Detail
from .models import Size, Material, Bezel, Bracelet, Dial
from .models import BezelFind, BraceletFind, DialFind

class DetailView(View):

    def product(self, data, product_id):
        product  = Product.objects.get(id=product_id)
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
        data["description"] = {
            "first_paragraph"  : product.description,
            "second_paragraph" : product.sub_description
        }
        data["main_features"] = {
            "thumbnail_image"   : product.middle_image.thumbnail_url,
            "click_image"       : product.middle_image.image_url,
            "title"             : product.middle_image.title,
            "sub_title"         : product.middle_image.sub_title,
            "description"       : product.middle_image.description
        }
        return data 

    def sub_features(self, data, feature_list, prd_id):
        sub_features = Feature.objects.filter(product_id=prd_id)
        title_list  = [f.title for f in sub_features]
        sub_list    = [f.sub_title for f in sub_features]
        small_img   = [f.thumbnail_url for f in sub_features]
        large_img   = [f.image_url for f in sub_features]
        description = [f.description for f in sub_features]
        
        for item in zip(title_list, sub_list, small_img, large_img, description):
            data = {
                'title' : item[0], 'sub_title' : item[1],
                'small_image' : item[2], 'large_image' : item[3], 'description' : item[4]
            }
            feature_list.append(data)
        return feature_list

    def get(self, request, product_id):
        try:	
            if Product.objects.filter(id=product_id).exists():
                data = {}
                feature_list = []
                self.product(data, product_id)
                self.sub_features(data,feature_list, product_id)
                return JsonResponse( {'product':data, 'sub_features':feature_list}, status=200 )
            return JsonResponse({'message': 'PRODUCT_DOES_NOT_EXIST'}, status = 404)

        except KeyError:
            return HttpResponse(status=404)


def basic_info(data, watch_id):
    product                  = Product.objects.get(id=watch_id)
    detail                   = Detail.objects.get(id=watch_id)
    data['collection']       = product.collection.name
    data['is_oyster']        = detail.is_oyster
    data['diameter']         = detail.size.diameter
    data['price']            = detail.price
    data['watch_image']      = product.header_watch
    data['background_image'] = product.header_background
    data['product_id']       = detail.id

def remove_str_diamond(get_material):
    get_material = [ get_material.remove(m) for m in get_material if '다이아몬드' in m.material.name]

class ConfigSizeView(View):
    def get(self, request):
        sizes = [ Product.objects.get(id=1), Product.objects.get(id=105) ] # default product
        option_list = []
        for size in sizes:
            data = {}
            basic_info(data, size.id)
            option_list.append(data)
        return JsonResponse({'model_data': option_list}, status = 200)
            

class ConfigMaterialView(View):
    def get(self, request):
        size_opt = request.GET.get('size', None)
        try:
            get_material = list(BezelFind.objects.filter(size__diameter=size_opt).order_by('material_id'))
            remove_str_diamond(get_material)
            remove_str_diamond(get_material)

            option_list = []
            for g in get_material:
                watch_id = Detail.objects.filter(size__diameter=size_opt, material_id=g.material.id).first().id
                data  = {'name' : g.material.name, 'material_url' : g.material.image_url}
                basic_info(data, watch_id)
                option_list.append(data)
            return JsonResponse({'material_data' : option_list}, status = 200)

        except KeyError:
            return HttpResponse(status=404)


class ConfigBezelView(View):
    def get(self, request):
        size_opt = request.GET.get('size', None)
        material_opt = request.GET.get('material', None)
        try:
            if material_opt == '플래티넘':
                plus_diamond = material_opt + '과 다이아몬드'
            else:
                plus_diamond = material_opt +'와 다이아몬드'

            get_bezel = BezelFind.objects.filter(size__diameter=size_opt, material__name=material_opt) | BezelFind.objects.filter(size__diameter=size_opt, material__name=plus_diamond)

            option_list = []
            for b in get_bezel:
                data      = {}
                data      = {'name' : Bezel.objects.get(id=b.bezel_id).name, 'bezel_url' : b.image_url}
                watch_id  = Detail.objects.filter(size__diameter=size_opt, material_id=b.material.id, bezel_id=b.bezel.id).first().id
                basic_info(data, watch_id)
                option_list.append(data)
            return JsonResponse({'bezel_data':option_list}, status = 200)

        except KeyError:
            return HttpResponse(status=404)


class ConfigBraceletView(View):
    def get(self, request):
        size_opt = request.GET.get('size', None)
        material_opt = request.GET.get('material', None)
        bezel_opt = request.GET.get('bezel', None)
        try:
            plus_diamond = material_opt + '와 다이아몬드'
            get_bracelet = BraceletFind.objects.filter(size__diameter=size_opt, material__name=material_opt, bezel__name=bezel_opt) | BraceletFind.objects.filter(size__diameter=size_opt, material__name=plus_diamond, bezel__name=bezel_opt) 

            option_list = []
            for b in get_bracelet:
                data = {}
                data = {'name' : Bracelet.objects.get(id=b.bracelet.id).name, 'bracelet_url' : b.image_url}
                watch_id = Detail.objects.filter(size__diameter=size_opt, material_id=b.material.id, bezel__name=bezel_opt, bracelet_id=b.bracelet.id).first().id
                basic_info(data, watch_id)
                option_list.append(data)
            return JsonResponse({'bracelet_data' : option_list}, status = 200)

        except KeyError:
            return HttpResponse(status=404)


class ConfigDialView(View):
    def get(self, request):
        size_opt = request.GET.get('size', None)
        material_opt = request.GET.get('material', None) 
        try:
            get_dial = DialFind.objects.filter(size__diameter=size_opt, material__name=material_opt)
            option_list = []
            for d in get_dial:
                data = {}
                watch_id = Detail.objects.filter(size__diameter=size_opt, material__name=material_opt, dial__name=d.dial.name).first().id
                watch_dial_id = Detail.objects.get(id=watch_id).dial_id
                data = {'name' : Dial.objects.get(id=watch_dial_id).name, 'dial_url' : d.image_url}
                basic_info(data, watch_id)
                option_list.append(data)
            return JsonResponse({'dial_data' : option_list}, status =200)

        except KeyError:
            return HttpResponse(status=404)


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