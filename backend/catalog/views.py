from functools import reduce

from django.db.models import Q
from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404

from .serializers import *
from .models import *
from .permissions import *


class CategoryAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.filter(level=0)
        return queryset


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(is_available=True)


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ProductListByCategoryAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        descendants = Category.objects.get(slug=self.kwargs.get('cat_slug')).get_descendants(include_self=True)
        descendants_ids = [item.id for item in descendants]
        products = Product.objects.filter(is_available=True)
        # фильтр по потомкам
        products = products.filter(reduce(lambda x, y: x | y, [Q(pk=item) for item in descendants_ids]))
        return products


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        product_id = self.kwargs.get('product_id')
        product = get_object_or_404(Product, pk=product_id)

        review_author = self.request.user

        serializer.save(product=product, review_author=review_author)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]


class BreadcrumbAPIView(generics.ListAPIView):
    serializer_class = BreadcrumbSerializer

    def get_queryset(self):
        breadcrumb = Category.objects.get(slug=self.kwargs.get('cat_slug')) \
            .get_ancestors(ascending=False, include_self=True)

        return breadcrumb

# class ProductInfoListView(APIView):
#     def get(self, request):
#         data_list = []
#         for item in Product.objects.filter(is_available=True):
#             variants = ProductVariant.objects.filter(product_id=item.article)
#             if sum([variant.quantity for variant in variants]) > 0:
#                 color_list = []
#                 size_list = []
#                 for note in variants:
#                     if note.quantity > 0:
#                         color_list.append(note.color.name)
#                         size_list.append(note.size.name)
#
#                 data = dict(article=item.article,
#                             name=item.name,
#                             description=item.description,
#                             category=item.category.name,
#                             full_url=item.get_full_url(),
#                             image=request.build_absolute_uri(item.image.url),
#                             price=item.price,
#                             color=list(set(color_list)),
#                             size=list(set(size_list)))
#                 data_list.append(data)
#         data_list = {'products': data_list}
#         return JsonResponse(data_list, status=200)
#
#
# class ProductDetailView(APIView):
#     def get(self, request, article_slug):
#         try:
#             item = Product.objects.get(article=article_slug)
#             variants = ProductVariant.objects.filter(product_id=item.article)
#             color_list = []
#             size_list = []
#             variants_list = []
#             for note in variants:
#                 if note.quantity > 0:
#                     color_list.append(note.color.name)
#                     size_list.append(note.size.name)
#                     variants_list.append(
#                         dict(color=note.color.name,
#                              size=note.size.name,
#                              quantity=note.quantity)
#                     )
#
#             data = dict(article=item.article,
#                         name=item.name,
#                         description=item.description,
#                         category=item.category.name,
#                         full_url=item.get_full_url(),
#                         image=item.image.url,
#                         price=item.price,
#                         color=list(set(color_list)),
#                         size=list(set(size_list)),
#                         variants=variants_list)
#             return JsonResponse(data, status=200)
#         except:
#             raise Http404()


# class ProductCategoryListView(APIView):
#     def get(self, request, cat_id):
#         breadcrumb = Category.objects.get(pk=cat_id).get_ancestors(ascending=False, include_self=True)
#         products = Product.objects.none()
#         # дочерние категории
#         for category in Category.objects.get(pk=cat_id).get_children_id_list():
#             products |= (Product.objects.filter(category_id=category).filter(is_available=True))
#         products_list = []
#         for item in products:
#             variants = ProductVariant.objects.filter(product_id=item.article)
#             if sum([variant.quantity for variant in variants]) > 0:
#                 color_list = []
#                 size_list = []
#                 for note in variants:
#                     if note.quantity > 0:
#                         color_list.append(note.color.name)
#                         size_list.append(note.size.name)
#
#                 data = dict(article=item.article,
#                             name=item.name,
#                             description=item.description,
#                             category=item.category.name,
#                             full_url=item.get_full_url(),
#                             image=request.build_absolute_uri(item.image.url),
#                             price=item.price,
#                             color=list(set(color_list)),
#                             size=list(set(size_list)))
#                 products_list.append(data)
#         breadcrumb_list = []
#         for item in breadcrumb:
#             bc = dict(
#                 id=item.id,
#                 name=item.name,
#                 slug=item.slug,
#                 url=item.get_full_url(),
#             )
#             breadcrumb_list.append(bc)
#         context = {
#             'breadcrumb': breadcrumb_list,
#             'products': products_list,
#         }
#         return JsonResponse(context, status=200)
