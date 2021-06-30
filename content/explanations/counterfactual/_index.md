---
title: Counterfactual explanations
---

A clear description counterfactual explanations, which is very important for human causal reasoning, is provided by Molnar & Dandl:

> A counterfactual explanation describes a causal situation in the form: "If X had not occurred, Y would not have occurred". For example: "If I hadn't taken a sip of this hot coffee, I wouldn't have burned my tongue". Event Y is that I burned my tongue; cause X is that I had a hot coffee. Thinking in counterfactuals requires imagining a hypothetical reality that contradicts the observed facts (for example, a world in which I have not drunk the hot coffee), hence the name "counterfactual". The ability to think in counterfactuals makes us humans so smart compared to other animals. ([Molnar & Dandl](https://christophm.github.io/interpretable-ml-book/counterfactual.html))

They also give a general approach for supporting counterfactual explanations about machine learning models:

> We simply change the feature values of an instance before making the predictions and we analyze how the prediction changes. We are interested in scenarios in which the prediction changes in a relevant way, like a flip in predicted class (for example, credit application accepted or rejected) or in which the prediction reaches a certain threshold (for example, the probability for cancer reaches 10%). A counterfactual explanation of a prediction describes the smallest change to the feature values that changes the prediction to a predefined output. ([Molnar & Dandl](https://christophm.github.io/interpretable-ml-book/counterfactual.html))
