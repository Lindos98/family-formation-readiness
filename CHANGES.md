# Corrections to Fangzhou's submission

1. Kept the data, primary six-predictor model, controls, role coding and author-supplied main estimates unchanged.
2. Marked classification accuracy and fitted calibration as in-sample; removed claims of external predictive performance. Moza's work is not duplicated.
3. Removed archived custom Brant p-values from the current diagnostics table and JSON. The script exports threshold-specific fits/warnings rather than presenting an unreliable omnibus decision. The lowest split has only five records and no Emirati category-1 records.
4. Removed the LR comparison of merged category indicators against unmerged numeric predictors: those specifications are not nested. The exploratory categorical sensitivity remains, without this p-value.
5. Corrected the claim that D1 awareness and nationality are inseparable: the contrast lacks within-Emirati support, but non-Emirati records include both groups.
6. Softened non-significant, policy-priority, group-gap and family-location interpretations. Explained that scenario predictions use the primary shared-slope model and different averaging populations from the adjusted nationality table.
7. Flagged partial overlap checks, unestablished scenario support, selection of the D8.1 subset, and the boundary-sensitive 1,000-draw nationality interval.
8. Aligned three confidence-interval endpoints in the prose with Fangzhou's own table (C1, C14 and E13).
9. Removed unverified precise literature descriptions; retained contextual citations from the existing project bibliography. Full source verification remains a team responsibility.
10. Corrected output locations so regenerated PDF figures/LaTeX tables replace the files Overleaf reads. Added a stable data path and repository entry point.
11. Replaced author-declared exact dependency pins with explicit compatibility ranges; full corrected-script execution remains pending in an environment with statsmodels installed.
12. Removed a reference to an unavailable sec:model label, replacing it with a self-contained one-sentence model specification.

## Not changed or claimed complete
- No original survey records were edited.
- No new held-out validation or calibration is presented.
- No claim that proportional odds or cross-group measurement validity is established.
- Alanoud's dataset is included, but her missing results text/figures are not replaced with newly attributed work.
- This package has not been pushed to GitHub or uploaded to Overleaf.

## Placeholder correction
Added explicit placeholder files for Mohamed, Moza and Alanoud, plus Linda's integration notes. Wired Mohamed's Discussion into the main document. Analysis and data are unchanged.


## 10 November 2026 column count correction

Corrected Alanoud Table 4 from 136 to 135 columns following her confirmation. Added a note that the synthetic-data indicator column was removed before analysis and all 700 records remain synthetic. Updated the data-status row and resolved the column-count review note. No datasets or model results were changed. The separately supplied Word draft has not been updated in this package-only revision.
