from multipledispatch import dispatch


class Habitant:
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age

    @dispatch(object, str)
    def set_info(self, nom):
        self.nom = nom

    @dispatch(object, str, int)
    def set_info(self, nom, age):
        self.nom = nom
        self.age = age