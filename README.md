Implement the function get_relation_class(a). The function takes a set M and returns a class representing relations on M (that is a subset of MxM). The class should support the following operations and predicates:

    does the relation contain given element
    adding an element to the relation
    removing an element from the relation
    union of two relations
    intersection of two relations
    subtraction of two relations
    inverse relation
    composition of two relations
    is the relation reflexive
    is the relation symmetric
    is the relation transitive
    reflexive-transitive closure

The instances of the class representing relation should be immutable. That, is after an instance is created, its state cannot be modified. The time-complexity of your function need not to be optimal but it needs to be reasonable (e.g. adding n elements to an empty relation should not take O(n^2) time). To attain this you will probably need a data structure that is reasonable efficient at making changes in immutable objects. You probably do not want to implement one, I recommend using something from Pyrsistent library).
