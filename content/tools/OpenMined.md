---
title: 'OpenMined (PySyft)'
values: ['privacy', 'security']
categories: ['model-specific']
tasks: ['classification', 'regression', 'NLP']
data: ['tabular', 'image', 'text']
stages: ['in-processing']
licence: 'Apache License 2.0'
repo: 'https://github.com/OpenMined'
languages: ['Python']
frameworks: ['TensorFlow', 'Keras', 'PyTorch']
references: 
- 
    name: 'OpenMined'
    url: 'https://www.openmined.org/'
-
    name: 'Video resources'
    url: 'https://www.youtube.com/c/OpenMinedOrg'
---

The OpenMined community is a collaboration of several organizations, including TensorFlow, PyTorch and Keras, to create an open-source ecosystem of privacy tools that extend libraries such as PyTorch with cryptographic techniques and differential privacy.
The aim is to contribute to the adaptation of *privacy-preserving AI*. 

To this end, OpenMined offers several privacy-preserving tools on their [github](https://github.com/OpenMined). 
A main tool is [PySyft](https://github.com/OpenMined/PySyft), which allows "computing on data you do not own and cannot see".

The [main website of OpenMined](https://www.openmined.org/) categorizes their efforts towards private AI as such:

- **Remote execution**: Extensions to PyTorch and Tensorflow to support execution on remote machines you don't have access to
    * *Federated learning*: send models to several remote machines that have (part of) the training data and train locally on them, without the need to download sensitive training data
    * *On-device prediction*: run model inference locally on devices without the need to have the dataset e.g. in the cloud
- **Encrypted computation**: the previous steps keeps training data secure, but it is also possible to keep computations themselves secure.
    * *Multi-party computation*: ensure that several parties together can train a model, but no single party can see the model contents, or use or train it by themselves.  
    * *Homomorphic encryption*: a single model owner can use homomorphic encryption to allow untrusted 3rd parties to use or train the model, without being able to steal the model.
- **Differential Privacy**: determine the right amount of obfuscation based on how much information is leaked for example when revealing the predictions of a trained model. 
    * Several published techniques are provided
    * *Automatic DP*: support for automatically determining an appropriate amount of obfuscation, based on the operations you use.

From January 2021 on, OpenMined also publishes free courses on private AI and the tools they offer.
