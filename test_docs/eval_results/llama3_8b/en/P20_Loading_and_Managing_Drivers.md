---
title: Loading and Managing Drivers
shortTitle: Drivers
intro: 'Learn to create, import, and maintain the driver database in GoalBus, review their operational profile, and leave a reliable template before moving on to assignment, rules, and Rostering calculation.'
contentType: how-tos
versions:
  - '*'
---

## Creating or Importing the Driver Template

Before discussing Rostering rules, absences, or shift assignments, you need to have a reliable base of drivers. In GoalBus, driver management acts as the primary source of truth for human operational data: it allows combining manual creation and bulk loading, and it centralizes identity, depot affiliation, and availability in a single directory.

Use this quick start when you already have a clear transition from Scheduling to Rostering and need to prepare the actual team of people who will participate in the assignment.

Before starting, ensure that:
1. You have already closed the transition from Scheduling in P19.
2. You are clear about which team of drivers will participate in the calculation.
3. You know whether you will add a few drivers manually or if you need a bulk load.
4. You have access to the environment with permissions to manage personnel.

For this quick start, use this reference case:

> **I will load and review the driver template that the L1 solution can cover before entering assignment, rules, and availability.**

To create or import the driver template:
1. In GoalBus, go to the **Configuration** > **Personnel** > **Driver Management** module.
ref: P20_Imagen1.png | compact
2. Check if the drivers from the case already exist in the general list.
3. If you need to create a few drivers, click on **New Driver**.
ref: P20_Imagen2.png | compact(2x)
4. If you need to load many drivers, perform a bulk import via CSV file from **Personnel Load**.
ref: P20_Imagen3.png | compact
5. If you choose bulk import, prepare the file with the minimum data your operation needs to correctly identify each person. The import window will act as a help to prepare the CSV load file.
ref: P20_Imagen4.png
6. Execute the load and review the result.
7. Return to the general list and check that the drivers appear correctly.
8. If you detect duplicates or incomplete records, correct them before proceeding.

## Verifying the Driver Profile and Structural Data

Before proceeding, ensure that:
1. Drivers from L1 are already registered or imported.
2. The general list reflects a single reference template.
3. You can open each driver's profile to review their operational context.

Once you have completed this section, you should have a loaded and visible driver template in the system. fileciteturn38file0L1-L7 fileciteturn38file2L1-L24

## Reviewing the Driver Profile and Structural Data

After creating the template, you need to review the **driver profile**. The profile is not just a contact card: it is the complete digital file of the employee within the operation. There, static data, operational context, and attributes that the system will use later to reason about their eligibility coexist. fileciteturn38file0L8-L20 fileciteturn38file2L25-L40

Before starting this section, make sure that:
1. You have visible drivers in the general list.
2. You know which driver or group to use as an example.
3. You want to validate that the registration is not only administrative, but also operational.

To review the driver profile:
1. In the general list, click on a driver's name.
ref: P20_Imagen5.png | full
2. Review the static data sidebar.
3. Check at least these groups of information:
   1. basic data, such as name and code,
   2. operational data, such as collective agreement or contract type,
   3. operational links, such as main depot, work group, area, or authorized vehicle types.
4. If any critical structural data is missing, complete it before proceeding.
5. Save any necessary changes.
6. Repeat the review for several drivers to confirm consistency in the template.

# Checking the Reference Case

1. Check the driver's code.
2. Review their main depot.
3. Check their work group.
4. Review the operational properties that will condition their subsequent assignment.

When you finish this section, you should have a clear understanding that each driver has a coherent and usable operational file. 

## Reviewing the Operational Context and Dynamic Data of the Driver

In addition to the structural data, the driver's profile includes dynamic data that directly affects how the system reasons about the person. On the administration tab, you can review counters and work patterns, which form part of the operational context used later by the assignment logic. 

Before starting this section, ensure that:
1. You have already reviewed the static data of the profile.
2. You know if your operation uses counters or cyclic patterns.
3. You want to check that the driver not only exists, but also has an interpretable operational context.

