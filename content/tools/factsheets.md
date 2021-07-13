---
title: "FactSheets: Increasing Trust in AI Services through Supplier's Declaration of Conformity"
values: ['accountability']
categories: ['model-agnostic']
stages: ['post-processing']
references: 
- 
    name: "Arnold et al. - FactSheets: Increasing Trust in AI Services through Supplier's Declaration of Conformity"
    url: 'https://ieeexplore.ieee.org/document/8843893'
---

FactSheets, as proposed by Arnold et al. from IBM Research, are similar to the {{< tool "model-card" >}} and {{< tool "datasheet" >}}, but are significantly more comprehensive because they focus on *whole AI services*.
A main difference is that live AI services may comprise several trained models that interact with each other.
The model card and datasheet instead concern a single model and the data it is trained on.
However, Arnold et al. point out that an AI service with safe components is not necessarily safe overall and "so it is prudent to also consider transparency and accountability of services in addition to datasets and models" (p. 2).

The FactSheet tailors the concept of a *supplier's declaration of conformity*, which is provided to engender trust in a product by its users, towards the usage of AI services.
A FactSheet involves the following:

> Toward transparency for developing trust, we propose a FactSheet for AI Services. A FactSheet will contain sections on all relevant attributes of an AI service, such as intended use, performance, safety, and security. Performance will include appropriate accuracy or risk measures along with timing information. Safety, discussed in [5, 3] as the minimization of both risk and epistemic uncertainty, will include explainability, algorithmic fairness, and robustness to dataset shift. Security will include robustness to adversarial attacks. Moreover, the FactSheet will list how the service was created, trained, and deployed along with what scenarios it was tested on, how it may respond to untested scenarios, guidelines that specify what tasks it should and should not be used for, and any ethical concerns of its use. Hence, FactSheets help prevent overgeneralization and unintended use of AI services by solidly grounding them with metrics and usage scenarios. (p. 1-2)

For the FactSheet with detailed questions and checks, see Appendix A of the referenced paper.
