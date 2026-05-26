---
id: prototype-sprint01-m01
type: prototype
status: draft
owner: "@module-owner-m01"
version: 0.1
last_updated: 2026-05-26
parent: modules/m01_project_initialization/index.md
tags: [prototype, m01, ui, prompt, sprint-01]
---

# Prototype Prompt — Sprint 01: Project Initialization

> ⚠️ **This is a generated prompt derived from the UPE knowledge base (`master.md` and M01 module artifacts). It is NOT a manually maintained source of truth. If this prompt contradicts master, master wins.**

---

## System Context

You are building a UI prototype for **UPE (Unified Project Execution)** — an enterprise platform for engineering project management. This prototype demonstrates the **Project Initialization & Provisioning** module (M01), which automates the creation and configuration of new project environments.

**Technology Stack:** React + TypeScript + Tailwind CSS (or similar modern stack)  
**Target:** Clickable prototype / MVP for stakeholder demo

---

## Data Objects

Use these data objects in the prototype:

### Project
```typescript
interface Project {
  id: string;
  name: string;
  code: string;
  type: { id: string; name: string };
  template: { id: string; name: string };
  client: { name: string; id: string };
  gbu: string;
  location: string;
  status: 'seed' | 'draft' | 'provisioning' | 'partial' | 'active';
  disciplines: Discipline[];
  members: ProjectMember[];
  workspaces: {
    teamsUrl?: string;
    sharepointUrl?: string;
    cdeUrl?: string;
    plannerUrl?: string;
  };
  provisioningTasks: ProvisioningTask[];
  createdAt: Date;
}
```

### ProjectMember
```typescript
interface ProjectMember {
  user: { id: string; name: string; email: string; avatar: string };
  role: { id: string; name: string };
  startDate: Date;
}
```

### ProvisioningTask
```typescript
interface ProvisioningTask {
  id: string;
  type: 'erp_setup' | 'm365_provision' | 'cde_provision' | 'data_model_init' | 'access_setup';
  targetSystem: string;
  status: 'pending' | 'running' | 'completed' | 'failed' | 'retrying';
  startedAt?: Date;
  completedAt?: Date;
  errorMessage?: string;
  retryCount: number;
}
```

### Template
```typescript
interface ProjectTemplate {
  id: string;
  name: string;
  description: string;
  projectClass: string;
  estimatedSetupDuration: string;
  includedTools: string[];
  defaultChannels: string[];
}
```

---

## Screens to Build

### Screen 1: Project Creation Wizard (Multi-Step)

**Step 1: Project Type & Template Selection**
- Grid/card view of project types (Buildings, Energy, Transport, Water, etc.)
- After selecting type, show available templates with descriptions
- Show "Similar Projects" sidebar (3 items with similarity scores) — collapsible

**Step 2: Project Details**
- Form fields: Project Name (auto-suggested from CRM), Project Code (from ERP), Client, Location
- Auto-populated from CRM opportunity when available
- Validation indicator (green checkmarks for completed fields)

**Step 3: Team Setup**
- Search and add team members (mock Azure AD search)
- Assign roles from dropdown (Project Manager, Lead Engineer, Designer, etc.)
- Show org structure context

**Step 4: Review & Submit**
- Summary of all choices
- Estimated provisioning time
- Submit button with confirmation dialog

### Screen 2: Provisioning Status Dashboard

**Layout:** Left sidebar with project info, main area with provisioning progress

**Provisioning Pipeline Visual:**
- Horizontal pipeline showing steps: ERP → M365 → CDE → Data Model → Standards
- Each step shows icon with status (spinning for running, checkmark for complete, X for failed)
- Progress bar at top
- Failed steps show error message and "Retry" button
- "View Details" link for each step showing JSON payload

**Real-time updates:** Simulate progress with timed transitions (2-3 seconds per step)

### Screen 3: Project Dashboard (Post-Provisioning)

**Layout:** Dashboard with cards/sections

- **Project Overview Card:** Name, code, type, client, status (Active), team size
- **Quick Links Card:** Teams URL, SharePoint URL, CDE URL, Planner URL — clickable buttons that show URLs
- **Team Card:** List of team members with roles, avatars
- **Recent Activity Feed:** Mock events (e.g., "Teams team created", "CDE workspace provisioned", "Standards loaded")

### Screen 4: Template Library (Admin)

- Grid view of all templates
- Each template card shows: Name, description, supported project types, estimated setup time
- "Preview" button showing template configuration
- Status badge (Active, Draft, Deprecated)

### Screen 5: Access/Team Management

- Team member list with role badges
- Add member button (opens search dialog)
- Role assignment dropdown
- Start/end date for temporary access
- Bulk actions: Add multiple members from template default roles

---

## UX Assumptions

- **Design system:** Clean, professional enterprise UI (similar to Azure Portal or Jira)
- **Color scheme:** Blue primary (#4472C4), green for success (#70AD47), amber for warning (#FFC000), red for error (#FF0000)
- **Navigation:** Left sidebar with: Dashboard, Projects, Templates, Team, Settings
- **Responsive:** Desktop-first, tablet-second, mobile is low priority
- **Language:** English (MVP), future: multilingual
- **Notifications:** Toast notifications for provisioning events
- **Empty states:** Helpful messages when no projects exist ("Create your first project")

---

## Mock Data

Provide realistic mock data for:
- 3 project types: Buildings, Energy, Transport
- 4 templates: "Standard Building Project", "Energy Assessment", "Infrastructure Design", "Blank Project"
- 10 team members with realistic names and roles
- 1 completed project (for dashboard demo)
- 1 in-progress provisioning (for status demo)

---

## Source References

This prompt is derived from:
- `knowledge-base/master.md` — UPE vision, domains, architecture
- `knowledge-base/modules/m01_project_initialization/requirements.md` — Functional requirements
- `knowledge-base/modules/m01_project_initialization/data_model.md` — Entities and ERD
- `knowledge-base/modules/m01_project_initialization/workflows.md` — Provisioning flow
- `knowledge-base/architecture/module_interfaces.md` — Interface contracts
