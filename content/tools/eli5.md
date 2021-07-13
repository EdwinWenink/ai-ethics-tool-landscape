---
title: 'ELI5'
values: ['explainability']
explanations: ['white box', 'gradient-based', 'local surrogate', 'perturbation']
categories: ['model-specific', 'model-agnostic']
tasks: ['classification', 'NLP']
data: ['tabular', 'text', 'image']
stages: ['in-processing', 'post-processing']
licence: 'MIT'
repo: https://github.com/TeamHG-Memex/eli5
languages: ['Python']
references: 
---

ELI5 provides model-specific support for models from `scikit-learn`, `lightning`, decision tree ensembles using the `xgboost`, `LightGBM`, `CatBoost` libraries.
ELI5 mainly provides convenient wrappers to couple the feature importance coefficients that these libraries already provide with feature names, as well as convenient ways to visualize importances, e.g. by highlighting words in a text.
For Keras image classifiers an implementation of the gradient-based Grad-CAM visualizations is offered, but the TensorFlow V2 backend is not supported.

Additionally, two model agnostic approaches are provided that work for black box models.
The `TextExplainer` class offers an implementation of {{< tool "LIME" >}}, specifically tailored towards text classifiers (which is slightly counter-intuitive, since LIME is a model-agnostic approach).
The `PermutationImportance` computes attribute based permutation importance as the "Mean Decrease Accuracy (MDA)".
