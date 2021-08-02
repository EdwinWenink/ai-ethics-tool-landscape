---
title: 'AI Explainability 360'
values: ['explainability']
explanations: ['local surrogate', 'global surrogate', 'example-based', 'Shapley value', 'contrastive', 'white box']
categories: ['model-agnostic']
tasks: ['classification', 'regression']
data: ['tabular', 'image', 'text']
stages: ['preprocessing', 'in-processing', 'post-processing']
licence: 'Apache License 2.0'
repo: 'https://github.com/Trusted-AI/AIX360'
languages: ['Python']
frameworks: ['TensorFlow', 'PyTorch', 'scikit-learn']
references: 
-
    name: 'Arya et al. - One Explanation Does Not Fit All: A Toolkit and Taxonomy of AI Explainability Techniques'
    url: 'https://arxiv.org/abs/1909.03012'
-
    name: 'AI Explainability 360 Homepage'
    url: 'https://aix360.mybluemix.net/'
- 
    name: 'Interactive tutorial with different explanations for different audiences'
    url: 'http://aix360.mybluemix.net/data'
---

The AI Explainability 360 (AIX360) toolkit is a Python library that offers a wide range of explanation types as well as some explainability metrics. 
AIX360 offers excellent [guidance material](http://aix360.mybluemix.net/resources#guidance), an [interactive demo](http://aix360.mybluemix.net/data) as well as [developer tutorials](http://aix360.mybluemix.net/resources#tutorials).
What's particularly good about this material is that it stimulates reflection on which type of explanation is appropriate, not only from a technical point of view, but also with respect to the target explainer and explainee.

This library supports the *faithfulness* metric, which tracks whether features that are important according to an explanation method correlate with improved model performance, and *monotonicity*, which tracks that important features indeed increase model performance.

`TensorFlow`, `PyTorch` and `scikit-learn` are supported.

## Supported Algorithms

This library distinguishes two broad categories of explanations: explanations of the dataset and of the model.
The [guidance chart for AI Explainability 360 algorithms](https://github.com/Trusted-AI/AIX360/blob/master/aix360/algorithms/README.md) offers a decision tree for selecting an appropriate algorithm.

For explaining the dataset two methods are supported. `ProtoDash` finds example instances that are prototypical for the dataset. 
`DIPVAE` is a variational autoencoder that learns meaningful latent structures of the dataset.

All other methods are for explaining models and decisions based on model outputs.
Several local (post-hoc) explanations are supported, such as {{< tool "SHAP" >}}, {{< tool "LIME" >}}, contrastive explanation method ({{< tool "CEM" >}}), as well as the {{< explanation "example-based" >}} method `ProtoDash`.
Notice that `ProtoDash` can both be used to represent the dataset in terms of prototypes, as well as for explaining a prediction by providing similar examples with the same outcome decision.
This category includes {{< explanation "local surrogate" >}} models.

`ProfWeight` is a method to train a {{< explanation "global surrogate" >}} model instead.

Three methods offer what AIX360 calls *direct* explanations.
In the taxonomy of this project, this is called a {{< explanation "white box" >}} explanation.
*Boolean Decision Rules via Column Generation* (BRCG) and *Generalized Linear Rule Models* (GLRM) offer a *global* model explanation by generating easy to understand rules for the model outputs. 
A method called *Teaching Explanations for Decisions* (TED) outputs explanations directly alongside predictions, so this is a *local* direct explanation.
