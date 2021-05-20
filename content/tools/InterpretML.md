---
title: 'InterpretML'
values: ['explainability']
categories: ['model-agnostic', 'model-specific']
stages: ['learning', 'post-hoc']
licence: 'MIT'
repo: https://github.com/interpretml/interpret
languages: ['Python']
models: ['decision tree', 'decision tree ensemble']
tasks: ['TODO']
data: ['TODO']
references: 
- 
    name: 'Nori et al. - InterpretML: A Unified Framework for Machine Learning Interpretability'
    url: 'https://arxiv.org/abs/1909.09223'
---

The InterpretML toolkit, developed at Microsoft, can be decomposed in two major components:

1. A set of interpretable "glassbox" models
2. Techniques for explaining black box systems.

W.r.t. 1, InterpretML particularly contains a new interpretable "glassbox" model that combines Generalized Additive Models (GAMs) with machine learning techniques such as gradient boosted trees, called an *Explainable Boosting Machine*.

Other than this new interpretable model, the main utility of InterpretML is to unify existing explainability techniques under a single API.

{{< tool "Interpret-Text" >}} is an extension of InterpretML to support various text models.

## Glassbox models

- Explainable Boosting Machine
- Decision tree
- Decision rule list
- Linear/logistic regression 

## Blackbox explainers

- SHAP kernel explainer
- SHAP tree explainer
- {{< tool "LIME" >}}
- Morris sensitivity analysis
- Partial dependence plots

So this package contains both {{< category "model-agnostic" >}} and {{< category "model-specific" >}} explainers.

