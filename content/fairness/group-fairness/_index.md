---
title: Group fairness
---

There are different ways of defining {{< value "fairness" >}}.
One major distinction is between group fairness and [individual fairness](/fairness/individual-fairness).


The [guidance material of the AI Fairness 360 Toolkit](http://aif360.mybluemix.net/resources#guidance) explains  group fairness as such:

> Group fairness, in its broadest sense, partitions a population into groups defined by protected attributes and seeks for some statistical measure to be equal across groups. 

The [Fairlearn](https://fairlearn.org/main/user_guide/fairness_in_machine_learning.html#fairness-of-ai-systems) toolkit takes a group fairness approach and explains it as follows:

> There are many approaches to conceptualizing fairness. In Fairlearn, we follow the approach known as group fairness, which asks: *Which groups of individuals are at risk for experiencing harms?*
The relevant groups (also called subpopulations) are defined using sensitive features (or sensitive attributes), which are passed to a Fairlearn estimator as a vector or a matrix called sensitive_features (even if it is only one feature). The term suggests that the system designer should be sensitive to these features when assessing group fairness. Although these features may sometimes have privacy implications (e.g., gender or age) in other cases they may not (e.g., whether or not someone is a native speaker of a particular language). Moreover, the word sensitive does not imply that these features should not be used to make predictions – indeed, in some cases it may be better to include them.

When one strives for group fairness, one has to decide how to define groups in terms of sensitive of protected features.
This choice itself is not technical but sociological or ethical, and if this choice itself is unjust no technical tool will help you achieve fairness.

Another interesting and potentially counter-intuitive dynamic is that in order to ensure parity in terms of protected features, you need to have access to those. 
The gut feeling, from a privacy perspective, may instead be to not collect sensitive data in the first place.

Toolkits addressing group fairness typically implement several constraints that should be satisfied in order to speak of parity between groups.
The [guidance material](http://aif360.mybluemix.net/resources#guidance) of the {{< tool "IBM-AI-Fairness-360" >}} toolkit further distinguishes two different "worldviews" underlying group fairness, the "we're all equal" worldview and the "what you see if what you get worldview":

> There are two opposing worldviews on group fairness: we’re all equal (WAE) and what you see is what you get (WYSIWYG) [4],[5]. The WAE worldview holds that all groups have similar abilities with respect to the task (even if we cannot observe this properly), whereas the WYSIWYG worldview holds that the observations reflect ability with respect to the task.  For example in college admissions, using SAT score as a feature for predicting success in college, the WYSIWYG worldview says that the score correlates well with future success and that there is a way to use the score to correctly compare the abilities of applicants.  In contrast, the WAE worldview says that the SAT score may contain structural biases so its distribution being different across groups should not be mistaken for a difference in distribution in ability.

Again, using fairness tools responsibly requires awareness of these different worldviews and their implications on fairness.
