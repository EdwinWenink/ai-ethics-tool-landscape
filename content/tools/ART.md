---
title: 'ART: Adversial Robustness 360 Toolbox'
values: ['safety']
categories: ['model-specific', 'model-agnostic']
stages: ['preprocessing', 'learning', 'evaluation', 'prediction' , 'post-hoc']
licence: 'MIT'
repo: https://github.com/Trusted-AI/adversarial-robustness-toolbox 
languages: ['Python']
references: 
-
    name: 'Nicolae et al. - Adversarial Robustness Toolbox v1.0.0'
    url: 'https://arxiv.org/abs/1807.01069'
---

The Adversial Robustness Toolbox (ART) is the first comprehensive toolbox that unifies many defensive techniques for four categories of adversial attacks on machine learning models.
These categories are model evasion, model poisoning, model extraction and inference (e.g. inference of sensitive attributes in the training data; or determining whether an example was part of the training data).
ART supports all popular machine learning frameworks, all data types and all machine learning tasks.

![Adversial machine learning attacks](https://raw.githubusercontent.com/Trusted-AI/adversarial-robustness-toolbox/main/docs/images/adversarial_threats_attacker.png)

The documentation of ART is excellent because a whole wiki is hosted on the github repository. 
On the github repostory you can find an extensive explanation of the different categories of [attacks](https://github.com/Trusted-AI/adversarial-robustness-toolbox/wiki/ART-Attacks) with paper references for many concrete attacks.
Many of these attacks are also implemented in ART.
An overview of [defences](https://github.com/Trusted-AI/adversarial-robustness-toolbox/wiki/ART-Defences) is also provided.
Some attacks assume white box models, whereas others assume black box models.
The toolbox addresses both model-specific and model-agnostic techniques.

Additionally, ART provides tools (such as metrics) to [evaluate](https://github.com/Trusted-AI/adversarial-robustness-toolbox/wiki/ART-Metrics) the robustness of machine learning methods and applications.

With all techniques combined, ART provides offensive and defensive techniques for each stage of the machine learning pipeline.

