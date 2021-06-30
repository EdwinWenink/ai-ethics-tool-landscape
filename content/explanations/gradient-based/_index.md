---
title: Gradient-based explanations
---

Gradient-based explanation methods use gradients (e.g. in deep neural networks) to evaluate the contribution of a model component on the model output. 
Some methods use gradients for evaluating the contribution of input features on the output, but others instead show the influence of a single (hidden) neuron on the output, or instead the influence of an input feature on a particular neuron's activation value.

In the case of computer vision (where deep convolutional neural networks are heavily used), one can show gradient-based information as a *salience map*.
