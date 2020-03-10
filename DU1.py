from pyrsistent import s


class Relation:
    def __init__(self, set, relation):
        self.set = set
        self.relation = relation

    def contains(self, tuple):
        return self.relation.__contains__(tuple)

    def add(self, tuple):
        if (tuple[0] in self.set) & (tuple[1] in self.set):
            return Relation(self.set, self.relation.add(tuple))
        else:
            return self

    def remove(self, tuple):
        if tuple in self.relation:
            return Relation(self.set, self.relation.remove(tuple))
        else:
            return self
        
    def union(self):
       pass

    def intersection(self):
        pass

    def subtraction(self):
        pass

    def inverse(self):
        pass

    def composition(self):
        pass

    def isReflexive(self):
        pass

    def isSymmetric(self):
        pass

    def isTransitive(self):
        pass

    def reflexiveTransitiveClosure(self):
        pass


def get_relation_class(set):
    pass


if __name__ == "__main__":


