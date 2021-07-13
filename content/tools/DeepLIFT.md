---
title: 'DeepLIFT'
values: ['explainability']
explanations: ['gradient-based']
categories: ['model-specific']
tasks: ['classification', 'segmentation' ]
data: ['image', 'text']
stages: ['in-processing', 'post-processing']
licence: MIT
repo: 'https://github.com/kundajelab/deeplift'
language: ['Python']
frameworks: ['TensorFlow', 'Keras']
references: 
- 
    name: 'Shrikumar et al. - Learning Important Features Through Propagating Activation Differences'
    url: 'https://arxiv.org/abs/1704.02685'
- 
    name: 'Springenberg et al. - Striving for Simplicity: The All Convolutional Net'
    url: 'https://arxiv.org/abs/1412.6806'
- 
    name: 'Sundararajan et al. - Gradients of Counterfactuals'
    url: 'https://arxiv.org/abs/1611.02639'
-
    name: 'Sundararajan et al. - Axiomatic Attribution for Deep Networks'
    url: 'https://arxiv.org/abs/1703.01365'
---

A brief explanation of the {{< explanation "gradient-based" >}} interpretability method called DeepLIFT is given by Shrikumar et al. in the abstract of the linked paper:

> DeepLIFT (Deep Learning Important FeaTures), a method for decomposing the output prediction of a neural network on a specific input by backpropagating the contributions of all neurons in the network to every feature of the input. DeepLIFT compares the activation of each neuron to its 'reference activation' and assigns contribution scores according to the difference. By optionally giving separate consideration to positive and negative contributions, DeepLIFT can also reveal dependencies which are missed by other approaches. Scores can be computed efficiently in a single backward pass.

The linked repository implements the functionality explained in this paper.
Other {{< explanation "gradient-based" >}} interpretation methods are also implemented, including:

- gradient * input (equivalent to Layerwise Relevance Propagation in networks using ReLU; see Shrikumar et al. )
- guided backprop (see Springenberg et al.)
- integrated gradients ( see the two papers from Sundararajan et al. )

DeepLIFT is {{< category "model-specific" >}} because it is designed specifically for deep neural networks, more specifically `Keras` and `TensorFlow` models. 

The first step to applying `DeepLIFT` is to construct a new layer for each layer in the original neural network and specify it's inputs, thereby creating a network that will return importances.
For `Keras` (2.0) models, there is autoconversion functionality as illustrated in the quickstart of the README.

Note that because these layers are extra, existing gradient operators are not overridden.
The application of `DeepLIFT` should thus not affect the predictions of the original network.

<!--TODO: explain difference between the Rescale rule and the RevealCancel rule.-->

A 15-min introduction to DeepLIFT can be found [here](https://vimeo.com/238275076):

{{< vimeo 238275076 >}} 

A more extended tutorial can be found [here](https://www.youtube.com/playlist?list=PLJLjQOkqSRTP3cLB2cOOi_bQFw6KPGKML).

## Other implementations

The `DeepLIFT` package does not support all model types, because not all layers have a `DeepLIFT` equivalent.
In the FAQ the author explains that other packages that directly override gradient operators instead support a broader array of architectures.
Variants of `DeepLIFT` are also implemented in other packages.

- The {{< tool "SHAP" >}} package includes a `DeepExplainer` that extends `DeepLIFT` with the concept of Shapley values. In addition to `TensorFlow` and `Keras` models, this implementation has *preliminary PyTorch* support at the moment of writing.
- {{< tool "DeepExplain" >}} also connects DeepLIFT with Shapley values, and is actually the basis of `SHAP`'s `DeepExplainer`
- {{< tool "Captum" >}} has a `DeepLIFT` implementation for `PyTorch`.

The [FAQ](https://github.com/kundajelab/deeplift#faq) contains an in-depth discussion of differences in functionality between these `DeepLIFT` implementations.
