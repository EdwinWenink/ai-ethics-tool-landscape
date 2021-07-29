---
title: 'CleverHans'
values: ['security']
categories: ['model-specific']
tasks: ['classification']
data: ['image']
stages: ['in-processing','post-processing']
licence: 'MIT'
repo: 'https://github.com/cleverhans-lab/cleverhans'
languages: ['Python']
frameworks: ['JAX', 'PyTorch', 'TensorFlow']
---

`CleverHans` is a Python library with the main purpose of providing good reference implementations of attacks for benchmarking machine learning models against adversarial examples. 
The main maintainers of this library are Ian Goodfellow and Nicolas Papernot.
Attacks (i.e. methods for generating adversarial examples) are listed under [`/cleverhans`](https://github.com/cleverhans-lab/cleverhans/tree/master/cleverhans) and each of the supported frameworks has its own folder with attack implementations.
`CleverHans` also aims to implement a set of defenses, but this is currently work in progress (currently there is only a defense implementation for `PyTorch`).

In the latest version of `CleverHans`, both `TensorFlow 1` and `Python 2` are no longer supported.
To me it seems that not all content from `v3.1.0` is ported yet to the latest version of `CleverHans (v4.0.0)`, which for example may explain the mostly empty `/defenses` folder.
However, `v4.0.0` was only released 5 days prior to the writing of this text.
According to the README the current focus is on implementing attacks in `PyTorch`.

The supported frameworks in v4 are `JAX`, `PyTorch` and `TensorFlow 2` (legacy implementations for `TensorFlow 1` and `Python 2` are still available under `cleverhans_v3.1.0`).

Tutorials on `Cifar10` and `MNIST` are available alongside a wide array of example use-cases of the library.
