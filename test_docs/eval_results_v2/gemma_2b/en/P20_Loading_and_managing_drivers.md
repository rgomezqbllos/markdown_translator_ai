---
title: Loading and managing drivers
shortTitle: Drivers
intro: Learn to create, import, and maintain the driver base in GoalBus, review their operational profile, and create a reliable template before proceeding to assignment, rules, and Rostering calculation.
contentType: how-tos
versions:
  - '*'
---

## Creating or Importing the Driver Template

Before discussing Roster rules, absences, or shift assignments, you need a reliable database of drivers. In GoalBus, driver management acts as the primary source of truth for operational human activity: it allows for manual creation and mass loading, and concentrates identity, affiliation to the depot, and availability in a single directory. 
fileciteturn38file2L1-L24

Use this quick start when you have a clear transition from Scheduling to Roster and need to prepare the real group of people who will participate in the assignment.

Before you begin, make sure that:
1. You have closed the transition from Scheduling in P19.
2. You are clear about which driver group will participate in the calculation.
3. You know whether you will be registering a few drivers manually or if you need a mass loading.
4. You have access to the environment with permissions to manage personnel.

For this quick start, use this reference case:

> **I am going to load and review the driver template that will cover the L1 solution before entering into adherence, rules, and availability.**

To create or import the driver template:
1. In GoalBus, go to the **Configuration** > **Personnel** > **Driver Management** module.
ref: P20_Imagen1.png | compact
2. Review if the drivers from the case already exist in the general list.
3. If you need to create a few drivers, click **New Driver**.
ref: P20_Imagen2.png | compact(2x)
4. If you need to load many drivers, perform a mass import via CSV from **Mass Personnel Load**.
ref: P20_Imagen3.png | compact
5. If you choose mass import, prepare the file with the minimum data your operation needs to correctly identify each person. The import window will help you prepare the CSV for loading.
ref: P20_Imagen4.png
6. Execute the load and review the result.
7. Return to the general list and check that the drivers appear correctly.
8. If you detect duplicates or incomplete records, correct them before proceeding.

For reference purposes, end this section only when you can affirm:
1. Drivers for L1 have been registered or imported.
2. The general list reflects a single reference template.
3. You can open each driver's profile to review their operational context.

When you finish this section, you should have a driver template loaded and visible in the system. 
fileciteturn38file0L1-L7
fileciteturn38file2L1-L24

## Reviewing the driver profile and its structural data

Once the template is created, you need to review the **driver profile**. The profile is not just a contact sheet: it is the complete digital file of the employee within the operation. There you will find static data, operational context, and attributes that the system will use later to reason about their eligibility. 
fileciteturn38file0L8-L20
fileciteturn38file2L25-L40

Before starting this section, make sure that:
1. You have visible drivers on the general list.
2. You know which driver or group you will use as a sample.
3. You want to validate that the record is not just administrative, but operational.

To review the driver profile:
1. On the general list, click on a driver's name.
ref: P20_Imagen5.png | full
2. Review the sidebar of static data.
3. Check at least these groups of information:
   1. Basic data, such as name and code,
   2. Operational data, such as collective agreement or contract type,
   3. Operational links, such as main depot, work group, area or authorized vehicle types.
4. If any key structural data is missing, complete it before proceeding.
5. Save any necessary changes.
6. Repeat the review in several drivers to confirm consistency in the template.

For reference purposes, review at least:
1. The driver's code.
2. Their main depot.
3. Their work team.
4. The operational properties that will condition their subsequent assignment.

When you finish this section, you should be clear that each driver has a coherent and usable operational file. 

## Reviewing the operational context and dynamic data of the driver

In addition to structural data, the driver profile includes dynamic data that directly affects how the system reasons about the person. In the administration tab, you can review counters and work patterns, which form part of the operational context used later by the assignment logic. 

Before starting this section, make sure that:
1. You have reviewed the static data of the profile.
2. You know if your operation uses counters or cyclical patterns.
3. You want to verify that the driver exists and has an interpretable operational context.

To review the dynamic operational context:
1. Within the driver's profile, open the **Administration Details** tab.
2. Review the associated counters or KPIs for the driver if they exist.
3. Check if the driver is linked to any work pattern.
4. If your operation uses cyclical patterns, review the offset or current position of the driver within the pattern.
5. Confirm that this data makes sense for the real context.
6. If the dynamic information is incorrect, adjust it before moving to rules or calculations.

For reference purposes, ask yourself:
1. Does this driver have the pattern they should have?
2. Are their counters or KPIs available if the process needs them?
3. Could the system reason correctly about this person in a scheduling calculation?

When you finish this section, you should have validated not only the driver's identity, but also their dynamic operational context. fileciteturn38file0L12-L17


## Validating qualifications before using the driver in Rostering

Before considering a driver eligible, you need to review their **qualifications**. These qualifications answer the question “Can this person legally or technically work in this depot, group, or unit?”. They are managed in a temporal timeline with start and end dates, and the system displays states like active, future, expired, or about to expire to facilitate reading. If a person is not qualified for the required context, the engine generates an error when attempting to assign them. fileciteturn38file0L17-L34


Before starting this section, make sure that:
1. You have already reviewed the driver's profile.
2. You know which depot, group, or unit you will need for your case.
3. You understand that a qualification is not the same as a temporary assignment or a temporary affiliation.

To review and validate qualifications:
1. Within the driver's profile, open the **Qualifications / Qualifications** tab.
2. Review if there are any valid records for:
   1. depots,
   2. work groups,
   3. business units.
3. Check the visual status of each qualification:
   1. active,
   2. future,
   3. about to expire,
   4. expired.
4. If a necessary qualification is missing, add it with the correct dates.
5. If a qualification has expired and should not be used, leave it as historical without attempting to rewrite the past.
6. Save the changes.
7. Confirm that the driver is already qualified for the context where you expect to use them.

For reference purposes, do not proceed until you can affirm:
1. The driver is authorized for the correct depot.
2. The required work team is covered.
3. There are no expirations that break current eligibility.

When you finish this section, you should have drivers who not only exist in the roster but are also eligible from an operational and regulatory standpoint. fileciteturn38file0L17-L34

## Confirming that the roster is ready for the next layer of Rostering

The last step is to verify that the driver database is ready to enter the next layer: operational assignment, rules, absences, and calculation. The goal here is not just to have names loaded, but a coherent, traceable, and usable template by the engine.

Before finishing, make sure that:
1. You have loaded or imported the template.
2. You have reviewed the main profiles.
3. You have checked structural and dynamic data.
4. You have validated essential authorizations.

To confirm that the template is ready:
1. Return to the general list of drivers.
2. Verify that the necessary team for your case is present.
3. Check that critical profiles do not have important information gaps.
4. Make sure that the people you expect to use are authorized for the correct context.
5. Ask yourself if the system could already use this base as a starting point for:
   1. Operational assignment,
   2. Rostering rules,
   3. and real availability.
6. If the answer is yes, proceed with the next quick start.
7. If the answer is no, correct the driver base before continuing.

For reference purposes, complete this quick start only when you can affirm:
1. The L1 driver template is loaded.
2. The key profiles have been reviewed.
3. Essential authorizations are active.
4. The base is ready to move to operational assignment.

When you finish this section, you should have a robust driver template to proceed to the next Rostering layer.

## Additional Readings

- [Managing the operational assignment of the driver](P21_Gestionando_la_adscripcion_operativa_del_conductor.md)