To review the dynamic operational context:
1. Within the driver's profile, open the **Administration Details** tab.
2. Review the **counters** or KPIs associated with the driver if they exist.
3. Check if the driver is linked to any **work patterns**.
4. If your operation uses cyclic patterns, also review the shift or current position of the driver within the pattern.
5. Confirm that these data make sense in the real context.
6. If the dynamic information is incorrect, adjust it before moving on to rules or calculations.

## Validating Authorizations Before Using the Driver in Rostering

Before considering a driver eligible, you need to review their **authorizations**. These authorizations answer the question “Can this person work legally or technically in this depot, group, or unit?”. They are managed in a temporal line with start and end dates, and the system displays states such as active, future, expired, or about to expire to facilitate reading. If a person is not authorized for the required context, the engine generates an error when attempting to assign them.

Before starting this section, ensure that:
1. You have already reviewed the driver's profile.
2. You know which depot, group, or unit will be needed for your case.
3. You understand that an authorization is not the same as a temporary assignment or transfer.

To review and validate authorizations:
1. Within the driver's profile, open the **Authorizations / Qualifications** tab.
2. Check if there are active records for:
   1. depots,
   2. work groups,
   3. business units.
3. Verify the visual state of each authorization:
   1. active,
   2. future,
   3. about to expire,
   4. expired.
4. If a necessary authorization is missing, add it with the correct dates.
5. If an authorization has expired and should not be used, leave it as a historical record without attempting to rewrite the past.
6. Save the changes.
7. Confirm that the driver is now authorized for the context where you plan to use them.

## Validating Authorizations Before Using the Driver in Rostering

When you finish this section, you should have validated not only the driver's identity but also their dynamic operational context.

### Questions to Ask Yourself

1. Does this driver have the pattern they should have?
2. Are their counters or KPIs available if the process needs them?
3. Can the system reason correctly about this person in an assignment calculation?

fileciteturn38file0L12-L17

fileciteturn38file0L17-L34

## Confirming the Roster is Ready for the Next Layer of Rostering

Before proceeding, ensure that the driver base is ready to enter the next layer: operational assignment, rules, absences, and calculation. Here, the goal is not only to have names loaded, but a coherent, traceable, and usable roster by the system.

Before finishing, make sure that:
1. You have already loaded or imported the roster.
2. You have reviewed the main profiles.
3. You have checked structural and dynamic data.
4. You have validated essential authorizations.

To confirm that the roster is already prepared:
1. Go back to the general list of drivers.
2. Check that the necessary team is present for your case.
3. Verify that critical profiles do not have important information gaps.
4. Ensure that the people you plan to use are authorized for the correct context.
5. Ask yourself if the system could already use this base as a starting point for:
   1. operational assignment,
   2. Rostering rules,
   3. and real-time availability.
6. If the answer is yes, continue with the next quick start.
7. If the answer is no, correct the driver base before proceeding.

## Confirming the Roster is Ready for the Next Layer of Rostering

The final step is to verify that the driver base is ready to enter the next layer of Rostering. Here, the objective is not only to have drivers that exist in the template, but also to have them eligible from an operational and regulatory perspective.

Before finishing, make sure that:
1. The driver is authorized for the correct depot.
2. The required work group is covered.
3. There are no expirations that break the current eligibility.

When you finish this section, you should have drivers that are not only present in the template, but also operationally and normatively eligible.

## Reference Case Completion

To complete this quick start, you should be able to confirm the following:
1. The L1 driver template is loaded.
2. Key profiles have been reviewed.
3. Essential authorizations are active.
4. The base is ready for operational assignment.

Once you complete this section, you should have a solid driver template in place to proceed with the next layer of Rostering.

## Additional Readings

- [Managing the Operational Assignment of the Driver](P21_Gestionando_la_adscripcion_operativa_del_conductor.md)