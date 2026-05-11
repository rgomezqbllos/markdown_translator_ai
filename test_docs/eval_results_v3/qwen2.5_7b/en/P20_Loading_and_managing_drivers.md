---
title: Loading and managing drivers
shortTitle: Drivers
intro: Learn to create, import, and maintain the driver database in GoalBus, review their operational profile, and leave a reliable template before moving to adscription, rules, and Rostering calculation.
contentType: how-tos
versions:
  - '*'
---

## Creating or Importing the Driver Template

Before discussing rostering rules, absences, or shift assignments, you need a reliable base of drivers. In GoalBus, driver management acts as the primary source of truth for human operations: it allows for a combination of manual creation and bulk loading, and it centralizes identity, depot affiliation, and availability in a single directory. fileciteturn38file2L1-L24

Use this quick start when you have a clear transition from Scheduling to Rostering and need to prepare the actual group of people who will be involved in the assignment.

Before starting, make sure you:
1. Have already closed the transition from Scheduling in P19.
2. Are clear about which group of drivers will participate in the calculation.
3. Know whether you will manually add a few drivers or need a bulk upload.
4. Have access to the environment with permissions to manage personnel.

For this quick start, use this reference case:

> **I will load and review the driver template that can cover the L1 solution before entering into affiliation, rules, and availability.**

To create or import the driver template:
1. In GoalBus, go to the **Configuration** > **Personal** > **Driver Management** module.
ref: P20_Imagen1.png | compact
2. Check if the drivers from the case already exist in the general list.
3. If you need to create a few drivers, click on **New Driver**.
ref: P20_Imagen2.png | compact(2x)
4. If you need to load many drivers, perform a bulk import via CSV from **Bulk Personal Upload**.
ref: P20_Imagen3.png | compact
5. If you choose bulk import, prepare the file with the minimum data needed by your operation to correctly identify each person. The import window will act as a helper to prepare the CSV upload.
ref: P20_Imagen4.png
6. Run the upload and review the result.
7. Go back to the general list and check that the drivers appear correctly.
8. If you detect duplicates or incomplete records, correct them before proceeding.

For the reference case, end this section only when you can affirm:
1. L1 drivers are already onboarded or imported.
2. The general list reflects a single reference template.
3. You can open each driver's profile to review their operational context.

When you finish this section, you should have a driver template loaded and visible in the system. fileciteturn38file0L1-L7 fileciteturn38file2L1-L24

## Reviewing the Driver Profile and Structured Data

Once the template is created, you need to review the **driver profile**. The profile is not just a contact sheet: it is the complete digital dossier of the employee within the operation. It houses static data, operational context, and attributes that the system will use later to reason about their eligibility. fileciteturn38file0L8-L20 fileciteturn38file2L25-L40

Before starting this section, make sure:
1. You have visible drivers in the general list.
2. You know which driver or which group you will use as a sample.
3. You want to validate that the record is not just administrative, but operational.

To review the driver profile:
1. In the general list, click on a driver's name.
ref: P20_Imagen5.png | full
2. Review the static data sidebar.
3. Check at least these groups of information:
   1. basic data, such as name and code,
   2. operational data, such as collective agreement or contract type,
   3. operational links, such as main depot, work team, area, or authorized vehicle types.
4. If any key structured data is missing, complete it before proceeding.
5. Save any necessary changes.
6. Repeat the review for several drivers to confirm consistency in the template.

For the reference case, review at least:
1. The driver's code.
2. Their main depot.
3. Their work team.
4. Operational properties that will condition their subsequent assignment.

Once you finish this section, you should be clear that each driver has a coherent and usable operational file. fileciteturn38file0L8-L20

## Reviewing the Operational Context and the Driver's Dynamic Data

In addition to the structural data, the driver profile includes dynamic data that directly affect how the system reasons about the person. In the administration tab, you can review counters and work patterns, which form part of the operational context used later by the assignment logic. fileciteturn38file0L12-L17

Before starting this section, ensure that:
1. You have already reviewed the static profile data.
2. You know whether your operation uses counters or cyclic patterns.
3. You want to check that the driver not only exists but also has an interpretable operational context.

To review the dynamic operational context:
1. Within the driver profile, open the **Management Details** tab.
2. Review any KPIs associated with the driver if they exist.
3. Check if the driver is linked to any **work pattern**.
4. If your operation uses cyclic patterns, also review the driver's offset or current position within the pattern.
5. Confirm that these data make sense in the real context.
6. If the dynamic information is incorrect, adjust it before moving to rules or calculation.

For the reference case, ask yourself:
1. Does this driver have the pattern he should have?
2. Are his counters or KPIs available if the process needs them?
3. Could the system reason correctly about this person in an assignment calculation?

When you finish this section, you should have validated not only the identity of the driver, but also his dynamic operational context. fileciteturn38file0L12-L17

## Validating Qualifications Before Using the Driver in Rostering

Before considering a driver eligible, you need to review their **qualifications**. These qualifications answer the question “Can this person legally or technically work in this depot, group, or unit?” They are managed in a timeline with start and end dates, and the system shows states such as active, future, expired, or expiring to facilitate reading. If a person is not qualified for the required context, the engine generates an error when trying to assign them. fileciteturn38file0L17-L34

Before starting this section, make sure:
1. You have already reviewed the driver's profile.
2. You know which depot, group, or unit will be needed for your case.
3. You understand that a qualification is not the same as a transfer or a temporary assignment.

To review and validate the qualifications:
1. Within the driver's profile, open the **Qualifications / Qualifications** tab.
2. Check if there are valid records for:
   1. depots,
   2. work groups,
   3. business units.
3. Check the visual state of each qualification:
   1. active,
   2. future,
   3. expiring soon,
   4. expired.
4. If a necessary qualification is missing, add it with the correct dates.
5. If a qualification has already expired and should not be used, leave it as historical without trying to rewrite history.
6. Save the changes.
7. Confirm that the driver is already qualified for the context where you plan to use him.

For the reference case, do not proceed until you can affirm:
1. The driver is authorized for the correct depot.
2. The required work team is covered.
3. There are no expirations that break current eligibility.

When you finish this section, you should have drivers that not only exist in the template but are also operationally and administratively eligible. fileciteturn38file0L17-L34

## Confirming that the template is ready for the next Rostering layer

The last step is to check that the driver base is ready to enter the next layer: operational assignment, rules, absences, and calculation. Here, the goal is not just to have names loaded, but a coherent, traceable, and usable template for the engine.

Before finishing, ensure that:
1. You have already loaded or imported the template.
2. You have already reviewed the main profiles.
3. You have already checked structural and dynamic data.
4. You have already validated essential authorizations.

To confirm that the template is ready:
1. Go back to the general list of drivers.
2. Verify that the collective necessary for your case is present.
3. Check that critical profiles do not have important information gaps.
4. Ensure that the people you intend to use are authorized for the correct context.
5. Ask yourself if the system could already use this base as a starting point for:
   1. operational assignment,
   2. Rostering rules,
   3. and real availability.
6. If the answer is yes, proceed with the next quick start.
7. If the answer is no, correct the driver base before proceeding.

For the reference case, complete this quick start only when you can affirm:
1. The L1 driver template is already loaded.
2. The key profiles have already been reviewed.
3. The essential qualifications are already valid.
4. The base is ready to proceed to operational assignment.

When you finish this section, you should have a sufficiently robust driver template to continue with the next layer of Rostering.

## Additional Readings

- [Managing the Operational Assignment of the Driver](P21_Gestionando_la_adscripcion_operativa_del_conductor.md)