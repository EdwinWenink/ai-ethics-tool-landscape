---
title: 'Captum'
values: ['explainability']
explanations: ['gradient-based', 'Shapley value']
categories: ['model-specific']
tasks: ['classification', 'segmentation', 'regression']
data: ['tabular', 'image']
stages: ['in-processing', 'post-processing']
licence: 'BSD-3'
repo: https://github.com/pytorch/captum
languages: ['Python']
references: 
- 
    name:  'captum.ai'
    url: 'https://captum.ai/docs/algorithms_comparison_matrix'
---

Captum is a model interpretability library specifically `PyTorch`.
It is actively maintained at the moment of writing and supports an extensive array of interpretability methods.

The Captum website also offers a large range of [hands-on tutorials](https://captum.ai/tutorials/) for various use cases.

## Supported interpretability methods

`Captum` supports a very extensive list of interpretability algorithms.
All paper references for each of the supported methods are [listed in the README](https://github.com/pytorch/captum#references-of-algorithms), so they will not be repeated here.

Have a look at this nice [algorithms comparison matrix](https://captum.ai/docs/algorithms_comparison_matrix) offered on the [captum.ai](captum.ai) website.
All supported algorithms are [described here](https://captum.ai/docs/algorithms).

It is good to note that many of these algorithms have multiple variants, as also explained in the [algorithm explanations](https://captum.ai/docs/algorithms):

- Primary Attribution: Evaluates contribution of each input feature to the output of a model.
- Layer Attribution: Evaluates contribution of each neuron in a given layer to the output of the model.
- Neuron Attribution: Evaluates contribution of each input feature on the activation of a particular hidden neuron.

A nice touch is that some methods provide a "convergence delta" argument which quantifies the approximation error for a single input sample.

Supported interpretability algorithms:

- `IntegratedGradients`, `LayerIntegratedGardients`
- `InputXGradient`
- `SmoothGrad`
- `NoiseTunnel`
- `NeuronConductance`
- `LayerConductance`
- `DeepLift`, `NeuronDeepLift`, `LayerDeepLift`
- `NeuronIntegratedGradients`
- `GradientShap`, `NeuronGradientShap`, `LayerGradientShap`, `DeepLiftShap`, `NeuronDeepLiftShap`, `LayerDeepLiftShap`
- `InternalInfluence`
- `Saliency`, `NeuronGradient`
- `GradCAM`, `Guided GradCAM`
- `Deconvolution`, `Neuron Deconvolution`
- `Guided Backpropagation`, `Neuron Guided Backpropagation`
- `Feature Permutation`
- `Occlusion` 
- `Shapley Value`
- `Infidelity and Sensitivity`

## Insights interface

A nice web interface is also provided to apply and visualize the offered interpretability algorithms.
For an example, run:

```
python -m captum.insights.example
```

`Insights` requires `Node >= 8x` and `Yarn >= 1.5`.
