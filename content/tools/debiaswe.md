---
title: 'Debiaswe: try to make word embeddings less sexist'
values: ['fairness']
fairness: ['group fairness']
categories: ['model-specific']
data: ['text']
stages: ['preprocessing', 'in-processing']
tasks: ['NLP', 'clustering']
licence: 'MIT'
repo: https://github.com/tolga-b/debiaswe
languages: ['Python']
references: 
- 
    name: 'Bolukbasi et al. - Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings'
    url: 'https://dl.acm.org/doi/10.5555/3157382.3157584'
---

Word embeddings are a widely used representation for text data.
A well-known example in natural language processing (NLP) is `Word2vec`, which uses a neural network to learn latent vector representations of words.
It turns out that relations in this latent vector space capture semantic relations quite well.
For example, by finding similar vectors you typically end up with highly related or synonymous words.
Another typical example is that when you add up the vectors of "king" and "woman", you end up with the vector corresponding to "queen", so even a form of conceptual calculus is possible. 

In the previous example, the learned association between "queen" and "woman" is not problematic because conceptually speaking a queen is feminine ("drag queens" may or may not agree).
However, Bolukbasi et al. show that word embeddings also capture gender stereotypes, even for example in news articles (Google News dataset).
For example, whereas the association between "queen" and "female" is not problematic, the association between "receptionist" and "female" captures a form of social bias (example from paper abstract).
If machine learning applications use these embeddings, e.g. in a clustering tasks, they can make and/or support biased inferences.

In their paper, Bolkbasi et al. identify vector properties of gender stereotypes that allow intervention directly on the word embeddings themselves.
They are able to identify a vector direction associated with the she-he divide.
This allows them to show that e.g. profession related words strongly correlate with (biased) gender direction.
In the [tutorial notebook](https://github.com/tolga-b/debiaswe/blob/master/tutorial_example1.ipynb) we see that when projected onto the gender dimension, the word "receptionist" receives a projection score of 0.27 whereas the word "philosopher" receives a score of -0.19 (in this example, positive scores are defined as the female direction).
A similar analysis can be performed not for gender bias, but other forms of bias such as racial bias.
The tutorial also shows that after debiasing, unbiased gender information is still captured (i.e. don't throw the baby out with the bathwater).
For example, it still desirable that "businesswoman" receives a high positive direction (0.41) whereas "businessman" receives a high negative direction (-0.41).

As input, this tool can use a list of gender-specific words and gender pairs that you want to be on par.
This tool thus supports a type of {{< fairness "group fairness" >}}, {{< category "model-specific" >}} to models using word embedding.
The outcome of the debiasing step depends of the human definition of which associations are undesirable.
