---
title: 'Model cards for Model Reporting'
values: ['accountability', 'fairness']
categories: ['model-agnostic']
stages: ['design phase', 'preprocessing', 'post-processing']
references: 
-
    name: 'Mitchell et al. - Model Cards for Model Reporting'
    url: 'https://doi.org/10.1145/3287560.3287596'
---

Model cards are an extension of the {{< tool "datasheet">}} to machine learning models.

> Model cards are short documents accompanying trained machine learning models that provide benchmarked evaluation in a variety of conditions, such as across different cultural, demographic, or phenotypic groups (e.g., race, geographic location, sex, Fitzpatrick skin type [15]) and intersectional groups (e.g., age and race, or sex and Fitzpatrick skin type) that are relevant to the intended application domains. Model cards also disclose the context in which models are intended to be used, details of the performance evaluation procedures, and other relevant information. While we focus primarily on human-centered machine learning models in the application fields of computer vision and natural language processing, this framework can be used to document any trained machine learning
model. (1)

A model card records the following fields.

1. Model details
    * E.g. model type, information about training algorithms and parameters, fairness constraints etc.
2. Intended use
    * Can also include a specification of how the model is *not* intended to be used.
3. Relevant factors
    * E.g. involved demographic groups
4. Metrics
    * "should be chosen to reflect potential real-world impacts of the model"
5. Evaluation data
    * Which datasets were used for evaluation? Why those? And which preprocessing was used?
6. Training data
    * If private, try to include as much as possible, such as distributions over relevant factors
7. Quantitative analyses
    * Should be *disaggregated* and run both on each identification factor (cf. 3) independently, and on combinations of factors.
8. Ethical considerations
9. Caveats and recommendations

See the paper for more details and examples of filled in model cards.
