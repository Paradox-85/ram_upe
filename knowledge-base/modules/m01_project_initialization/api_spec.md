---
id: m01-api-spec
type: api-spec
status: in-review-demo
owner: "@module-owner-m01"
version: 1.0
last_updated: 2026-05-26
parent: modules/m01_project_initialization/index.md
tags: [m01, api, events, errors]
---

# M01 API Specification — Project Initialization

## Overview

M01 exposes both synchronous REST APIs for the creation wizard and asynchronous event-driven interfaces for provisioning orchestration.

---

## REST API Endpoints

### Project Creation

#### `POST /api/v1/projects` — Create Project
Creates a new project from a seed or from scratch.

**Request:**
```json
{
  "opportunity_id": "string (optional)",
  "name": "string (required)",
  "project_type_id": "uuid (required)",
  "template_id": "uuid (required)",
  "client_name": "string (required)",
  "client_id": "string (required)",
  "gbu": "string (required)",
  "location": "string (required)",
  "disciplines": ["uuid"],
  "estimated_start_date": "date",
  "metadata": {}
}
```

**Response (201 Created):**
```json
{
  "project_id": "uuid",
  "status": "draft",
  "created_at": "datetime",
  "wizard_url": "string"
}
```

#### `GET /api/v1/projects/{project_id}` — Get Project
Returns project details including provisioning status.

**Response (200 OK):**
```json
{
  "project_id": "uuid",
  "name": "string",
  "project_code": "string",
  "status": "provisioning",
  "provisioning_job": {
    "job_id": "uuid",
    "status": "running",
    "tasks": [
      {
        "task_id": "uuid",
        "task_type": "m365_provision",
        "status": "completed",
        "completed_at": "datetime"
      },
      {
        "task_id": "uuid",
        "task_type": "cde_provision",
        "status": "running"
      }
    ]
  },
  "workspaces": {
    "teams_url": "string",
    "sharepoint_url": "string",
    "cde_url": "string"
  }
}
```

#### `POST /api/v1/projects/{project_id}/submit` — Submit for Provisioning
Triggers the provisioning workflow after PM confirms configuration.

**Response (202 Accepted):**
```json
{
  "project_id": "uuid",
  "status": "provisioning",
  "job_id": "uuid",
  "estimated_completion": "datetime"
}
```

#### `POST /api/v1/projects/{project_id}/retry` — Retry Failed Provisioning
Retries specific or all failed provisioning tasks.

**Request:**
```json
{
  "task_ids": ["uuid"],
  "retry_all": false
}
```

---

### Template Management

#### `GET /api/v1/templates` — List Templates
Returns available templates filtered by project type/class.

**Query Parameters:**
| Parameter | Type | Required | Description |
|---|---|---|---|
| `project_type_id` | UUID | No | Filter by project type |
| `gbu` | String | No | Filter by business unit |
| `status` | String | No | Filter by template status |

#### `GET /api/v1/templates/{template_id}` — Get Template Details

---

### Team Assembly

#### `POST /api/v1/projects/{project_id}/members` — Add Team Member
```json
{
  "user_id": "uuid",
  "role_id": "uuid",
  "start_date": "date",
  "end_date": "date (optional)"
}
```

#### `GET /api/v1/users/search` — Search Users
Proxies to Azure AD for user search during team assembly.

**Query Parameters:** `q` (search term), `department`, `discipline`

---

## Events

### Published Events

| Event | Trigger | Payload |
|---|---|---|
| `project.created` | New project record created | `{ project_id, name, type, gbu }` |
| `project.provisioning.started` | Provisioning workflow begins | `{ project_id, job_id }` |
| `project.provisioning.task.completed` | Individual provisioning step done | `{ project_id, job_id, task_type, task_id }` |
| `project.provisioning.task.failed` | Individual provisioning step failed | `{ project_id, job_id, task_type, error }` |
| `project.provisioning.completed` | All provisioning tasks done | `{ project_id, workspaces }` |
| `project.provisioning.partial` | Some tasks failed after retries | `{ project_id, failed_tasks, completed_tasks }` |
| `project.activated` | Project moves to active status | `{ project_id, dashboard_url }` |

### Consumed Events

| Event | Source | Action |
|---|---|---|
| `crm.opportunity.won` | CRM | Create project seed (WF-M01-010) |
| `erp.project_code.assigned` | Maconomy | Update project with financial context |
| `m365.provisioning.complete` | M365 Connector | Mark task complete, proceed to next |
| `cde.workspace.ready` | ACC/PW Connector | Mark task complete, proceed to next |

---

## Error States

### Error Response Format
```json
{
  "error": {
    "code": "string",
    "message": "string",
    "details": {},
    "retryable": true,
    "retry_after_seconds": 300
  }
}
```

### Error Codes

| Code | HTTP | Description | Retryable |
|---|---|---|---|
| `PROJECT_NAME_EXISTS` | 409 | Project with this name already exists | No |
| `TEMPLATE_NOT_FOUND` | 404 | Requested template does not exist | No |
| `OPPORTUNITY_NOT_FOUND` | 404 | CRM opportunity not found | No |
| `OPPORTUNITY_ALREADY_LINKED` | 409 | Opportunity already has a project | No |
| `ERP_UNAVAILABLE` | 502 | Maconomy API not responding | Yes |
| `M365_PROVISION_FAILED` | 502 | Teams/SharePoint provisioning error | Yes |
| `CDE_PROVISION_FAILED` | 502 | ACC/ProjectWise provisioning error | Yes |
| `USER_NOT_FOUND` | 404 | Azure AD user not found | No |
| `INSUFFICIENT_PERMISSIONS` | 403 | User cannot create projects | No |
| `PROVISIONING_TIMEOUT` | 504 | Provisioning step exceeded time limit | Yes |
| `RATE_LIMIT_EXCEEDED` | 429 | API rate limit hit | Yes |

---

## External Dependencies

| System | API | Used For | Criticality |
|---|---|---|---|
| CRM | REST API | Opportunity data | High (but can work without) |
| Azure AD | Microsoft Graph | User search, org data | Critical |
| Maconomy | REST API | Project codes, cost centers | High |
| Microsoft Teams | Microsoft Graph | Team/channel provisioning | High |
| SharePoint | Microsoft Graph | Site/folder provisioning | High |
| Planner | Microsoft Graph | Board provisioning | Medium |
| Autodesk ACC | ACC API | CDE workspace | High |
| ProjectWise | PW API | CDE workspace (alt) | Medium |
| UPE Knowledge Graph | Internal API | Similar projects | Low (optional) |
