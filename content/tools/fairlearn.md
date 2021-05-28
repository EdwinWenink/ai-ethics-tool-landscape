---
title: 'Fairlearn'
values: ['fairness']
fairness: ['group fairness']
categories: ['model-agnostic']
tasks: ['classification', 'regression']
data: ['tabular']
stages: ['preprocessing', 'learning', 'post-hoc']
licence: MIT
repo: https://github.com/fairlearn/fairlearn
languages: ['Python']
references: 
- 
    name: 'Agarwal et al. - Fair Regression: Quantitative Definitions and Reduction-based Algorithms'
    url: 'http://proceedings.mlr.press/v97/agarwal19d.html'
- 
    name: 'Agarwal et al. - A Reductions Approach to Fair Classification'
    url: 'https://arxiv.org/abs/1803.02453'
- 
    name: 'Hardt et al. - Equality of Opportunity in Supervised Learning'
    url: 'https://papers.nips.cc/paper/2016/hash/9d2682367c3935defcb1f9e247a97c0d-Abstract.html'
    
---

The documentation of `fairlearn` is excellent and provides a good introduction to the topic of fairness in AI. 
It is emphasized that fairness algorithms are no plug-and-play technical solutions, but require serious thought about the context of the data and the problem at hand.

> Fairness is a fundamentally sociotechnical challenge and cannot be solved with technical tools alone. They may be helpful for certain tasks such as assessing unfairness through various metrics, or to mitigate observed unfairness when training a model. Additionally, fairness has different definitions in different contexts and it may not be possible to represent it quantitatively at all. ([source](https://fairlearn.org/main/quickstart.html))

Fairlearn contains two main components:

- "[Metrics](https://fairlearn.org/main/user_guide/assessment.html) for assessing which groups are negatively impacted by a model, and for comparing multiple models in terms of various fairness and accuracy metrics."
- "[Algorithms](https://fairlearn.org/main/user_guide/mitigation.html) for mitigating unfairness in a variety of AI tasks and along a variety of fairness definitions."
    * Not all algorithms are applicable to all machine learning tasks.
    * Not all algorithms support all fairness definitions

`Fairlearn` contains two *reduction algorithms* that incorporate fairness constraints into a (binary) classification  or regression problem by reducing the problem into a sequence of weighted classification or regression problems. 
The only requirement of the `fairlearn` implementation is that the base estimator has a `fit` and `predict` call, so for example all your typical `sklearn` estimators are compatible.
This is applied in the {{< stage "learning" >}} stage.
Note that currently multi-class classification is not supported!

An interesting difference with a typical predict function is that sometimes *randomized* predictions are used:

> Fairlearn mitigation algorithms largely follow the conventions of scikit-learn, meaning that they implement the fit method to train a model and the predict method to make predictions. However, in contrast with scikit-learn, Fairlearn algorithms can produce randomized predictors. Randomization of predictions is required to satisfy many definitions of fairness. Because of randomization, it is possible to get different outputs from the predictor’s predict method on identical data. For each of our algorithms, we provide explicit access to the probability distribution used for randomization. [source](https://fairlearn.org/main/user_guide/mitigation.html#fairness-constraints-for-multi-class-classification)

`Fairlearn` also contains a {{< stage "preprocessing" >}} algorithm to remove correlation of non-sensitive features with sensitive features.
This addresses the potential issue that a machine learning model makes inferences based on sensitive features, even when these features are not explicitly included in the data, by instead using highly correlated features that were not considered to be sensitive on their own.

`Fairlearn` also contains a postprocessing algorithm ({{< stage "post-hoc" >}}) that takes (possibly biased) model output and then fits a monotone transformation such that a chosen parity constraint is still satisfied.

All these methods are thus {{< category "model-agnostic" >}}.
Note that being model-agnostic does not necessarily imply that the methods are also {{< stage "post-hoc" >}}, even though this generally does hold in the case of {{< value "explainability" >}}.

## Fairness definitions / Parity constraints

Generally speaking, the goal of the type of fairness that `fairlearn` implements is to *avoid harm*.
There are various ways to implement this.
The `fairlearn` package distinguishes and implements the following  [fairness constraints](https://fairlearn.org/main/user_guide/fairness_in_machine_learning.html#parity-constraints) for [group fairness](/fairness/group-fairness):

### Binary classification:

- DP - Demographic Parity: "the percentage of samples with label 1 should be equal across all groups"
    * Note that this concerns the *predicted* label, not the true label.
- TPRP - True positive rate parity: sensitive features should not affect the true positive rate
- FPRP - False positive rate parity: sensitive features should not affect the false positive rate
- EO - Equalized odds: "satisfies both *true positive rate parity* and *false positive rate parity*"
- ERP - Error Rate Parity: "error rates should be the same across all groups", which again is another way of saying that sensitive features should not affect error rates

`Fairlearn` includes various possible relaxations for these constraints, as exact parity is often unrlistic.

### Regression:

- BGL - Bounded Group Loss: the expected (regression) loss of each group must be below a chosen threshold


