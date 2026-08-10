# The Unified Production Environement (UPE)

## The big idea

The Unified Production Environement (UPE) is an wide initiative in Ramboll that addresses AI-enabled readiness and standardization of our ways of working (embedding our processes in the toolbox) while leaving enough flexibility to each of our EAC projects, with their specificities (client, geography, industry, etc.) It is a challenging undertaking that we need to break into components.

We want to empower every engineer to leverage tech to elevate their capacity:
- via using AI
- a catalog of curated services, data products, agents, knowledge bases
- a low-code/no-code approach
- while keeping things secure and cost under control


1. Some more AI oriented, thinking in terms of knowledge bases, data products, librairies of AI agent skills, MCP servers, specialist agents.

2. Some others components of the overarching UPE, will be more traditional, following industry standards characteristics:
- task automation / workflow engine
- microservices for dedicateds tasks (behind APIs or MCP servers)
- event-driven architecture for scalability
- approval workflows with human in the loop


## The existing tech ecosystem
We use mostly the Microsoft 365 ecosystem, Azure Entra, Azure cloud resources, but also some GCP.
Microsoft is the domimant tech, besides our tier one vendors like Autodesk (Forma, AutoCAD Civil, Revit), Trimble (Trimble Connect), ESRI (ArciGIS), Bentley, AVEVA, etc.

The "Production" in UPE refers to what engineers produce in the various respective projects they are involved with, and less with corporate data, such as cost, finance, CRM, that belong to the Enterprise Architecture (EA).
EA seems to lean towards adoptiong Microsoft Fabric for modernizing some systems. Data should be easy to combine with project-centric data.
Open-source self-hosted (K8S) is not off the table for some systems.
Keeping a sovereign approach and avoiding vendor lock-in is important. So open formats like OKF/wiki/ontologies (and others that you can suggest) are relevant

## Capture/document our processes
In an easy standardize way,
For humans and for machine consumption.
We would like, from a unique source of truth, be able to gradually implement them into the tools and models. For instance, a low tech hanging fruit is adding custom internal property sets to our BIM models for tracking production status, collaboration along the way. Such data set may be stripped before delivery time.

The rules for quality-checks, checklists, etc could be "baked-in" ideally using low tech approach. 

## Interoperabily across data environments, BIM, VDC
We like buildingSmart standards like IFC, bsdd data catalog, classifications, information delivery specification (IDS).
ISO 19650 should be the inspiration, while remaining practical. 

VDC stands for Virtual Design and Construction. It is a comprehensive management method that uses digital models, like building information modeling (BIM), to plan, coordinate, and simulate construction projects.
The main aspects:
- Clash Detection: Finding and fixing mistakes in the computer before workers start building on site.
- Time Savings: Reducing delays by planning exact steps and material deliveries ahead of time.
- Cost Control: Preventing expensive re-work on the physical site by testing ideas virtually first


## A common way across projects to break down client contract deliveries
Ideally we can establish a common versatile way to describe top-level deliveries into discipline-scoped work packages in a way that also keeps track of dependencies, planning and deadlines.
Such information need not necessarily to be captive in a proprietary format. On the contrary, it should be described as much as possible as a data representation that can then be translated into various tools depending on the preference of the project, for instance, it could be Microsoft Planner or something else.

## Project digital platform provisioning
The idea is that at project startup, we can bootstrap the project digital platform, made of the various SaaS services and other resources, fine-tuned for the project. This implies a catalog of templates and a set of parameters to configure the templates based on the project specificities.
Microsoft Teams / SharePoint is a constant across all projects, which makes it a good candidate to host the bootstraper.

## Project's members onboarding/offboarding and centralized access management
At anytime a new member (inrenal or external) can join the project. Following the process, some conditions must ne fullfilled (available CV + basic user info), approuval from the PM, etc..
Once approved, based on the role, the new member needs to be granted access to various systems.
We envision defining roles at the project level, that in-tuen are mapped to the access groups (or roles) in each system involved.
Such configuration needs to be configured up-front.


## A golden principle: separate the "What" and the "How"
The 'what' is the description, plain data, open format, strcutured , but simple (YAML?)
The 'how' is the implementation (swappable in the future). Likely configured with assitance from AI, based on the 'What' and the underlying software/service capabilities/limitations.
This creat clarity and reduces the risk of vendor lock-in.

The configuration part of the "What", fairly static, could be persisted inside a project-dedicated git repo.
Ex repo:
Project Repo/

- Project-Metadata.yaml
    - Client
    - Maconomy code
    - Project type
    - Location
    - Time 
    - Coordinate Systems

 Key Members
    PrjM
    Prj controller
    Discipline Leads:
        D1: Bob@ramboll.com
        D2: Alice@ramboll.com 
    Digital Support:
      - olivier@ramboll.com
      - adrian@ramboll.com

  Data Platforms
    autodesk-forma.yaml
        - folder-structure:
            - 00-Admin
            - 01-Tender
            - 02-WIP
                - Discipline-A
                - Discipline-B
            - 03-Shared
            - 04-Published

        approuval-workflows?
        access-management?
            roles:
                - <RoleXYZ-in-Forma>
                    MapsTo: <Organization-01>-<Role-A>
                    permissions? (supported? Maybe not, but ok)
                        default: ReadOnly
                        folder-overrides:
                            - path: some/path/with/write-access
                              access: Write
    - esri-arcgis.yaml
        - layer-structure
        - groups
        - apps

    - trimble-connnect.yaml
          folder-structure:
            00-Admin
            01-Tender
            02-WIP
              - Discipline-A
              - Discipline-B
            03-Shared
            04-Published

    - xyz.yaml

- AccessManagement/
    - ProjectRoles:
        - <Organization-01>-<Role-A>
        - <Organization-01>-<Role-B>
        - <Organization-02>-<Role-A> 

Of course, custom databases are possible, but we try to leverage our pervasive Microsoft 365 envionement.
Teams feature such as tagging or standardized Microsoft lists are regarded as candiate for more dynamic and user facing data.


# Please tell me:
- Can you spot any contradictions in this vision?
- What are the low-hanging fruits to start with?
- How would you divide the work in separate - potentially parallel work streams
- What are the main risks?
- What tech or standards could you suggest that I did not mention