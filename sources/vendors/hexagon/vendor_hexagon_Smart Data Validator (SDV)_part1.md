

# SOURCE: vendor_hexagon\Smart Data Validator (SDV)\SDV Advanced Training Email Drafts.docx
---

**<Already registered>**

**Subject: Add Intergraph Smart® Data Validator Advanced Training to your HxGN LIVE Registration!**

Dear xxx,

I’m looking forward to seeing you at HxGN LIVE! We have discussed your interest in Intergraph Smart® Data Validator (SDV), and HxGN LIVE would be a great opportunity to learn more about it. This year we are offering an exciting hands-on session to help users address handover challenges with huge register validation requirements. In this hands-on session on Smart Data Validator, learn the end-to-end process of validating incoming information submissions, as well as how to utilize SDV to validate registers, per the new emerging CFIHOS standard. CFIHOS (Capital Facility Information Handover Specification) is a standard being developed under the auspices of USPI in the Netherlands and the Engineering Advancement Association in Japan. Are you wondering what the inverted format could be and how it will simplify importing new register types? Come hear about it!

Since you’ve already registered for the conference, visit [this page](https://hxgnlive17.smarteventscloud.com/portal/newreg.ww) to log in and add Session 1501, “Validation of Engineering Registers Using Intergraph Smart Data Validator” to your HxGN LIVE experience.

Learn more by reading our entire Advanced Training [Sneak Peek](http://app.response.intergraph.com/e/er?s=628&lid=12774&elqTrackId=FDBD5A16657BA6C102B78E62B249FC7C&elq=79f08034f2354bc4b5ac436bc9868829&elqaid=20471&elqat=1).

See you there!

**<Not registered>**

**Subject: Learn more about Intergraph Smart Data Validator at HxGN LIVE**

Dear xxx,

I hope to see you at HxGN LIVE! We have discussed your interest in Intergraph Smart® Data Validator (SDV), and HxGN LIVE would be a great opportunity to learn more about it. This year we are offering an exciting hands-on session to help users address handover challenges with huge register validation requirements. In this hands-on session about Smart Data Validator, learn the end-to-end process of validating incoming information submissions, as well as how to utilize SDV to validate registers, per the new emerging CFIHOS standard. CFIHOS (Capital Facility Information Handover Specification) is a standard being developed under the auspices of USPI in the Netherlands and the Engineering Advancement Association in Japan. Are you wondering what the inverted format could be and how it will simplify importing new register types? Come hear about it!

Begin your [conference registration](http://hxgnlive.com/2017/registration?elqTrackId=50031CD91502C552E2C18EF7AF1E7775&elq=79f08034f2354bc4b5ac436bc9868829&elqaid=20471&elqat=1&elqCampaignId=9074) and look for the advanced training option; look for Session 1501, “Validation of Engineering Registers Using Intergraph Smart Data Validator.”

Learn more by reading our entire Advanced Training [Sneak Peek](http://app.response.intergraph.com/e/er?s=628&lid=12774&elqTrackId=FDBD5A16657BA6C102B78E62B249FC7C&elq=79f08034f2354bc4b5ac436bc9868829&elqaid=20471&elqat=1).

Hope to see you there!


# SOURCE: vendor_hexagon\Smart Data Validator (SDV)\Collateral\SDV Introduction 08APR2015.pptx
---

<!-- Slide number: 1 -->

# Introduction to Smart Data Validator
Presenter NamePresenter Title

![C:\Users\lrdearma\Documents\000 In Process\Hexagon\HexagonEndorsement Suite\Marketing Materials\Left\Primary-WHITE\FULL COLOUR\HEX-L-primary_endorse_flag-white-FULL_COLOUR.png](Picture4.jpg)

### Notes:
Title Slide
To edit this slide, simply click in the text boxes to alter the text.

<!-- Slide number: 2 -->

# Business Challenges with Maintaining Data Quality
i
i
i
i
i
i
i
i
i
i
i
i
i

i

i
i
i
i

i

i

i
i

i
i
i
i

Continuous data accumulation
Enormous data volumes in transition
Transformation and validation of data
Impacts all lifecycle phases
Not just a technology challenge

### Notes:
0- Monitoring and maintaining data quality is a challenging task, especially when it is being transferred from one source to another -- like during project handover, brownfield data take-on, data loads and migrations.  The challenge is multiplied when data arrives in batches from different sources.
1- Managing the handover of data and documentation from projects to operations is especially daunting. The volumes of data handed over are vast – even a moderate-sized project can contain hundreds of thousands of tags and documents, and millions of individual data items.
2-  Data and documents are often delivered with missing, incorrect or inconsistent data, which must be identified and validated. This poses an even greater challenge at the end of the project, when staff is being demobilized, budgets are exhausted, and management is trying to wrap-up the project. But information managers must still ensure that only correct and validated data is loaded into target system.  As a rule, data handover can easily account for 1.5% of total CAPEX costs and take a year or more to complete.
3- As important as data handover is during the projects phase, the real value associated with quality data handover is in the operations phase.  High-quality data is critical to the safe, reliable and effective operation of any manufacturing facility.  If the quality of information handed over to operations is questionable, there is a constant need to physically verify the true physical state of the plant. This can drive up the cost of modifications by 30 percent or more over the entire lifecycle of the facility.
4- Of course, this is not just a technology challenge. It requires a thorough knowledge of the engineering data, requiring highly competent individuals who are often scarce resources.

<!-- Slide number: 3 -->

# Validation from Multiple Sources

Staging area

![Picture 2](Picture2.jpg)

### Notes:
Intergraph Smart Data Validator is a comprehensive data validation, transformation and migration platform that helps you significantly reduce the time and costs associated with ensuring the quality of information.

With Smart Data Validator, you can have complete control of how supplied data is imported from multiple data sources. Data files – such as equipment lists, cable schedules, valve lists, etc. – are imported into the Smart Data Validator staging area using an import definition. The imported data elements of the imported file are mapped against the data structures of the target system.  Validation rules are then applied to check the quality of the data before exporting to the target system.

If you’re mapping to an SPF-based system, Smart Data Validator will auto-generate a set of validation rules using the existing class definitions, property definitions, and relationship definitions of the target system. This means that you can validate your input data against the data structure of your target system simply by creating the mapping!

Examples of auto-generated rules could include:
Checking that an item exists… Does Project 401-A exist in the target system?
Confirming mandatory fields… A tag classification is required for each tag.
Ensuring relationship cardinality is maintained… A tag can only belong to one Area.
Verifying data types and properties… Design temperature must be a numeric value with a correct unit of measure.
Verifying pick list values… Does the tag classification match one of the values in the defined list?
Detecting inconsistent property values… If the same tag was loaded from more than one input source, does it have the same description?

Subject matter experts with no IT knowledge can easily set up additional rules that go beyond those that are automatically generated. For example, a rule to check that maximum operating temperature does not exceed maximum design temperature.

Established rules and rule sets ensure efficiency and consistency in testing.  As a project develops and more data is available or as data quality improves, additional rules can be added to improve quality even further. A staging area captures all results from testing, providing full auditable traceability of what testing has been performed, by whom and when, as well as the results of the testing.

Smart Data Validator is bundled with a pre-configured export adaptor to Intergraph’s SmartPlant® Foundation (SPF)*, which means that it works out-of-the-box with any Intergraph SPF-based system, like SmartPlant Construction, SmartPlant Fusion, and SmartPlant Enterprise for Owner-Operators.  Export adaptors for other target systems can be custom developed.

<!-- Slide number: 4 -->
# Work Process

### Notes:
1. Setup – In this administrative step, target systems are identified, import and export mappings are created, and rules for error handling are defined.  Smart Data Validator can auto-generate many of the validation and mapping rules, based on its analysis of the import file and the target database. Custom rules can also be developed using an intuitive user interface – no custom coding is required.  In this step, you also set up the job definitions which allow you to execute the entire data migration process as a workflow.

2. Import - This step allows you to import data into a staging area. The staging area is where imported data is held and validated before being exported to a target system. When an import job is run, Smart Data Validator compares the header of the input file against the defined mapping.  For each job processed, Smart Data Validator generates a set of tables for objects, relationships and properties.  Keeping these tables segregated for each job guarantees that jobs do not override or conflict with each other, ensuring data integrity.

3. Validate - The validation process evaluates the imported data against a defined set of rules to ensure the validity of the data.  For example, do tag numbers comply with the Engineering Numbering System?  Are all mandatory fields populated?  Do tag types match the defined pick list values?  Etc. These rules can be modified to filter the data to match the required output system.  In addition, error management will allow the blocking of properties, objects and related objects from being exported. For example, an error related to one instrument may be ascribed to all other objects in the instrument loop to ensure that a loop is only sent to the target system when all objects pass testing. It also provides a validation report to help with error correction.  At this stage, the job can be approved or rejected.

4. Export – The Export step is used to rapidly transfer the approved data to one or more target systems. If the target system is an SPF based system, SPF runs a preprocessor against the incoming data as an extra validation step to ensure data consistency. Smart Data Validator tracks all steps in the data import, validation and export process to provide a complete audit trail of the entire handover process.

<!-- Slide number: 5 -->
# Smart Data Validator Walkthrough

![Picture 2](Picture2.jpg)

### Notes:
AVI File

<!-- Slide number: 6 -->
# Smart Data Validator Walkthrough

![Picture 2](Picture2.jpg)

### Notes:
AVI File

<!-- Slide number: 7 -->

# Business Impact
Reduce time and costs associated with data handover
Accelerate  commisioning & start-up due to higher data quality
Ensure quality of data delivered from contractors & suppliers
Improve engineering data integrity

![Picture 2](Picture2.jpg)

### Notes:


# SOURCE: vendor_hexagon\Smart Data Validator (SDV)\Sales Presentations\SDV Introduction 08APR2015.pptx
> [!] DUPLICATE SKIP


# SOURCE: vendor_hexagon\Smart Data Validator (SDV)\Collateral\ARCHIVE-SmartDataValidator_Brochure_2015\ARCHIVE-SmartDataValidator_Brochure_2015_A4_Press.pdf
---

www.intergraph.com

INTERGRAPH
SMART™ DATA
VALIDATOR

Intergraph Smart™ Data Validator

is a comprehensive data validation,

transformation, and migration platform

that helps our customers to ensure the

quality of information and significantly

reduce the time and costs associated

with data take-on.

BENEFITS:

• Reduce time and cost associated

with data validation, transformation,
and migration

• Ensure quality of data delivered from
contractors, suppliers, and vendors

• Improved range, quality, and

consistency of validations performed

• Automatic generation of validation

rules and export mapping saves time
and avoids coding

• Manual rules can be added quickly
using the extensive library of pre-
defined validation rule templates

• High performance architecture allows
concurrent processing of multiple
jobs

• User roles and security ensures that
only approved users perform certain
functions

• Powerful export mechanism to load

data into target systems

• Provides complete audit trail of the

data handover process

THE CHALLENGE OF ENSURING DATA QUALITY

Monitoring and maintaining data quality is a challenging task. It is even more difficult

to manage when data is being moved from one source to another, like during project

handover, brownfield data take-on, data loads and migrations.

Managing the handover of data and documentation from projects to operations is

especially daunting. The volume of data handed over is vast. Data and documents arrive

throughout the project from multiple sources – often delivered with missing, incorrect, or

inconsistent data. As a rule, data handover can easily account for 1-2 percent of total

capital expenditure (CAPEX) costs and can take a year or more to complete.

As important as data handover is during projects, the real value associated with quality

data handover is in the operations phase. High-quality data is critical to the safe, reliable,

and effective operation of any manufacturing facility. If the quality of information handed

over to operations is questionable, there is a constant need to physically verify the true

physical state of the plant. This can drive up the cost of modifications by 30 percent or

more over the entire lifecycle of the facility.

Data Validator

OO / PMC

Legacy
Systems

Validate

Transform

Report

Approve

Target
Systems

EPC
Contractors

THE SOLUTION – SMART DATA VALIDATOR

Intergraph Smart™ Data Validator is a comprehensive data validation, transformation,

and migration platform that helps you significantly reduce the time and costs associated

with ensuring the quality of information. Smart Data Validator supports the import,

validation, and export of data, providing consistency and traceability of the entire data

migration process.

Smart Data Validator enables you to:

• Check the quality of information being transferred

• Keep records of which checks have been performed and the results obtained

• Load approved information into target systems

• Route unapproved information back to responsible parties for remediation

EXAMPLES OF
VALIDATION RULES
INCLUDE:

Checking that an item exists.
Does Project 401-A exist in the
target system?

Conﬁ rming mandatory ﬁ elds.
A tag classiﬁ cation is required for
each tag.

Ensuring relationship cardinality
is maintained.
A tag can only belong to one area.

Verifying data types and proper-
ties.
Design temperature must be a
numeric value with a correct unit of
measure.

Verifying pick list values.
Does the tag classiﬁ cation match
one of the values in the deﬁ ned list?

Detecting inconsistent property
values.
If the same tag was loaded from
more than one input source, does it
have the same description?

SET UP

• Defi ne Target Systems
• Import Mappings
• Validation & Delete Rules
• Export Mappings
• Job Defi nitions

VALIDATE

• Inconsistency Check
• Process Rules
• Propagate Errors
• Generate Report
• Approve or Reject

IMPORT

• Identify Job Scope
• Check Integrity
• Prompt for Inputs
• Process Job
• Bulk Load Staging Area

EXPORT

• Filter Data
• Run Preprocessor
• Generate Report
• Export and Load
• Generate Statistics

HOW IT WORKS

With Smart Data Validator, you have complete control of how data is imported, validated,

and loaded into one or more target systems.

Data fi les – such as equipment lists, cable schedules, valve lists, etc. – are imported into the

Smart Data Validator staging area using an import defi nition. The imported data elements are

mapped against the data structures of the target system. Validation rules are then applied to

check the quality of the data before exporting to the target system.

Smart Data Validator is bundled with a pre-confi gured export adaptor to Intergraph®’s

SmartPlant® Foundation (SPF)*, which means that it works out-of-the-box with any SPF-

based system, like SmartPlant Construction, SmartPlant Fusion, and SmartPlant Enterprise

for Owner Operators. In these cases, Smart Data Validator will auto-generate a set of

validation rules using the existing class, property, and relationship defi nitions of the target

system. This means that you can validate your input data against the data structure of your

target system simply by creating the mapping.

Subject matter experts with no IT knowledge can easily set up additional rules that go

beyond those that are automatically generated. For example, a rule that ascribes an error

related to one instrument to all other instruments in the same loop can easily be created. In

this way, you can ensure that a loop is only sent to the target system when all objects pass

testing.

Established rules and rule sets ensure effi ciency and consistency in testing. As a project

develops and more data is available, or as data quality improves, additional rules can be

added to improve quality even further. A staging area captures all results from testing,

providing full auditable traceability of what testing has been performed, by whom and when,

as well as the results of the testing.

When a job is approved, a ﬂ exible export mechanism initiates external loading programs for

the specifi ed target system, and a report is generated with complete job statistics.

As a rule,
data handover
can easily
account for
1-2 percent of
total capital
expenditure
(CAPEX) costs
and can take
a year or more
to complete.

Data mapping in Smart Data Validator

USAGE SCENARIOS FOR SMART DATA VALIDATOR

Verify project data prior to handover: EPCs can use Smart Data Validator to check the

quality of incoming information from their subcontractors and suppliers. They can also

use it to verify data quality prior incremental or fi nal data handover to their customers,

even if the target system is disconnected.

Validate project data take-on: The solution enables owner operators and project manage-

ment contractors to verify the quality of incoming engineering data prior to loading into a

target system.

Updates from plant modiﬁ cations: Data from turnaround projects and operational expendi-

ture (OPEX) modifi cations can be validated to ensure correctness and completion prior to

loading into operations systems.

Initial data loads: Smart Data Validator can play a key role in initial data loading of engi-

neering data management systems or other operational applications.

Data migrations: The solution can also be used to manage data migrations from legacy

systems. Data can be imported from one or more existing applications for consolidation

and verifi cation before loading into new target systems.

Improving data quality in operations: Smart Data Validator can also play a key role in

maintaining or improving legacy data quality during the operations phase of a plant. Data

may be extracted from operational systems into Smart Data Validator to check data

quality and perform corrections before reloading.

* SPF 2014R3 or later version

ABOUT INTERGRAPH

Intergraph helps the world work smarter. The company’s software and

solutions improve the lives of millions of people through better facilities, safer

communities, and more reliable operations.

utilities, transportation, and other global challenges. For more information,

visit www.intergraph.com.

Intergraph is part of Hexagon (Nasdaq Stockholm: HEXA B; hexagon.

com), a leading global provider of information technologies that drive quality

and productivity improvements across geospatial and industrial enterprise

Intergraph Process, Power & Marine (PP&M) is the world’s leading provider

applications.

of enterprise engineering software enabling smarter design and operation

of plants, ships, and offshore facilities. Intergraph Security, Government &

Infrastructure (SG&I) is the leader in smart solutions for emergency response,

© Intergraph Corporation. All rights reserved. Intergraph is part of Hexagon. Intergraph, the Intergraph logo, and SmartPlant are registered trademarks and Intergraph Smart is a trademark of Intergraph Corp. or its subsidiaries in the United
States and in other countries. 4/15 PPM-US-0341A-ENG




# SOURCE: vendor_hexagon\Smart Data Validator (SDV)\Collateral\PPM-Brochure-SmartSDV-EN-US-2017-Print.pdf
---

PRODUCT BROCHURE

THE SOLUTION TO ENSURING
DATA QUALITY
INTERGRAPH SMART® DATA VALIDATOR

THE CHALLENGE OF ENSURING DATA QUALITY

Monitoring and maintaining data quality is a challenging task. It is even more diffi cult

to manage when data is being moved from one source to another, like during project

handover, brownfi eld data take-on, data loads, and migrations.

Managing the handover of data and documentation from projects to operations is

especially daunting. The volume of data handed over is vast. Data and documents

arrive throughout the project from multiple sources – often delivered with missing,

incorrect, or inconsistent data. As a rule, data handover can easily account for 1-2

percent of total capital expenditure (CAPEX) costs and can take a year or more

BENEFITS

•  Reduce time and cost associated

to complete.

with data validation, transformation,

As important as data handover is during projects, the real value associated with

and migration

quality data handover is in the operations phase. High-quality data is critical to the

•  Ensure quality of data delivered from

safe, reliable, and effective operation of any manufacturing facility. If the quality of

contractors, suppliers, and vendors

information handed over to operations is questionable, there is a constant need to

•  Improved range, quality, and

physically verify the true physical state of the plant. This can drive up the cost of

consistency of validations performed

modifi cations by 30 percent or more over the entire life cycle of the facility.

•  Automatic generation of validation

rules and export mapping saves time

and avoids coding

•  Manual rules can be added quickly

using the extensive library of

predefi ned validation rule templates

•  High performance architecture allows

concurrent processing of multiple

jobs

•  User roles and security ensures that

only approved users perform certain

functions

•  Powerful export mechanism to load

data into target systems

•  Provides complete audit trail of the

data handover process

2

SMART DATA VALIDATOR  |   HexagonPPM.com

OO / PMC

Legacy
Systems

Staging Area

Validate

Transform

Report

Approve

EPC
Contractors

Target
Systems

THE SOLUTION
INTERGRAPH SMART® DATA VALIDATOR

Intergraph Smart® Data Validator is a comprehensive data validation, transformation,

and migration platform that helps you signifi cantly reduce the time and costs

associated with ensuring the quality of information. Smart Data Validator supports

the import, validation, and export of data, providing consistency and traceability of

the entire data migration process.

Smart Data Validator enables you to:

•  Check the quality of information being transferred

•  Keep records of which checks have been performed and the results obtained

•  Load approved information into target systems

•  Route unapproved information back to responsible parties for remediation.

SET UP
• Define Target Systems
• Import Mappings
• Validation & Delete Rules
• Export Mappings
• Job Definitions

IMPORT
• Identify Job Scope
• Check Integrity
• Prompt for Inputs
• Process Job
• Bulk Load Staging Area

VALIDATE
• Inconsistency Check
• Process Rules
• Propagate Errors
• Generate Report
• Approve or Reject

EXPORT
• Filter Data
• Run Preprocessor
• Generate Report
• Export and Load
• Generate Statistics

HOW IT WORKS

When a job is approved, a flexible export mechanism initiates

external loading programs for the specified target system, and

With Smart Data Validator, you have complete control of how

a report is generated with complete job statistics.

data is imported, validated, and loaded into one or more

target systems.

Data files – such as equipment lists, cable schedules, valve

lists, etc. – are imported into the Smart Data Validator staging

EXAMPLES OF VALIDATION RULES:

area using an import definition. The imported data elements

Checking that an item exists.

are mapped against the data structures of the target system.

Does Project 401-A exist in the target system?

Validation rules are then applied to check the quality of the

data before exporting to the target system.

Smart Data Validator is bundled with a pre-configured export

adaptor to SmartPlant® Foundation (SPF)*, which means

that it works out-of-the-box with any SPF-based system, like

Confirming mandatory fields.

A tag classification is required for each tag.

Ensuring relationship cardinality is maintained.

A tag can only belong to one area.

SmartPlant Construction, SmartPlant Fusion, and SmartPlant

Verifying data types and properties.

Enterprise for Owner Operators. In these cases, Smart Data

Design temperature must be a numeric value with a

Validator will auto-generate a set of validation rules using the

correct unit of measure.

existing class, property, and relationship definitions of the

target system. This means that you can validate your input

Verifying pick list values.

data against the data structure of your target system simply by

Does the tag classification match one of the values in

creating the mapping.

the defined list?

Subject matter experts with no IT knowledge can easily set up

Detecting inconsistent property values.

additional rules that go beyond those that are automatically

If the same tag was loaded from more than one input

generated. For example, a rule that ascribes an error related to

source, does it have the same description?

one instrument to all other instruments in the same loop can

easily be created. In this way, you can ensure that a loop is only

sent to the target system when all objects pass testing.

Established rules and rule sets ensure efficiency and

consistency in testing. As a project develops and more data is

available, or as data quality improves, additional rules can be

added to improve quality even further. A staging area captures

all results from testing, providing full auditable traceability of

what testing has been performed, by whom and when, as well

as the results of the testing.

As a rule, data handover can easily
account for 1-2 percent of total
capital expenditure (CAPEX) costs
and can take a year or more to

complete.”

HexagonPPM.com   |   SMART DATA VALIDATOR

3

Initial data loads: Smart Data Validator can play a

key role in initial data loading of engineering data

management systems or other operational applications.

Data migrations: The solution can also be used to

manage data migrations from legacy systems. Data can

be imported from one or more existing applications for

consolidation and verification before loading into new

target systems.

Data mapping in Smart Data Validator

Validator can also play a key role in maintaining or

Improving data quality in operations: Smart Data

improving legacy data quality during the operations

phase of a plant. Data may be extracted from

operational systems into Smart Data Validator to check

data quality and perform corrections before reloading.

* SPF 2014R3 or later version

USAGE SCENARIOS FOR SMART
DATA VALIDATOR

Verify project data prior to handover: EPCs can use

Smart Data Validator to check the quality of incoming

information from their subcontractors and suppliers.

They can also use it to verify data quality prior to

incremental or final data handover to their customers,

even if the target system is disconnected.

Validate project data take-on: The solution enables

owner operators and project management contractors

to verify the quality of incoming engineering data prior

to loading into a target system.

Updates from plant modifications: Data from

turnaround projects and operational expenditure

(OPEX) modifications can be validated to ensure

correctness and completion prior to loading into

operations systems.

About Hexagon PPM
Hexagon PPM (formerly Intergraph Process, Power & Marine) is the leading global provider of engineering software and project

control solutions. We transform unstructured information into a smart digital asset, empowering our clients to visualize, create,

and manage the life cycle of facilities and structures of all complexities. For more information visit HexagonPPM.com.
Hexagon PPM is part of Hexagon (Nasdaq Stockholm: HEXA B; Hexagon.com), a leading global provider of information technology

solutions that drive productivity and quality across geospatial and industrial landscapes.

© 2017 Intergraph Corporation d/b/a Hexagon PPM. Hexagon PPM is part of Hexagon. All rights reserved. Hexagon PPM and the Hexagon PPM logo are trademarks
of Hexagon or its subsidiaries in the United States and in other countries. SmartPlant are registered trademarks and Intergraph Smart is a trademark of Intergraph

Corporation. Other brands and product names are trademarks of their respective owners. 6/17 PPM-US-0341B-ENG




# SOURCE: vendor_hexagon\Smart Data Validator (SDV)\Collateral\ARCHIVE-SmartDataValidator_Brochure_2015\ARCHIVE-SmartDataValidator_Brochure_2015_US_Press.pdf
> [!] DUPLICATE SKIP


# SOURCE: vendor_hexagon\Smart Data Validator (SDV)\Sales Presentations\SDV Introduction 11May2015.pptx
---

<!-- Slide number: 1 -->

# Introducing Smart Data Validator
NameTitle

![C:\Users\lrdearma\Documents\000 In Process\Hexagon\HexagonEndorsement Suite\Marketing Materials\Left\Primary-WHITE\FULL COLOUR\HEX-L-primary_endorse_flag-white-FULL_COLOUR.png](Picture4.jpg)

### Notes:
Introducing a new product called Smart Data Validator, or SDV for short.

<!-- Slide number: 2 -->

# Business Challenges with Maintaining Data Quality
i
i
i
i
i
i
i
i
i
i
i
i
i

i

i
i
i
i

i

i

i
i

i
i
i
i

Continuous data accumulation
Enormous volumes of data in transition
Validating and correcting data
Impacts all lifecycle phases
Not just a technology challenge

### Notes:
0- First, let’s talk about the business challenge that Smart Data Validator was designed to address…
Anyone who has had a job managing data quality what a challenge it can be. This is especially true when data is being passed from one source to another -- like during system loads and migrations, brownfield data take-on, and project handover.  And data migration isn’t a one-time exercise – it arrives in batches from various sources over the entire lifecycle of the asset.
1- Managing the handover of data and documentation from projects to operations is especially daunting. The volumes are vast – even a moderate-sized project can contain hundreds of thousands of tags and documents, and millions of individual data items.
2-  Data and documents are often delivered with missing, incorrect or inconsistent data.  But it’s up to information managers to ensure that only correct and validated data is loaded into target systems.  As a rule, data handover can easily account for 1 to 2% of total CAPEX costs and take a year or more to complete.
3- As important as data handover is during the projects phase, the real value associated with quality data handover is in the operations phase.  High-quality data is critical to the safe, reliable and effective operation of any manufacturing facility.  If the quality of information handed over to operations is questionable from the start, plant personnel quickly learn that they have to walk-down equipment to physically verify the true state of the plant. Of course, this dramatically increases operational costs over the entire lifecycle of the facility.
4- Data validation isn’t something that can be fully automated. It requires input from highly competent individuals with a thorough knowledge of engineering information.  And as you know, these are often scarcest of resources.

<!-- Slide number: 3 -->

Replacement
for VTL

High Performance
Easy to Use
Improved Data Handling
# Introducing…

### Notes:
0 - So, with these business challenges in focus, we created Smart Data Validator – a comprehensive data validation, transformation and migration solution.

1 - Some of you may be familiar with our current product – VTL.  Smart Data Validator is a next generation replacement for VTL.  SDV is a completely new development from the ground up.  Current users of VTL can rest assured, however…  VTL will continue to be supported.  For those wishing to migrate from VTL to Smart Data Validator, a product license exchange program is available.  Please contact your Intergraph account representative for more information.

2 – One of the main design objectives for SDV was High Performance.  It can easily handle large data sets with millions of records, and its processing speeds are in the order of 10 to 30 times faster as compared with VTL.

3 - SDV is also Easy to Use
It has a completely redesigned user experience
The creation of validation rules is all GUI-based – no need to write code

4 - And finally, it has vastly improved data handling
It includes an out-of-the-box Target System adaptor for SPF 5.3, which allows the auto-generation of mappings & validation rules based on the target system schema.  Martin will demonstrate this powerful feature in a moment.
For non-SPF-based target systems, SDV has a common API so you can write your own adaptor.
It also has full traceability of all validation performed, and records the results.

<!-- Slide number: 4 -->

# How it Works

Staging area

Syntax Rules (ENS)
Uniqueness validation
Relationship cardinality
Date/Time validation
Integer validation
String validation
Pick-List validation
Unit of Measure validation
Mandatory fields
Cascading errors

Auto Generation ofData Mappings andValidation Rules

### Notes:
0 – SDV helps you significantly reduce the time and costs associated with ensuring the quality of information, whether that data is coming PMCs, EPCs, or legacy systems.  With SDV, you have complete control of how supplied data – such as equipment lists, cable schedules, valve lists, etc. – are imported from multiple data sources
1- Once imported, the data elements are mapped against the data structures of the target system. If you’re mapping to an SPF-based system, SDV will auto-generate a set of validation rules using the existing class, property, and relationship definitions of the target system. This means that you can validate your input data against the data structure of your target system simply by creating the mapping! A great time savings.  Subject matter experts can also easily set up additional rules that go beyond those that are automatically generated.
Validation rules could include things like:
Checking that an item exists… Does Project 401-A exist in the target system?
Confirming mandatory fields… A tag classification is required for each tag.
Ensuring relationship cardinality is maintained… A tag can only belong to one Area.
Verifying pick list values… Does the tag classification match one of the values in the defined list?

2- In the validation step, the rules are applied to check the quality of the data. Transformation rules can also be applied for things like converting data formats, for example.

3 – A quality report is generated for each job.  Data that fails validation can be corrected or sent back to the originator for remediation. SDV captures all results from testing, providing full auditable traceability of what testing has been performed, by whom and when, as well as the results of the testing.

4 – Once approved, the dataset is exported and loaded into the Target System. Again, SDV is bundled with a pre-configured export adaptor for SPF, which means that it works out-of-the-box with any Intergraph SPF-based system, like SmartPlant Construction, SmartPlant Fusion, and SmartPlant Enterprise for Owner-Operators.  Export adaptors for other target systems can be custom developed.

<!-- Slide number: 5 -->
# Basic Work Process

![Picture 2](Picture2.jpg)

### Notes:
1. Setup – In this administrative step, target systems are identified, import and export mappings are created, and rules for error handling are defined.  Smart Data Validator can auto-generate many of the validation and mapping rules, based on its analysis of the import file and the target database. Custom rules can also be developed using an intuitive user interface – no custom coding is required.  In this step, you also set up the job definitions which allow you to execute the entire data migration process as a workflow.

2. Import - This step allows you to import data into a staging area. The staging area is where imported data is held and validated before being exported to a target system. When an import job is run, Smart Data Validator compares the header of the input file against the defined mapping.  For each job processed, Smart Data Validator generates a set of tables for objects, relationships and properties.  Keeping these tables segregated for each job guarantees that jobs do not override or conflict with each other, ensuring data integrity.

3. Validate - The validation process evaluates the imported data against a defined set of rules to ensure the validity of the data.  For example, do tag numbers comply with the Engineering Numbering System?  Are all mandatory fields populated?  Do tag types match the defined pick list values?  Etc. These rules can be modified to filter the data to match the required output system.  In addition, error management will allow the blocking of properties, objects and related objects from being exported. For example, an error related to one instrument may be ascribed to all other objects in the instrument loop to ensure that a loop is only sent to the target system when all objects pass testing. It also provides a validation report to help with error correction.  At this stage, the job can be approved or rejected.

4. Export – The Export step is used to rapidly transfer the approved data to one or more target systems. If the target system is an SPF based system, SPF runs a preprocessor against the incoming data as an extra validation step to ensure data consistency. Smart Data Validator tracks all steps in the data import, validation and export process to provide a complete audit trail of the entire handover process.

<!-- Slide number: 6 -->
# SDV Demonstration – Setting up Data Mapping & Rules

![Picture 2](Picture2.jpg)

### Notes:
AVI File

<!-- Slide number: 7 -->

<!-- Slide number: 8 -->
# SDV Demonstration – Processing Jobs

![Picture 2](Picture2.jpg)

### Notes:
AVI File

<!-- Slide number: 9 -->

<!-- Slide number: 10 -->

# Business Impact
Reduce time and costs associated with data handover
Accelerate  commissioning & start-up due to higher data quality
Ensure quality of data delivered from contractors & suppliers
Improve engineering data integrity

![Picture 2](Picture2.jpg)

### Notes:

<!-- Slide number: 11 -->

# Thank you!

![C:\Users\lrdearma\Documents\000 In Process\Hexagon\HexagonEndorsement Suite\Marketing Materials\Left\Primary-WHITE\FULL COLOUR\HEX-L-primary_endorse_flag-white-FULL_COLOUR.png](Picture4.jpg)

![comp3 of Daratech banner](Picture6.jpg)

![Picture 1](Picture1.jpg)

### Notes:


# SOURCE: vendor_hexagon\Smart Data Validator (SDV)\Collateral\ARCHIVE-SmartDataValidator_Brochure_2015\ARCHIVE-SmartDataValidator_Brochure_2015_A4_screen.pdf
---

www.intergraph.com

INTERGRAPH
SMART™ DATA
VALIDATOR

Intergraph Smart™ Data Validator

is a comprehensive data validation,

transformation, and migration platform

that helps our customers to ensure the

quality of information and significantly

reduce the time and costs associated

with data take-on.

BENEFITS:

• Reduce time and cost associated

with data validation, transformation,
and migration

• Ensure quality of data delivered from
contractors, suppliers, and vendors

• Improved range, quality, and

consistency of validations performed

• Automatic generation of validation

rules and export mapping saves time
and avoids coding

• Manual rules can be added quickly
using the extensive library of pre-
defined validation rule templates

• High performance architecture allows
concurrent processing of multiple
jobs

• User roles and security ensures that
only approved users perform certain
functions

• Powerful export mechanism to load

data into target systems

• Provides complete audit trail of the

data handover process

THE CHALLENGE OF ENSURING DATA QUALITY

Monitoring and maintaining data quality is a challenging task. It is even more difficult

to manage when data is being moved from one source to another, like during project

handover, brownfield data take-on, data loads and migrations.

Managing the handover of data and documentation from projects to operations is

especially daunting. The volume of data handed over is vast. Data and documents arrive

throughout the project from multiple sources – often delivered with missing, incorrect, or

inconsistent data. As a rule, data handover can easily account for 1-2 percent of total

capital expenditure (CAPEX) costs and can take a year or more to complete.

As important as data handover is during projects, the real value associated with quality

data handover is in the operations phase. High-quality data is critical to the safe, reliable,

and effective operation of any manufacturing facility. If the quality of information handed

over to operations is questionable, there is a constant need to physically verify the true

physical state of the plant. This can drive up the cost of modifications by 30 percent or

more over the entire lifecycle of the facility.

Data Validator

OO / PMC

Legacy
Systems

Validate

Transform

Report

Approve

Target
Systems

EPC
Contractors

THE SOLUTION – SMART DATA VALIDATOR

Intergraph Smart™ Data Validator is a comprehensive data validation, transformation,

and migration platform that helps you significantly reduce the time and costs associated

with ensuring the quality of information. Smart Data Validator supports the import,

validation, and export of data, providing consistency and traceability of the entire data

migration process.

Smart Data Validator enables you to:

• Check the quality of information being transferred

• Keep records of which checks have been performed and the results obtained

• Load approved information into target systems

• Route unapproved information back to responsible parties for remediation

EXAMPLES OF
VALIDATION RULES
INCLUDE:

Checking that an item exists.
Does Project 401-A exist in the
target system?

Confirming mandatory fields.
A tag classification is required for
each tag.

Ensuring relationship cardinality
is maintained.
A tag can only belong to one area.

Verifying data types and proper-
ties.
Design temperature must be a
numeric value with a correct unit of
measure.

Verifying pick list values.
Does the tag classification match
one of the values in the defined list?

Detecting inconsistent property
values.
If the same tag was loaded from
more than one input source, does it
have the same description?

SET UP

• Define Target Systems
• Import Mappings
• Validation & Delete Rules
• Export Mappings
• Job Definitions

VALIDATE

• Inconsistency Check
• Process Rules
• Propagate Errors
• Generate Report
• Approve or Reject

IMPORT

• Identify Job Scope
• Check Integrity
• Prompt for Inputs
• Process Job
• Bulk Load Staging Area

EXPORT

• Filter Data
• Run Preprocessor
• Generate Report
• Export and Load
• Generate Statistics

HOW IT WORKS

With Smart Data Validator, you have complete control of how data is imported, validated,

and loaded into one or more target systems.

Data files – such as equipment lists, cable schedules, valve lists, etc. – are imported into the

Smart Data Validator staging area using an import definition. The imported data elements are

mapped against the data structures of the target system. Validation rules are then applied to

check the quality of the data before exporting to the target system.

Smart Data Validator is bundled with a pre-configured export adaptor to Intergraph®’s

SmartPlant® Foundation (SPF)*, which means that it works out-of-the-box with any SPF-

based system, like SmartPlant Construction, SmartPlant Fusion, and SmartPlant Enterprise

for Owner Operators. In these cases, Smart Data Validator will auto-generate a set of

validation rules using the existing class, property, and relationship definitions of the target

system. This means that you can validate your input data against the data structure of your

target system simply by creating the mapping.

Subject matter experts with no IT knowledge can easily set up additional rules that go

beyond those that are automatically generated. For example, a rule that ascribes an error

related to one instrument to all other instruments in the same loop can easily be created. In

this way, you can ensure that a loop is only sent to the target system when all objects pass

testing.

Established rules and rule sets ensure efficiency and consistency in testing. As a project

develops and more data is available, or as data quality improves, additional rules can be

added to improve quality even further. A staging area captures all results from testing,

providing full auditable traceability of what testing has been performed, by whom and when,

as well as the results of the testing.

When a job is approved, a flexible export mechanism initiates external loading programs for

the specified target system, and a report is generated with complete job statistics.

As a rule,
data handover
can easily
account for
1-2 percent of
total capital
expenditure
(CAPEX) costs
and can take
a year or more
to complete.

Data mapping in Smart Data Validator

USAGE SCENARIOS FOR SMART DATA VALIDATOR

Verify project data prior to handover: EPCs can use Smart Data Validator to check the

quality of incoming information from their subcontractors and suppliers. They can also

use it to verify data quality prior incremental or final data handover to their customers,

even if the target system is disconnected.

Validate project data take-on: The solution enables owner operators and project manage-

ment contractors to verify the quality of incoming engineering data prior to loading into a

target system.

Updates from plant modifications: Data from turnaround projects and operational expendi-

ture (OPEX) modifications can be validated to ensure correctness and completion prior to

loading into operations systems.

Initial data loads: Smart Data Validator can play a key role in initial data loading of engi-

neering data management systems or other operational applications.

Data migrations: The solution can also be used to manage data migrations from legacy

systems. Data can be imported from one or more existing applications for consolidation

and verification before loading into new target systems.

Improving data quality in operations: Smart Data Validator can also play a key role in

maintaining or improving legacy data quality during the operations phase of a plant. Data

may be extracted from operational systems into Smart Data Validator to check data

quality and perform corrections before reloading.

* SPF 2014R3 or later version

ABOUT INTERGRAPH

Intergraph helps the world work smarter. The company’s software and

solutions improve the lives of millions of people through better facilities, safer

communities, and more reliable operations.

utilities, transportation, and other global challenges. For more information,

visit www.intergraph.com.

Intergraph is part of Hexagon (Nasdaq Stockholm: HEXA B; hexagon.

com), a leading global provider of information technologies that drive quality

and productivity improvements across geospatial and industrial enterprise

Intergraph Process, Power & Marine (PP&M) is the world’s leading provider

applications.

of enterprise engineering software enabling smarter design and operation

of plants, ships, and offshore facilities. Intergraph Security, Government &

Infrastructure (SG&I) is the leader in smart solutions for emergency response,

© Intergraph Corporation. All rights reserved. Intergraph is part of Hexagon. Intergraph, the Intergraph logo, and SmartPlant are registered trademarks and Intergraph Smart is a trademark of Intergraph Corp. or its subsidiaries in the United
States and in other countries. 4/15 PPM-US-0341A-ENG




# SOURCE: vendor_hexagon\Smart Data Validator (SDV)\Collateral\ARCHIVE-SmartDataValidator_Brochure_2015\ARCHIVE-SmartDataValidator_Brochure_2015_US_screen.pdf
> [!] DUPLICATE SKIP
