import graphene
from Todo import Todo

class Query(graphene.ObjectType):
    getTodos = graphene.List(Todo)

    def resolve_getTodos(self, info):
        return [
            {
                "id": "123",
                "text": "todo 1",
                "completed": True
            },
            {
                "id": "456",
                "text": "todo 2",
                "completed": False
            },
        ]

