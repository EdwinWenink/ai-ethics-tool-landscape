---
title: 'Equity Evaluation Corpus (EEC)'
values: ['fairness']
fairness: ['group fairness']
categories: ['model-agnostic']
data: ['text']
tasks: ['NLP']
stages: ['evaluation']
references: 
- 
    name: 'Biases in Sentiment Analysis Systems'
    url: 'https://saifmohammad.com/WebPages/Biases-SA.html'
- 
    name: 'Kiritchenko & Mohammad - Examining Gender and Race Bias in Two Hundred Sentiment Analysis Systems'
    url: 'https://saifmohammad.com/WebDocs/EEC/ethics-StarSem-final_with_appendix.pdf'
---

This handcrafted dataset can be used to evaluate bias in AI using text data for NLP tasks.
Dataset description:

> Automatic machine learning systems can inadvertently accentuate and perpetuate inappropriate human biases. Past work on examining inappropriate biases has largely focused on just individual systems and resources. Further, there is a lack of benchmark datasets for examining inappropriate biases in system predictions. Here, we present the Equity Evaluation Corpus (EEC), which consists of 8,640 English sentences carefully chosen to tease out biases towards certain races and genders. We used the dataset to examine 219 automatic sentiment analysis systems that took part in a recent shared task, SemEval-2018 Task 1 ‘Affect in Tweets’. We found that several of the systems showed statistically significant bias; that is, they consistently provide slightly higher sentiment intensity predictions for one race or one gender. We make the EEC freely available, and encourage its use to evaluate biases in sentiment and other NLP tasks.
