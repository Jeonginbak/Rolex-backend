import json

from django.views          import View
from django.http           import HttpResponse
from django.http           import JsonResponse

from .models               import Product, Detail, Size, Material, Bezel, Bracelet, Dial, Collection

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