---
title: 'Data Statements for NLP'
values: ['accountability', 'fairness']
categories: ['model-agnostic']
tasks: ['NLP']
data: ['text']
stages: ['design phase', 'preprocessing']
references: 
- 
    name: 'Bender & Friedman - Data Statements for Natural Language Processing: Toward Mitigating System Bias and Enabling Better Science'
    url: 'https://www.aclweb.org/anthology/Q18-1041/'
---

A data statement, according to the authors, is ...

> a characterization of a dataset that provides context to allow developers and users to better understand how experimental results might generalize,how  software  might  be  appropriately  deployed,and what biases might be reflected in systems built on the software.  (587)

This paper specifically focuses on ethically responsive *NLP* technology.
The authors argue that a data statement should be an integral part of work and writing on NLP.

Explicitly filling in a data statement are helpful for identifying emergent bias, which may emerge when a NLP model is deployed, as well as historical bias in the training data, because it helps finding potential gaps between the speaker populations that are represented in the data and the populations the NLP system will work with.
Additionally, subtleties like the annotator demographic are also explicated, because the linguistic context of annotators may also influence the performance of the system.

Similar efforts are the {{< tool datasheet >}} and {{< tool "data nutrition label" >}} 

## Data Statement Schema

Statements can be offered in short and long form.
The long form is intended for systems documentation and academic papers.
The following table summarizes the components of the long form, see p. 590-591.
The short form is essentially a prose summary of the long form that should not replace, but instead introduce and point to the long form.
For further clarifications and justifications of these categories, consult the paper.


|  Name               | Content |
|---------------------|-------------|
| Curation Rationale  | "Which texts were included and what were the goals in selecting texts, both in the original collection and in any further sub-selection?" (p. 590) |
| Language variety | Provide a language tag (from [BCP-47](https://tools.ietf.org/rfc/bcp/bcp47.txt)) that identifies a language variety, and additional prose description of the language variety |
| Speaker demographic | Specifications of age, gender, ethnicity, native language, socioeconomic status, number of different speakers represented, presence of disordered speech |
| Annotator demographic | Specifications of age, gender, ethnicity, native language, socioeconomic status, training in linguistics or relevant discipline | 
| Speech situation | Time and place, modality, scripted/edited vs spontaneous, synchronous vs. asynchronous interaction, intended audience |
| Text characteristics | Specify genre, topic and structural characteristics | 
| Recording Quality | If applicable, indicatie factors impacting recording quality | 
| Other | The above is not exclusive and may be appended with other relevant information | 

## Case studies

Two case studies are provided in the article itself, so refer to the article for a concrete in-depth example.
The first case study is about hate speech Twitter annotations.
The second case study concerns a collection of video interviews *Voices from the Rwanda Tribunal*.
