---
title: Example-based explanations
---

Example-based explanations can be used either to provide more insight into a data set or insight into the predictions of machine learning models.
The explanations themselves are (a selection of) data instances, which assumes that data instances can be presented in a meaningful way.
For example, a data instance with 1000 features is not going to provide meaningful insights for humans.

Insight into data can be gained by providing *prototypical* examples, i.e. data instances that are representative of the data.
Model predictions can in turn be explained by referring to similar examples for which the same prediction is made.

{{< explanation "Counterfactual" >}} and {{< explanation "contrastive" >}}  examples are special cases for which this taxonomy has separate entries.
Adversarial examples are discussed under {{< value "security" >}}.
