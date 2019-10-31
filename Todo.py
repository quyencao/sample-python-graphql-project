import graphene
from db import db

class Todo(graphene.ObjectType):
    id = graphene.ID()
    text = graphene.String()
    completed = graphene.Boolean()

class CreateTodo(graphene.Mutation):
    class Arguments:
        text = graphene.String(required=True)

    Output = Todo

    def mutate(self, info, todo):
        return Todo(text=todo.text, completed=False, id="123")

class DeleteTodo(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    
    output = graphene.Boolean()

    def mutate(self, info, id):
        output = db.getTable("todosTable").deleteRecordById(id)
        return DeleteTodo(output=output)