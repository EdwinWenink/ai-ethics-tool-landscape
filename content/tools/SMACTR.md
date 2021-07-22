---
title: 'SMACTR: End-to-End Framework for Internal Algorithmic Auditing'
values: ['accountability']
categories: ['model-agnostic']
stages: ['design phase', 'preprocessing', 'in-processing','post-processing']
references: 
- 
    name: 'Raji et al. - Closing the AI Accountability Gap: Defining an End-to-End Framework for Internal Algorithmic Auditing'
    url: 'https://arxiv.org/abs/2001.00973'
---

## Introduction

A major downside of external auditing is that it typically only can be done *after* model deployment.
This paper presents a methodology for *internal* algorithmic auditing as an integral part of the development process, end-to-end.

Those who move fast and break things, beware:

> The audit process is necessarily boring, slow, meticulous and methodical—antithetical to the typical rapid development pace for AI technology. However, it is critical to slow down as algorithms continue to be deployed in increasingly high-stakes domains.  (33)

## Five stages of SMACTR

1. Scoping
2. Mapping
3. Artefact Collection
4. Testing
5. Reflection

For each stage the SMACTR method recommends a certain type of key artefact as output.
These stages are described in detail in the paper, but a short summary is provided below.
What's quite nice about this paper is that it comes with [supplementary materials](https://drive.google.com/drive/folders/1GWlq8qGZXb2lNHxWBuo2wl-rlHsjNPM0) offering templates for some key artefacts.
Some artefacts are very project-specific and do not have a general template.

### Scoping

> The goal of the scoping stage is to clarify the objective of the audit by reviewing the motivations and intended impact of the investigated system, and confirming the principles and values meant to guide product development. This is the stage in which the risk analysis begins by mapping out intended use cases and identifying analogous deployments either within the organization or from competitors or adjacent industries. The goal is to anticipate areas to investigate as potential sources of harm and social impact. At this stage, interaction with the system should be minimal. (39)

Pre-requisite documents:

- Declaration or confirmation statement of the ethical principles, standards and AI principles.
- Product Requirements Document (PRD) or something similar, like a project planning

[Key artefacts of auditers](https://drive.google.com/drive/folders/1-NR9dumIy5tiAMDTaZVkdXKkYraCStJX):

1. Ethical review of system use case
2. Social Impact Assessment

### Mapping

This is not yet a testing phase, but is about relating the documents from the scoping phase to those stakeholders that will be involved in the actual testing/reviewing.

- map internal stakeholders
    * "enables an internal record of individual accountability with respect to participation towards the final outcome" (39)
    * "enables the trace of relevant contacts for future inquiry" (39)
- identify key collaborators for the internal audit
- "orchestrate the appropriate stakeholder buy-in required for execution" (39)
- initiate risk prioritization for later testing
    * identify failure modes, e.g. what's the impact of false negatives and false positives?

[Key artefacts](https://drive.google.com/drive/folders/1KuOCwhrUrlrLAhkhbNMzXFFOXG5Mgq7_):

1. Stakeholder map and collaborator contact list
2. System map of product development lifecycle and engineering system overview, especially when multiple models inform the end product
3. Design history file review of past product versions
4. "Report or interview transcripts on key findings from internal ethnographic fieldwork involving the stakeholders and engineers." (40)

### Artifact Collection

> Often this implies a record of data and model dynamics though application-based systems can include other product development artifacts such as design documents and reviews, in addition to systems architecture diagrams and other
implementation planning documents and retrospectives.

[Key artefacts](https://drive.google.com/drive/folders/1l8RkF5FBIM1sVoL9FKep9nmJpM-mXs86):

- Audit checklist that is used to verify that all documentation required for the audit is provided
    * Can include model and data transparency documentation
- Datasheets and model cards

### Testing

The testing phase can be highly dependent on the specific usage context and the project.
The paper discusses two [example artifacts](https://drive.google.com/drive/folders/1vMEBzexh8_3-0g2TxTBU8gejbaKHz8gq):

- Report on adversarial testing
- Ethical risk analysis chart

The goal of this phase is to test compliance with *prioritized* ethical values. 
Such a prioritization can be based on a risk assessment methodology such as a so-called "failure modes and effects analysis" (FMEA), which is very common in aerospace engineering:

> The main purpose of a FMEA is to define, identify and eliminate potential failures or problems in different products, designs, systems and services. Prior to conducting a FMEA, known issues with a proposed technology should be thoroughly mapped through a literature review and by collecting and documenting the experiences of the product designers, engineers and managers. Further, the risk exercise is based on known issues with relevant datasets and models, information that can be gathered from interviews and from extant technical documentation. (36)


### Reflection

- Discuss results in relation to the original scoping.
- Based on test results, highlight the ethical principles that may be jeopardized when the AI system is deployed

[Key artefacts](https://drive.google.com/drive/folders/1IHwiJwSjz1UjJ-lw5wNOkG-Q73LbxwKp):

- Algorithmic Use-related Risk Analysis
    * The above mentioned FMEA can be the basis for this
- Risk mitigation plan to counter identified failures; joint effort by auditers and engineers
    * E.g. after identifying class imbalance issues related to fairness, decide what is acceptable in terms of class parity and then include more data for balancing
    * E.g. make design choices like opt-out or opt-in functionality
- Algorithmic Design History File (ADHF)
    * "collect all the documentation from the activities outlined above related to the development of the algorithm. It should point to the documents necessary to demonstrate that the product or model was developed in accordance with an organization’s ethical values, and that the benefits of the product outweigh any risks identified in the risk analysis process." (42)
- Algorithmic Audit Summary Report
    * "The report aggregates all key audit artifacts, technical analyses and documentation, putting this in one accessible location for review. This audit report should be compared qualitatively and quantitatively to the expectations outlined in the given ethical objectives and any corresponding engineering requirements." (42)
