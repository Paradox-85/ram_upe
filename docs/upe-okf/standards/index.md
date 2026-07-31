---
type: Standards Profile
title: UPE standards and technology guidance
description: Selective standards profile separating durable interoperability contracts from replaceable products.
tags: [upe, standards, technology, interoperability]
generated:
  by: agent:github-copilot
  at: 2026-08-01T00:00:00Z
status: draft
stale_after: 2026-11-01
sources:
  - id: initial-prompt
    resource: ../../../main.md
    title: UPE initial prompt
  - id: process-format
    resource: ../../../../knowledge-base/raw-input/business-process-capture-format.md
    title: Business process capture format
  - id: iso19650
    resource: ../../../../knowledge-base/raw-input/iso-19650.md
    title: ISO 19650 raw input
---

# UPE standards and technology guidance

## Adopt now

| Contract | UPE use |
|---|---|
| Open Knowledge Format v0.2 | Portable curated knowledge with provenance, verification, lifecycle, freshness, and links |
| YAML or JSON plus JSON Schema | Project configuration, domain contracts, controlled values, examples, and validation |
| OpenAPI | Stable commands and queries across services, Teams interfaces, add-ins, and adapters |
| OAuth 2.0 and OpenID Connect | Portable authentication and delegated authorization patterns around Entra ID |
| OpenTelemetry | Vendor-neutral traces, metrics, and logs across APIs, events, adapters, and agents |
| IFC, bSDD, and IDS | Open model exchange, shared definitions, machine-readable requirements, and validation |

## Adopt when the use case appears

| Contract | Trigger |
|---|---|
| AsyncAPI and CloudEvents | Multiple teams publish or consume domain events and need discoverable contracts |
| BPMN and DMN | Workflow and decision semantics outgrow a simple state-machine definition |
| SCIM and policy as code | Identity lifecycle spans enough systems to justify standard provisioning and testable policy |
| W3C PROV or OpenLineage | Transformations and AI outputs require interoperable provenance beyond OKF document sources |
| BCF | Cross-tool BIM issue exchange is part of a selected pilot |
| COBie | Structured asset handover is contractually required |
| ISO 12006 or IEC/ISO 81346 | Project classification or reference designation requires them |
| ArchiMate Exchange | Enterprise architecture needs machine exchange with the simpler UPE model |

## Defer until justified

RDF, JSON-LD, and SHACL are useful when federation, inference, or graph validation becomes a demonstrated need. Do not introduce a knowledge-graph platform merely because the information is graph-shaped. OKF links and the retained typed analytical model are sufficient for the current strategic stage.

## Technology guidance

- Use GitHub or Azure DevOps for versioned desired state and knowledge review.
- Use Bicep, Terraform, scripts, or APIs as replaceable provisioning adapters.
- Use Microsoft Lists, Teams, Power Apps, and Power Automate for rapid M365-native pilots where their limits are understood.
- Use Azure Functions, App Service, Kubernetes, Service Bus, or Event Grid according to workload needs, not as canonical UPE concepts.
- Use Fabric, OneLake, and Power BI as an optional portfolio metadata and analytics implementation, not as a replacement CDE.
- Use databases suited to operational consistency for live workflow state; do not treat OKF or Git as transactional stores.

The decisive architectural rule is described in [Understanding UPE](../understanding/upe-operating-model.md): standards define the durable **what**, while technologies remain a replaceable **how**.