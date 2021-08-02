---
title: Individual Conditional Expectation (ICE)
---

An ICE plot can be seen as a {{< explanation "partial dependence plot" >}} (PDP) that does not use the overal expectation of other features than the feature of interest, but instead the feature values of a single data point only.
So the reasoning behind an ICE plot is similar to a PDP, but the main difference is that whereas a PDP uses a "global" expectation over the other data points, the ICE plot contains a single line for each data instance.
Each line is computed by taking a data instance and varying only a feature of interest while keeping the other features the same, and then plotting the result on the predicted value for that instance.

An advantage of this approach over the PDP is that whereas a PDP is not accurate when there are (strong) correlations between features, an ICE plot will allow you to visualize and spot these correlations. 

The following figure shows an ICE plot from Molnar's [Interpretable Machine Learning](https://christophm.github.io/interpretable-ml-book/ice.html) book:

![ICE plot example](https://christophm.github.io/interpretable-ml-book/images/ice-cervical-1.png)

