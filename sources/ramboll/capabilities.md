### Capabilities
::: mermaid
%%{init: {"flowchart": {"curve": "stepBefore", "nodeSpacing": 35, "rankSpacing": 45}} }%%
flowchart LR
  UPE[UPE]

  UPE --> Understand[Understand]
  Understand --> ProjectContext[Project Context]
  ProjectContext --> Client[Client]
  ProjectContext --> Regulation[Regulation]
  ProjectContext --> Constraints[Constraints]
  Understand --> OurResources[Our Resources]
  OurResources --> People[People]
  OurResources --> Tools[Tools]

  UPE --> Plan[Plan]
  Plan --> PlanDeliveries[Project Deliveries]
  Plan --> DisciplinesCollab[Disciplines Collaboration]

  UPE --> Produce[Produce]
  Produce --> ProduceDeliveries[Project Deliveries]
  ProduceDeliveries --> Models[Models]
  ProduceDeliveries --> Drawings[Drawings]
  ProduceDeliveries --> Analysis[Analysis]
  ProduceDeliveries --> Reports[Reports]

  UPE --> Monitor[Monitor]
  Monitor --> Quality[Quality]
  Monitor --> Progress[Progress]
  Monitor --> Costs[Costs]

  UPE --> Learn[Learn]
  Learn --> ImproveProcess[Improve Process]
  Learn --> RefineCookbook[Refine the Cookbook]

  UPE --> Enable[Enable]
  Enable --> BetterDecisionMaking[Better Decision Making]
  Enable --> NewClientOpportunities[New Client Opportunities]
  Enable --> BottomUpInnovation[Bottom-up Innovation]

  UPE --> Govern[Govern]
  Govern --> InternalProcess[Internal Process]
  Govern --> ProjectKnowledge[Project-level Knowledge]
:::