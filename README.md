# Dashboard
A hierarchical, all-encompassing, quantifiable life organization system.

## Overview
Conceptualization of a productivity system that I have been playing around with for quite some time. This project is the prototypical programmatic implementation of such a system – a CLI application written entirely in Python (~500 LoC), in procedural progamming style. My proposed [Orbital '23](https://orbital.comp.nus.edu.sg) project was closely related to this idea, which can be found [here](docs/ORTBITAL_PROPOSAL.pdf)).

<img width="1103" alt="image" src="https://github.com/sp4ce-cowboy/executive/assets/19762596/30ff9403-cda2-437f-a335-f8a34d002a61">

Having a quantified representation of things can make them less subjective and more actionable. Something that can be quantified can be tracked, and something that can be tracked can be improved. Something that can be tracked and improved can be gamified and incentivized as well. The concept is relatively straightforward, but the process of setting up the system might require some self-reflection into the things that constitute your life, regardless of how minor they might be. Everything from renewing your passport once every 10 years to walking your dog everyday. 

## The Concept

- **Step 1:** Categorize your life into several domains.
- **Step 2:** Categorize these domains into sub-areas.
- **Step 3:** Assign "directives" to each sub-area, and a weightage score for each.
- **Step 4:** Address each directive as they become relevant.
- **Step 5:** At any point in time, have a quantified representation of how "intact" your life is.
- **Bonus:** Reconfigure domains, sub-areas, directives and their weightage as needed.

## Features

### Main Features
- View all directives
- View directives sorted by their type, chronology, or completion
- View statistics
- Complete and Reset (i.e. mark and unmark) directives

### Additional Features
- Write/journal notes which are automatically timestamped
- Read notes
- Set tasks for the day

### Statistics
As shown below, different statistic metrics (overall, daily, entropy, critical) can be tabulated based on the specific combination of completed directives,
providing different perspectives about the current state of affairs.

<a>
    <img height="280" align="center" alt="image" src="https://github.com/sp4ce-cowboy/executive/assets/19762596/b44a3595-c021-4fb4-b2df-39666b132f29">

</a>
<a>
    <img height="280" align="center" alt="image" src="https://github.com/sp4ce-cowboy/executive/assets/19762596/03cdef86-3fc7-4565-aa6e-4735e1416ed7">

</a>

### Pending Features
- Add/Delete directives from the application directly*

_*Note: Directives can still be added/deleted from the .csv file directly_

## Usage
Running this program requires that you have `pandas` installed, for csv file manipulation.
   
```sh
pip3 install pandas
```

1. Download the latest release from [here](https://github.com/sp4ce-cowboy/executive/releases/tag/v1.0)

2. Unzip the downloaded release, ensure that all files are contained within the same folder.

3. Navigate into the directory with

```sh
cd <PATH>
```

4. Run Dashboard

```sh
python3 main.py
```

All files are directly accessible in their text form. Thus, deleting the application will not delete your notes, tasks, or directives.

## Notes
_I wrote this CLI application during the winter break (december) of 2022, after my first [introductory programming course](https://nusmods.com/courses/CS1010E/programming-methodology), without any real SWE experience, so expect some subpar code quality and unhandled exceptions. I don't intend to fix it as this project is more of a proof-of-concept prototype than anything else, instead I'll be incorporating this idea of quantification/gamification into a future project._

