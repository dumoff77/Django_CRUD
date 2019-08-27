
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from phone_handbook.models import HandBook
from phone_handbook.serializers import HandBookSerializers


@api_view(['GET', 'POST'])
def handbook_list(request):
    """
    List all phone handbook records, or create a new records.
    """
    if request.method == 'GET':
        queryset = HandBook.objects.all()
        serializer = HandBookSerializers(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HandBookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def handbook_by_name(request, name):
    try:
        queryset = HandBook.objects.get(full_name=name)
    except HandBook.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HandBookSerializers(queryset)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HandBookSerializers(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#class HandBookView(APIView):
#
#    def get(self, request):
#        queryset = HandBook.objects.all()
#        serializer = HandBookSerializers(queryset, many=True)
#        return Response(serializer.data)