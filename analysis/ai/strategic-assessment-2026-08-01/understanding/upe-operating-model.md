---
type: Operating Model
title: Understanding UPE
description: A bounded interpretation of UPE as a portfolio of project-production capabilities.
tags: [upe, operating-model, boundaries, principles]
generated:
  by: agent:github-copilot
  at: 2026-08-01T00:00:00Z
status: draft
stale_after: 2026-11-01
sources:
  - id: initial-prompt
    resource: ../../../main.md
    title: UPE initial prompt
  - id: vision
    resource: ../../../../knowledge-base/raw-input/UPE-vision.md
    title: UPE vision raw input
  - id: capabilities
    resource: ../../../../knowledge-base/raw-input/capabilities.md
    title: UPE capabilities raw input
---

# Understanding UPE

## Core interpretation

UPE is a project-centric operating environment for engineering production across the full project lifecycle. It connects the capabilities needed to understand, plan, produce, monitor, learn, enable, and govern project delivery.[^capabilities]

It should be treated as a **portfolio and contract system**:

1. A portfolio of independently owned capability products.
2. A small set of shared semantic and technical contracts.
3. A curated knowledge layer usable by people and agents.
4. Replaceable adapters into Microsoft, vendor, open-source, and client environments.

## The durable "what"

The durable model should describe:

- project context and constraints;
- organizations, people, project roles, and accountability;
- work packages, deliveries, dependencies, milestones, and deadlines;
- information requirements, classifications, lifecycle states, and authoritative sources;
- process definitions, checks, decisions, approvals, and evidence;
- desired platform configuration and mappings from project roles to platform permissions;
- reusable services, data products, skills, agents, and knowledge sources;
- outcomes, measures, risks, and decisions.

These definitions require stable identities, controlled vocabulary, validation, versioning, provenance, and explicit extension rules.

## The replaceable "how"

Products and runtimes implement the model. They include Teams, SharePoint, Lists, Power Platform, Azure services, Fabric, CDE products, engineering authoring tools, databases, workflow engines, APIs, MCP servers, and AI platforms.

Microsoft-first is a sensible delivery preference because of the existing ecosystem. It should not leak into the canonical domain model. Vendor-specific configuration belongs in adapters and implementation mappings.

## Authority and state

UPE cannot have one universal physical source of truth. Authority must be declared per data class:

| Information | Likely authority |
|---|---|
| Desired project configuration | Version-controlled project repository |
| Project membership and identity | Identity and project-access services |
| Workflow transitions and approval history | Workflow service or controlled pilot state store |
| Engineering information containers | Applicable project CDE |
| Embedded model properties | Snapshot linked by stable delivery ID |
| Portfolio metadata and measures | Information register or analytics layer |
| Curated process and engineering knowledge | OKF knowledge bundle |

A system may project another system's state, but projections need timestamps, authority labels, and reconciliation behavior.

## Knowledge and AI

Agents should operate over curated, permission-aware knowledge rather than an indiscriminate document index. Each consequential concept should expose where it came from, who generated it, whether a human or process verified it, its lifecycle status, and when it should be reviewed.

[OKF](../index.md#why-okf-fits) provides the portable document contract. Access enforcement, retrieval filtering, evaluation, tool authorization, and runtime audit remain platform responsibilities.

## Boundary with enterprise architecture

UPE owns project-production semantics and workflows. Enterprise architecture owns or coordinates corporate systems and shared enterprise platforms. The boundary must be expressed through contracts for identity, finance, resources, portfolio reporting, and enterprise data rather than duplicated ownership.

The next architectural choices are summarized in [architecture recommendation](../recommendations/architecture.md).

[^capabilities]: The raw capability model groups UPE around Understand, Plan, Produce, Monitor, Learn, Enable, and Govern.