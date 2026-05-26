---
id: prototype-sprint01-m01
type: prototype
status: in-progress
owner: "@module-owner-m01"
version: 0.1
last_updated: 2026-05-26
parent: ../../modules/m01_project_initialization/index.md
branch_note: >
  This is the canonical working copy on feature/m01-project-initialization.
  Derived from: modules/m01_project_initialization/data_model.md,
  requirements.md, and architecture/module_interfaces.md.
  Will be merged to main via PR #1 after architecture review.
  PR: https://github.com/Paradox-85/ram_upe/pull/1
tags: [prototype, m01, ui, prompt, sprint-01]
---

> 📝 **Canonical working copy** on branch `feature/m01-project-initialization`.
> Derived from approved architecture artifacts in `modules/m01_project_initialization/`
> and `architecture/module_interfaces.md`.
> Will enter `main` after [PR #1](https://github.com/Paradox-85/ram_upe/pull/1) is approved.

# Prototype Prompt — Sprint 01: M01 Project Initialization

> ⚠️ **This is a design validation prototype, not production code.** The purpose is to validate UX flows and data concepts with stakeholders before committing engineering resources to implementation. All mock data is simulated.

---

## Instructions

Copy the prompt below and paste it into **v0.dev**, **Replit**, or **Claude** to generate a clickable UI prototype. The prototype demonstrates the M01 (Project Initialization & Provisioning) module of the UPE platform.

**Tech stack:** React + TypeScript + TailwindCSS (or shadcn/ui). Mock data is acceptable — no backend required.

**Canonical data model reference:** [../../modules/m01_project_initialization/data_model.md](../../modules/m01_project_initialization/data_model.md)

> **Note on `estimated_setup_duration`:** This field appears in the Template Library interface (`IF-M01-TEMPLATE-001`) as a display metadata field for the wizard UI. It is NOT a canonical attribute of the `ENT-ProjectTemplate` entity in the approved data model. Include it in the prototype UI but label it as "estimated" — do not persist it as part of the template entity.

---

## Prompt

```
You are building a UI prototype for UPE (Unified Project Execution) — an enterprise platform
for engineering project management. This prototype demonstrates the Project Initialization &
Provisioning module (M01).

This is a DESIGN VALIDATION PROTOTYPE — the goal is to validate UX flows and data concepts
with stakeholders, NOT to build production code. Use mock data throughout.

Technology: React + TypeScript + TailwindCSS (or shadcn/ui).

Build exactly FIVE screens described below. Use the data objects provided.
```

---

## Data Objects

```typescript
// Aligned with ENT-Project from canonical data model
interface Project {
  project_id: string;
  name: string;
  project_code: string;
  project_type_id: string;
  template_id: string;
  client_name: string;
  client_id: string;
  gbu: string;                    // Global Business Area
  location: string;
  status: 'seed' | 'draft' | 'provisioning' | 'partial' | 'active';
  start_date: string;
  target_end_date: string;
  estimated_value: number;
  currency: string;
  opportunity_id: string;
  disciplines: string[];
  members: ProjectMembership[];
  workspaces: {
    teamsUrl?: string;
    sharepointUrl?: string;
    cdeUrl?: string;
    plannerUrl?: string;
  };
  created_at: string;
  created_by: string;
}

// Aligned with ENT-ProjectTemplate from canonical data model
interface ProjectTemplate {
  template_id: string;
  name: string;
  description: string;
  project_class: string;
  supported_types: string[];
  folder_structure: object;
  tool_configuration: object;
  standards_set: string;
  default_roles: string[];
  default_channels: string[];
  status: string;
  version: string;
}

interface ProjectMembership {
  user_id: string;
  user_name: string;
  user_email: string;
  role: string;
}

// Aligned with ENT-ProvisioningJob + ENT-ProvisioningTask
interface ProvisioningJob {
  job_id: string;
  project_id: string;
  status: 'pending' | 'running' | 'completed' | 'failed';
  tasks: ProvisioningTask[];
  started_at: string;
  completed_at?: string;
}

interface ProvisioningTask {
  task_id: string;
  task_type: 'erp_setup' | 'm365_provision' | 'cde_provision' | 'data_model_init' | 'access_setup';
  target_system: string;
  status: 'pending' | 'running' | 'completed' | 'failed' | 'retrying';
  started_at?: string;
  completed_at?: string;
  error_message?: string;
  retry_count: number;
}

// Display metadata from Template Library interface (not a canonical entity)
interface TemplateDisplay {
  template_id: string;
  name: string;
  description: string;
  estimated_setup_duration: string;  // e.g. "15 min" — UI display field only
  included_tools: string[];
}
```

---

## Screen 1: Project Creation Wizard — Step 1 (Project Type + Template Selection)

**Layout:** Full-width wizard with step indicator (Step 1 of 3) at the top.

**Left panel — Project Type Selection:**
- Grid of project type cards: Buildings, Energy, Transport, Water, Environment & Health, Management Consulting
- Each card shows: icon, type name, brief description
- Selected card is highlighted

**Right panel — Template Selection:**
- After selecting a type, show available templates as a vertical list
- Each template shows: name, description, `project_class`, `estimated_setup_duration` (labeled "Est. setup time")
- Radio button or card selection — one template must be chosen to proceed

**Bottom bar:**
- "Next" button (disabled until both type and template are selected)
- "Cancel" link

**Mock data:** 3 project types, 4 templates across types.

---

## Screen 2: Project Metadata Form — Step 2 (Name, Client, Disciplines, GBA, Location)

**Layout:** Form wizard with step indicator (Step 2 of 3).

**Form fields (pre-populated from CRM where available):**

| Field | Source | Behavior |
|---|---|---|
| Project Name | CRM (IF-M01-CRM-001) | Pre-filled from `project_name`, editable |
| Client Name | CRM | Pre-filled from `client_name`, locked after confirmation |
| Client ID | CRM | Pre-filled, read-only |
| Opportunity ID | CRM | Pre-filled, read-only |
| GBU | CRM | Pre-filled, dropdown editable |
| Location | CRM | Pre-filled, editable |
| Disciplines | Template | Pre-populated from template, multi-select with add/remove |
| Estimated Value | CRM | Pre-filled, editable |
| Currency | CRM | Pre-filled, dropdown |
| Start Date | CRM | Pre-filled from `expected_start_date`, date picker |

**Validation:**
- Required fields: Name, Client, GBU, Location
- Green checkmarks on valid fields
- "Back" and "Next" buttons in bottom bar

**Mock data:** One CRM opportunity pre-loaded with realistic values.

---

## Screen 3: Team & Access Setup — Step 3 (Add Members, Assign Roles)

**Layout:** Form wizard with step indicator (Step 3 of 3).

**Top section — Add Members:**
- Search bar with autocomplete (simulates Azure AD lookup via IF-M01-HR-001)
- Clicking a result adds the person to the team list
- Show user avatar, name, email, discipline

**Team list:**
- Table or card list of added members
- Each row: avatar, name, email, role dropdown, remove button
- Role dropdown populated from template's `default_roles`
- First member auto-assigned "Project Manager" role

**Bottom section:**
- Show "Default roles from template" as reference (read-only)
- "Back" and "Create Project" button (confirmation dialog on click)

**Mock data:** 10 searchable users, 5 default roles from template.

---

## Screen 4: Provisioning Status Dashboard

**Layout:** Full-width dashboard with project header and real-time status display.

**Header:**
- Project name, code, status badge ("Provisioning...")

**Provisioning pipeline:**
- Horizontal or vertical pipeline showing tasks:
  1. ERP — Project code & cost center (IF-M01-ERP-001)
  2. M365 — Teams + SharePoint + Planner (IF-M01-M365-001)
  3. CDE — ACC/ProjectWise workspace (IF-M01-CDE-001)
  4. Access — Role assignments
- Each task shows:
  - Status icon: spinner (running), checkmark (completed), X (failed)
  - System name and task description
  - Timestamps: started, completed
  - Error message if failed
  - "Retry" button if failed (with retry count)

**Progress bar:**
- Overall progress: X of Y tasks complete

**Auto-progression:**
- Simulate real-time updates with timed transitions (3-5 seconds per task)
- Show a failure scenario on one task with retry behavior

**Mock data:** 1 provisioning job with 4 tasks — 2 completed, 1 running, 1 pending. Then simulate a failure + retry.

---

## Screen 5: Project Landing Page (Post-Initialization)

**Layout:** Dashboard with summary cards and quick actions.

**Summary card:**
- Project name, code, type, status ("Active"), GBU, location
- Client name and ID
- Team size (X members)

**Quick actions card:**
- Clickable buttons with URLs:
  - "Open in Teams" → teamsUrl
  - "Open SharePoint" → sharepointUrl
  - "Open CDE" → cdeUrl
  - "Open Planner" → plannerUrl

**Team card:**
- List of team members with role badges, avatars

**Notifications card:**
- Recent activity feed:
  - "Teams team created — 5 minutes ago"
  - "CDE workspace provisioned — 4 minutes ago"
  - "Standards loaded from template — 3 minutes ago"
  - "Project is now Active ✅ — just now"

**Quick links:**
- "View provisioning log" → navigates to Screen 4
- "Edit project details" → navigates to Screen 2

**Mock data:** 1 fully provisioned active project.

---

## UX Guidelines

- **Design system:** Clean, professional enterprise UI (reference: Azure Portal, Jira)
- **Color scheme:** Blue primary (#4472C4), green success (#70AD47), amber warning (#FFC000), red error (#FF0000)
- **Navigation:** Left sidebar: Dashboard, Projects, Templates, Team, Settings
- **Responsive:** Desktop-first
- **Notifications:** Toast notifications for provisioning events
- **Empty states:** Helpful messages ("Create your first project")
- **Mock data:** Use realistic Ramboll-style project names, client names, and discipline labels

---

## Source References

This prototype prompt is derived from:
- [../../modules/m01_project_initialization/data_model.md](../../modules/m01_project_initialization/data_model.md) — canonical entities and attributes
- [../../modules/m01_project_initialization/requirements.md](../../modules/m01_project_initialization/requirements.md) — functional requirements
- [../../architecture/module_interfaces.md](../../architecture/module_interfaces.md) — interface contracts (IF-M01-*)

**Remember: This is a design validation prototype, not production code.**
