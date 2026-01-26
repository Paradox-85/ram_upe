# UPE Brainstorming

## The 'What'

### Capabilities (Simplified)
::: mermaid
kanban
  Provisionin/Deprovisioning<br/>of the Project Environment
    Initialize Tools and Services according to project-class template
    Archive Project Data at project closeout
    Configure Common Data Environment 
  User Access Managemnent
      Streamline On/Offboarding project members
      Streamline Tools Access Administration
      Leverage Approval workflows
  Project Oservability
    Track Progress
    Track Cost
    Highligh Delays/Risks/Issues
  "Embed the processes into the tools as much as possible"
    Support Interdisciplinary Collaboration
    Prevent error/non-compliance
    Simplify Engineers' design work
  Data Quality
    Configurable Classification System
    Validation against standards
  Planning and Delivery Management
    Work Package Definitions
    WBS Milestones-Tasks
    Responsibility Matrix
:::


<!-- ### Capabilities
::: mermaid
mindmap
  root((UPE))
    Provisionin/Deprovisioning<br/>of the Project Environment
      Initialize Tools and Services according to project-class template
      Archive Project Data at project closeout
      Configure Common Data Environment 
    User Access Managemnent
        Streamline On/Offboarding project members
        Streamline Tools Access Administration
        Leverage Approval workflows
    Project Oservability
      Track Progress
      Track Cost
      Highligh Delays/Risks/Issues
    "Embed the processes into the tools as much as possible"
      Support Interdisciplinary Collaboration
      Prevent error/non-compliance
      Simplify Engineers' design work
    Data Quality
      Configurable Classification System
      Validation against standards
    Planning and Delivery Management
      Work Package Definitions
      WBS Milestones-Tasks
      Responsibility Matrix
::: -->

### Caracteristics
* Project-scoped
* User friendly (Most ppl in Ramboll work on several projects at the same time)


## The 'How'

### Considerations
* scalability
* interoperability
* security
* build vs. buy
* cost of operation/maintenance

### Architecture
UPE can be seen as a collection of modules, where each module addresses a particular set of needs, identified as common across Ramboll's projet portfolio.
From the users point of view, a module constitutes a logical grouping of features. From the implementor's point of view, a module is made of artifacts, such as:

* templates / configuration files
* approval workflows
* dashboards
* backend automation scripts
* databases
* web applications


### Suggeted Tech Stack
* Microsoft Teams/SharePoint
* Microsoft PowerBI
* Microsoft Power Automate Flows
* Microsoft Planner 
(offers consolidated views of tasks across all projects)
* Microsoft Azure

We beleve in utilizing the existing technology available to us through our Microsoft Office E5 license and leverage the many available extension points and robust APIs to build the UPE in terms of integration on top of robust and secure components, without reinventing the wheel.

### Integrations
* CRM
* Maconomy
* Common data environments
* Design tools (templates/scripts/addons)
* BIM/GIS/Visualization tools