---
title: Partial dependence plot (PDP)
---

A partial dependence plot (PDP) visualizes the marginal effect of a feature on the outcome of a machine learning model.
This effect is computed by "marginalizing out" the contribution of all other features, so that the result is a function that only depends on the feature of interest.
Contributions by other features are factored into the marginal effect. 
The PDP is then produced by plotting the predicted outcome (y-axis) against the values of the feature of interest (x-axis).
You can compute the marginal effect of more features, but when using more than two features you will not be able to visualize the result.

The computed effect is only accurate if the feature of interest does not correlate with the other features.
{{< explanation "ALE" >}} alleviates this issue because ALE plots work with a conditional a  distribution instead of a marginal distribution.

A PDP is the average of the lines in an {{< explanation "ICE plot" >}}.

Examples such as the following can be found in Christoph Molnar's [chapter on PDP](https://christophm.github.io/interpretable-ml-book/pdp.html):

![PDP example](https://christophm.github.io/interpretable-ml-book/images/pdp-bike-1.png)
