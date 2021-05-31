---
title: 'SHAP: SHapley Additive exPlanations'
values: ['explainability']
explanations: ['local surrogate', 'Shapley value', 'salience', 'partial_dependence_plot', 'white box']
categories: ['model-agnostic', 'model-specific']
tasks: ['classification']
data: ['tabular', 'image', 'text']
stages: ['post-hoc']
licence: 'MIT'
repo: https://github.com/slundberg/shap
languages: ['Python']
references: 
- 
    name: 'Lundberg et al. 2017 - A Unified Approach to Interpreting Model Predictions'
    url: 'https://proceedings.neurips.cc/paper/2017/hash/8a20a8621978632d76c43dfd28b67767-Abstract.html'
- 
    name: 'Lundberg et al. 2020 - From local explanations to global understanding with explainable AI for trees'
    url: 'https://www.nature.com/articles/s42256-019-0138-9'
- 
    name: 'Shrikumar et al. 2019 - Learning Important Features Through Propagating Activation Differences'
    url: 'https://arxiv.org/abs/1704.02685'
- 
    name: 'Smilkov et al. 2017 - SmoothGrad: removing noise by adding noise'
    url: 'https://arxiv.org/abs/1706.03825'
- 
    name: 'Sundararajan et al. 2017 - Axiomatic Attribution for Deep Networks'
    url: 'https://arxiv.org/abs/1703.01365'
---

<!-- TODO is this indeed local surrogate ? -->

<!-- TODO What is a Shapley value? -->

The SHAP package is built on the concept of a {{< explanation "Shapley value" >}} and can generate explanations model-agnostically.
So it only requires input and output values, not model internals:

> SHAP (SHapley Additive exPlanations) is a game theoretic approach to explain the output of any machine learning model. It connects optimal credit allocation with local explanations using the classic Shapley values from game theory and their related extensions. (README)

## Model-specific optimizations

Additionally, this package also contains several model-specific implementations of Shapley values that are optimized for a particular machine learning model and sometimes even for a particular library.

### Ensembles of trees

There is specific support for tree (ensemble) models from `XGBoost`, `LightGBM`, `CatBoost`, `scikit-learn`, `pyspark`.
These models can be passed directly into the `shap.Explainer`.
This particular implementation can compute Shapley values exactly.

The `shap.TreeExplainer` can also compute SHAP interaction values for pairwise interactions between features.

`shap.TreeExplainer(model).shap_interaction_values(X)`.


### Natural Language models

You can generate Shapley values for a NLP transformer pipeline (e.g. one from [Hugging Face](https://huggingface.co/)) by passing the whole pipeline into the default `shap.Explainer`.

### Deep Neural Networks

A `shap.DeepExplainer` is provided specifically for deep learning models and is an extension of *DeepLIFT* (see Shrikumar et al., 2018).

- Support for TensorFlow/Keras and PyTorch (preliminary support at the moment of writing).
- "DeepLIFT compares the activation of each neuron to its 'reference activation' and assigns contribution scores according to the difference. By optionally giving separate consideration to positive and negative contributions, DeepLIFT can also reveal dependencies which are missed by other approaches." (Shrikumar et al., 2017)

### Gradient-based explanations

`shap.GradientExplainer`

Gradient-based methods can also be used to explain the effect of (intermediate) deep learning layers on the network's output.
For example for an input image, you can visualize which pixels in a feature map increase the probability of a particular class and which ones decrease that probability.

> Expected gradients combines ideas from Integrated Gradients, SHAP, and SmoothGrad into a single expected value equation. This allows an entire dataset to be used as the background distribution (as opposed to a single reference value) and allows local smoothing. If we approximate the model with a linear function between each background data sample and the current input to be explained, and we assume the input features are independent then expected gradients will compute approximate SHAP values. (README)


### Model-agnostic explanations

`shap.KernelExplainer`

> Kernel SHAP uses a specially-weighted local linear regression to estimate SHAP values for any model. (README)

The Shapley values indicate a positive or negative push away from the average model output over the whole training dataset.
