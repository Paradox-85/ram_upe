---
id: m01-data-model
type: data-model
status: in-review-demo
owner: "@module-owner-m01"
version: 1.0
last_updated: 2026-05-26
parent: modules/m01_project_initialization/index.md
tags: [m01, data-model, entities, erd]
---

# M01 Data Model — Project Initialization

## Entity Relationship Diagram

```mermaid
erDiagram
    Project ||--o{ ProjectMembership : "has members"
    Project ||--|| ProjectTemplate : "created from"
    Project ||--|| ProjectType : "classified as"
    Project ||--o{ Discipline : "includes"
    Project ||--o{ ProvisioningJob : "undergoes"
    Project ||--|| CDEWorkspace : "provisions"
    Project ||--|| CollaborationSpace : "provisions"
    Project ||--o{ Standard : "references"
    Project }o--|| ReferenceDataSet : "uses"

    ProjectTemplate ||--o{ ProjectType : "supports"
    ProjectTemplate }o--|| ReferenceDataSet : "seeds from"

    User ||--o{ ProjectMembership : "holds"
    User }o--|| Role : "assigned"
    User }o--|| Discipline : "belongs to"

    ProvisioningJob ||--o{ ProvisioningTask : "contains"

    Project {
        uuid project_id PK
        string name
        string project_code
        uuid project_type_id FK
        uuid template_id FK
        string client_name
        string client_id
        string gbu
        string location
        string status
        date start_date
        date target_end_date
        decimal estimated_value
        string currency
        string opportunity_id
        datetime created_at
        string created_by
    }

    ProjectTemplate {
        uuid template_id PK
        string name
        string description
        string project_class
        string[] supported_types
        object folder_structure
        object tool_configuration
        object standards_set
        string[] default_roles
        string[] default_channels
        string status
        integer version
    }

    ProjectType {
        uuid type_id PK
        string name
        string code
        string description
        string gbu
    }

    Discipline {
        uuid discipline_id PK
        string name
        string code
        string description
    }

    Role {
        uuid role_id PK
        string name
        string code
        string description
        string[] permissions
    }

    User {
        uuid user_id PK
        string display_name
        string email
        string department
        string job_title
        string office_location
        string azure_ad_id
        string discipline_id FK
    }

    ProjectMembership {
        uuid membership_id PK
        uuid project_id FK
        uuid user_id FK
        uuid role_id FK
        date start_date
        date end_date
        string status
    }

    CDEWorkspace {
        uuid workspace_id PK
        uuid project_id FK
        string platform
        string workspace_url
        string template_workspace_id
        string status
        datetime provisioned_at
    }

    CollaborationSpace {
        uuid space_id PK
        uuid project_id FK
        string teams_team_id
        string teams_team_url
        string sharepoint_site_url
        string planner_plan_id
        string status
        datetime provisioned_at
    }

    ProvisioningJob {
        uuid job_id PK
        uuid project_id FK
        string status
        datetime started_at
        datetime completed_at
        string triggered_by
        integer retry_count
    }

    ProvisioningTask {
        uuid task_id PK
        uuid job_id FK
        string task_type
        string target_system
        string status
        string input_payload
        string output_payload
        string error_message
        datetime started_at
        datetime completed_at
        integer retry_count
    }

    Standard {
        uuid standard_id PK
        string name
        string code
        string version
        string discipline
        string document_url
    }

    ReferenceDataSet {
        uuid dataset_id PK
        string name
        string type
        string version
        string source
    }
```

---

## Entity Definitions

### ENT-Project
The central entity representing an engineering project in UPE.

| Attribute | Type | Required | Description |
|---|---|---|---|
| `project_id` | UUID | ✅ | Primary key, auto-generated |
| `name` | String(200) | ✅ | Human-readable project name |
| `project_code` | String(20) | ✅ | ERP project code (from Maconomy) |
| `project_type_id` | UUID (FK) | ✅ | Reference to ProjectType |
| `template_id` | UUID (FK) | ✅ | Template used for provisioning |
| `client_name` | String(200) | ✅ | Client organization name |
| `client_id` | String(50) | ✅ | Client ID from CRM |
| `gbu` | String(10) | ✅ | Global Business Unit code |
| `location` | String(200) | ✅ | Project location / geography |
| `status` | Enum | ✅ | Current lifecycle status |
| `opportunity_id` | String(50) | — | CRM opportunity reference |

**Status values:** `seed`, `draft`, `provisioning`, `partial`, `active`, `suspended`, `closed`, `archived`

### ENT-ProjectTemplate
Reusable configuration template for project provisioning.

| Attribute | Type | Required | Description |
|---|---|---|---|
| `template_id` | UUID | ✅ | Primary key |
| `name` | String(100) | ✅ | Template name |
| `project_class` | String(50) | ✅ | Class/category this template serves |
| `folder_structure` | JSON | ✅ | Folder tree definition |
| `tool_configuration` | JSON | ✅ | Tool provisioning config |
| `standards_set` | JSON | ✅ | Standards to associate |
| `default_roles` | String[] | ✅ | Default role set |
| `default_channels` | String[] | ✅ | Default Teams channels |

### ENT-ProvisioningJob
Tracks the provisioning process for a project from start to finish.

| Attribute | Type | Required | Description |
|---|---|---|---|
| `job_id` | UUID | ✅ | Primary key |
| `project_id` | UUID (FK) | ✅ | Project being provisioned |
| `status` | Enum | ✅ | `pending`, `running`, `completed`, `failed`, `partial` |
| `retry_count` | Integer | ✅ | Number of retries attempted |

### ENT-ProvisioningTask
Individual provisioning step within a job (e.g., "Create Teams team", "Provision CDE workspace").

| Attribute | Type | Required | Description |
|---|---|---|---|
| `task_id` | UUID | ✅ | Primary key |
| `job_id` | UUID (FK) | ✅ | Parent job |
| `task_type` | String(50) | ✅ | `m365_provision`, `cde_provision`, `erp_setup`, `access_setup`, `data_model_init` |
| `target_system` | String(50) | ✅ | External system name |
| `status` | Enum | ✅ | `pending`, `running`, `completed`, `failed`, `skipped`, `retrying` |
