# Research No.27 candidate — Exact optimal stretch of period-3 temporal cycles

**Date:** 2026-10-15  
**Researcher:** Ryutaro Yonezu / Yonezu Research Lab  
**Stage:** Candidate, mathematical proof internally assembled; independent audit pending.  
**Novelty:** INCONCLUSIVE. No priority or world-first claim.

## Model

Let $C_n$ be an undirected cycle, $n\ge3$, whose edges receive one availability phase $\lambda(e)\in\mathbb{Z}_3$ each period of length 3. A temporal path must traverse edges at strictly increasing integer times. For a path with phases $a_1,\ldots,a_d$, the duration is

$$\operatorname{dur}(a_1,\ldots,a_d)=1+\sum_{j=1}^{d-1} w(a_j,a_{j+1}),\quad w(a,b)=1+((b-a-1)\bmod3).$$

For distinct vertices $u,v$, minimize duration over both simple arcs of the cycle. Let

$$\alpha^*(C_n,3)=\min_{\lambda}\max_{u\ne v}\frac{\operatorname{dur}_\lambda(u,v)}{d_{C_n}(u,v)}.$$

## Proposed exact theorem

$$\boxed{\alpha^*(C_n,3)=\begin{cases}
1 & n=3,4,\\
3/2 & n=5\text{ or even }n\ge6,\\
5/3 & \text{odd }n\ge7.
\end{cases}}$$

### Constructive upper bounds

- $n=3$: every pair is adjacent, so stretch 1. $n=4$: the phase pattern `0101` gives stretch 1, since for each opposite pair one of the two two-edge arcs has duration 2.
- $n=5$: every pair has static distance at most 2. Proper cyclic edge-phase coloring `02101` ensures adjacent phases differ, so every shortest two-edge arc has duration at most 3. Therefore the stretch is at most $3/2$.
- Even $n\ge6$: alternating phases `0101...` give cyclic phase increments 1,2,1,2,..., hence every $d$-edge simple arc has duration at most $d+\lceil(d-1)/2\rceil\le 3d/2$.
- $n=7$: pattern `0210101` is proper edge coloring and the diameter is 3. Every shortest arc with $d\le3$ has duration at most $1+2(d-1)=2d-1\le5d/3$.
- Odd $n\ge9$: use cyclic edge phases `0202121` followed by alternating `01` repeated $(n-7)/2$ times. All cyclic phase increments lie in $\{1,2\}$, and no three consecutive increments are identical. For either travel direction and every path with $d$ edges, at most $\lceil 2(d-1)/3\rceil\le2d/3$ waiting increments are 2; hence its duration is at most $d+2d/3=5d/3$. This also bounds fastest paths.

### Lower bounds

- For any $n\ge5$, $\alpha<3/2$ would force both orientations of every two-edge path to have duration 2: the alternative arc has at least 3 edges. But for two successive edge phases $a,b$, their required waiting increments in opposite directions cannot both be 1 modulo 3. Therefore $\alpha^*\ge3/2$.
- For odd $n\ge9$, suppose $\alpha<5/3$. Since the alternative to a shortest two-edge path has length $n-2\ge7$, all adjacent edge phases must differ (otherwise one direction has duration 4). In every directed three-edge arc, duration must be at most 4: the alternate arc has length $n-3\ge6$. Write cyclic successive edge-phase increments as $g_i\in\{1,2\}$. Forward and backward three-edge arcs on the same three edges must both have duration at most 4. Since their two waiting sums add to 6, the forward adjacent pair $g_i,g_{i+1}$ must sum to 3, so $g_i\ne g_{i+1}$ for all $i$. Such a cyclic alternating sequence is impossible for odd $n$. Hence $\alpha^*\ge5/3$.
- For $n=7$, assume $\alpha<5/3$. Again adjacent edge phases differ, so all seven cyclic increments $g_i\in\{1,2\}$. Because their total is divisible by 3, the number of 2's must be either 2 or 5. Reversing the traversal orientation exchanges the counts, so take five 2's. There is a consecutive pair $g_i=g_{i+1}=2$. The three-edge clockwise route using that pair takes duration 5, so its complementary four-edge route must have duration 4 or less; that requires $g_{i+3}=g_{i+4}=g_{i+5}=2$. These exhaust the five 2's, forcing $g_{i+2}=g_{i+6}=1$. Now the consecutive pair $g_{i+3}=g_{i+4}=2$ gives another three-edge clockwise duration 5; the four-edge complementary route cannot have duration 4 because one of its reverse increments corresponds to $g_{i+6}=1$ (so it waits 2). Contradiction.

## Computational checks

`No27_Periodic_Cycle_Exact_Check_20261015.py` uses Python 3 standard library only, works directly with rational `Fraction`s, and exhausts $3^{n-1}$ normalized phase labelings for $3\le n\le9$. It independently checks the constructed examples through $n=101$ and the no-three-identical-gap property for odd $n\ge9$ through 101. Exhaustive search is finite supporting evidence; the proof arguments above are needed for all $n$.

Independent prototype computations used a C++ brute-force enumerator through $n=15$ at period 3 and a separately implemented Python enumerator for small values. **These are internal checks, not external audits.**

## Prior art and risk

1. Mertzios, Molter, Morawietz and Spirakis, *Temporal Graph Realization with Bounded Stretch*, MFCS 2025, DOI 10.4230/LIPIcs.MFCS.2025.75 (also JCSS 2026). Establishes the STGR model, hardness and general algorithms.
2. Meusel, Morawietz, Müller-Hannemann and Reinhardt, *Brief Announcement: Revisiting the Realizability of Periodic Temporal Graphs with Bounded Stretch*, SAND 2026, DOI 10.4230/LIPIcs.SAND.2026.21. Considers period 2, complexity, possible stretch and notes restricted graph classes as future work.

The searched primary papers and targeted search terms did **not** identify this exact period-3 cycle theorem. That is **not** sufficient to claim novelty or historical priority. Independent specialized prior-art audit remains required.

## Gate

- Precise theorem/proof: INTERNAL PASS PENDING INDEPENDENT AUDIT.
- Finite enumeration: INTERNAL PASS once checked evidence script output and hashes are frozen.
- Literature novelty: INCONCLUSIVE.
- Publication: HOLD until independent mathematical and evidence audit. No alteration of the shared runtime/harness is needed.
