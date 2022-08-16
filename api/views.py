from rest_framework.response import Response
from rest_framework.decorators import api_view
from transaction.models import Transaction
from .serializers import ItemSerializers


@api_view(["GET"])
def get_data(request):
    items = Transaction.objects.all()
    serializer = ItemSerializers(items, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def add_item(request):
    serializer = ItemSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
