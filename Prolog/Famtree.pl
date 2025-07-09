% --- Facts ---

% Gender
male(john).
male(mike).
male(tom).
male(james).

female(susan).
female(lisa).
female(mary).
female(anna).

% Parent-child relationships
father(john, mike).
father(john, lisa).
father(mike, tom).
father(mike, mary).
father(james, anna).

mother(susan, mike).
mother(susan, lisa).
mother(lisa, tom).
mother(lisa, mary).
mother(anna, james).

% --- Rules ---

% parent(X, Y): X is a parent of Y
parent(X, Y) :- father(X, Y).
parent(X, Y) :- mother(X, Y).

% grandparent(X, Y): X is a grandparent of Y
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

% sibling(X, Y): X and Y are siblings (share at least one parent, and are not the same person)
sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

% brother(X, Y): X is brother of Y
brother(X, Y) :-
    sibling(X, Y),
    male(X).

% sister(X, Y): X is sister of Y
sister(X, Y) :-
    sibling(X, Y),
    female(X).
