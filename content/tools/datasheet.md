---
title: 'Datasheets for Datasets'
values: ['accountability']
categories: ['model-agnostic']
stages: ['design phase', 'preprocessing']
references: 
- 
    name: 'Gebru et al. - Datasheets for Datasets'
    url: 'https://arxiv.org/abs/1803.09010v7'
---

The method described in this paper aids in documenting datasets to help avoid unwanted consequences of data usage.

Abstract:

> The machine learning community currently has no standardized process for documenting datasets, which can lead to severe consequences in high-stakes domains. To address this gap, we propose datasheets for datasets. In the electronics industry, every component, no matter how simple or complex, is accompanied with a datasheet that describes its operating characteristics, test results, recommended uses, and other information. By analogy, we propose that every dataset be accompanied with a datasheet that documents its motivation, composition, collection process, recommended uses, and so on. Datasheets for datasets will facilitate better communication between dataset creators and dataset consumers, and encourage the machine learning community to prioritize transparency and accountability. 

The paper provides several questions and workflows to help describe the

1) motivation
2) composition
3) collection process
4) preprocessing
5) use cases
6) distribution
7) maintenance ...

... of the dataset.

A {{< tool "model card" >}} is a similar idea but then applied to machine learning models.
