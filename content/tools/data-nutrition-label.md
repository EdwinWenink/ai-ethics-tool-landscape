---
title: 'Data Nutrition Label'
values: ['accountability', 'fairness']
categories: ['model-agnostic']
stages: ['design phase', 'preprocessing']
references: 
- 
    name: 'Data Nutrition Project'
    url: 'https://datanutrition.org/'
- 
    name: 'Holland et al. - The Dataset Nutrition Label: A Framework To Drive Higher Data Quality Standards'
    url: 'https://arxiv.org/abs/1805.03677'
- 
    name: 'Data Nutrition Label Demo'
    url: 'https://ahmedhosny.github.io/datanutrition/'
---

In analogy with nutrition labels on food products, the authors of this paper propose a way to create a Data Nutrition Label.
The goal of this method is to asses data quality and mitigate potential problems early on *before* building models on the data.

According to the authors, their approach is different from the {{< tool "datasheet" >}} in that the "proposed datasheet [i.e. by Gebru et al.] includes dataset provenance, key characteristics, relevant regulations and test results, but also significant yet more subjective information such as potential bias, strengths and weaknesses of the dataset, API, or model, and suggested uses." (5)
The Data Nutrition Label instead relies more on computational tools and statistics.

A practical guide is provided as a [demo](https://ahmedhosny.github.io/datanutrition/).
A brief summary of the goals and component modules are provided below.

## Goals

The goals of the Dataset Nutrition Label are:

> Three goals drive this work. First, to inform and improve data specialists' selection and interrogation of datasets and to prompt critical analysis. Consequently, data specialists are the primary intended audience. Second, to gain traction as a practical, readily deployable tool, we prioritize efficiency and flexibility. To that end, we do not suggest one specific approach to the Label, or charge one specific community with creating the Label. Rather, our prototype is modular, and the underlying framework is one that anyone can use. Lastly, we leverage probabilistic computing tools to surface potential corollaries, anomalies, and proxies. This is particularly beneficial because resolving these issues requires excess development time, and can lead to undesired correlations in trained models. (p. 5)

## Modules

See p. 7 of the linked paper for the following table:

| Module Name               | Description | Contents |
|---------------------------|-------------|----------|
| Metadata                  | Meta information. This module is the only required module. It represents the absolute minimum information to be represented.            |   Filename, file format, URL, domain keywords, type, dataset size, % of missing cells, license, release data, collection range, description       |
| Provenance                |   Information regarding the origin and lineage of the dataset          |    Source and author contact information with version history      |
| Variables                 |      Descriptions of each variable (column) in the dataset       | Textual descriptions          |
| Statistics                |  Simple statistics for all variables, in addition to stratifications into ordinal, nominal, continuous and discrete           | Least/most frequent entries, min/max, median, mean, etc.          |
| Pair Plots                | Distributions and linear correlations between two chosen variables              | Histograms and heatmaps          |
| Probabilistic Model       | Synthetic data generated using distribution hypotheses from which the data was drawn - leverages a probabilistic programming backend            | Histograms and other statistical plots          |
| Ground Truth Correlations | Linear correlations between a chosen variable in the dataset and variables from other datasets considered to be "ground truth", such as Census Data            | Heatmaps          |

For more details and justification of these modules, refer to the accompanying paper.
