from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIViews features"""
        a_simple_list = [
            'Apple',
            'Mango',
            'Cherry'
        ]

        return Response({'message': 'My First get API', 'a_simple_list': a_simple_list})     # The response will convert the return into a JSON object, hence it should either be dictonary or a list
