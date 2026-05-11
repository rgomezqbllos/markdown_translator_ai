---
title: 'Loading and managing drivers'
shortTitle: 'Drivers'
intro: 'Learn to create, import, and maintain the driver database in GoalBus, review its operational profile, and leave a reliable template before moving on to affiliation, rules, and Rostering calculation.'
contentType: 'how-tos'
versions:
  - '*'
---

## Creating or Importing the Driver Template

Before discussing rostering rules, absences, or shift assignment, you need a reliable base of drivers. In GoalBus, driver management acts as the primary source of truth for human operations: it allows combining manual creation and bulk loading, and consolidates identity, depot affiliation, and availability in one directory. fileciteturn38file2L1-L24

Use this quick start when you have a clear transition from Scheduling to Rostering and need to prepare the actual group of people who will participate in the assignment.

Before starting, ensure that:
1. You have already closed the transition from Scheduling on P19.
2. You are clear about which pool of drivers will be involved in the calculation.
3. You know whether you will manually add a few drivers or need bulk loading.
4. You have access to the environment with permissions for personnel management.

For this quick start, use this reference case:

> **I am going to load and review the driver template that can cover Solution L1 before entering into affiliation rules and availability.**

To create or import the driver template:
1. In GoalBus, go to the module of **Configuration** > **Personal** > **Driver Management**.
ref: P20_Imagen1.png | compact
2. Check if the drivers from your case already exist in the general list.
3. If you need to create a few drivers, click on **New Driver**.
ref: P20_Imagen2.png | compact(2x)
4. If you need to load many drivers, perform a bulk import via CSV file under **Personal Load**.
ref: P20_Imagen3.png | compact
5. If choosing bulk import, prepare the file with the minimum data required by your operation to correctly identify each person. The import window will act as an aid for preparing the loading CSV.
ref: P20_Imagen4.png
6. Run the load and review the result.
7. Go back to the general list and check that drivers appear correctly.
8. If you detect duplicates or incomplete records, correct them before proceeding.

For the reference case, conclude this section only when you can affirm:
1. L1 drivers are already onboarded or imported.
2. The general list reflects a single reference template.
3. You can open each driver's profile to review their operational context.

When you finish this section, you should have a loaded and visible driver template in the system. fileciteturn38file0L1-L7 fileciteturn38file2L1-24

## Reviewing the Driver Profile and Structural Data

Once you have created the template, you need to review the **driver profile**. The profile is not just a contact sheet: it's the complete digital dossier of an employee within operations. It houses static data, operational context, and attributes that the system will use later for reasoning about their eligibility. fileciteturn38file0L7-20 fileciteturn38file2L25-40

Before starting this section, ensure that:
1. You have visible drivers in the general list.
2. You know which driver or group you will use as a sample.
3. You want to validate that the record is not just administrative but operational.

To review the driver profile:
1. In the general list, click on a driver's name. ref: P20_Imagen5.png | full
2. Review the static data sidebar.
3. Check at least these groups of information:
   1. basic details such as name and code,
   2. operational data like collective agreement or contract type,
   3. operational links such as main depot, work group, area, or authorized vehicle types.
4. If any key structural data is missing, complete it before proceeding.
5. Save any necessary changes.
6. Repeat the review for several drivers to confirm consistency in the template.

For the reference case, review at least:
1. The driver's code.
2. Their main depot.
3. Their work team.
4. Operational properties that will condition their subsequent assignment.

Upon completing this section, you should be clear that each driver has a coherent and usable operational file. fileciteturn38file0L8-L20

## Reviewing the Operating Context and Dynamic Data of the Driver

In addition to structural data, the driver profile includes dynamic data directly affecting how the system reasons about the individual. In the management tab, you can review counters and work patterns, which form part of the operating context used later by the assignment logic. fileciteturn38file0L12-L17

Before starting this section, ensure that:
1. You have already reviewed static profile data.
2. You know whether your operation uses counters or cyclic patterns.
3. You want to verify not only the driver's existence but also their interpretable operating context.

To review dynamic operational context:
1. Within the driver’s profile, open the **Management Details** tab.
2. Review any KPIs associated with the driver if they exist.
3. Check whether the driver is linked to a work pattern.
4. If your operation uses cyclic patterns, also check the offset or current position of the driver within the pattern.
5. Confirm that these data make sense in the real-world context.
6. If dynamic information is incorrect, adjust it before moving on to rules or calculation.

<div id="G_REF_..."></div>

For the reference case, ask yourself:
1. Does this driver have the pattern they should?
2. Are their counters or KPIs available if the process needs them?
3. Could the system reason correctly about this person in a scheduling calculation?

When you finish this section, you should validate not only the identity of the driver but also their dynamic operational context.

## Validating Qualifications Before Using Driver for Rostering

Before considering a driver eligible, you need to review their **qualifications**. These qualifications answer the question “Can this person legally or technically work in this depot, group, or unit?” They are managed on a timeline with start and end dates, and the system displays states such as active, future, expired, or expiring soon for easy reading. If a person is not qualified for the required context, the engine generates an error when attempting to assign them.

Before starting this section, ensure that:
1. You have already reviewed the driver's profile.
2. You know which depot, group, or unit will be needed in your case.
3. You understand that a qualification is different from a transfer or temporary assignment.

To review and validate qualifications:
1. Within the driver’s profile, open the **Qualifications / Qualifications** tab.
2. Check if there are valid records for:
   1. depots,
   2. work groups,
   3. business units.
3. Verify the visual state of each qualification:
   1. active,
   2. future,
   3. expiring soon,
   4. expired.
4. If a necessary qualification is missing, add it with its correct dates.
5. If an existing qualification has already expired and should not be used again, leave it as historical without attempting to rewrite history.
6. Save the changes.
7. Confirm that the driver is qualified for the context where you intend to use them.

For the reference case, do not proceed until you can affirm:
1. The driver is eligible for the correct depot.
2. The required work team is covered.
3. There are no expirations that break current eligibility.

When you finish this section, you should have drivers who exist in the template and also meet operational and regulatory eligibility requirements. fileciteturn38file0L17-L34

## Confirming That the Template Is Ready for the Next Level of Rostering

The last step is to check that the driver base is ready to enter the next level: operational assignment, rules, absences, and calculation. Here the goal is not just having names loaded but a coherent, traceable, and usable template by the engine.

Before finishing, ensure you have:
1. Already loaded or imported the template.
2. Already reviewed primary profiles.
3. Already checked structural and dynamic data.
4. Already validated essential qualifications.

To confirm that the template is ready:
1. Return to the general list of drivers.
2. Verify that the collective necessary for your case is present.
3. Check that critical profiles do not have important information gaps.
4. Ensure that people you intend to use are eligible in the correct context.
5. Ask if the system could already use this base as a starting point for:
   1. operational assignment,
   2. rostering rules,
   3. and real availability.
6. If the answer is yes, continue with the next quick start.
7. If the answer is no, correct the driver base before proceeding.

For the reference case, complete this quick start only when you can affirm:
1. The L1 driver template is already loaded.
2. Key profiles have been reviewed.
3. Essential qualifications are already valid.
4. The base is ready for operational assignment.

When you finish this section, you should have a sufficiently robust driver template to continue with the next layer of Rostering.

## Additional Readings

- [Managing Driver Operational Assignment](P21_Gestionando_la_adscripcion_operativa_del_conductor.md)