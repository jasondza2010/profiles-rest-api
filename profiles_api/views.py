from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIViews features"""
        a_simple_list = [
            'Apple',
            'Mango',
            'Cherry'
        ]

        return Response({'message': 'My First get API', 'a_simple_list': a_simple_list})     # The response will convert the return into a JSON object, hence it should either be dictonary or a list

    def post(self, request):
        """Create a Hello message with out name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = (f'Hello {name}')
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object//Replacing the object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """A Partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})

