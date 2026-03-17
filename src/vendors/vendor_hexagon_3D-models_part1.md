

# SOURCE: vendor_hexagon\3D-models\storageemulated0Androiddataru.yandex.diskfilesdiskАндрей_IntergraphИнформация по ЭнергетикеIntergraph - PPM3D Model.pdf
---

Develop 3D Piping/Equipment Design 30% Completion - Basic Engineering - Level 2 Diagram

Intergraph Proprietary Information

DSPE1-PE-200130A - Updated Enterprise Work Process for Piping and Equipment Design

1

Develop 3D Piping/Equipment Design 30% Completion - Basic Engineering - Level 2

1.  As a member of the Process department, I need to develop P&IDs so that I can convey the updated status of the plant to other disciplines.

2.  As a member of the Process department, I need to publish the P&IDs so that the information can be shared with other disciplines.

3.  As an instrumentation engineer, I need to develop the instrumentation of the plant so that I can convey its status to other disciplines.

4.  As an instrumentation engineer, I need to publish the dimensional data sheets so that the piping designer can place the instruments in the 3D model with the correct dimensions.

  See the following Integration Capability Statement for more information:

  Using Instrument Dimensional Data to Drive 3D Design

5.

If the document has publishable data, the document and data are loaded into SmartPlant Foundation and are subsequently available for use by other applications. If the document does not have publishable data, it is available for viewing in SmartPlant
Foundation.

6.  After documents with data are published and loaded in the SmartPlant Foundation data warehouse, it is possible to check the consistency of data coming from various tools for the objects published in that document, such as instruments, equipment,

Intergraph Proprietary Information

or pipe runs. See the applicable subprocess in the Appendix.

7.  As a piping designer, I need to retrieve the P&IDs so that I can update the 3D model and check consistency with the P&IDs.

  See the following Integration Capability Statements for more information:

  P&ID Guided 3D Design and Change Management

  Consistency Check Between P&IDs and the 3D Model

8.  As a piping designer, I need to retrieve the dimensional data sheets so that I can place the instruments in the 3D model.

  See the following Integration Capability Statement for more information:

  Using Instrument Dimensional Data to Drive 3D Design

9.  As a piping designer, I need to develop the 3D piping/equipment design so that I can convey the updated status of the plant to other disciplines, continually reviewing the To Do list and IFC list to resolve inconsistencies and interferences.

10.  As a piping designer, I need to generate the SmartPlant Review files so that I can conduct internal reviews and 3D model reviews with the client.

11.  As a project manager, I need to review the 3D model with the client, noting comments and required revisions.

  See the following Integration Capability Statement for more information:

  Review of Smart 3D Projects in SmartPlant Review

12.  As a piping designer, I need to update the 3D model based on input from the client and other design criteria, continually reviewing the To Do list and IFC list to resolve inconsistencies and interferences. See the work process Update 3D Model for more

information.

13.  As a piping designer, I need to publish the 3D model so that it can be stored in SmartPlant Foundation for historical record.

  See the following Integration Capability Statement for more information:

  Review of Smart 3D Projects in SmartPlant Foundation

14.  If the document has publishable data, the document and data are loaded into SmartPlant Foundation and are subsequently available for use by other applications. If the document does not have publishable data, it is available for viewing in SmartPlant

Foundation.

15.  After documents with data are published and loaded in the SmartPlant Foundation data warehouse, it is possible to check the consistency of data coming from various tools for the objects published in that document, such as instruments, equipment,

or pipe runs. See the applicable subprocess in the Appendix.

16.  As a piping designer, I need to generate preliminary MTO reports so that a cost estimate can be created.

17.  As a member of the Project Controls department, I need to create a cost estimate.

18.  As a piping designer, I need to have pipe stress analysis run on critical pipelines so that the location of critical pipe supports can be determined.

19.  As a piping designer, I need to update the 3D model based on the results of the pipe stress analysis (including pipe supports) and other design criteria so that I can convey the updated status of the plant to other disciplines. See the work process

Update 3D Model for more information.

20.  As a piping designer, I need to generate preliminary orthographic drawings to convey the layout of the plant.

