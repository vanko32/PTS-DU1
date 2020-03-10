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
        
    def union(self, relation):
        for i in relation:
            if (i[0] not in self.set) | (i[1] not in self.set):
                return self
        return Relation(self.set, self.relation.union(relation))

    def intersection(self, relation):
        return Relation(self.set, self.relation.intersection(relation))

    def subtraction(self, relation):
        return Relation(self.set, self.relation.difference(relation))

    def inverse(self):
        new_relation = s()
        for i in self.relation:
            new_relation = new_relation.add(i[:: -1])
        return Relation(self.set, new_relation)

    def composition(self, relation):
        new_relation = s()
        for i in self.relation:
            for j in relation:
                if i[1] == j[0]:
                    new_relation = new_relation.add((i[0],j[1]))
        return Relation(self.set, new_relation)
    
     def isReflexive(self):
        for i in self.set:
            if ((i,i) not in self.relation):
                return False
        return True

    def isSymmetric(self):
        for i in self.relation:
            if ((i[1],i[0]) not in self.relation):
                return False
        return True

    def isTransitive(self):
        for i in self.relation:
            for j in self.relation:
                if (i[1] == j[0]) & ((i[0],j[1]) not in self.relation):
                    return False
        return True

    def reflexiveTransitiveClosure(self):
        pass


def get_relation_class(set):
    pass


if __name__ == "__main__":


