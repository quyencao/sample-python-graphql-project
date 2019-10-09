import graphene

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