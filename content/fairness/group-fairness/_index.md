---
title: Group fairness
---

There are different ways of defining {{< value "fairness" >}}.
"Group fairness" is one of them.

From the [Fairlearn](https://fairlearn.org/main/user_guide/fairness_in_machine_learning.html#fairness-of-ai-systems) website:

> There are many approaches to conceptualizing fairness. In Fairlearn, we follow the approach known as group fairness, which asks: *Which groups of individuals are at risk for experiencing harms?*
The relevant groups (also called subpopulations) are defined using sensitive features (or sensitive attributes), which are passed to a Fairlearn estimator as a vector or a matrix called sensitive_features (even if it is only one feature). The term suggests that the system designer should be sensitive to these features when assessing group fairness. Although these features may sometimes have privacy implications (e.g., gender or age) in other cases they may not (e.g., whether or not someone is a native speaker of a particular language). Moreover, the word sensitive does not imply that these features should not be used to make predictions – indeed, in some cases it may be better to include them.

The [guidance material of the AI Fairness 360 Toolkit](http://aif360.mybluemix.net/resources#guidance) explains  the difference between group fairness and individual fairness:

> Group fairness, in its broadest sense, partitions a population into groups defined by protected attributes and seeks for some statistical measure to be equal across groups.  Individual fairness, in its broadest sense, seeks for similar individuals to be treated similarly.  If the application is concerned with individual fairness, then the metrics in the SampleDistortionMetric class should be used.  If the application is concerned with group fairness, then the metrics in the DatasetMetric class (and in its children classes such as the BinaryLabelDatasetMetric class) as well as the ClassificationMetric class (except the ones noted in the next sentence) should be used.  If the application is concerned with both individual and group fairness, and requires the use of a single metric, then the generalized entropy index and its specializations to Theil index and coefficient of variation in the ClassificationMetric class should be used.  Of course, multiple metrics, including ones from both individual and group fairness can be examined simultaneously.
