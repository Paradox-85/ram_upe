---
id: glossary
type: glossary
status: approved
owner: "@chief-architect"
version: 1.0
last_updated: 2026-05-26
parent: master.md
tags: [glossary, terms, definitions]
---

# UPE Glossary — Canonical Terminology

## Core Terms

| Term | Definition |
|---|---|
| **UPE** | **Unified Project Execution** — Ramboll's enterprise digital backbone for orchestrating project delivery. Not a single application, but a cohesive platform ecosystem. |
| **CDE** | **Common Data Environment** — Project-level system of record for document management, version control, and design coordination (e.g., Autodesk ACC, Bentley ProjectWise). CDE ≠ enterprise brain. |
| **DMS** | **Document Management System** — System for storing, organizing, and managing documents. UPE integrates with DMS but is not a DMS itself. |
| **Master** | The canonical, approved knowledge base (`master.md` + `modules/`). Contains only reviewed and approved content. Like the `main` branch in Git. |
| **Fork** | A working copy of knowledge used by a module owner to propose changes. Contains hypotheses, deltas, and proposals. Like a feature branch in Git. |
| **Merge** | The process of moving approved changes from a fork into the master knowledge base. Requires passing all merge gates. |
| **ADR** | **Architecture Decision Record** — A documented decision capturing context, choice, consequences, alternatives, and review date. Format: `ADR-{NNNN}`. |
| **Module** | A logical grouping of features addressing a specific domain (e.g., M01 = Project Initialization). Each module has its own folder with index, requirements, data model, workflows, API spec, and backlog. |
| **Interface Contract** | A formal specification of data exchange between UPE and an external system. Includes producer, consumer, payload, trigger, output, and failure modes. Format: `IF-M{NN}-{SYS}-{SEQ}`. |
| **Knowledge Graph** | An enterprise-wide graph structure representing projects, deliverables, standards, processes, and their relationships. Enables cross-project learning, semantic search, and AI-powered retrieval. |
| **Project Initialization** | The process of creating and provisioning a new project environment — from CRM opportunity to fully operational workspace with all tools, services, and data structures. |
| **Provisioning** | The automated setup of tools and services for a project (Teams team, SharePoint site, CDE workspace, Planner board, etc.). |
| **DDDM** | **Dialogue-Driven Design Method** — The LLM-native product design methodology where design happens through structured dialogue with AI, and outputs are stored as structured Markdown. |
| **Stable ID** | A unique, persistent identifier for a knowledge artifact (requirement, entity, workflow step, interface, decision). Never changes once assigned. |
| **Merge Gate** | A quality checkpoint that must be passed before a fork can be merged to master (completeness, traceability, interface impact, data model impact, architect approval). |
| **GBA** | **Global Business Area** — Ramboll's organizational business units (Buildings, Energy, Transport, Water, etc.). |
| **GBU** | **Global Business Unit** — Alternative term for GBA in some contexts. |
| **Idempotency** | The property where making the same API request multiple times produces the same result. Critical for retry-safe provisioning. |
| **Template** | A reusable configuration defining how a project should be set up — folder structure, tools, access rules, standards, default roles. |
| **Prototype Prompt** | A generated prompt (for v0.dev, Replit, Claude) derived from the knowledge base to rapidly produce UI prototypes. NOT source of truth. |

## Abbreviations

| Abbreviation | Full Form |
|---|---|
| ACC | Autodesk Construction Cloud |
| AAD | Azure Active Directory |
| APIM | API Management |
| BPMN | Business Process Model and Notation |
| COTS | Commercial Off-The-Shelf |
| ERD | Entity Relationship Diagram |
| FTE | Full-Time Equivalent |
| IFC | Industry Foundation Classes |
| iPaaS | Integration Platform as a Service |
| KPI | Key Performance Indicator |
| MVP | Minimum Viable Product |
| OKR | Objectives and Key Results |
| PLM | Product Lifecycle Management |
| RBAC | Role-Based Access Control |
| RDF | Resource Description Framework |
| RACI | Responsible, Accountable, Consulted, Informed |
| SaaS | Software as a Service |
| SLA | Service Level Agreement |
| SOP | Standard Operating Procedure |
| WBS | Work Breakdown Structure |
