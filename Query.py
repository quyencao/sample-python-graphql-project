import graphene
from Todo import Todo
from db import db

class Query(graphene.ObjectType):
    getTodos = graphene.List(Todo)

    def resolve_getTodos(self, info):
        todos = db.getTable("todosTable").getRecords({})
        return todos

