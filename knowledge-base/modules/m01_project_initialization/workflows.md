---
id: m01-workflows
type: workflow
status: in-review-demo
owner: "@module-owner-m01"
version: 1.0
last_updated: 2026-05-26
parent: modules/m01_project_initialization/index.md
tags: [m01, workflow, state-machine, flowchart]
---

# M01 Workflows — Project Initialization

## Project Lifecycle State Machine

```mermaid
stateDiagram-v2
    [*] --> Seed : CRM Opportunity Won
    Seed --> Draft : PM Opens Creation Wizard
    Draft --> InReview : PM Submits for Approval
    InReview --> Draft : Revision Requested
    InReview --> Provisioning : Approved
    Provisioning --> Active : All Tasks Completed
    Provisioning --> Partial : Some Tasks Failed
    Partial --> Provisioning : Manual Retry
    Partial --> Active : All Remaining Tasks Completed
    Provisioning --> Failed : Critical Task Failed (max retries)
    Failed --> Provisioning : Force Retry
    Active --> Suspended : PM Pauses Project
    Suspended --> Active : PM Resumes
    Active --> Closed : Project Closeout
    Closed --> Archived : Retention Policy
```

---

## End-to-End Project Initialization Flow

```mermaid
flowchart TD
    Start([CRM: Opportunity Won]) --> Seed[WF-M01-010: Create Project Seed]
    Seed --> Wizard[WF-M01-020: PM Opens Creation Wizard]

    Wizard --> SelectType{Select Project Type}
    SelectType --> LoadTemplate[WF-M01-030: Load Template]
    LoadTemplate --> CheckKG[WF-M01-035: Query Knowledge Graph<br/>for Similar Projects]

    CheckKG --> FillMeta[WF-M01-040: Fill Project Metadata<br/>Name, Code, Location, Client]
    FillMeta --> AssignTeam[WF-M01-050: Assign Initial Team<br/>Roles & Disciplines]

    AssignTeam --> Review{PM Reviews & Submits}
    Review -->|Revise| Wizard
    Review -->|Submit| CreateERP[WF-M01-060: Create Project in ERP<br/>IF-M01-ERP-001]

    CreateERP -->|Success| CreateM365[WF-M01-070: Provision M365<br/>IF-M01-M365-001]
    CreateERP -->|Failure| HandleERPError[Log Error<br/>Queue Retry]

    CreateM365 -->|Success| CreateCDE[WF-M01-080: Provision CDE<br/>IF-M01-CDE-001]
    CreateM365 -->|Failure| HandleM365Error[Log Error<br/>Queue Retry]

    CreateCDE -->|Success| InitData[WF-M01-090: Initialize Data Model<br/>Entities & Relationships]
    CreateCDE -->|Failure| HandleCDEError[Log Error<br/>Queue Retry]

    InitData --> SeedStandards[WF-M01-100: Seed Standards<br/>& Reference Data]
    SeedStandards --> Notify[WF-M01-110: Notify PM<br/>Project Ready]
    Notify --> Active([Project Active ✅])

    HandleERPError --> PartialState[Mark Partial State<br/>Notify Support]
    HandleM365Error --> PartialState
    HandleCDEError --> PartialState
    PartialState --> ManualRetry[Manual Retry<br/>or Force Retry]
    ManualRetry --> CreateERP

    style Start fill:#4472C4,color:#fff
    style Active fill:#70AD47,color:#fff
    style PartialState fill:#FFC000,color:#000
    style HandleERPError fill:#FF0000,color:#fff
    style HandleM365Error fill:#FF0000,color:#fff
    style HandleCDEError fill:#FF0000,color:#fff
```

---

## Workflow Steps Detail

### WF-M01-010: Create Project Seed
- **Trigger:** CRM webhook (opportunity status = "Won") or manual trigger
- **Actor:** System (automated)
- **Input:** Opportunity data from CRM (IF-M01-CRM-001)
- **Output:** Project record with status `seed`
- **Error:** If CRM data incomplete → create `draft` project with missing fields flagged

### WF-M01-020: Open Creation Wizard
- **Trigger:** PM navigates to "New Project" or clicks link from seed notification
- **Actor:** Project Manager
- **Input:** Project seed (if exists) or blank form
- **Output:** Draft project in wizard state

### WF-M01-030: Load Template
- **Trigger:** PM selects project type/class
- **Actor:** System
- **Input:** Project type, class, GBU
- **Output:** Template configuration loaded (IF-M01-TEMPLATE-001)

### WF-M01-035: Query Knowledge Graph
- **Trigger:** Template loaded
- **Actor:** System
- **Input:** Project type, client, location, disciplines
- **Output:** List of similar projects and suggested standards (IF-M01-KG-001)
- **Note:** Non-blocking — failure does not prevent creation

### WF-M01-040: Fill Project Metadata
- **Trigger:** Template loaded
- **Actor:** Project Manager
- **Input:** Template defaults + PM overrides
- **Output:** Complete project metadata

### WF-M01-050: Assign Initial Team
- **Trigger:** Metadata complete
- **Actor:** Project Manager
- **Input:** User search from Azure AD (IF-M01-HR-001)
- **Output:** Initial team with roles assigned

### WF-M01-060: Create Project in ERP
- **Trigger:** PM submits creation
- **Actor:** System
- **Input:** Project metadata
- **Output:** ERP project code and financial context (IF-M01-ERP-001)

### WF-M01-070: Provision M365
- **Trigger:** ERP code assigned
- **Actor:** System
- **Input:** Template config + team + project metadata
- **Output:** Teams team, SharePoint site, Planner board URLs (IF-M01-M365-001)

### WF-M01-080: Provision CDE
- **Trigger:** M365 provisioning complete
- **Actor:** System
- **Input:** Template config + project metadata
- **Output:** CDE workspace URL and folder structure (IF-M01-CDE-001)

### WF-M01-090: Initialize Data Model
- **Trigger:** CDE provisioning complete
- **Actor:** System
- **Input:** Project metadata, template, team
- **Output:** All data model entities created (Project, Memberships, Workspaces)

### WF-M01-100: Seed Standards & Reference Data
- **Trigger:** Data model initialized
- **Actor:** System
- **Input:** Template standards set
- **Output:** Standards linked to project, reference data loaded

### WF-M01-110: Notify PM
- **Trigger:** All provisioning tasks complete
- **Actor:** System
- **Input:** Project record with all URLs
- **Output:** Email/Teams notification to PM with project dashboard link

---

## Failure & Recovery Workflow

```mermaid
flowchart LR
    Task[Provisioning Task] -->|Execute| Result{Result}
    Result -->|Success| Next[Next Task]
    Result -->|Failure| Retry1[Retry Attempt 1<br/>5 min delay]
    Retry1 --> Result1{Result}
    Result1 -->|Success| Next
    Result1 -->|Failure| Retry2[Retry Attempt 2<br/>15 min delay]
    Retry2 --> Result2{Result}
    Result2 -->|Success| Next
    Result2 -->|Failure| Retry3[Retry Attempt 3<br/>30 min delay]
    Retry3 --> Result3{Result}
    Result3 -->|Success| Next
    Result3 -->|Failure| Alert[Alert PM & Support<br/>Mark as Partial/Failed]
    Alert --> ManualAction{Manual Action}
    ManualAction -->|Force Retry| Task
    ManualAction -->|Skip| Next
    ManualAction -->|Abort| Abort[Abort Provisioning]
```
