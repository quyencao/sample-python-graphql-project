import graphene
from Todo import CreateTodo, DeleteTodo

class Mutation(graphene.ObjectType):
    create_todo = CreateTodo.Field()
    delete_todo = DeleteTodo.Field()