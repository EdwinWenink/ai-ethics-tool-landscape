---
title: Fairness
---

When trying to operationalize fairness it is important to realize that fairness in machine learning is a complex socio-technical issue.
At minimum, this means that fairness tools should never be seen as plug-and-play solutions.
This is already evident from the fact that - as most of the listed tools will emphasize - choices have to be made in which *type* of fairness is strived for.
One general distinction for example is between [group fairness](/fairness/group-fairness) and [individual fairness](/fairness/individual-fairness).
Within group fairness, different parity metrics correspond to different "worldviews" on equality.

Additionally, there are different [stages](/stages/) in the machine learning pipeline where you can intervene.
The choice for a particular algorithm will partially be guided by the level of access to different stages of the machine learning pipeline.
Generally speaking, it is optimal to intervene as early as possible.
In particularly, bias mitigation in the {{< stage "preprocessing" >}} stage can address both group- and individual fairness.

With all these factors combined, choosing an appropriate bias mitigation strategy is a complex tasks that requires both expertise in data science and sensitivity to context and values. 
