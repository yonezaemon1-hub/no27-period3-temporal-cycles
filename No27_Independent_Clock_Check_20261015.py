#!/usr/bin/env python3
"""Independent brute-check for No.27, without importing the candidate solver.

Enumerate edge phase labels, and simulate next usable absolute clock time
one step at a time on each of the two simple arcs.  The optimization is over
all ordered vertex pairs. Uses standard library only (Python 3.12).
"""
from fractions import Fraction
from itertools import product
from collections import Counter
import json
from pathlib import Path


def traverse_at_absolute_times(edge_phases):
    # Edges usable at nonnegative integer t satisfying t % 3 == phase.
    # The first edge is taken at its first available time; periodic shifts
    # of that time do not change duration.
    t = edge_phases[0]
    start = t
    for next_phase in edge_phases[1:]:
        t += 1  # strict, cannot take two edges at the same time
        while t % 3 != next_phase:
            t += 1
    return t - start + 1


def all_directed_pairs_score(labels):
    n = len(labels)
    result = Fraction(1)
    for src in range(n):
        for dst in range(n):
            if src == dst:
                continue
            step_cw = (dst - src) % n
            clockwise_arc = tuple(labels[(src + j) % n] for j in range(step_cw))
            anticlockwise_arc = tuple(labels[(src - 1 - j) % n] for j in range(n - step_cw))
            fastest = min(traverse_at_absolute_times(clockwise_arc),
                          traverse_at_absolute_times(anticlockwise_arc))
            distance = min(step_cw, n-step_cw)
            score = Fraction(fastest, distance)
            if score > result:
                result = score
    return result


def expected(n):
    if n < 5:
        return Fraction(1)
    if n % 2 == 0 or n == 5:
        return Fraction(3, 2)
    return Fraction(5, 3)


def witness(n):
    if n == 3:
        return (0,0,0)
    if n == 4:
        return (0,1,0,1)
    if n == 5:
        return (0,2,1,0,1)
    if n == 7:
        return (0,2,1,0,1,0,1)
    if n % 2 == 0:
        return (0,1) * (n//2)
    return (0,2,0,2,1,2,1) + (0,1)*((n-7)//2)


def main():
    data = {"independent_clock_check": True, "enumeration": [], "witnesses": []}
    # Exhaustive full phase-normalized space, not just a candidate optimizer.
    for n in range(3, 10):
        counts = Counter()
        for tail in product(range(3), repeat=n-1):
            value = all_directed_pairs_score((0,)+tail)
            counts[value] += 1
        optimum = min(counts)
        assert optimum == expected(n), (n, optimum, expected(n))
        row = dict(n=n, cases=sum(counts.values()), optimum=str(optimum),
                   count_optimal=counts[optimum])
        data['enumeration'].append(row)
        print('CLOCK_FULL', row)
    for n in [3,4,5,6,7,8,9,10,11,12,19,20,31,32,51,52,100,101]:
        value = all_directed_pairs_score(witness(n))
        assert value == expected(n), (n,value,expected(n))
        row = dict(n=n, value=str(value), witness=''.join(map(str, witness(n))))
        data['witnesses'].append(row)
    # Finite combinatorial contradiction check for the exceptional n=7 lower bound.
    candidates = 0
    valid = 0
    for g in product((1,2), repeat=7):
        if sum(g) % 3:
            continue
        candidates += 1
        # A 3-edge arc has waiting costs g_i + g_{i+1} forward,
        # or complement route with three reverse waits from opposite arc.
        possible = True
        for i in range(7):
            cw_3edge_dur = 1 + g[i] + g[(i+1)%7]
            reverse_4edge_dur = 1 + sum(3-g[(i+j)%7] for j in (3,4,5))
            ccw_3edge_dur = 1 + (3-g[i]) + (3-g[(i+1)%7])
            forward_4edge_dur = 1 + sum(g[(i+j)%7] for j in (3,4,5))
            if (min(cw_3edge_dur,reverse_4edge_dur) > 4 or
                min(ccw_3edge_dur,forward_4edge_dur) > 4):
                possible = False
                break
        if possible:
            valid += 1
    assert candidates > 0 and valid == 0
    data['n7_gap_assignments_divisible_by_3'] = candidates
    data['n7_surviving_assignments_under_stretch_below_5_over_3'] = valid
    with open(Path(__file__).resolve().parent / 'No27_Independent_Check_Result_20261015.json','w',encoding='utf-8') as f:
        json.dump(data,f,indent=2,ensure_ascii=False)
    print('N7_GAP_CONTRADICTION', candidates,valid)
    print('RESULT=PASS')

if __name__=='__main__':
    main()
