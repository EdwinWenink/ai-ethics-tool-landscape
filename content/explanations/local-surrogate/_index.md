---
title: Local surrogate models
---

One approach to explain predictions of "black box" models is to approximate its predictions with a
{{< explanation "white box" >}} model that *is* interpretable.
A *local* surrogate model is a model that does this approximation more accurately only in the "local" feature space corresponding to a single input.
The idea is that even though a white box model may not accurately capture the behavior of a black box model *globally* (the feature space of a large set of training instances), it may e.g. linearly approximate the feature space *local* to a single training instance.
Also see {{< explanation "global surrogate" >}} models.
