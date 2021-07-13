---
title: 'DeepExplain'
values: ['explainability']
explanations: ['gradient-based', 'perturbation', 'Shapley value']
categories: ['model-specific']
tasks: ['classification', 'segmentation']
data: ['image', 'text']
stages: ['post-processing']
licence: 'MIT'
repo: https://github.com/marcoancona/DeepExplain
languages: ['Python']
references: 
- 
    name: 'Simonyan et al. - Deep Inside Convolutional Networks: Visualising Image Classification Models and Saliency Maps'
    url: 'https://arxiv.org/abs/1312.6034'
- 
    name: 'Shrikumar et al. - Learning Important Features Through Propagating Activation Differences'
    url: 'https://arxiv.org/abs/1704.02685'
- 
    name: 'Sundararajan et al. - Gradients of Counterfactuals'
    url: 'https://arxiv.org/abs/1611.02639'
- 
    name: 'Sundararajan et al. - Axiomatic Attribution for Deep Networks'
    url: 'https://arxiv.org/abs/1703.01365'
- 
    name: 'Bach - On Pixel-Wise Explanations for Non-Linear Classifier Decisions by Layer-Wise Relevance Propagation'
    url: 'https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0130140'
- 
    name: 'Castro et al. - Polynomial calculation of the Shapley value based on sampling'
    url: 'https://www-sciencedirect-com.ru.idm.oclc.org/science/article/pii/S0305054808000804'
-
    name: 'Zeiler et al. - Visualizing and Understanding Convolutional Networks'
    url: 'https://arxiv.org/abs/1311.2901'
---

The `DeepExplain` Python package for TensorFlow models and Keras models with TensorFlow backend offers two types of interpretability methods for deep convolutional neural networks: gradient-based methods and perturbation-based methods.
This package does not seem to be very actively maintained anymore and support for TensorFlow V2 is limited.

## Attributions

The README gives the following clear and succinct explanation of what an "attribution" is.
All methods included in this approach allow visualization of how each input feature contributes to the final prediction, in terms of what a particular targeted neuron "sees":

> Consider a network and a specific input to this network (eg. an image, if the network is trained for image classification). The input is multi-dimensional, made of several features. In the case of images, each pixel can be considered a feature. The goal of an attribution method is to determine a real value R(x_i) for each input feature, with respect to a target neuron of interest (for example, the activation of the neuron corresponsing to the correct class).
>
> When the attributions of all input features are arranged together to have the same shape of the input sample we talk about attribution maps (as in the picture below), where red and blue colors indicate respectively features that contribute positively to the activation of the target output and features having a suppressing effect on it. 

## Included approaches

The README of the package provide an excellent guide on [which method to use](https://github.com/marcoancona/DeepExplain#which-method-to-use), with the pros and cons of each approach, as well as notes on the relevant parameters to set and in which context the method is appropriate.

### Gradient-based interpretability methods

- Saliency maps (see Simonyan et al.)
- Gradient * input (see Shrikumar et al. )
- Integrated gradients ( see the two papers from Sundararajan et al. )
- A {{< tool "DeepLIFT" >}} implementation that only implements the "Rescale rule" of the original implementation 
    * The original implementation later added an additional "RevealCancel" rule.
- Pixel-wise explanations by layer-wise relevance propagation (e-LRP, see Bach et al.)

DeepLIFT and pixel-wise explanations using LRP *override* gradient operators, i.e. they use a modified chain-rule.
This is thus a notable difference with the original {{< tool "DeepLIFT" >}} implementation.

### Perturbation-based interpretability methods

- Occlusion (extension of the method explained by Zeiler et al. )
- Shapley value sampling (see Castro et al.)
    * Cf. {{< tool "SHAP" >}}, where insights from this project have been integrated in the `DeepExplainer`.

