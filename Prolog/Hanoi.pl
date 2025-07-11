% hanoi(N, Source, Target, Auxiliary)
% N = number of disks
% Source = starting peg
% Target = destination peg
% Auxiliary = helper peg

hanoi(1, Source, Target, _) :-
    write('Move disk from '), write(Source),
    write(' to '), write(Target), nl.

hanoi(N, Source, Target, Auxiliary) :-
    N > 1,
    N1 is N - 1,
    hanoi(N1, Source, Auxiliary, Target),
    hanoi(1, Source, Target, _),
    hanoi(N1, Auxiliary, Target, Source).
