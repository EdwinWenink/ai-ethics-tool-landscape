---
title: Shapley value explanations
---

Methods using Shapley values are very influential and use a particular form of {{< explanation "perturbation">}} to explain the importance of features for predictions. 
The importance of a feature for a prediction is measured in terms of how much this feature "pushes" the prediction away from *a relevant baseline value*, such as an average over a reference set.
Different methods use different forms of perturbation. 
One could for example look at the difference in model output between 1) when a feature is present and 2) when a feature is occluded, repeat this for all subsets of features, and then compute the average difference per feature.
Often it is not possible to compute the exact Shapley value due to the combinatorial explosion of subsets, so in practice packages implement smart approximations to Shapley values.
