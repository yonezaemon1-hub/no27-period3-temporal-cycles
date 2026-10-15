# No.27 — Publication and Review Gate v1.0

Date: 2026-10-15  
Author: Ryutaro Yonezu / Yonezu Research Lab  
Status: PREPRINT RELEASE CANDIDATE — analytical/reproducibility review PASS; scholarly novelty INCONCLUSIVE; public upload not yet verified.

## Main theorem and scope

For the periodic STGR model with one undirected edge phase in period 3, strict temporal paths, and stretch maximizing over ordered pairs:

- alpha*(C_n,3)=1 for n=3,4;
- alpha*(C_n,3)=3/2 for n=5 or even n>=6;
- alpha*(C_n,3)=5/3 for odd n>=7.

Historical priority/newness is not asserted. The STGR formulation is known from Mertzios et al. (MFCS 2025); the candidate contribution is the restricted exact classification for period-three cycles. The work is not peer reviewed.

## Primary source audit — passed (15 October 2026)

Full proceedings HTML (Section 2): https://drops.dagstuhl.de/storage/00lipics/lipics-vol345-mfcs2025/html/LIPIcs.MFCS.2025.75/LIPIcs.MFCS.2025.75.html
DOI: https://doi.org/10.4230/LIPIcs.MFCS.2025.75

The paper matches the published model on (i) strict temporal path times; (ii) duration = last edge traversal time minus first + 1; (iii) earliest-next appearance at each edge; (iv) maximization over ordered vertex pairs of fastest-path duration / static shortest distance. Our labels {0,1,2} reindex the original {1,2,3}. Restriction to two simple arcs is valid on a simple undirected cycle.

## Independent reviewer report — PASS (reported by user 15 October 2026)

- Two bundled scripts independently re-executed and consistent; all 8 hashes in source SHA256SUMS matched.
- Independent reviewer enumeration: walk-based n=3..7, arc-formula n=3..13, also checked through n=14; n=15 was still computing and is NOT a confirmed result.
- Odd-construction 0202121(01)^k was tested n=9..151.
- All four analytic lemmas were rederived and judged correct.
- Reviewer did NOT compare MFCS definitions directly; the separate primary-source comparison above addresses that omission.
- Reviewer confirms historical novelty remains inconclusive; the Meusel et al. SAND 2026 period-two result is not the same exact restricted theorem.

This reviewer report is an external account, not a stored signed or raw trace. Its extension beyond n=9 is not represented as locally reproducible evidence in this bundle.

## Local reproducibility and original bundle integrity

- Original source ZIP: `No27_Temporal_Cycles_Claude_Review_Bundle_DRAFT_20261015.zip`
- Source ZIP SHA-256: `45cee780b5ce5b2be034cf18864a64f6bfa648fe488c6bc869623a6de5981aa0`
- Original source ZIP manifest is **`No27_SHA256SUMS_20261015.txt`**, NOT `SHA256SUMS.txt`. All 8 listed payload files passed a local SHA-256 check.
- The original ZIP stores 9 files total (8 hashed payloads plus that manifest).
- Both original scripts were executed independently in a local Python environment on 15 October 2026. Exact enumeration n=3..9 and independent clock simulation n=3..9: PASS. Original n=3..101 witness and odd-gap checks: PASS.
- Original reviewed artefacts have **not been overwritten**. The public-candidate v1.0 PDF and TeX contain audit/status/attribution corrections and a single grammatical edit ("a exact" to "an exact"); the proof statements, constructions and computations were not changed.

## Publication rights and reuse

© 2026 Ryutaro Yonezu. All rights reserved. No permission is granted for reproduction, redistribution, modification or commercial reuse without prior written permission, except as permitted by applicable law. No separate reuse license is granted by this bundle. Reproducibility scripts are provided for review; any further public repository/Zenodo license metadata must be explicitly aligned before upload.

## Reference/novelty limitations

To the best of the author's knowledge, the stated all-n restricted-family formula was not identified in the consulted literature; this is NOT a claim to be first. Research inquiries: yonezaemon1+research@gmail.com

## Remaining publication actions

1. Upload PDF, scripts, proof-related notes, this gate and manifest to a GitHub repo for No.27.
2. Create the Zenodo record and set a license aligned with the statement above.
3. Verify published PDF and archive hashes; record DOI/commit and update the master research table.
