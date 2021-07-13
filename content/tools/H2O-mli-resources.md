---
title: 'H2O MLI Resources'
values: ['explainability']
explanations: ['local surrogate', 'global surrogate', 'partial dependence plot', 'ICE plot', 'shapley value', 'sensitivity analysis']
fairness: []
categories: ['model-agnostic']
tasks: ['classification']
data: ['tabular']
stages: ['in-processing', 'post-processing']
repo: 'https://github.com/h2oai/mli-resources'
languages: ['Python']
references: 
- 
    name: 'H2O.ai'
    url: 'https://www.h2o.ai/'
- 
    name: 'H2O documentation (Python)'
    url: 'https://docs.h2o.ai/h2o/latest-stable/h2o-py/docs/index.html'
---

This repository by H2O.ai contains useful resources and notebooks that showcase well-known machine learning interpretability techniques. 
The examples use the `h2o` Python package with their own estimators (e.g. their own fork of XGBoost), but all code is open-source and the examples are still illustrative of the interpretability techniques.
These case studies that also deal with practical coding issues and preprocessing steps, e.g. that LIME can be unstable when there are strong correlations between input variables.
In particular, there are helpful examples for:

- Global Surrogate Models (example with Decision Tree Surrogate) [[notebook]](https://github.com/h2oai/mli-resources/blob/master/notebooks/dt_surrogate.ipynb)
- XGBoost with monotonic constraints [[notebook]](https://github.com/h2oai/mli-resources/blob/master/notebooks/mono_xgboost.ipynb)
- Local Interpretable Model Agnostic Explanations (LIME) [[notebook]](https://github.com/h2oai/mli-resources/blob/master/notebooks/lime.ipynb)
    * cf. {{< tool "LIME" >}} 
- Local Feature Importance and Reason Codes using LOCO [[notebook]](https://github.com/h2oai/mli-resources/blob/master/notebooks/loco.ipynb)
- Partial Dependence and ICE Plots [[notebook]](https://github.com/h2oai/mli-resources/blob/master/notebooks/pdp_ice.ipynb)
- Sensitivity Analysis [[notebook]](https://github.com/h2oai/mli-resources/blob/master/notebooks/sensitivity_analysis.ipynb)

There is no license provided in the repository, just a request to cite original paper authors and the H20.ai machine learning interpretability team where appropriate.

The repository also contains the following interpretability cheatsheet:

![Cheatsheet](https://raw.githubusercontent.com/h2oai/mli-resources/master/cheatsheet.png)
