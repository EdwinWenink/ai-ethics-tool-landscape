---
title: 'Aequitas: Bias and Fairness Audit Toolkit'
values: ['fairness']
fairness: ['group fairness']
categories: ['model-agnostic']
tasks: ['classification']
data: ['tabular']
stages: ['preprocessing', 'post-processing']
licence: 'MIT'
repo: https://github.com/dssg/aequitas
languages: ['Python']
references: 
- 
    name: 'Aequitas project page'
    url: 'http://www.datasciencepublicpolicy.org/projects/aequitas/'
- 
    name: 'Aequitas: Bias and Fairness Audit Toolkit'
    url: 'http://aequitas.dssg.io/'
- 
    name: 'Saleiro et al. - Aequitas: A Bias and Fairness Audit Toolkit'
    url: 'https://arxiv.org/abs/1811.05577'
---

## Audit

The Aequitas toolkit can both be used on the command-line, programmatically via its [Python API](https://github.com/dssg/aequitas#input-data-for-python-api) or via a web interface.
The [web interface](http://aequitas.dssg.io/) offers a four step programme to audit a dataset on bias.
The four steps are:

1. Upload (tabular) data
2. Determine protected groups and reference group
3. Select fairness metrics and disparity intolerance
4. Inspect bias report 
    * [Example audit report](http://aequitas.dssg.io/example.html).

This toolkit is useful for auditing bias and fairness according to a limited set of common fairness metrics, but does not offer algorithms for mitigating bias.
It thus only requires input data and model outputs and does not intervene in the training of the model itself. 

[Further documentation](https://dssg.github.io/aequitas/).

## Fairness metrics

The amount of supported fairness metrics is relatively limited compared to other fairness toolkits.
They are about representatitivess and error rates per group, in this case relative to a reference group.

The following disparities are computed in the web interface:

- Equal Parity
- Proportional Parity
- False Positive Rate Parity
- False Discovery Rate Parity
- False Negative Rate Parity
- False Omission Rate Parity

With the Python API you can compute a few closely interrelated disparaties. 


## Fairness tree

What's particularly nice about this toolkit is the provided {{< tool "fairness tree" >}}, which can also be very helpful in combination with other toolkits.

![Complete Fairness Tree](http://www.datasciencepublicpolicy.org/wp-content/uploads/2021/04/Fairness-Full-Tree-1200x908.png)

![Zoomed in Fairness Tree](http://www.datasciencepublicpolicy.org/wp-content/uploads/2021/04/Fairness-Short-Tree-1200x746.png)

