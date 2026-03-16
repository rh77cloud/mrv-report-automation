# Validation Intake Schema

## Purpose

The Validation Intake step captures current-cycle review context that may not be fully reflected in source documents.

This includes:

- what changed since the last validation
- what stayed the same
- whether current monitoring results were reviewed
- whether new concerns were identified
- whether any concerns may need to be structured into findings

The intake step improves the quality of downstream report drafting, testing discussion, and finding generation.


### Current-cycle review context

This means your system now has two distinct knowledge sources:

1. Static / document-based knowledge

- standards
- templates
- prior reports
- model docs
- monitoring reports

2. Dynamic / review-cycle knowledge

- what changed
- what stayed the same
- what current concerns exist
- what areas need updated writeup
- what may become findings

That makes the tool much closer to how real validation reports are written.

---

## Design Principles

The intake form should:

- capture current-cycle context in a structured way
- use a mix of dropdowns, checkboxes, and short free-text inputs
- distinguish between factual updates and validator judgment
- support downstream generation modules
- remain lightweight in the MVP

The intake form is intended to supplement document-based evidence, not replace it.

---

## Core Intake Sections

### 1. Validation Context

Purpose:
Capture basic metadata for the current review.

Fields:

- validation_cycle
- review_date
- validation_type
- model_name
- model_id
- model_tier
- model_type
- business_line

Example validation types:

- Full Validation
- Periodic Review
- Targeted Review
- Change Review

---

### 2. Change Summary Since Prior Review

Purpose:
Capture material changes made since the prior validation or review.

Fields:

- methodology_changed
- data_appended
- data_source_changed
- variable_set_changed
- implementation_changed
- monitoring_framework_changed
- governance_or_controls_changed
- other_changes

For each field:
- Yes
- No
- Unknown

Optional:
- change_summary_notes

---

### 3. What Stayed the Same

Purpose:
Capture continuity since the prior review.

Fields:

- core_methodology_unchanged
- intended_use_unchanged
- major_data_sources_unchanged
- implementation_platform_unchanged
- key_assumptions_unchanged
- monitoring_approach_unchanged

For each field:
- Yes
- No
- Unknown

Optional:
- unchanged_summary_notes

---

### 4. Current-Cycle Materials Reviewed

Purpose:
Capture what materials were reviewed as part of the current cycle.

Fields:

- latest_model_documentation_reviewed
- latest_monitoring_results_reviewed
- latest_testing_outputs_reviewed
- change_log_reviewed
- prior_findings_status_reviewed
- implementation_documents_reviewed
- benchmark_results_reviewed

For each field:
- Yes
- No
- Not Available

Optional:
- materials_review_notes

---

### 5. Testing and Monitoring Context

Purpose:
Capture current-cycle testing context for downstream discussion drafting.

Fields:

- monitoring_results_period
- testing_results_period
- benchmark_used
- benchmark_name
- key_tests_performed
- notable_testing_observations
- notable_monitoring_observations

Examples of key_tests_performed:
- backtesting
- benchmarking
- sensitivity testing
- scenario analysis
- conceptual review
- implementation testing
- outcome analysis

---

### 6. Validator Observations and Concerns

Purpose:
Capture validator-identified issues, concerns, and areas requiring discussion.

Fields:

- key_concerns_identified
- key_model_challenges
- areas_requiring_stronger_writeup
- concerns_not_rising_to_finding
- strengths_or_positive_observations
- open_questions

These should be free-text fields.

---

### 7. Potential Findings Under Consideration

Purpose:
Capture issues that may need to be structured into formal findings.

Fields:

- potential_finding_1
- potential_finding_2
- potential_finding_3
- issue_findings_expected

Optional fields for each potential finding:
- category
- short_description
- evidence_summary
- possible_impact
- likely_finding
- notes

Example categories:
- Data
- Conceptual Soundness
- Technical Soundness
- Model Results
- Controls / Governance
- Implementation

---

## MVP Field Set

The MVP should keep the intake form lightweight.

Recommended MVP fields:

### Required
- validation_type
- model_name
- model_id
- model_tier
- model_type

### Recommended
- what_changed_since_prior_review
- what_stayed_the_same
- latest_monitoring_results_reviewed
- latest_testing_outputs_reviewed
- key_concerns_identified
- potential_findings_under_consideration
- additional_drafting_notes

---

## Example Usage in Downstream Modules

### Report Drafting
The intake form can support language such as:

- "The current review did not identify material changes to the core methodology since the prior validation."
- "Since the prior review, the dataset has been refreshed to incorporate more recent observations."
- "Monitoring results through the current review period were considered as part of this validation."

### Testing Analysis
The intake form can provide context such as:

- recent performance deterioration
- benchmark introduction this cycle
- monitoring period covered
- which tests were actually performed

### Finding Builder
The intake form can help distinguish:

- preliminary concerns
- confirmed findings
- concerns not elevated to findings
- legacy vs newly identified issues

---

## Governance Notes

The intake form should not:

- assign final findings
- assign final severity
- issue final conclusions
- replace validator judgment

The intake step is designed to improve drafting quality and preserve current-cycle context.

---

## Future Enhancements

Future versions may include:

- prior-cycle comparison fields
- remediation tracking inputs
- linked finding templates
- structured issue taxonomies
- validation manager review notes