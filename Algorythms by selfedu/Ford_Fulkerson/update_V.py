#!/usr/bin/python3

def updateV(V, T, f):
    for t in T:
        if t[1] == -1:  # это исток
            continue
        sgn = V[t[2]][t[1]][2]  # направление движения

        # меняем веса в таблице
        V[t[1]][t[2]][0] -= f * sgn
        V[t[1]][t[2]][1] += f * sgn

        V[t[2]][t[1]][0] -= f * sgn
        V[t[2]][t[1]][1] += f * sgn

