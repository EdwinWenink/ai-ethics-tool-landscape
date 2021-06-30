---
title: White box explanations
---

Typically a distinction is made between "black box" models and "white box" models.
White box models are models where it is meaningful to look at the model's components.
The most simple example is a linear regression problem, where the regression coefficients can (i.e. given proper preprocessing etc.) give insights into how much each feature contributes to the final prediction.

Some explainability packages do not try to explain "black boxes", but instead propose using white box models either as a replacement for the black box model, or a surrogate to it.
For the latter case, see {{< explanation "local surrogate" >}} and {{< explanation "global surrogate" >}}.
