% --- Facts: which birds can fly and which cannot

can_fly(sparrow).
can_fly(eagle).
can_fly(pigeon).
can_fly(parrot).

cannot_fly(penguin).
cannot_fly(ostrich).
cannot_fly(kiwi).

% --- Rule: bird_can_fly_or_not(Bird, Answer)
bird_can_fly_or_not(Bird, yes) :-
    can_fly(Bird).

bird_can_fly_or_not(Bird, no) :-
    cannot_fly(Bird).

bird_can_fly_or_not(Bird, unknown) :-
    \+ can_fly(Bird),
    \+ cannot_fly(Bird).