21.  As a piping designer, I need to publish preliminary orthographic drawings so that they can be stored in SmartPlant Foundation for historical record.

DSPE1-PE-200130A - Updated Enterprise Work Process for Piping and Equipment Design

2

22.  If the document has publishable data, the document and data are loaded into SmartPlant Foundation and are subsequently available for use by other applications. If the document does not have publishable data, it is available for viewing in SmartPlant

Foundation.

23.  As a piping designer, I need to generate isometric drawings for critical pipelines that might require long lead time.

24.  As a piping designer, I need to publish isometric drawings for critical pipelines so that Project Controls can procure materials for long lead items.

25.  If the document has publishable data, the document and data are loaded into SmartPlant Foundation and are subsequently available for use by other applications. If the document does not have publishable data, it is available for viewing in SmartPlant

Foundation.

26.  As a member of the Project Controls department, I need to procure material listed on the isometric drawings critical pipelines for long lead items.

Intergraph Proprietary Information

DSPE1-PE-200130A - Updated Enterprise Work Process for Piping and Equipment Design

3




# SOURCE: vendor_hexagon\3D-models\storageemulated0Androiddataru.yandex.diskfilesdiskАндрей_IntergraphИнформация по ЭнергетикеIntergraph - PPM3DModelViz.pdf
---

Review of Intergraph Smart™ 3D Projects in SmartPlant Review

Intergraph Proprietary Information

Integration Capability Statements Review of Intergraph Smart™ 3D Projects in SmartPlant Review

1

Intergraph Proprietary Information

Short Description of Work Process
This work process provides design review and visualization capabilities of Intergraph Smart™ 3D graphic and attribute data in SmartPlant Review. If you create
comments in SmartPlant Review, comments must be manually provided to the designers and reviewed for appropriate actions in the respective applications.
This work process only discusses a non-integrated environment. If working in an integrated environment, with SmartPlant Foundation, please see the Review
of Smart 3D Projects in SmartPlant Foundation capability statement, which discusses reviewing the model using either SmartPlant Foundation, SmartPlant
Markup Plus or SmartPlant Review.
After some initial setup in the Smart 3D catalog, the user can choose between the standard method and the new SPRDirect method for creating model data
documents.
The standard method of creating model data documents for SmartPlant Review creates XML data for a large number of object properties, then it creates the
Smart 3D model graphics (.vue file) and data. This method maintains relationships between the 3D object and those from other SmartPlant tools in SmartPlant
Foundation, allowing users to fully review the design. The standard method also maintains relationships with the plant hierarchy allowing users to trace objects
through the hierarchy; for example, from unit to area to plant.
The newest method, SPRDirect, allows project leads to modify 3D properties for review by other stakeholders, such as subcontractors. SPRDirect is faster
because it skips the XML data creation step, and creates the .vue and .mdb2 files for a smaller set of object properties as delivered. However, SPRDirect only
provides properties and does not maintain object relationships. If more properties are needed for viewing, SPRDirect is configurable using the drawings and
reports templates from Smart 3D.

Improve facilities management through direct access to documentation and maintenance records

Business Value
Designers & Engineers
  Create better designs by navigating the 3D model and data on the fly within SmartPlant Review, while modeling in Smart 3D. (Requires dual monitors).
  Make better engineering design judgments by accessing the model data

Improve maintainability, safety, and accuracy through a variety of communication tools
  Promote constructability design with the ability to preview possible construction sequences
EPC Project Management
  Speed and improve decision-making process by accessing up-to-date information

  Ensure effective team communication between disciplines using the tagging features
Construction
  Reduce costs by allocating more personnel resources to designing and less on reviewing
  Speed the schedule by defining the critical path and making it more complete

Plant Owners
  Enhance early problem detection with in-depth model review during detailed design
  Consider design alternatives much earlier in the design cycle by pinpointing potential problem areas

Improve facilities management through direct access to documentation and maintenance records

Improve safety by performing safety reviews with visualization

Integration Capability Statements Review of Intergraph Smart™ 3D Projects in SmartPlant Review

2


