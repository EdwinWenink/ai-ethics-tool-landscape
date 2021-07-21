---
title: Security
---

Security focuses on tools for mitigating AI-specific risks, such as tools that promote robustness against adversial attacks.

For example, it is possible to create adversial examples by finding perturbations that maximize the prediction error and then applying these perturbations to input images in such a way that 1) a human does not or barely see the difference but 2) the neural network misclassifies the input.
If the classifications of the neural network have impact, then this type of attack needs to be countered for safe usage of the model.

Security is important for the *safety* of AI, but safety may be construed as a broader category that also involves {{< value "explainability" >}} or {{< value "fairness" >}} in the sense of "protection against harm".
