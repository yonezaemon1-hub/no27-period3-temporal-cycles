# No.27 — Prior-art audit for the period-3 temporal cycle stretch theorem

Date: 2026-10-15
Research: Ryutaro Yonezu / Yonezu Research Lab
Status: **INCONCLUSIVE** (no claim of priority; not a mathematical proof audit)

## Precise candidate

The model is STGR (Stretched Temporal Graph Realization) with an undirected cycle C_n and one edge availability phase per period, period Δ=3. Strict temporal paths, duration equal to last time minus first time plus one, and stretch measured against static graph distance. This model and objective are **not new**.

Candidate residual claim (internally derived, not independently audited):

- α*(C_n,3)=1 for n=3,4;
- α*(C_n,3)=3/2 for n=5 and for even n≥6;
- α*(C_n,3)=5/3 for odd n≥7.

Distinctiveness, if any, concerns the explicit exact classification, finite exceptional cases, constructions, and lower-bound proof for **this restricted family**, not STGR itself.

## Primary literature examined

1. **N. Klobas, G. B. Mertzios, H. Molter, P. G. Spirakis**, *Temporal Graph Realization from Fastest Paths*, SAND 2024, DOI: https://doi.org/10.4230/LIPIcs.SAND.2024.16 ; full paper https://drops.dagstuhl.de/storage/00lipics/lipics-vol292-sand2024/LIPIcs.SAND.2024.16/LIPIcs.SAND.2024.16.pdf . Exact realization of a prescribed fastest-duration matrix; polynomial case for trees and FPT with respect to feedback edge number. This is not the minimax stretch problem. Text search for “cycle” and “unicyclic” found no matches in the conference paper; that is not a check of every proof or the linked full arXiv version https://arxiv.org/abs/2302.08860 .
2. **G. B. Mertzios, H. Molter, N. Morawietz, P. G. Spirakis**, *Temporal Graph Realization with Bounded Stretch*, MFCS 2025, DOI: https://doi.org/10.4230/LIPIcs.MFCS.2025.75 ; full HTML https://drops.dagstuhl.de/storage/00lipics/lipics-vol345-mfcs2025/html/LIPIcs.MFCS.2025.75/LIPIcs.MFCS.2025.75.html ; arXiv https://arxiv.org/abs/2504.14258 . **Direct prior art for the identical STGR model and objective**. Studies hardness, approximation, structural parameter algorithms and local search. Search for “cycle” in full MFCS HTML returned no match; no period-3 C_n exact sequence found in its stated results.
3. **Mertzios et al.**, journal version, *Journal of Computer and System Sciences* 160 (September 2026), 103814, DOI: https://doi.org/10.1016/j.jcss.2026.103814 . Publication and abstract verified; web-accessible full journal text was not exhaustively audited due to access limitations. Treat potential added statements relative to the MFCS version as **not fully ruled out**.
4. **J. Meusel, N. Morawietz, M. Müller-Hannemann, K. Reinhardt**, *Brief Announcement: Revisiting the Realizability of Periodic Temporal Graphs with Bounded Stretch*, SAND 2026, DOI: https://doi.org/10.4230/LIPIcs.SAND.2026.21 ; full HTML https://drops.dagstuhl.de/storage/00lipics/lipics-vol373-sand2026/html/LIPIcs.SAND.2026.21/LIPIcs.SAND.2026.21.html . Proves hardness for Δ=2, existence of optimal stretch 5/3 when Δ=2, and extreme achievable stretches. **Important: numerical 5/3 coincides with No.27, but period Δ=2 is different from Δ=3.** No cycle-specific period-3 formula found in the six-page announcement. A longer version with omitted examples/proofs was not located in this search.
5. **J. Cauvi, N. Morawietz, L. Viennot**, *Foremost, Fastest, Shortest: Temporal Graph Realization Under Various Path Metrics*, STACS 2026, DOI: https://doi.org/10.4230/LIPIcs.STACS.2026.24 ; full HTML https://drops.dagstuhl.de/storage/00lipics/lipics-vol364-stacs2026/html/LIPIcs.STACS.2026.24/LIPIcs.STACS.2026.24.html . Studies temporal realization with exact duration/earliest arrival/path length matrices and complexity for varied temporal path metrics. No closed-form STGR minimax stretch for period-3 cycles observed; “cycle” text search did not find a match.

## Search breadth / methodology

- Direct authors/title searches for STGR, periodic temporal graph realization and bounded stretch.
- Searches combining cycle/C_n, edge phases/edge labeling, Δ=3/period 3, fastest temporal path, stretch and values 3/2 and 5/3.
- Related research branches: periodic timetable minimax travel-time design; exact fastest-path realization; edge labeling with waiting times.
- Main published proceedings HTML was examined and targeted string searches used. PDF inspection for SAND 2024 and SAND 2026 also performed.
- Search engine absence of an exact hit **is not proof of novelty**. Abstracts, unpublished manuscripts, full versions not accessible in the current search, historical labeling terminology, and equivalent combinatorial reformulations remain possible overlap sources.

## Claim comparison

| Candidate element | Finding |
|---|---|
| Periodic temporal graph with one phase per edge | ALREADY KNOWN (at least Klobas et al. 2024) |
| Minimize max fastest-duration / static distance | ALREADY KNOWN (Mertzios et al. MFCS 2025) |
| Stretch 5/3 in temporal realizations | KNOWN AS A VALUE for Δ=2 (Meusel et al. 2026); **not** exact overlap of period-3 cycle theorem |
| Closed form α*(C_n,3)=1,3/2,5/3 with parity and exceptions | NOT IDENTIFIED in examined primary works; novelty **INCONCLUSIVE** |
| Specific alternating edge-phase construction and short parity lower bound | NOT IDENTIFIED in examined primary works; could be a simple consequence or known under alternate terminology |

## Publication claims / recommended text

A permissible cautious framing would be:
> We study the STGR objective introduced by Mertzios et al. for the restricted family of cycles with period three. We derive an explicit candidate classification of the optimal stretch for all cycle sizes. Although the cited works do not state this classification, a complete historical novelty assessment has not been established; no claim of priority is made.

**Publication gate**: mathematical proof/evidence independent audit is still required. The present literature audit is INCONCLUSIVE; do not claim world-first, newly introduced metric, or a resolution of an established open problem. Note also that a restricted class being mentioned as future work in Meusel et al. does not establish that every result on such a class is new.

## Outstanding targeted checks

1. Full 2026 JCSS journal text, especially differences vs MFCS 2025.
2. Any expanded version of Meusel et al. SAND 2026 and its Lemma 3.2 witness graph.
3. Older work on cyclic words/edge-phase scheduling/maximum waiting-time ratio where the same formula might appear without the term STGR.
4. Independent specialist audit of theorem, witness construction and smallest exceptional cases.

Overall: **KEEP as candidate, novelty INCONCLUSIVE, publication HOLD pending mathematical audit.**
