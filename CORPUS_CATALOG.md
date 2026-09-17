# PolicyPulse AI — Knowledge Gaps

## Purpose

This document defines questions for which the synthetic NovaCore Technologies
enterprise corpus intentionally does not provide a definitive answer.

These gaps are part of the ground truth for evaluating whether PolicyPulse AI
can recognize missing organizational knowledge instead of generating an
unsupported answer.

---

# Knowledge Gap Matrix

| ID | Question | Related Departments | Expected System Behavior |
|---|---|---|---|
| KG001 | Who gives final approval for vendor suspension after a compliance violation? | Procurement, Legal | Identify knowledge gap |
| KG002 | Who gives final approval for a permanent fully remote work arrangement? | HR, IT | Identify knowledge gap |
| KG003 | Who has final authority to close a major security-related operational incident? | Operations, IT | Identify knowledge gap |
| KG004 | What is the exact procedure for transferring a vendor between departments? | Procurement, Finance, Legal | Identify knowledge gap |
| KG005 | Who approves an employee's access to a newly introduced enterprise application? | HR, IT | Identify knowledge gap |
| KG006 | What is the escalation procedure when a critical vendor fails an SLA? | Procurement, Operations | Identify knowledge gap |

---

# KG001 — Vendor Suspension Authority

## Question

Who gives final approval for vendor suspension after a compliance violation?

## Relevant Documents

- P02 — Vendor Onboarding
- L02 — Vendor Legal Guidelines

## Ground Truth

The corpus describes vendor suspension/review responsibilities but does not
define the final approving authority.

## Expected Behavior

The system should state that the available corpus does not provide a
definitive final authority.

It should identify the relevant evidence and avoid inventing an approving
role.

---

# KG002 — Permanent Fully Remote Approval

## Question

Who gives final approval for a permanent fully remote work arrangement?

## Relevant Documents

- H02 — Remote Work Policy
- H03 — Employee Handbook
- I02 — Security Policy

## Ground Truth

The corpus defines ordinary remote-work eligibility and security
requirements but does not define the final authority for a permanent fully
remote arrangement.

## Expected Behavior

The system should identify this as a knowledge gap.

---

# KG003 — Major Security Incident Closure

## Question

Who has final authority to close a major security-related operational
incident?

## Relevant Documents

- O01 — Operations SOP
- O02 — SLA Policy
- I02 — Security Policy

## Ground Truth

The corpus defines incident handling and technical/security responsibilities
but does not specify a final authority for closing a major security-related
operational incident.

## Expected Behavior

The system should not invent a final approving authority.

---

# KG004 — Vendor Transfer Between Departments

## Question

What is the exact procedure for transferring a vendor between departments?

## Relevant Documents

- P02 — Vendor Onboarding
- P03 — Procurement Thresholds
- L02 — Vendor Legal Guidelines

## Ground Truth

The corpus describes vendor onboarding and procurement processes but does not
provide a definitive procedure specifically governing transfer of an existing
vendor between departments.

## Expected Behavior

Identify the missing procedure rather than combining unrelated steps and
presenting them as an official transfer procedure.

---

# KG005 — New Enterprise Application Access

## Question

Who approves an employee's access to a newly introduced enterprise
application?

## Relevant Documents

- H03 — Employee Handbook
- I02 — Security Policy
- I03 — IT Standards

## Ground Truth

The corpus specifies that authorized access requests and manager approval are
required in general, but it does not establish a definitive final authority
specifically for access to a newly introduced enterprise application.

## Expected Behavior

The system should identify the limitation of the available evidence.

---

# KG006 — Critical Vendor SLA Failure

## Question

What is the escalation procedure when a critical vendor fails an SLA?

## Relevant Documents

- P01 — Procurement Policy
- P02 — Vendor Onboarding
- O02 — SLA Policy
- O03 — Escalation Matrix

## Ground Truth

The corpus defines general procurement, vendor and operational escalation
processes, but does not provide a definitive cross-department procedure
specifically for a critical vendor SLA failure.

## Expected Behavior

The system should identify the knowledge gap instead of constructing an
unsupported procedure.

---

# Evaluation Principle

For all knowledge-gap questions, PolicyPulse AI should prioritize:

1. Evidence retrieval
2. Source attribution
3. Recognition of missing information
4. Transparent uncertainty
5. No unsupported assumptions
6. No fabricated organizational rules

A correct response to a knowledge-gap question is therefore not necessarily
a direct answer.

A correct response may be:

> The available enterprise corpus does not provide a definitive answer to this
> question.

The system should then identify the closest relevant documents and explain
what those documents actually establish.
