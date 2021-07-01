---
title: 'TensorFlow Privacy'
values: ['privacy']
categories: ['model-specific']
tasks: ['classification', 'regression', 'NLP']
data: ['image', 'tabular', 'text']
stages: ['learning']
licence: 'Apache License 2.0' 
repo: https://github.com/tensorflow/privacy
languages: ['Python']
references:
-
    name: 'McMahan et al. - A General Approach to Adding Differential Privacy to Iterative Training Procedures'
    url: 'https://arxiv.org/abs/1812.06210'
-   
    name: 'Introducing TensorFlow Privacy: Learning with Differential Privacy for Training Data'
    url: 'https://blog.tensorflow.org/2019/03/introducing-tensorflow-privacy-learning.html'
---

TensorFlow Privacy is a library that allows you to replace default TensorFlow optimizers with optimizers that allow {{< stage "learning" >}} with differential privacy, i.e. they implement forms of stochastic gradient descent (SGD) with differential privacy.

Because large neural networks or other differentiable models have a very large learning capacity, it can happen that the model achieves high performance on uncommon training input by simply "memorizing" the training input.
If the training data is sensitive, for example information about a specific user, this is undesired behavior that may leak private information.
The optimizers of TensorFlow Privacy address this issue and additionally provide analysis tools to mathematically determine privacy guarantees.
Notes on ["measuring" privacy](https://github.com/tensorflow/privacy/tree/aster/tutorials#measuring-privacy) in TensorFlow Privacy can be found [here](https://github.com/tensorflow/privacy/tree/aster/tutorials#measuring-privacy).

Because this library focuses on optimizers, it is possible to get started with TensorFlow Privacy by just dropping in the modified optimizers in existing TensorFlow code.
At the moment of writing, it seems that detailed documentation on the API is not published yet, so you have to dive into the doc strings in the code.
The supported optimizers can be found [here](https://github.com/tensorflow/privacy/tree/master/tensorflow_privacy/privacy/optimizers).

The referenced paper is a technical white paper explaining the foundations of Tensorflow Privacy.
TensorFlow Privacy works with TensorFlow 2
