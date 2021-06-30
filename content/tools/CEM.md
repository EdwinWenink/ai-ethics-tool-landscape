---
title: 'Contrastive Explanation Method (CEM)'
values: ['explainability']
explanations: ['contrastive']
categories: ['model-agnostic']
tasks: ['classification']
data: ['image'] 
stages: ['post-hoc'] 
licence: 'Apache License 2.0'
repo: https://github.com/IBM/Contrastive-Explanation-Method
languages: ['Python']
references: 
- 
    name: 'Dhurandhar et al. - Explanations based on the Missing: Towards Contrastive Explanations with Pertinent Negatives'
    url: 'https://arxiv.org/abs/1802.07623'
---

Dhurandhar et al. support a type of {{< explanation "contrastive" >}} explanation based on what they call *pertinent negatives*.
A contrastive explanation answers the question: "Why P, rather than Q"?

CEM supports such an explanation by finding the minimal set of features that lead to prediction P (a *pertinent positive* that resembles an {{< explanation "anchor" >}} explanation), and additionally a minimal set of features that should be *absent* to maintain decision P instead of the decision for closest class Q (a *pertinent negative* that is somewhat similar to a {{< explanation "counterfactual" >}}).

CEM is also implemented in the more encompassing {{< tool "Alibi" >}}.
