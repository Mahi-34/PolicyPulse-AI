---
department: Operations
document_name: Escalation_Matrix
document_type: XLSX
source_file: data/raw/Operations/Escalation_Matrix.xlsx
---

| Document ID      | OPS-MAT-001       |
|------------------|-------------------|
| Department       | Operations        |
| Document Name    | Escalation Matrix |
| Document Type    | Escalation Matrix |
| Version          | 2026              |
| Effective Date   | 01-Apr-2026       |
| Owner Department | Operations        |

| Priority      | Trigger                             | Initial Owner   | First Escalation                         | Escalation Deadline   | Business Coordination                                                |
|---------------|-------------------------------------|-----------------|------------------------------------------|-----------------------|----------------------------------------------------------------------|
| P1 — Critical | Critical business disruption        | Operations      | IT Duty Manager                          | 30 minutes            | Operations coordinates business impact and stakeholder communication |
| P2 — High     | Significant service/business impact | Operations      | IT Service Lead where technology-related | 2 hours               | Operations coordinates impact and escalation                         |
| P3 — Normal   | Limited operational impact          | Operations      | Department Manager where required        | 1 business day        | Routine operational coordination                                     |

| Incident Type          | Example Trigger                             | Primary Technical Owner   | Operations Role                                                         | Initial Response   |
|------------------------|---------------------------------------------|---------------------------|-------------------------------------------------------------------------|--------------------|
| Application Outage     | Business application unavailable            | IT                        | Coordinate business impact and communication                            | 30 minutes for P1  |
| Network Outage         | Material connectivity disruption            | IT                        | Coordinate business impact and escalation                               | 30 minutes for P1  |
| Security Incident      | Suspected security event                    | IT/Security               | Coordinate operational impact; follow restricted communication controls | Priority-based     |
| Data Access Issue      | Authorized user cannot access required data | IT                        | Coordinate business requirement                                         | Priority-based     |
| Hardware Failure       | Critical organizational hardware failure    | IT                        | Coordinate affected business service                                    | Priority-based     |
| Infrastructure Failure | Infrastructure service disruption           | IT                        | Coordinate operational impact                                           | Priority-based     |

| Priority   | Response Target   | Resolution Target   | P1 Update Requirement                                               | Escalation Reference   | Exception Examples                                                                          |
|------------|-------------------|---------------------|---------------------------------------------------------------------|------------------------|---------------------------------------------------------------------------------------------|
| P1         | 30 minutes        | 4 hours             | Initial update within 60 minutes; subsequent at least every 2 hours | Incident Escalation    | Force majeure, planned maintenance, third-party failure, restricted security communications |
| P2         | 2 hours           | 8 hours             | As appropriate                                                      | Incident Escalation    | Force majeure, planned maintenance, third-party failure                                     |
| P3         | 1 business day    | 3 business days     | As appropriate                                                      | Incident Escalation    | Force majeure, planned maintenance, third-party failure                                     |

| Role                   | Department          | Responsibility                                                  | Trigger                            | Contact Method                    |
|------------------------|---------------------|-----------------------------------------------------------------|------------------------------------|-----------------------------------|
| Operations Coordinator | Operations          | Coordinate business incident                                    | Operational incident               | Designated organizational channel |
| IT Duty Manager        | IT                  | Technical escalation for critical technology incidents          | P1 technology incident             | Designated organizational channel |
| IT Service Lead        | IT                  | Technical escalation for high-priority technology incidents     | P2 technology incident             | Designated organizational channel |
| Department Manager     | Business Department | Business decision and coordination                              | P3 or business-specific escalation | Designated organizational channel |
| Legal Representative   | Legal               | Legal guidance when incident has contractual/legal implications | Applicable legal issue             | Designated organizational channel |