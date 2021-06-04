---
title: 'Agile Ethics for AI'
values: ['explainability', 'fairness', 'accountability', 'privacy']
categories: ['model-agnostic']
stages: ['design phase', 'preprocessing', 'learning', 'evaluation', 'prediction','post-hoc']
references: 
- 
    name: 'Agile Ethics for AI Trello Board '
    url: 'https://trello.com/b/SarLFYOd/agile-ethics-for-ai-hai'
- 
    name: 'HAI: Human-Centered Artificial Intelligence'
    url: 'https://hai.stanford.edu/'
---

Butnaru and others associated with the HAI center at Stanford set up a Agile Ethics workflow in the form of a Trello board.
From left to right, the workflow walks you through relevant ethical considerations at the various steps of a machine learning pipeline.
The phases are:

- Scope
    * Consider ethical implications of the project
    * Consider skill mapping (what's the impact of AI on jobs)?
        - Facilitates up-skilling or a change of strategy in the use of human talent
- Data audit
    * Led by Chief Data Officer
    * "Meet and plan" stage in Agile
    * Helpful: [Data Ethics Canvas](https://theodi.org/article/why-we-need-the-data-ethics-canvas/)
- Train
    * Build stage in Agile
    * Consider (tools for) transparency and fairness
- Analyse
    * Benchmarks, including benchmarks related to e.g. fairness
    * Correct e.g. bias where necessary
- Feedback
    * Similar to the "review" stage in Agile
    * Wizard of Oz experiments to assess acceptance rate prior to deployment
        - Potential resource here is the *Technology acceptance model* (TAM)
- Calibrate
    * With a focus on machine-human interaction
- Augment, e.g.
    * In which ways does AI augment a job? And which skills cannot and/or should not be replaced?
    * In which ways can users augment the AI?
- People & Environment
    * Long-term accountability with respect to the impact on people and the environment where AI is deployed.
