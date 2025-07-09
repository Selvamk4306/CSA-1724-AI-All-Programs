% Monkey and Banana Problem in Prolog

% Possible actions:
%   - grasp
%   - climb
%   - push(Box, From, To)
%   - walk(From, To)

% move(StateBefore, StateAfter, Action)

% The state is represented as:
% state(MonkeyPosition, HasBanana, BoxPosition, MonkeyOnBox)

% Case when monkey grasps the banana
move(state(middle, has_not, middle, on_box),
     state(middle, has, middle, on_box),
     grasp).

% Monkey can climb onto the box
move(state(Pos, has_not, Pos, on_floor),
     state(Pos, has_not, Pos, on_box),
     climb).

% Monkey can push the box from one position to another
move(state(Pos, has_not, Pos, on_floor),
     state(NewPos, has_not, NewPos, on_floor),
     push(Pos, NewPos)).

% Monkey can walk from one position to another
move(state(Pos, has_not, BoxPos, on_floor),
     state(NewPos, has_not, BoxPos, on_floor),
     walk(Pos, NewPos)).

% Plan: find a sequence of moves leading to the banana
% plan(State, GoalState, Moves)

plan(State, State, []). % if current state is goal state, done

plan(State, GoalState, [Move|Moves]) :-
    move(State, NextState, Move),
    plan(NextState, GoalState, Moves).

% Start planning from initial state
% monkey_starts_plan(Moves)
% Initial state: monkey at door, has_not banana, box at window, monkey on floor
% Goal state: monkey has banana

monkey_starts_plan(Moves) :-
    plan(state(at_door, has_not, at_window, on_floor),
         state(_, has, _, _),
         Moves).