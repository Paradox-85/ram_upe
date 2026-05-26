---
id: arch-overview
type: architecture
status: approved
owner: "@chief-architect"
version: 1.0
last_updated: 2026-05-26
parent: master.md
tags: [architecture, overview, cde, integration]
---

# Architecture Overview

## UPE Position in the Technology Landscape

UPE is NOT a CDE. UPE is NOT a DMS. UPE is NOT a replacement for engineering authoring tools.

**CDE is necessary but not the enterprise brain.** CDEs like Autodesk ACC and ProjectWise serve as the project-level system of record for document management, version control, approvals, and design coordination. They are project-centric, not enterprise-centric.

**UPE sits ABOVE CDEs and authoring tools** as a coordination and intelligence layer:

```mermaid
graph TB
    subgraph "What UPE is NOT"
        CDE["CDE<br/>(ACC / ProjectWise)<br/><i>Project system of record</i>"]
        Tools["Authoring Tools<br/>(Revit / Bentley / AVEVA)<br/><i>Production engines</i>"]
    end

    subgraph "What UPE IS"
        UPE_Core["UPE Coordination & Intelligence Layer"]
        UPE_AI["AI Decision Support"]
        UPE_Orchestration["Cross-System Orchestration"]
        UPE_Knowledge["Enterprise Knowledge Graph"]
        UPE_UX["Unified Collaboration UX"]
    end

    subgraph "Enterprise Systems"
        CRM["CRM"]
        ERP["ERP"]
        HR["HR / Azure AD"]
    end

    Tools --> CDE
    CDE --> UPE_Core
    CRM --> UPE_Core
    ERP --> UPE_Core
    HR --> UPE_Core
    UPE_Core --> UPE_AI
    UPE_Core --> UPE_Orchestration
    UPE_Core --> UPE_Knowledge
    UPE_Core --> UPE_UX

    style UPE_Core fill:#4472C4,color:#fff
    style UPE_AI fill:#5B9BD5,color:#fff
    style UPE_Orchestration fill:#5B9BD5,color:#fff
    style UPE_Knowledge fill:#5B9BD5,color:#fff
    style UPE_UX fill:#5B9BD5,color:#fff
```

---

## Build vs. Buy Principle

**Buy commodity layers. Build differentiating layers.**

### Buy (Don't reinvent)
| Layer | Recommended | Rationale |
|---|---|---|
| CDE | Autodesk ACC / Bentley ProjectWise | Market-leading, vendor-supported |
| iPaaS | MuleSoft / Workato / Dell Boomi | Proven integration platforms |
| Data Lake | Microsoft Fabric / OneLake | Enterprise scale, Azure-native |
| Identity & Security | Azure AD, Microsoft Entra | Already in E5 license |
| Workflow Engine | Power Automate / Camunda | Commodity orchestration |

### Build (Strategic differentiators)
| Layer | What to Build | Why |
|---|---|---|
| AI-Ready Engineering Decomposition | Document decomposition, metadata enrichment, chunking for LLM | Domain-specific, no vendor provides this |
| Cross-Platform Knowledge Graph | Project memory, semantic relationships, cross-project learning | Enterprise moat |
| Decision Intelligence Layer | Margin-aware design intelligence, risk detection | Ramboll-specific business logic |
| Unified Collaboration UX | Cross-tool project dashboards, multi-system issue resolution | Missing in current market |
| Engineering-Specific AI Agents | Domain agents for each discipline workflow | Competitive advantage |

---

## Component Architecture

```mermaid
graph LR
    subgraph "User-Facing"
        Portal["UPE Portal<br/>(React / Teams Tab)"]
        Dashboards["Power BI<br/>Dashboards"]
        Planner["Planner<br/>Task Boards"]
    end

    subgraph "Orchestration"
        PA["Power Automate<br/>Flows"]
        Orch["Orchestration<br/>Engine"]
    end

    subgraph "Intelligence"
        AICore["AI Core<br/>(Azure OpenAI)"]
        KGraph["Knowledge<br/>Graph"]
        Rules["Rules<br/>Engine"]
    end

    subgraph "Integration"
        APIHub["API Hub<br/>(Azure APIM)"]
        SP["SharePoint<br/>Connector"]
        TeamsConn["Teams<br/>Connector"]
    end

    subgraph "External Systems"
        CRMExt["CRM"]
        ERPExt["Maconomy"]
        ADExt["Azure AD"]
        ACExt["Autodesk ACC"]
        PWExt["ProjectWise"]
    end

    Portal --> Orch
    Dashboards --> APIHub
    Planner --> Orch

    Orch --> APIHub
    Orch --> AICore
    AICore --> KGraph
    AICore --> Rules

    APIHub --> SP
    APIHub --> TeamsConn
    APIHub --> CRMExt
    APIHub --> ERPExt
    APIHub --> ADExt
    APIHub --> ACExt
    APIHub --> PWExt
```

---

## Key Integration Points

| Integration | Direction | Protocol | Priority |
|---|---|---|---|
| CRM → UPE | Project seed data on won opportunity | REST API / Webhook | Phase 1 |
| Azure AD → UPE | User identity, org structure, roles | Graph API | Phase 1 |
| Maconomy → UPE | Project codes, cost centers | REST API | Phase 1 |
| Teams/SharePoint ↔ UPE | Collaboration spaces, document stores | Graph API, Power Automate | Phase 1 |
| Autodesk ACC ↔ UPE | CDE workspace provisioning, file metadata | ACC API / Webhooks | Phase 1 |
| ProjectWise ↔ UPE | CDE workspace (alternative stack) | PW API | Phase 2 |
| Workday → UPE | HR data, skills, org hierarchy | REST API | Phase 2 |
| Power BI ← UPE | Analytics and dashboards | DirectQuery / Semantic models | Phase 1 |

---

## References
- **Source:** `src/loop/loop.md` (Copilot Sparing Session — 9-layer architecture)
- **Source:** `docs/brainstorming.md` (Tech stack, module architecture)
- **Related:** [module_interfaces.md](module_interfaces.md) — detailed interface contracts for M01
