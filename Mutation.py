import graphene
from Todo import CreateTodo

class Mutation(graphene.ObjectType):
    create_todo = CreateTodo.Field()