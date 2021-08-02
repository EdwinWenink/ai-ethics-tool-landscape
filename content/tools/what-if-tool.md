---
title: 'What-If Tool'
values: ['fairness' , 'explainability']
explanations: ['Shapley value', 'gradient-based', 'counterfactual', 'partial dependence plot']
fairness: ['individual fairness', 'group fairness']
categories: ['model-agnostic']
tasks: ['classification', 'regression']
data: ['tabular', 'image', 'text']
stages: ['post-processing']
licence: 'Apache'
repo: https://github.com/pair-code/what-if-tool
languages: ['Python']
references: 
- 
    name: 'Explanation of supported fairness metrics'
    url: 'https://pair-code.github.io/what-if-tool/ai-fairness.html'
- 
    name: 'Demo site'
    url: 'https://pair-code.github.io/what-if-tool/index.html#demos'
---

The What-If Tool (WIT) takes a pretrained model and then allows you to visualize the effect of changing e.g. classification thresholds or the data points themselves on performance, explainability and fairness metrics.

Many convenient functions for gaining insight in the data set are provided, such as binning on particular features, attribution values, or inference scores, computing partial dependence plots, and typical performance indicators such as a confusion matrix or ROC curve.

Because you can interactively edit the data set or prediction thresholds, you can also answer "what if" questions, which goes beyond typical interactive visualization. 
For example, what happens to the demographic parity fairness metric when I adjust the classification threshold?
And how do the Shapley value for the features change?

The What-If Tool works with python-accessible models in a notebook, and works with most models hosted by TF-serving in Tensorboard.

## Explainability

In terms of explainability, WIT hooks into existing feature attribution methods like {{< tool "SHAP" >}} and {{< tool "LIME" >}} when used in notebook mode.

The following [demo](https://colab.research.google.com/github/PAIR-code/what-if-tool/blob/master/WIT_COMPAS_with_SHAP.ipynb#scrollTo=KF00pJvkeicT) shows how to use Shapley values in WIT.
As the title of the tool already suggests, WIT also computes the {{< explanation "counterfactual" >}}  for any data point given some distance metric (potentially a custom metric).

## Fairness

Supported fairness metrics:

- Group unaware / individual fairness
- Group threshold (adjust classification threshold per group to compensate for historical bias against that group)
- Demographic parity
- Equal opportunity
- Equal accuracy

For binary classification models you can use fairness optimization strategies.
