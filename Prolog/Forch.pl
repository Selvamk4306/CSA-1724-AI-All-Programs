% Facts
fact(rain).
fact(wet_grass).

% Rules
rule(wet_grass, rain).
rule(slippery_road, wet_grass).

% Forward chaining inference
infer(Fact) :- fact(Fact).
infer(Fact) :- rule(Fact, Condition), infer(Condition).