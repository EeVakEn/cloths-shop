from rest_framework import permissions


# проверка на то что именно наш пользоваель оставил отзыв
class IsReviewAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method is permissions.SAFE_METHODS:
            return True

        return obj.review_author == request.user
