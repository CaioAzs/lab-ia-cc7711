% casal Pietro e Antonita criou cinco filhos, o João, a Clara,o Francisco, a Valéria e a Ana
pai(pietro, joao).
pai(pietro, clara).
pai(pietro, francisco).
pai(pietro, valeria).
pai(pietro, ana).

mae(antonita, joao).
mae(antonita, clara).
mae(antonita, francisco).
mae(antonita, valeria).
mae(antonita, ana).

%o Mário é filho do João
pai(joao, mario).
%Ana teve duas filhas, a Helena e a Joana
mae(ana, helena).
mae(ana, joana).

% Carlos nasceu da relação entre a Helena, muito formosa, e o Mário
pai(mario, carlos).
mae(helena, carlos).

%Clara era mãe de Pietro e Enzo
pai(clara, pietro_jr).
pai(clara, enzo).

%Francisca e Antonia,filhas de Jacynto e Claudia
pai(jacynto, francisca).
pai(jacynto, antonia).
mae(claudia, francisca).
mae(claudia, antonia).

pai(pablo, jacynto).
mae(luzia, jacynto).

% Francisco não teve filhos, mas casou-se com Fabiana
casado(francisco, fabiana).
% Pietro e Enzo, que casaram com as irmãs Francisca e Antonia
casado(pietro_jr, francisca).
casado(enzo, antonia).

avo(X, Y) :- pai(X, Z), (pai(Z, Y); mae(Z, Y)).
ava(X, Y) :- mae(X, Z), (pai(Z, Y); mae(Z, Y)).
tio(X, Y) :- pai(Z, Y), irmao(X, Z).
tia(X, Y) :- mae(Z, Y), irmao(X, Z).
irmao(X, Y) :- pai(Z, X), pai(Z, Y), X \= Y.
irmao(X, Y) :- mae(Z, X), mae(Z, Y), X \= Y.
primo(X, Y) :- pai(Z, X), pai(W, Y), irmao(Z, W).
primo(X, Y) :- mae(Z, X), mae(W, Y), irmao(Z, W).
descendente(X, Y) :- pai(Y, X).
descendente(X, Y) :- mae(Y, X).
descendente(X, Y) :- pai(Y, Z), descendente(X, Z).
descendente(X, Y) :- mae(Y, Z), descendente(X, Z).
ascendente(X, Y) :- descendente(Y, X).