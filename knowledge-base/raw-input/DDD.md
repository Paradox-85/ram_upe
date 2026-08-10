Q:

We're building a knowledge base to help our team understand, classify and address different areas in our business that need digital support and automation. Many topics seem to entangled and it is hard to identify/name clear "problems" and then to propose "solutions". Obviously we would like to implement solutions in terms of reusable/composable "modules" that can be artifacts or services.We started gathering input using OKF 0.2 format. It helps a bit but we wonder if we could borrow from the Domain-Driven Design (DDD) practice. Could you suggest a repo layout (OKF-style) that is also in line with DDD principles, to help us emerge a solution or solutions architecture?


A:

Executive Summary: Domain-Driven Design (DDD)

Domain-Driven Design (DDD) is a way of organizing knowledge, software, and business improvement initiatives around the business itself, rather than around systems, applications, departments, or technologies.

Its central idea is simple:

Understand the business domains first. Build solutions second.

For a team trying to identify opportunities for automation and digitalization, DDD is less about software design patterns and more about creating a shared understanding of:

What business problems exist
Who owns them
How work actually flows
Where automation can help
Which solution components can be reused
Why DDD Matters

Many organizations end up with knowledge bases that look like this:

Power BI
Power Automate
SharePoint
Python Scripts
Revit Add-ins
Azure Functions


But these are technologies, not business concepts.

DDD encourages thinking like this:

Project Delivery
│
├── Model Validation
├── Information Exchange
├── Coordination Reviews
└── Approval Workflows


The technology becomes an implementation detail.

This makes it easier to:

Prioritize investments
Identify duplication
Discover reusable services
Build a coherent architecture
The Core Concepts
1. Domain

A domain is an area of business activity.

Examples:

Project Delivery
Engineering
Commercial
Operations
Asset Management


A domain answers:

"What area of the business are we talking about?"

2. Subdomain

A smaller area within a domain.

Example:

Project Delivery
│
├── BIM Coordination
├── Information Management
├── Quality Assurance
└── Design Review


Subdomains often become candidates for focused initiatives or products.

3. Ubiquitous Language

One of DDD's most important ideas.

Everyone should use the same vocabulary for the same concept.

Example:

Bad:

Asset
Object
Element
Component
Model Item


Good:

Asset = physical object tracked through lifecycle


The knowledge base should contain a glossary and consistently use it.

4. Bounded Context

A bounded context defines where a specific meaning applies.

Example:

The word "Project" might mean:

Commercial Context:
    Contract Opportunity

Project Delivery Context:
    Executing Project

Finance Context:
    Cost Center


DDD says:

The same word may mean different things in different contexts.

This prevents endless discussions caused by terminology collisions.

5. Business Capability

A capability is something the organization needs to be able to do.

Examples:

Validate Models
Manage Documents
Approve Deliverables
Generate Reports
Manage Workflows


Capabilities tend to remain stable even when systems are replaced.

For automation planning, capabilities are often the most useful organizational unit.

6. Business Events

DDD places strong emphasis on events.

Examples:

Model Submitted
Approval Requested
Document Published
Issue Created
Issue Closed


Events represent things that happen in the business.

Events often reveal automation opportunities.

Example:

Model Submitted
    ->
Validation Performed
    ->
Issues Identified
    ->
Coordinator Notified


This sequence can later become an automated workflow.

7. Aggregates, Entities, and Value Objects

These are software modeling concepts, but they are less important initially.

For your knowledge base, don't start here.

Focus first on:

Domains
Capabilities
Problems
Events
Use Cases


The deeper technical patterns can emerge later.

Applying DDD to Digitalization

Instead of starting with:

We need a Power Automate Flow


Start with:

Problem:
    Model reviews take too long

Capability:
    Model Validation

Events:
    Model Submitted
    Validation Completed

Users:
    BIM Coordinator

Potential Solutions:
    Validation Service
    Workflow Engine
    Dashboard


This keeps business needs separate from implementation choices.

How DDD Helps Discover Reusable Modules

Suppose you document several problems:

Model Validation
Document Validation
Data Quality Validation


You may discover they all need:

Rules
Checks
Exceptions
Reports


A reusable module naturally emerges:

Rule Engine


Similarly:

Model Approval
Document Approval
Change Approval


might all require:

Approval Workflow Module


DDD helps identify these common patterns.

A DDD-Inspired Knowledge Architecture
Domains
    ↓
Capabilities
    ↓
Problems
    ↓
Use Cases
    ↓
Events
    ↓
Solution Candidates
    ↓
Reusable Modules


Example:

Domain:
    Project Delivery

Capability:
    Model Validation

Problem:
    Manual checking

Use Case:
    Validate IFC delivery

Events:
    Model Submitted
    Validation Completed

Solution:
    Automated Validation

Module:
    Rule Engine

What Your Team Should Focus on First

If you're building a knowledge base rather than designing software, I'd suggest concentrating on just five DDD concepts:

Domains

Major business areas

Capabilities

What the business must be able to do

Problems

Pain points and inefficiencies

Events

Things that happen in the business

Ubiquitous Language

Shared glossary of terms

Everything else can evolve later.

One-Sentence Summary

Use DDD to organize knowledge around business domains, capabilities, problems, and events; then let reusable automation services and solution architecture emerge from recurring patterns rather than designing technology first.