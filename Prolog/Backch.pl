% Facts
fact(rain).
fact(wet_grass).

% Rules
rule(wet_grass) :- fact(rain).
rule(slippery_road) :- rule(wet_grass).

% Backward chaining inference
infer(Fact) :- fact(Fact).
infer(Fact) :- rule(Fact).