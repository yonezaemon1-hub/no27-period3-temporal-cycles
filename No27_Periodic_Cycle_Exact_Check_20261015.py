#!/usr/bin/env python3
"""No.27 candidate: exact optimal stretch for cycles with period 3.
Pure Python 3.12, standard library only. No APIs, no new runtime.
Exhausts all phase labelings modulo a global phase shift for n=3..9,
then checks the claimed infinite-family upper-bound witnesses up to n=101.
Not a substitute for an independent mathematical or novelty audit.
"""
from collections import Counter
from fractions import Fraction
from itertools import product

PERIOD = 3


def duration(labels, period=PERIOD):
    """Duration of a temporal path in edge order, first crossing counts as 1."""
    assert labels
    t = 1
    for a, b in zip(labels, labels[1:]):
        t += (b - a - 1) % period + 1
    return t


def stretch(labels, period=PERIOD):
    """Exact maximum fastest-path-duration / static distance on a cycle."""
    n = len(labels)
    worst = Fraction(1)
    for start in range(n):
        for destination in range(n):
            if start == destination:
                continue
            clockwise_steps = (destination - start) % n
            clockwise_edges = [labels[(start + k) % n]
                               for k in range(clockwise_steps)]
            counterclockwise_edges = [labels[(start - 1 - k) % n]
                                      for k in range(n - clockwise_steps)]
            fastest = min(duration(clockwise_edges, period),
                          duration(counterclockwise_edges, period))
            distance = min(clockwise_steps, n - clockwise_steps)
            worst = max(worst, Fraction(fastest, distance))
    return worst


def upper_witness(n):
    if n == 3:
        return (0, 0, 0)
    if n == 4:
        return (0, 1, 0, 1)
    if n == 5:
        return (0, 2, 1, 0, 1)
    if n == 7:
        return (0, 2, 1, 0, 1, 0, 1)
    if n >= 6 and n % 2 == 0:
        return (0, 1) * (n // 2)
    if n >= 9 and n % 2 == 1:
        return (0, 2, 0, 2, 1, 2, 1) + (0, 1) * ((n - 7) // 2)
    raise ValueError(n)


def theorem_value(n):
    if n in (3, 4):
        return Fraction(1)
    if n == 5 or n >= 6 and n % 2 == 0:
        return Fraction(3, 2)
    return Fraction(5, 3)


def exhaustive(n):
    histogram = Counter()
    best = None
    for tail in product(range(PERIOD), repeat=n - 1):
        # A uniform time-phase shift leaves all durations unchanged.
        lab = (0,) + tail
        r = stretch(lab)
        histogram[r] += 1
        if best is None or r < best:
            best = r
    assert best == theorem_value(n), (n, best, theorem_value(n))
    print(f"EXHAUSTIVE n={n}: phase-normalized_labelings={PERIOD ** (n-1)}, "
          f"optimal={best}, optimizers={histogram[best]}, PASS")
    return histogram


def main():
    for n in range(3, 10):
        exhaustive(n)
    for n in range(3, 102):
        lab = upper_witness(n)
        assert len(lab) == n
        r = stretch(lab)
        assert r == theorem_value(n), (n, r, theorem_value(n))
    print('CONSTRUCTIVE WITNESSES n=3..101: PASS')
    # For n>=9 odd, every three consecutive cyclic phase increments
    # contain both 1 and 2. Thus no directed path of d edges
    # has more than ceil(2(d-1)/3) waits of size 2.
    for n in range(9, 102, 2):
        lab = upper_witness(n)
        gaps = [(lab[(i+1) % n] - lab[i]) % PERIOD for i in range(n)]
        assert all(x in (1, 2) for x in gaps)
        assert all(len({gaps[i], gaps[(i + 1) % n], gaps[(i + 2) % n]}) == 2
                   for i in range(n)), n
    print('ODD FAMILY CYCLIC GAP PROPERTY n=9..101: PASS')
    print('RESULT=PASS (finite calculations and witness checks only)')


if __name__ == '__main__':
    main()
