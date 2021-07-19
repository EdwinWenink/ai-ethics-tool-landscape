---
title: 'XAI Toolbox'
values: ['explainability', 'fairness']
explanations: ['perturbation']
fairness: ['group fairness']
tasks: ['classification']
data: ['tabular']
stages: []
licence: 'MIT'
repo: https://github.com/EthicalML/xai
languages: ['Python']
frameworks: ['pandas']
---

This library is a small toolbox that offers some convenience functions for quickly visualizing imbalances in the data set, computing (permutation) feature importances and metrics such as the ROC-curve.
A function to balance the data is offered through basic up- or downsampling, but other than this no fairness criteria are defined.

Compared to other libraries the XAI Toolbox is very basic and currently the [roadmap](https://github.com/EthicalML/xai/blob/master/ROADMAP.md) (which is not updated since 2019) does not include any major improvements.
The library is in early alpha and does not seem to be actively maintained anymore.
