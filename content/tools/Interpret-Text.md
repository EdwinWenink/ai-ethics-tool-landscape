---
title: 'Interpret-Text'
values: ['explainability']
categories: ['model-specific']
stages: ['learning', 'post-hoc']
licence: 'MIT'
repo: https://github.com/interpretml/interpret-text
languages: ['Python']
models: ['BERT', 'RNN']
---

Interpret-Text is an extension of {{< tool "InterpretML" >}}, specifically for several text models.
Three modules are provided: `ClassicalTextExplainer`, `UnifiedInformationExplainer` and `IntrospectiveRationaleExplainer`.

## Classical Text Explainer

The `ClassicalTextExplainer` supports linear models from `sklearn` with a `coefs_` call and tree-based models for which `feature_importances_` is defined.

`ClassicalTextExplainer` includes a NLP pipeline from preprocessing to hyperparameter tuning, so it accepts raw text data as input.
The default pipeline uses a unigram bag-of-words model.
Elements of the pipeline can be replaced if desired.

The explainability of this model relies on the input models being interpretable (in particular that their weights are meaningful):

> The family of linear models such as logistic regression and ensemble methods like random forests can be considered to be under the umbrella of glass-box explainers (...) the ClassicalTextExplainer leverages this inherent explainability by exposing weights and importances over encoded tokens as explanations over each word in a document.

Note however that even though ensembles of trees in `sklearn` implement `feature_importances_`, and contrary to what is stated here, ensembles of trees (e.g. gradient boosting trees) are generally actually not considered to be interpretable (due to the sheer size of the model and the amount of trees and splits).

This module is also reported to work with gradient boosting libraries with a similar API layout, such as `LightGBM`.

## Unified Information Explainer

Currently only a trained `BERT` model is accepted as input.

From README:

> The UnifiedInformationExplainer uses an information-based measure to provide unified and coherent explanations on the intermediate layers of deep NLP models. While this model can explain various deep NLP models, we only implement text interpretability for BERT here.

## Introspective Rationale Explainer

Supports `BERT` and `RNN` models.

From README:

> The IntrospectiveRationaleExplainer uses a generator-predictor framework to produce a comprehensive subset of text input features or rationales that are relevant for the classification task. This introspective model predicts the labels and incorporates the outcome into the rationale selection process. The outcome is a hard or soft selection of rationales (words that have useful information for the classification task) and anti-rationales (words that do not appear to have useful information).

