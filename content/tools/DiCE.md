---
title: 'DiCE: Diverse Counterfactual Explanations'
values: ['explainability']
categories: ['model-agnostic', 'model-specific']
stages: ['post-hoc']
licence: 'MIT'
repo: https://github.com/interpretml/DiCE
languages: ['Python']
tasks: ['classification', 'regression']
data: ['tabular']
explanations: ['example-based', 'counterfactual']
references: 
- 
    name: 'Mothilal et al. - Explaining Machine Learning Classifiers through Diverse Counterfactual Explanations'
    url: 'https://arxiv.org/abs/1905.07697'
-
    name: 'Mahajan et al. - Preserving Causal Constraints in Counterfactual Explanations for Machine Learning Classifiers'
    url: 'https://arxiv.org/abs/1912.03277'
- 
    name: 'Wachter et al. - Counterfactual Explanations without Opening the Black Box: Automated Decisions and the GDPR'
    url: 'https://arxiv.org/abs/1711.00399'
---

From README:

> DiCE implements counterfactual (CF) explanations that provide this information by showing feature-perturbed versions of the same person who would have received the loan, e.g., you would have received the loan if your income was higher by \$10,000. In other words, it provides "what-if" explanations for model output and can be a useful complement to other explanation methods, both for end-users and model developers.

A main innovation of `DiCE` is that it implements a method to make producing counter-factual examples more model-agnostic:

> Barring simple linear models, however, it is difficult to generate CF examples that work for any machine learning model. DiCE is based on recent research that generates CF explanations for any ML model. The core idea is to setup finding such explanations as an optimization problem, similar to finding adversarial examples.

`DiCe` supports various {{< category "model-agnostic" >}} methods to find counterfactual examples.

- Randomized sampling
- KD-tree algorithm
- Genetic algorithm

Additionally, *gradient-based methods* are provided for *differentiable* models (e.g. a neural network).

- Loss-based method from Mothilal et al. (2020)
- Method based on a variational auto-encoder, Mahajan et al. (2019)

An interesting detail is that DiCE does not necessarily need access to the full data set, so it is possible to generate counterfactuals while keeping the data private.


