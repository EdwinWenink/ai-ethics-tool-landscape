---
title: 'Fairness in Classification'
values: ['fairness']
fairness: ['group fairness']
categories: ['model-specific']
tasks: ['classification']
data: ['tabular']
stages: ['in-processing']
licence: 'GNU General Public License v3'
repo: 'https://github.com/mbilalzafar/fair-classification'
languages: ['Python']
references: 
- 
    name: 'Muhammad Bilal Zafar et al. - Fairness Constraints: Mechanisms for Fair Classification (2017a)'
    url: 'https://arxiv.org/abs/1507.05259'
- 
    name: 'Muhammad Bilal Zafar et al. - Fairness Beyond Disparate Treatment & Disparate Impact: Learning Classification without Disparate Mistreatment (2017b)'
    url: 'https://arxiv.org/abs/1610.08452'
- 
    name: 'Muhammad Bilal Zafar et al. - From Parity to Preference-based Notions of Fairness in Classification (2017c)'
    url: 'https://arxiv.org/abs/1707.00010'
---

The not-so originally named "fairness in classification" provides a Python implementation of three fairness constraints for logistic regression:

1. Disparate impact: similar acceptance rate for different demographic groups. See Zafar et al., 2017 a.
2. Disparate mistreatment: similar misclassification rate for different demographic groups. See Zafar et al., 2017b
3. Preference-based fairness (as opposed to parity-based fairness): a more game-theoretical approach where decision boundaries are chosen such that it can be shown that each group prefers its own decision boundary, if rational. See Zafar et al., 2017c.

This library is a good demo on how to implement fairness constraints from scratch, more than being a comprehensive fairness toolkit.
