from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from django.http import HttpResponse
from .models import Image
from .serializers import ImageSerializer
from .utils.functions import get_image_link
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser, FormParser)

    # TODO: Following needs to be re-written so the logic handleing of getting image in order
    # to returne the relevant thumbnail along with its link is handeled properly.

    # def create(self, request, *args, **kwargs):
    #     image = request.data["image"]
    #     user = request.data["user"]
    #     Image.objects.create(image=image, user=user)
    #     return Response("Image Uploaded Successfully.", status=status.HTTP_200_OK)


@api_view(['GET'])
def download_image(request, image_id):
    try:
        image_link = get_image_link(image_id)
        return HttpResponse(content_type=f"{image_link}")
    except Exception as e:
        return Response({'error': f"{e}"}, status=404)


class ImageUploadView(APIView):

    parser_classes = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

        image_serializer = ImageSerializer(data=request.data)

        if image_serializer.is_valid():
            image_serializer.save()
            return Response(image_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)