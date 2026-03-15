# Report Section Library

This document defines the report sections supported by the Model Validation Copilot.

Each section is categorized based on whether it can be drafted by AI or requires human review.

---

## AI Draftable Sections (Initial Scope)

These sections primarily summarize factual information and are well suited for AI-assisted drafting.

### Model Overview

Description of the model, including:

- Model purpose
- Business context
- Intended users
- Key outputs
- Model dependences

Sources:

- Model documentation
- Model inventory information

---

### Intended Use

Explanation of how the model is used within the business process.

Includes:

- Decision-making context
- Scope of application
- Key stakeholders

---

### Model Framework

Overview of the model methodology and structure.

Examples include:

- statistical models
- rule-based models
- forecasting models
- Machine learning models

The section describes how inputs are transformed into outputs.

---

### Data Description

Description of model inputs including:

- internal data sources
- external data sources
- data transformations
- data limitations

---

### Governance and Monitoring

Description of model governance framework, including:

- monitoring processes
- performance review procedures
- change management
- escalation procedures

---

## AI-Assisted Sections (Human Review Required)

These sections involve more analytical interpretation.

AI may assist with drafting but requires validator review.

### Testing Summary

Summary of validation testing activities including:


- backtesting
- benchmarking
- sensitivity testing
- scenario analysis

Summary of PR testing activities including:

- ongoing monitoring

---

### Outcome Analysis

Interpretation of testing results and model performance.

AI may summarize patterns observed in testing outputs.

---

### Limitations

Discussion of known model limitations based on documentation and validation review.

---

## Human-Owned Sections

These sections require validator judgment and are not automatically generated.

### Findings

Description of validation issues identified during review.

The system may help structure findings but does not originate them.

---

### Validation Conclusion

Final assessment of model adequacy.

This section must be written by the validator.

---

## Future Section Support

Future versions may support additional sections such as:

- conceptual soundness assessment
- implementation testing
- monitoring framework evaluation