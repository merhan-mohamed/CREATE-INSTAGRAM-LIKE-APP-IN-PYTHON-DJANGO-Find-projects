from __future__ import absolute_import, unicode_literals

import base64
import os
from io import BytesIO
import PIL
import boto3
from PIL import Image
from celery import shared_task
from rest_framework import status
from rest_framework.response import Response

from Insta.models import Asset
from instacat.settings import S3_BASE_URL, S3_BUCKET


@shared_task
def resize_and_upload(image_string,salt,kind,asset_id):
    img = Image.open(BytesIO(base64.b64decode(image_string)))
    aspect = (img.width / img.height)
    width = 0
    height = 0
    resized_img = None
    if kind == 'original':
        print('ORIGINAL')
        width = img.width
        height = img.height
        resized_img = img.resize(width, height), PIL.Image.ANTIALIAS
    if kind == 'large':
        print('LARGE')
        width = 1024
        height = aspect * 1024
        resized_img = img.resize(width, height), PIL.Image.ANTIALIAS
    if kind == 'small':
        print('SMALL')
        width = 128
        height = aspect * 128
        resized_img = img.resize(width, height), PIL.Image.ANTIALIAS
    else:
        print('error-size not handled')
        #Response({'error': 'size not handled'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    filename = '%s _%s.jpg' % (salt, kind)
    temp_location = '%s%s' % (S3_BASE_URL, filename)
    img.save(temp_location)

    s3_client = boto3.client('s3')
    s3_client.upload_file(temp_location, S3_BUCKET, 'image/%s' % filename)

    s3_resource = boto3.resource('s3')
    object_acl = s3_resource.Object_acl(S3_BUCKET, 'image/%s' % filename)
    response = object_acl.put(ACL='public-read')

    asset = Asset.objects.get(pk=asset_id)
    asset.width = width
    asset.height = height
    asset.processing = False
    asset.save()
    os.remove(temp_location)

    return

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


