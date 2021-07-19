---
title: 'TreeInterpreter'
values: ['explainability']
explanations: ['white box']
categories: ['model-specific']
tasks: ['regression', 'classification']
data: ['tabular']
stages: ['in-processing']
licence: 'BSD-3'
repo: 'https://github.com/andosa/treeinterpreter'
languages: ['Python']
frameworks: ['scikit-learn']
references: 
- 
    name: 'Demo and explanation'
    url: 'http://blog.datadive.net/random-forest-interpretation-with-scikit-learn/'
---

This library provides a separate `predict()` function for `scikit-learn` tree-based models (so also ensembles) that outputs a prediction with interpretable elements of the shape `prediction = bias + feature_1_contribution + ... + feature_n_contribution`.

That is, it turns these tree-based models into a {{< explanation "white box" >}}, where we can inspect how much each feature contributes to the predicted value (in the case of regression) or how much it contributes to the estimated probability of a class (given classification).
