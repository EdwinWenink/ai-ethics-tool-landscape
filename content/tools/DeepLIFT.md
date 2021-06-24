---
title: 'DeepLIFT'
values: ['explainability']
explanations: ['gradient-based']
categories: ['model-specific']
tasks: ['classification', 'regression']
data: ['image', 'text']
stages: ['prediction']
licence: MIT
repo: 'https://github.com/kundajelab/deeplift'
language: ['Python']
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
---

A brief explanation of the {{< explanation "gradient-based" >}} interpretability method called DeepLIFT is given by Shrikumar et al. in the abstract of the linked paper:

> DeepLIFT (Deep Learning Important FeaTures), a method for decomposing the output prediction of a neural network on a specific input by backpropagating the contributions of all neurons in the network to every feature of the input. DeepLIFT compares the activation of each neuron to its 'reference activation' and assigns contribution scores according to the difference. By optionally giving separate consideration to positive and negative contributions, DeepLIFT can also reveal dependencies which are missed by other approaches. Scores can be computed efficiently in a single backward pass.

The linked repository implements the functionality explained in this paper.
Other {{< explanation "gradient-based" >}} interpretation methods are also implemented, including:

- gradient-times-input (equivalent to Layerwise Relevance Propagation in networks using ReLU)
- guided backprop (see Springenberg et al.)
- integrated gradients ( see Sundararajan et al. )

DeepLIFT is {{< category "model-specific" >}} because it is designed specifically for deep neural networks, more specifically `Keras` and `TensorFlow` models. 

The first step to applying `DeepLIFT` is to construct a new layer for each layer in the original neural network and specify it's inputs, thereby creating a network that will return importances.
For `Keras` (2.0) models, there is autoconversion functionality as illustrated in the quickstart of the README.

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


<!--
### TODO Differences between libraries

DeepExplain (Ancona et al.) or Captum (if you are using pytorch) to see if any of them satisfy your needs. They are implemented by overriding gradient operators and thus support a wider variety of architectures. However, none of these implementations support the RevealCancel rule (which deals with failure modes such as the min function). The pros and cons of DeepSHAP vs DeepExplain are discussed in more detail below. If you would really like to have the RevealCancel rule, go ahead and post a github issue, although my energies are currently focused on other projects and I may not be able to get to it for some time.

Great explanation of other packages!

Both DeepExplain (Ancona et al.) and DeepSHAP/DeepExplainer work by overriding gradient operators, and can thus support a wider variety of architectures than those that are covered in the DeepLIFT repo (in fact, the DeepSHAP/DeepExplainer implementation was inspired by Ancona et al.'s work and builds on a connection between DeepLIFT and SHAP, described in the SHAP paper). For the set of architectures described in the DeepLIFT paper, i.e. linear matrix multiplications, convolutions, and single-input nonlinearities (like ReLUs), both these implementations are identical to DeepLIFT with the Rescale rule. However, neither implementation supports DeepLIFT with the RevealCancel rule (a rule that was developed to deal with failure cases such as the min function, and which unfortunately is not easily implemented by overriding gradient operators). The key differences are as follows:

(1) DeepExplain uses standard gradient backpropagation for elementwise operations (such as those present in LSTMs/GRUs/Attention). This will likely violate the summation-to-delta property (i.e. the property that the sum of the attributions over the input is equal to the difference-from-reference of the output). If you have elementwise operations, I recommend you use DeepSHAP/DeepExplainer, which employs a summation-to-delta-preserving backprop rule. The same is technically true for Maxpooling operations when a non-uniform reference is used (though this has not been a salient problem for us in practice); the DeepSHAP/DeepExplainer implementation guarantees summation-to-delta is satisfied for Maxpooling by assigning credit/blame to either the neuron that is the max in the actual input or the neuron that was the max in the reference (this is different from the 'Max' attribution rule proposed in the SHAP paper; that attribution rule does not scale well).

(2) DeepExplain (by Ancona et al.) does not support the dynamic reference that is demonstrated in the DeepLIFT repo (i.e. the case where a different reference is generated according to the properties of the input example, such as the 'dinucleotide shuffled' references used in genomics). I've implemented the dynamic reference feature for DeepSHAP/DeepExplainer, with an associated example notebook here (warning: the process of generating the dinucleotide shuffled sequences is in many applications the bottleneck for running interpretation; if you are getting poor GPU usage, that may be why; to get around this, it may be a good idea to have a cache of pre-generated shuffled sequences of particular GC content and retrieve examples from the cache according to the GC content of the input sequence).

(3) DeepSHAP/DeepExplainer is implemented such that multiple references can be used for a single example, and the final attributions are averaged over each reference. However, the way this is implemented, each GPU batch calculates attributions for a single example, for all references. This means that the DeepSHAP/DeepExplainer implementation might be slow in cases where you have a large number of samples and only one reference. By contrast, DeepExplain (Ancona et al.) is structured such that the user provides a single reference, and this reference is used for all the examples. Thus, DeepExplain (Ancona et al.) allows GPU batching across examples, but does not allow for GPU batching across different references.

In summary, my recommendations are: use DeepSHAP if you have elementwise operations (e.g. GRUs/LSTMs/Attention), a need for dynamic references, or a large number of references compared to samples. Use DeepExplain when you have a large number of samples compared to references.

What's DeepLIFT
DeepLIFT-RevealCancel
-->
