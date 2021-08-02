---
title: Anchor
---

An "anchor" is a subset of features and their value ranges for which the model will almost always output the same prediction. 
Another way of saying this is that if the feature values of an anchor are satisfied, other features will very likely not affect the prediction, i.e. the prediction is "anchored".
Anchors are by design interpretable, because they clearly indicate for which feature values they apply.
Such an anchor can be expressed as an *if-then* rule.
Algorithms for computing anchors are model-agnostic.
