---
title: 'Alibi'
values: ['explainability']
explanations: ['global surrogate', 'local surrogate', 'example-based', 'Shapley value', 'anchor', 'contrastive', 'counterfactual', 'ALE', 'gradient-based']
categories: ['model-specific', 'model-agnostic']
tasks: ['classification', 'regression']
data: ['image', 'text', 'tabular' ]
stages: ['post-processing']
licence: 'Apache License 2.0'
repo: 'https://github.com/SeldonIO/alibi'
languages: ['Python']
---

Alibi is an open-source Python library that supports various interpretability techniques and a broad array of explanation types. 
The README already provides an overview of the supported methods and when they are applicable. 
The following table with supported methods is copied from the [README](https://github.com/SeldonIO/alibi/blob/master/README.md) (slightly abbreviated):

### Supported methods

|Method|Models|Explanations|Classification|Regression|Tabular|Text|Images|Categorical features|
|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|[ALE](https://docs.seldon.io/projects/alibi/en/latest/methods/ALE.html)|BB|global|✔|✔|✔| | | |
|[Anchors](https://docs.seldon.io/projects/alibi/en/latest/methods/Anchors.html)|BB|local|✔| |✔|✔|✔|✔|
|[CEM](https://docs.seldon.io/projects/alibi/en/latest/methods/CEM.html)|BB* TF/Keras|local|✔| |✔| |✔| 
|[Counterfactuals](https://docs.seldon.io/projects/alibi/en/latest/methods/CF.html)|BB* TF/Keras|local|✔| |✔| |✔| |
|[Prototype Counterfactuals](https://docs.seldon.io/projects/alibi/en/latest/methods/CFProto.html)|BB* TF/Keras|local|✔| |✔| |✔|✔|
|[Integrated Gradients](https://docs.seldon.io/projects/alibi/en/latest/methods/IntegratedGradients.html)|TF/Keras|local|✔|✔|✔|✔|✔|✔|
|[Kernel SHAP](https://docs.seldon.io/projects/alibi/en/latest/methods/KernelSHAP.html)|BB|local <br></br>global|✔|✔|✔| | |✔|
|[Tree SHAP](https://docs.seldon.io/projects/alibi/en/latest/methods/TreeSHAP.html)|WB|local <br></br>global|✔|✔|✔| | |✔|

The README also explains the keys:

- BB - black-box (only require a prediction function)
- BB* - black-box but assume model is differentiable
- WB - requires white-box model access. There may be limitations on models supported
- TF/Keras - TensorFlow models via the Keras API
- Local - instance specific explanation, why was this prediction made?
- Global - explains the model with respect to a set of instances

For more detailed information on the supported methods, see the [algorithm overview](https://docs.seldon.io/projects/alibi/en/latest/overview/algorithms.html).
