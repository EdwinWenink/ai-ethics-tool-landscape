---
title: Contrastive explanations
---

Human explanations are often contrastive, meaning that they do not answer the indeterminate "Why?" question, but instead "Why P, rather than Q?".
For example, when a mortgage application is denied, we are not interested in a very long list of tiny little details that all contributed to that decision, but we want a to-the-point explanation that shows us what we minimally have to change to get the mortgage.

<!-- TODO -->
For example, the {{< tool "CEM" >}} method supports such an explanation by finding the minimal set of features that lead to prediction P (so this looks like an {{< explanation "anchor" >}} explanation), and additionally a minimal set of features that should be absent to maintain decision P instead of the closest class Q (which is somewhat similar to a {{< explanation "counterfactual" >}}).
