from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class DictDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, reqest):
        return Response({'key': 'HIIIIIIII'})
