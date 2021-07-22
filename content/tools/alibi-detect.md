---
title: 'Alibi Detect'
values: ['security', 'fairness']
fairness: ['group fairness']
categories: ['model-agnostic']
tasks: ['classification']
data: ['text', 'image', 'tabular', 'time series']
stages: ['design phase']
licence: 'Apache License 2.0'
repo: https://github.com/SeldonIO/alibi-detect
frameworks: ['TensorFlow', 'PyTorch']
languages: ['Python']
---

*Alibi Detect* is an open source Python library (sister library to {{< tool "Alibi" >}}) focused detecting outliers, adversarial examples, and concept drift.

Finding adversarial examples is relevant for assessing the {{< value "security" >}} of machine learning models.
Machine learning models learn complex statistical patterns in datasets. 
If these statistical patterns "drift" (in unforeseen ways) after a model is deployed, this will decrease the model performance over time.
In systems where model predictions have an impact on people, this may be a threat to the {{< value "fairness" >}} of the predictions.

For each of these detection problems *Alibi Detect* supports a broad array of methods.
The README shows tables with these methods' characteristics, for [outlier detection](https://github.com/SeldonIO/alibi-detect#outlier-detection), [adversarial detection](https://github.com/SeldonIO/alibi-detect#adversarial-detection), and [drift detection](https://github.com/SeldonIO/alibi-detect#drift-detection).
[Paper references](https://github.com/SeldonIO/alibi-detect#reference-list) for all supported methods are also provided.

For drift detection methods, TensorFlow and PyTorch are supported.
