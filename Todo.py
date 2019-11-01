import graphene
from db import db

class Todo(graphene.ObjectType):
    id = graphene.ID()
    text = graphene.String()
    completed = graphene.Boolean()

class CreateTodo(graphene.Mutation):
    class Arguments:
        text = graphene.String(required=True)

    def mutate(self, info, text):
        return {
            'id': '11111111',
            'text': text,
            'completed': True
        }
        
# class CreateTodoInput(graphene.InputObjectType):
#     text = graphene.String(required=True)
#     completed = graphene.Boolean(required=False)

# class CreateTodo(graphene.Mutation):
#     class Arguments:
#         input = CreateTodoInput(required=True)

#     def mutate(self, info, input):
#         data = db.getTable("todosTable").insertRecord(input)
#         return data

# class DeleteTodo(graphene.Mutation):
#     class Arguments:
#         id = graphene.ID(required=True)

#     def mutate(self, info, id):
#         output = db.getTable("todosTable").deleteRecordById(id)
#         return output