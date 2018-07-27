from rest_framework.views import APIView
from rest_framework.response import Response

class ToDoViews(APIView):
    """docstring for ToDoView."""
    def get(self, request):
        return Response({'test':'it worked'})
