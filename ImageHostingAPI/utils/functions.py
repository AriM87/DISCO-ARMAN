from PIL import Image
from ..models import Image
from ..serializers import ImageSerializer

def get_image_link(image_id):
    try:
        image_instance = Image.objects.get(id=image_id)
    except Image.DoesNotExist:
        return None

    serializer = ImageSerializer(image_instance)
    image_link = serializer.data['image']
    return image_link


# TODO: Following to be completed it is a better way to resize the photo to get a thumbnail,
# Follwoing will replace the current method(ImageSpecField+ResizeToFill) that is in model.

# def resize_image(image, new_height):

#     try:
#         # Get the original image dimensions
#         original_width, original_height = image.size

#         # Calculate the new width based on the original aspect ratio
#         new_width = int((original_width / original_height) * new_height)

#         # Resize the image while preserving the aspect ratio
#         resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)

#         # Return the resized image
#         return resized_image

#     except Exception as e:
#         print("Error:", str(e))
#         return None