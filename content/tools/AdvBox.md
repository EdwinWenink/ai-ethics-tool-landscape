---
title: 'AdvBox'
values: ['security']
categories: ['model-specific']
tasks: ['classification']
data: ['image']
stages: ['in-processing', 'post-processing']
licence: 'Apache License 2.0'
repo: https://github.com/advboxes/AdvBox/blob/master/adversarialbox.md
languages: ['Python']
frameworks: ['PaddlePaddle', 'PyTorch', 'Caffe2', 'MxNet', 'Keras', 'TensorFlow']
references: 
- 
    name: 'Adversial Box Homepage'
    url: 'https://github.com/advboxes/AdvBox/blob/master/adversarialbox.md'
---

`Advbox` offers a number of AI model security toolkits. 
[`AdversialBox`](https://github.com/advboxes/AdvBox/tree/master/adversarialbox) allows zero-coding generation of adversial examples for a wide range of neural network frameworks. 
An overview of the supported attacks and defenses can be found [here](https://github.com/advboxes/AdvBox/blob/master/adversarialbox.md#supported-attack-and-defense-methods) and the corresponding code [here](https://github.com/advboxes/AdvBox/tree/master/adversarialbox).
It requires some effort to find all attacks mentioned on the homepage in the code base.

Generally speaking, the documentation of `AdvBox` is incomplete and not very user-friendly.
[`ODD: Object Detector Deception`](https://github.com/advboxes/AdvBox/tree/master/advbox_family/ODD) showcases a specific attack for object detection networks such as YOLO, but is not mentioned in the README.
`AdvDetect` *is* named in the README, but it's not clear if and how it differs from `ODD`. 
The "homepage" for `AdvDetect` is an empty markdown file at the moment of writing.
[`AdvPoison`](https://github.com/advboxes/AdvBox/tree/master/DataPoison) contains an example of a data poisoning attack for MNIST, implemented in Paddle and PyTorch.

The repository does contain a [wide range of tutorials](https://github.com/advboxes/AdvBox/tree/master/tutorials).

This library is said to be based on {{< tool "Foolbox" >}} , which is more comprehensive and has proper documentation.
