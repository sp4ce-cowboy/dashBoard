# _Executive_
A hierarchical, all-encompassing, quantifiable life-organization system.

## Background
> _“What is not defined cannot be measured. What is not measured, cannot be improved. What is not improved, is always degraded”_ - British Physicist William Thomson Kelvin

Conceptualization of a productivity system that I have been playing around with for quite some time. This project is the prototypical programmatic implementation of such a system, written entirely in Python. I wrote this program during the winter break (december) of 2022, after my first [introductory programming course](https://nusmods.com/courses/CS1010E/programming-methodology).

This endeavour was never really intended to be a proper, formal "coding project", more for my own personal use and thus I didn't think to host it on GitHub, at least not until it was "polished", but I'm doing so nonetheless in the interest of archiving my old projects, in hopes of imbuing them with some element of tangibility. _Also for logistical reasons, I might want to monetize this idea one day._

My proposed [Orbital '23](https://orbital.comp.nus.edu.sg) project was closely related to this, (proposal's [here](docs/ORTBITAL_PROPOSAL.pdf)) but due to unforeseen circumstances that inititative was halted in its infancy.

## The Concept

The concept is relatively straightforward, once certain key terms are defined.

- **Step 1:** Categorize your life into several domains.
- **Step 2:** Categorize these domains into sub-areas.
- **Step 3:** Assign "directives" to each sub-area.
- **Step 4:** Address each directive as they become relevant.
- **Step 5:** At any point in time, have a quantified representation of how "organized/intact/complete" your life is.

#### Domains
- Domains are large areas of your life that you need to actively manage.
- Each domain can be further divided into into sub-areas.
- For example:
    - Domains: "Health", "Finances", "Academics", etc.
    - Sub-areas could be "Physical Fitness", "Budget", and "Academic Plan", respectively.
    - Each domain can have any number of sub-areas.

#### Directives
- Directives are singular, actionable instructions for the maintenance of each sub-area.
- Each directive is assigned a weightage (points) between 0 and 10.
- Unless actively deleted, directives are permanent and do not "go away" once "completed".
- Instead, directives are "addressed" until they become relevant again (or "expire")
    - This could be on a **periodic** basis (daily, weekly, monthly) [E.g. _"Drink 3 liters of water everyday"_]
    - This could also be on an **entropic**  (i.e. ad-hoc) basis [E.g. _"Visit dentist"_]


#### Directives vs. Tasks
This might sound awfully similar to a habit tracker or a task manager, but there are some key differences that, from my experience, I could not find in any other application/system/framework. 

**Directives are persistent**
Unlike tasks, directives don't disappear once completed. Thus, not everything can be a directive. Only those specfific things that directly contribute to a certain part of your life (and do so continuously) can be considered a directive. 
- "Submit all assignments for the day" is a directive. "Submit CS2103 assignment" is not a directive.
- Rationale: The first refers to a general, broad-level repeating occurence. If all assignments are submitted for the day, or if a particular day has no assignments, this directive remains "addressed". The latter refers to a particular task that, once completed, can be discarded.
- _However, "Submit CS2103 weekly assignment" is a valid directive. It is sufficiently general and it is a repeating occurence for a reasonable period of time (i.e 1 semester)_

**Directives are quantifiable**
TBC

 

