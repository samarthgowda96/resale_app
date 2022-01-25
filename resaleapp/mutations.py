
import graphene
from graphene_file_upload.scalars import Upload
from .fields import(
    UserClass,
    BookClass,
    CommentClass,
)
from .models import (
    User,
    Book,
    Comment,
    BookUser,
    CommentUser
)

class createUser(graphene.Mutation):
    error = graphene.String()
    success = graphene.Boolean()
    user = graphene.Field(UserClass)

    class Meta:
        description = "Add user details"
        
    class Arguments:
        name =  graphene.String(required=True)
        email =  graphene.String(required=True)
        location = graphene.String()
        phone_no =  graphene.String()

    def mutate(self,info, phone_no= None, location=None, **kwargs):
        try:
            user = User.objects.create(
                name = kwargs.get("name"),
                email = kwargs.get("email"),
                phone_no = phone_no,
                location = location,
                )
            return createUser(user = user, success = True)
        except Exception as e:
            return createUser(user = None, success = False, error = e)

class createBook(graphene.Mutation):
    error = graphene.String()
    success = graphene.Boolean()
    book = graphene.Field(BookClass)

    class Arguments:
        user_id = graphene.ID(required=True)
        book_name = graphene.String(required=True)
        author = graphene.String(required=True)
        book_image = Upload()
        price = graphene.Int()
       
    def mutate(self,info, **kwargs):
        try:
            book = Book.objects.create(
                    book_name = kwargs.get('book_name'),
                    author = kwargs.get('author'),
                    book_image= kwargs.get('book_image'),
                    price = kwargs.get('price')
                    )
            book_user = BookUser.objects.create(
                        book_id = book.id,
                        user_id = kwargs.get('user_id')
            )
            return createBook(book = book, success = True)
        except Exception as e:
            return createBook(book = book, success = False, error = e)


    

class createComment(graphene.Mutation):
    error = graphene.String()
    success = graphene.Boolean()
    comment = graphene.Field(CommentClass)
    
    class Arguments:
        user_id = graphene.ID(required=True)
        book_id = graphene.ID(required=True)
        body = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        try:
            comment = Comment.objects.create(
                book_id = kwargs.get('book_id'),
                body = kwargs.get('body')
            )
            comment_user = CommentUser.objects.create(
                user_id = kwargs.get('user_id'),
                comment_id = comment.id
            )
            
            return createComment(success = True, comment = comment)
        except Exception as e:
            return createComment(success = False, error = e)


class delete(graphene.Mutation):
    error = graphene.String()
    success = graphene.Boolean()
    
    class Arguments:
        user_id = graphene.ID()
        book_id = graphene.ID()
        comment_id = graphene.ID()

    def mutate(self, info, **kwargs):
        try:
            if(kwargs.get('user_id')):
                User.objects.filter(id = kwargs.get('user_id')).delete()
            if(kwargs.get('book_id')):
                Book.objects.filter(id = kwargs.get('book_id')).delete()
            if(kwargs.get('comment_id')):
                Comment.objects.filter(id = kwargs.get('comment_id')).delete()
            return delete(success = True)
        except Exception as e:
            return delete(success= False, error = e)
            
            
            
            




    
    


