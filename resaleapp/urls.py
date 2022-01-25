from django.urls import path
from resaleapp.schema import schema
from django.views.decorators.csrf import csrf_exempt
from graphene_file_upload.django import FileUploadGraphQLView

urlpatterns = [path('graphql/',
               csrf_exempt(FileUploadGraphQLView.as_view(graphiql=True,
               schema=schema)))]