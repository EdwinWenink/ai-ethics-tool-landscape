---
title: 'Foolbox'
values: ['security']
categories: ['model-specific']
tasks: ['classification']
data: ['image']
stages: ['post-processing']
licence: 'MIT'
repo: https://github.com/bethgelab/foolbox
languages: ['Python']
frameworks: ['PyTorch', 'TensorFlow', 'JAX', 'numpy']
---

`Foolbox` is a comprehensive adversarial library for attacking machine learning models, with a focus on neural networks in computer vision.
At the moment of writing FoolBox contains 41 gradient-based and decision-based [adversarial attacks](https://foolbox.readthedocs.io/en/stable/modules/attacks.html), making it the second biggest adversial library after {{< tool "ART" >}}.
A notable difference with ART is that Foolbox only contains attacks, but no defenses and evaluation metrics.

The library is very user-friendly, with a clear API and documentation.
Foolbox has dedicated classes to wrap around `PyTorch`, `TensorFlow` and `JAX` models, e.g. `fb.PyTorchModel(model, bounds=bounds, preprocessing=preprocessing)` where `model` is a `PyTorch` model.
The `FoolBox` model can then be passed into an attack of choice.
This clear API makes it possible to easily experiment with many adversarial attacks.

Have a look at the well-written [guide](https://foolbox.jonasrauber.de/guide/).
For practical examples, have a look at the [tutorial notebook](https://github.com/jonasrauber/foolbox-native-tutorial/blob/master/foolbox-native-tutorial.ipynb) as well as the [example scripts](https://github.com/bethgelab/foolbox/tree/master/examples) listed on Github.

Implementation-wise `Foolbox` is built on [`EagerPy`](https://eagerpy.jonasrauber.de/) which allows Python code to run natively in the supported frameworks, e.g. in PyTorch.
I take this to mean that Foolbox will not support libraries unless they are supported by `EagerPy` as well.
Foolbox also comes with extensive type annotations, i.e. the library is up to speed with the latest Python 3 conventions.


