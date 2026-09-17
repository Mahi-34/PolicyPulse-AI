---
department: IT
document_name: IT_Standards
document_type: XLSX
source_file: data/raw/IT/IT_Standards.xlsx
---

| Document ID      | IT-MAT-001       |
|------------------|------------------|
| Department       | IT               |
| Document Name    | IT Standards     |
| Document Type    | Standards Matrix |
| Version          | 2026             |
| Effective Date   | 01-Apr-2026      |
| Owner Department | IT               |

| Device Type       | Standard Lifecycle               | Minimum Security Controls                                    | Primary Use                | Notes                   |
|-------------------|----------------------------------|--------------------------------------------------------------|----------------------------|-------------------------|
| Laptop            | 4 years                          | MFA, encryption, approved endpoint controls                  | General employee computing | IT assignment required  |
| Desktop           | 5 years                          | MFA where applicable, encryption, approved endpoint controls | Fixed workstation roles    | IT assignment required  |
| Mobile            | 3 years                          | MFA where supported, device security controls                | Business communication     | Company-approved device |
| Tablet            | 3 years                          | MFA where supported, device security controls                | Approved business use      | Company-approved device |
| Network Equipment | Lifecycle based on IT assessment | Configuration and access controls                            | Infrastructure             | IT-managed              |
| Peripherals       | Lifecycle based on condition     | Applicable device controls                                   | Business support           | Tracked where required  |

| Access Category   | Example Systems                   | MFA                                 | Review Frequency        | Approval/Input                         |
|-------------------|-----------------------------------|-------------------------------------|-------------------------|----------------------------------------|
| Standard          | Finance/HR business systems       | Required where supported/designated | Quarterly               | Authorized manager request             |
| Restricted        | Production systems                | Required                            | Monthly or risk-based   | Additional authorization as required   |
| Privileged        | Administrative systems            | Required                            | Monthly                 | Elevated authorization and IT review   |
| Remote Access     | Approved organizational resources | Required                            | Quarterly or risk-based | Authorized request + security controls |

| Control                     | Standard                                               | Applies To              | Review/Trigger             | Owner         |
|-----------------------------|--------------------------------------------------------|-------------------------|----------------------------|---------------|
| Multi-Factor Authentication | Required where supported and designated                | Organizational accounts | Access provisioning/review | IT            |
| Encryption                  | Required for designated organizational devices         | Company devices         | Asset lifecycle            | IT            |
| Credential Protection       | Credentials must not be shared                         | All users               | Continuous                 | Employee + IT |
| Secure Remote Access        | Approved devices, authentication and security controls | Remote workers          | Remote-work arrangement    | IT            |
| Incident Reporting          | Report suspected security incidents to IT              | All users               | When incident suspected    | Employee + IT |

| Lifecycle Event     | HR Action                      | IT Action                                       | Access Control                                 | Asset Control                                                  | Deadline                |
|---------------------|--------------------------------|-------------------------------------------------|------------------------------------------------|----------------------------------------------------------------|-------------------------|
| New Hire            | Create/confirm employee record | Provision authorized account and prepare assets | Based on authorized request + manager approval | Assign and record asset                                        | Before/at joining       |
| Role Change         | Update role/lifecycle record   | Review and modify access/assets as applicable   | Review privileges for new role                 | Review assigned assets                                         | When change is approved |
| Department Transfer | Update department information  | Review access and assets for new department     | Modify access as authorized                    | Review assignment                                              | At transfer             |
| Exit                | Complete separation process    | Disable organizational access                   | Access disabled by final working day           | Assets returned by final working day unless approved exception | Final working day       |