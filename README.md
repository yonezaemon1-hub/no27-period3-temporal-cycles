# No.27 — Exact Optimal Stretch of Period-Three Temporal Cycles

**Author:** Ryutaro Yonezu — Yonezu Research Lab  
**Manuscript:** unrefereed preprint v1.0, 15 October 2026  
**Status:** independent mathematics/reproducibility audit PASS; historical priority INCONCLUSIVE.

For the Mertzios et al. (MFCS 2025) model on undirected cycles of period Δ=3, the exact optimal stretch is 1 for n=3,4; 3/2 for n=5 and even n>=6; and 5/3 for odd n>=7. The model is prior art, and no first-discovery claim is made.

## Reproduction

Python 3.12 standard library:

```sh
python No27_Periodic_Cycle_Exact_Check_20261015.py
python No27_Independent_Clock_Check_20261015.py
sha256sum -c SHA256SUMS.txt
```

See `No27_Publication_Gate_v1_0_20261015.md` for the independent review, MFCS 2025 model comparison, and audit limitations.

**License:** © 2026 Ryutaro Yonezu. All rights reserved. No separate reuse license granted.  
**Contact:** yonezaemon1+research@gmail.com  
**DOI:** not assigned; update this README when the public DOI is active.
