import graphene
from Todo import Todo
from db import db

class Query(graphene.ObjectType):
    getTodos = graphene.List(Todo)
    # getTodo = graphene.Field(Todo, id=graphene.ID())

    def resolve_getTodos(self, info):
        todos = db.getTable("todosTable").getRecords({})
        return todos

    # def resolve_getTodo(self, info, id):
    #     todo = db.getTable("todosTable").getRecordById(id)
    #     return todo