% pattern_match(Pattern, String)
% Succeeds if Pattern matches the start of String

pattern_match([], _).
pattern_match([P|Ps], [P|Ss]) :-
    pattern_match(Ps, Ss).
