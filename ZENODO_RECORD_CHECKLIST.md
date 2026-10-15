# No.27 — Zenodo publication record checklist

## Status
- GitHub v1.0 publication: **PUBLIC**, commit `e8c29313c16da4cc575669f3bae57677c87b2ebc`.
- Independent mathematical and computational review: **PASS**.
- Historical priority / scholarly novelty: **INCONCLUSIVE**, with no first-discovery claim.
- Zenodo DOI: **NOT YET ASSIGNED**. This is deposit preparation, not evidence of Zenodo publication.

## Exact Zenodo metadata

- **Resource type:** Publication → Preprint
- **Title:** Exact Optimal Stretch of Period-Three Temporal Cycles
- **Creator:** Yonezu, Ryutaro
- **Affiliation:** Yonezu Research Lab
- **Publication date:** 2026-10-15
- **Publisher:** Zenodo
- **Version:** v1.0
- **Language:** English
- **Keywords:** periodic temporal graphs; stretched temporal graph realization; STGR; cycles; period three; optimal stretch; combinatorial optimization
- **Access to files:** Public
- **License:** Custom license, title **All rights reserved** (NOT Zenodo's CC-BY default).
- **License description:** © 2026 Ryutaro Yonezu. All rights reserved. No permission is granted for reproduction, redistribution, modification or commercial reuse without prior written permission, except as permitted by applicable law. No separate reuse license is granted.
- **Existing DOI?** No. Obtain a new Zenodo DOI for this preprint.

### Description

We analyze the stretched temporal graph realization (STGR) optimization model of Mertzios et al. on undirected cycles C_n with one edge-availability phase per period and period Δ=3. With strict temporal paths and fastest-path duration relative to static graph distance, the exact optimal multiplicative stretch is 1 for n=3,4; 3/2 for n=5 or even n≥6; and 5/3 for odd n≥7. Explicit cyclic phase labelings establish the upper bounds, while local constraints and a separate seven-cycle argument establish the lower bounds.

The mathematical proof and finite reproducibility evidence received independent review (PASS). Separate comparison against Mertzios et al. (MFCS 2025) supports alignment with its STGR duration and stretch conventions; this source comparison was not performed by the independent mathematical reviewer. The bundled scripts provide exact enumeration for n=3–9 and constructive checks through n=101. Independent reviewer extensions through n=14 were reported but are not included as raw evidence in this release. This is an unrefereed preprint. The STGR model and optimization objective are prior art. To the best of the author's knowledge, the specific period-three cycle classification was not identified in the literature consulted, but historical novelty remains unestablished and **no claim of priority or first discovery** is made.

Research Inquiries — Yonezu Research Lab  
Contact: yonezaemon1+research@gmail.com

GitHub repository: https://github.com/yonezaemon1-hub/no27-period3-temporal-cycles  
Frozen GitHub commit: https://github.com/yonezaemon1-hub/no27-period3-temporal-cycles/commit/e8c29313c16da4cc575669f3bae57677c87b2ebc

## Files to upload (exact names, no replacements)

1. `No27_Exact_Stretch_Period3_Temporal_Cycles_v1_0_20261015.pdf`
2. `No27_Exact_Period3_Temporal_Cycles_RELEASE_CANDIDATE_v1_0_20261015.zip`

Do not accidentally deposit the older DRAFT paper/bundle, and do not choose Software as the primary resource type: this record is for the preprint and its supplementary evidence.

## Publication and verification gate

1. Start a new manual Zenodo upload using the authenticated existing Zenodo account.
2. Upload the exact two files above and fill the metadata exactly. Check that Zenodo did not retain the default CC-BY license.
3. Save the draft and preview it. Publish only after confirming both files and the custom All rights reserved label.
4. Record the published DOI and URL (a reserved, unpublished DOI is not sufficient).
5. Download/check Zenodo-published PDF and ZIP against the audited GitHub v1.0 contents, comparing SHA-256 individually.
6. Update this document and `README.md` with the activated DOI, and update the master research spreadsheet entry No.27. Do not modify the frozen PDF or evidence archive for metadata-only changes.
