
% Basic Operations
add(X, Y, Z) :- Z is X + Y.
subtract(X, Y, Z) :- Z is X - Y.
multiply(X, Y, Z) :- Z is X * Y.
divide(X, Y, Z) :- Y \= 0, Z is X / Y.

% Factorial
factorial(0, 1).
factorial(N, F) :- 
    N > 0, 
    N1 is N - 1, 
    factorial(N1, F1), 
    F is N * F1.

% GCD & LCM
gcd(X, 0, X).
gcd(X, Y, G) :- 
    Y > 0, 
    R is X mod Y, 
    gcd(Y, R, G).

lcm(X, Y, L) :- 
    gcd(X, Y, G), 
    L is (X * Y) // G.

% Prime Number Check
is_prime(2).
is_prime(3).
is_prime(P) :- 
    P > 3, 
    P mod 2 =\= 0, 
    \+ has_factor(P, 3).

has_factor(N, F) :- 
    N mod F =:= 0.
has_factor(N, F) :- 
    F * F < N, 
    F2 is F + 2, 
    has_factor(N, F2).

% Maximum in a List
max_list([X], X).
max_list([X|T], Max) :- 
    max_list(T, Max1), 
    Max is max(X, Max1).

% Minimum in a List
min_list([X], X).
min_list([X|T], Min) :- 
    min_list(T, Min1), 
    Min is min(X, Min1).

% Family Tree
father(john, paul).
father(paul, lisa).
mother(susan, lisa).
mother(linda, paul).

parent(X, Y) :- father(X, Y).
parent(X, Y) :- mother(X, Y).

grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
