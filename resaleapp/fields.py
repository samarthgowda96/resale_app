import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import User, Book, Comment, BookUser, CommentUser

class BookClass(DjangoObjectType):
    class Meta:
        model = Book

class UserClass(DjangoObjectType):
    book = graphene.List(BookClass)
    class Meta:
        model = User
    def resolve_book(self, info, root):
        book_user = \
                  BookUser.objects.filter(user_id=self.id).values_list('book_id'
                )
        books = Book.object.filter(id__in=book_user)
        return books
        
class BookUserClass(DjangoObjectType):
    class Meta:
         model = BookUser
class CommentClass(DjangoObjectType):
    class Meta:
        model = Comment
class CommentUserClass(DjangoObjectType):
    class Meta:
        model = CommentUser