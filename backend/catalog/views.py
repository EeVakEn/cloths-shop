from django.http import JsonResponse, Http404
from rest_framework import generics, viewsets
from .serializers import CategorySerializer
from .models import Product, ProductVariant, Category
from rest_framework.views import APIView


class CategoryView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.filter(level=0)
        return queryset


class ProductInfoListView(APIView):
    def get(self, request):
        data_list = []
        for item in Product.objects.filter(is_available=True):
            variants = ProductVariant.objects.filter(product_id=item.article)
            if sum([variant.quantity for variant in variants]) > 0:
                color_list = []
                size_list = []
                for note in variants:
                    if note.quantity > 0:
                        color_list.append(note.color.name)
                        size_list.append(note.size.name)

                data = dict(article=item.article,
                            name=item.name,
                            description=item.description,
                            category=item.category.slug,
                            image=request.build_absolute_uri(item.image.url),
                            price=item.price,
                            color=list(set(color_list)),
                            size=list(set(size_list)))
                data_list.append(data)
        data_list = {'products': data_list}
        return JsonResponse(data_list, status=200)


class ProductDetailView(APIView):
    def get(self, request, article_slug):
        try:
            item = Product.objects.get(article=article_slug)
            variants = ProductVariant.objects.filter(product_id=item.article)
            color_list = []
            size_list = []
            variants_list = []
            for note in variants:
                if note.quantity > 0:
                    color_list.append(note.color.name)
                    size_list.append(note.size.name)
                    variants_list.append(
                        dict(color=note.color.name,
                             size=note.size.name,
                             quantity=note.quantity)
                    )

            data = dict(article=item.article,
                        name=item.name,
                        description=item.description,
                        category=item.category.slug,
                        image=item.image.url,
                        price=item.price,
                        color=list(set(color_list)),
                        size=list(set(size_list)),
                        variants=variants_list)
            return JsonResponse(data, status=200)
        except:
            raise Http404()
