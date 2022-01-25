import graphene

from .fields import(
    UserClass,
    CommentClass,
    BookClass
)
from .models import (
    User,
    Book,
    Comment
)
from .mutations import(
    createUser,
    createBook,
    createComment,
    delete
)



class Query(graphene.ObjectType):
    users = graphene.List(UserClass)
    user = graphene.Field(UserClass, id = graphene.ID())
    books = graphene.List(BookClass)
    book = graphene.Field(BookClass,id = graphene.ID())
    comments = graphene.List(CommentClass)
    comment = graphene.Field(CommentClass, id = graphene.ID())
    

    def resolve_users(root,info):
        return User.objects.all()
    
    def resolve_user(root,info, id):
        return User.objects.get(id = id)

    def resolve_books(root, info):
        return Book.objects.all()
    
    def resolve_book(root, info, id):
        return Book.objects.get(id = id)

    def resolve_comments(root, info):
        return Comment.objects.all()

    def resolve_comment(root, info, id):
        return Comment.objects.get(id = id)







class Mutation(graphene.ObjectType):
    create_user = createUser.Field()
    create_book = createBook.Field()
    create_comment = createComment.Field()
    delete = delete.Field()



schema = graphene.Schema(query = Query, mutation=Mutation)