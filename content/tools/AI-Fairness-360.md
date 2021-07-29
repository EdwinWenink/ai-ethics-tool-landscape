---
title: AI Fairness 360
values: ['fairness']
fairness: ['group fairness', 'individual fairness']
categories: ['model-agnostic']
tasks: ['classification', 'regression']
data: ['tabular']
stages: ['preprocessing', 'in-processing', 'Post-processing']
licence: 'Apache license'
repo: https://github.com/Trusted-AI/AIF360
languages: ['Python', 'R']
references: 
- 
    name: 'Bellamny et al. - AI Fairness 360: An Extensible Toolkit for Detecting, Understanding, and Mitigating Unwanted Algorithmic Bias'
    url: 'https://arxiv.org/abs/1810.01943'
---

The IBM AI Fairness 360 Toolkit contains several bias mitigation algorithms that are applicable to various stages of the machine learning pipeline.
The toolkit implements different notions of [fairness](/values/fairness), both on [individual](/fairness/individual-fairness) and the [group](/fairness/group-fairness) level, and several fairness metrics for both classes of fairness.
The toolkit provides additional [guidance on choosing metrics and mitigation algorithms](http://aif360.mybluemix.net/resources#guidance) given a particular goal and application.

The following should be noted when using the fairness toolkit (and other similar toolkits, for that matter):

> The toolkit should only be used in a very limited setting: allocation or risk assessment problems with well-defined protected attributes in which one would like to have some sort of statistical or mathematical notion of sameness. Even then, the code and collateral contained in AIF360 is only a starting point to a broader discussion among multiple stakeholders on overall decision making workflows. [source](http://aif360.mybluemix.net/resources#guidance)

Moreover, the choice for a particular algorithm from the toolkit also depends on assumptions on the equality of people.
Within the group fairness approach, the toolkit distinguishes two different "worldviews" underlying group fairness: the "we're all equal" worldview and the "what you see if what you get worldview". See [group fairness](/fairness/group-fairness) for a further explanation.

To choose an approach, we need to consider 1) the type of fairness to strive for 2) given that type, which fairness metrics/constraints to use (if applicable) 3) where in the pipeline to intervene 4) which algorithm is suitable to support the made choices.

## Choosing fairness metrics

The amount of implemented fairness metrics is very large, so we refer here to the [API](https://aif360.readthedocs.io/en/latest/modules/metrics.html) and summarize the directions given in the guidance material.

### Individual vs. group

For individual fairness, refer to the [SampleDistortionMetric](https://aif360.readthedocs.io/en/latest/modules/generated/aif360.metrics.SampleDistortionMetric.html#aif360.metrics.SampleDistortionMetric).

For group fairness, refer to [DatasetMetric](https://aif360.readthedocs.io/en/latest/modules/generated/aif360.metrics.DatasetMetric.html#aif360.metrics.DatasetMetric) and its children classes [BinaryLabelDatasetMetric](https://aif360.readthedocs.io/en/latest/modules/generated/aif360.metrics.BinaryLabelDatasetMetric.html#aif360.metrics.BinaryLabelDatasetMetric) and [ClassificationMetric](https://aif360.readthedocs.io/en/latest/modules/generated/aif360.metrics.ClassificationMetric.html#aif360.metrics.ClassificationMetric).

It is possible to combine individual- and group fairness in a single metric. 
The [ClassificationMetric](https://aif360.readthedocs.io/en/latest/modules/generated/aif360.metrics.ClassificationMetric.html#aif360.metrics.ClassificationMetric) contains several measures related to the [generalized entropy index](https://aif360.readthedocs.io/en/latest/modules/generated/aif360.metrics.ClassificationMetric.html#aif360.metrics.ClassificationMetric.generalized_entropy_index) suitable for this purpose.

### Stages

The metrics under `(BinaryLabel)DatasetMetric` apply to the training data and are thus relevant for the {{< stage "preprocessing" >}} stage.

The metrics under `ClassificationMetric` apply to the models themselves and are thus relevant during the {{< stage "in-processing" >}} stage.

### Worldviews

In the case of group fairness, the underlying "worldview" can be a relevant factor in choosing metrics.

For "we are all equal" worldview the *demographic parity metrics* are appropriate, e.g.

- `disparate_impact`
- `statistical_parity_difference`

If the application follows the "what you see is what you get" worldview, then variations of the *equality of odds* fairness metric is appropriate:

- `average_odds_difference`
- `average_abs_odds_difference`

Some metrics are not specific to a particular worldview, such as metrics based on error rates, e.g.:

- `false_negative_rate_ratio`
- `false_positive_rate_ratio`
- `error_rate_ratio`

## Choosing algorithms

The API nicely lists algorithms by the stage they are applicable in.
The algorithms that affect the {{< stage "in-processing" >}} stage are mostly suitable for classification.
However, a reduction-based approach such as [GridSearchReduction]( https://aif360.readthedocs.io/en/latest/modules/generated/aif360.algorithms.inprocessing.GridSearchReduction.html#aif360.algorithms.inprocessing.GridSearchReduction) can also be used for regression.

### Preprocessing

For {{< stage "preprocessing" >}} algorithms see [aif360.algorithms.preprocessing](https://aif360.readthedocs.io/en/latest/modules/algorithms.html#module-aif360.algorithms.preprocessing):

Relevant remarks from the guidance material on the preprocessing algorithms:

- "Among pre-processing algorithms, reweighing only changes weights applied to training samples; it does not change any feature or label values. Therefore, it may be a preferred option in case the application does not allow for value changes."
- "Disparate impact remover and optimized pre-processing yield modified datasets in the same space as the input training data, whereas LFR’s pre-processed dataset is in a latent space."
- "If the application requires transparency on the transformation, then disparate impact remover and optimized pre-processing may be preferred options"
- "Moreover, optimized pre-processing addresses both group fairness and individual fairness."

### In-processing

For algorithms for fair learning see [aif360.algorithms.inprocessing](https://aif360.readthedocs.io/en/latest/modules/algorithms.html#module-aif360.algorithms.inprocessing).

Relevant remarks from the guidance material on the "in-processing" algorithms:

- "Among in-processing algorithms, the prejudice remover is limited to learning algorithms that allow for regularization terms whereas the adversarial debiasing algorithm allows for a more general set of learning algorithms, and may be preferred for that reason."

### Post-processing

For {{< stage "post-processing" >}} algorithms, see [aif360.algorithms.postprocessing](https://aif360.readthedocs.io/en/latest/modules/algorithms.html#module-aif360.algorithms.postprocessing).

Relevant remarks from the guidance material on the "post-processing" algorithms:

- "Among post-processing algorithms, the two equalized odds post-processing algorithms have a randomized component whereas the reject option algorithm is deterministic, and may be preferred for that reason."
