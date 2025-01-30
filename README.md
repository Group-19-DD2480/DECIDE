# DECIDE

A hypothetical launcher of an anti-ballistic missile system.

The program will, based on radar tracking information, evaluate 15 Launch Interceptor Conditions (LICs) and decide whether or not to launch a response.

By default, the launcher is considered locked, and will only unlock if the relevant LICs are met. In addition to the LICs, the function will also take a vector of Preliminary Unlocking Vector (PUV) that determines which LICs are relevant for the decision, and a Logical Connector Matrix (LCM) which determines which LICs have to be considered in conjunction in order for the launch to proceed.

# Table of Contents

1. [DECIDE](#DECIDE)
2. [Installation](#installation)
3. [Configuration](#configuring-the-program)
4. [Running the program](#running-the-program)
5. [Essence: Our Way of Working](#essence)
6. [License](#license)
7. [Contributions](#contributions)

# Installation

The program is setup to run in a python virtual environment.

### Install venv

The following instructions are made for use in Ubuntu. For other operating systems, use your prefered package manager

```bash
sudo apt install python3-venv
```

### Setup virtual environment

In the home directory of this repo, to create and run a virtual environment:

```bash
python3 -m venv env &&  source ./env/bin/activate
```

Or run an existing environment:

```bash
source env/bin/activate
```

### Install Dependencies

Dependencies can be viewed in requirements.txt, install by running the following when you are in the virtual environment

```bash
pip install -r requirements.txt
```

# Configuring the program

## Input variables

The only function available is decide which takes the variables below as input:

```python
# A list of coordinates acting as radar data. Should be 2 <= x <= 100 elements long
points: list[tuple[float, float]]

# A list of input parameters to the LICs. See below for details on fields for this class
parameters: PARAMETERS_T

# A symmetrical 15x15 matrix of strings acting as logical operators.
# Elements must be either "ANDD", "ORR" or "NOTUSED" (case sensitive).
LCM: list[list[str]]

# A 15 element list of booleans where PUV[i] determines if LIC number i
# should be considered for the launch
PUV: list[bool]
```

### PARAMETERS_T

The class PARAMETERS_T is composed of the arguments to each LIC and has to be initialized with values before use. The available fields are:

```python
# Length parameter used in LICs 0, 7, 12
# Valid values: 0 <= length_1
# Default: 1.0
length_1: float

# Radius parameter using in LICs 1, 8, 13
# Valid values: 0 <= radius_1
# Default: 1.0
radius_1: float

# Deviation from PI in LICs 2, 9
# Valid values: 0 <= epsilon < pi
# Default: 0.5
epsilon: float

# Area used in LICs 3, 10, 14
# Valid values: 0 <= area_1
# Default: 1.0
area_1: float

# no. of consecutive points in LIC 4
# Valid values: 2 <= q_pts <= num_points
# Default: 2
q_pts: int

# No. of quadrants in LIC 4
# Valid values: 1 <= quads <= 3
# Default:  1
 quads: int

# Distance in LIC 6
# Valid values: 0 <= dist
# Default:  1.0
 dist: float

# No. of consecutive points in LIC 6
# Valid values: 3 <= n_pts <= num_points
# Default:  3
 n_pts: int

# No. of int. points in LICs 7, 12
# Valid values: 1 <= k_pts <= (num_points - 2)
# Default:  1
 k_pts: int

# No. of int. points in LICs 8, 13
# Valid values: 1 <= a_pts, a_pts + b_pts <= (num_points - 3)
# Default:  1
 a_pts: int

# No. of int. points in LICs 8, 13
# Valid values: 1 <= b_pts, a_pts + b_pts <= (num_points - 3)
# Default:  1
 b_pts: int

# No. of int. points in LICs 9
# Valid values: 1 <= c_pts, c_pts + d_pts <= (num_points - 3)
# Default:  1
 c_pts: int

# No. of int. points in LICs 8, 13
# Valid values: 1 <= d_pts, c_pts + d_pts <= (num_points - 3)
# Default:  1
 d_pts: int

# No. of int. points in LICs 10, 14
# Valid values: 1 <= e_pts, e_pts + f_pts <= (num_points - 3)
# Default:  1
 e_pts: int

# No. of int. points in LICs 10, 14
# Valid values: 1 <= f_pts, e_pts + f_pts <= (num_points - 3)
# Default:  1
 f_pts: int

# No. of int. points in LICs 11
# Valid values: 1 <= f_pts <= num_points - 2
# Default:  1
 g_pts: int

# Maximum length in LIC 12
# Valid values: 0 <= length_2
# Default:  1.0
 length_2: float

# Maximum radius in LIC 13
# Valid values: 0 <= radius_2
# Default:  1.0
 radius_2: float

# Maximum area in LIC 14
# Valid values: 0 <= area_2
# Default:  1.0
 area_2: float
```

# Running the program

The main function of the program is in src/decide.py. In order to run the program, run in terminal:

```
python src/decide.py
```

Running the program without modifications will use the default values. In order to modify the input values, either modify the global variables in the file, or modify the values passed to the function.

### Running the test suite

In order to run the tests, run the pytest command in the virtual environment:

```
pytest
```

# Essence: Our Way of Working<a name='essence'></a>

At the moment we are in the “Foundation Established” state since we have not met all of the requirements listed in the “In Use” state. The following is an overview of our updated checklist for the “In Use” state:

- [x] The practices and tools are being used to do real work.
- [x] The use of the practices and tools selected are regularly inspected.
- [x] The practices and tools are being adapted to the team’s context.
- [x] The use of the practices and tools is supported by the team.
- [ ] Procedures are in place to handle feedback on the team’s way of working.

_While the team is reflecting on our way of working, we do not at the moment have procedures in place for this. When someone notices an issue, it is brought up, but not in a structured or standardized way._

- [ ] The practices and tools support team communication and collaboration.

_There are some practices and tools that support team communication and collaboration, however they need to be revised as these practices are somewhat inadequate. An example of this would be the way the team reviews Pull Requests. At the moment, we do not have a solid practice for requesting PR-reviews, it is kind of a free-for-all. This has worked since everybody in the team has been good at checking when a PR is open and in need of review but a solid workflow for this should be established._

---

One obstacle to reach the next state is to establish practices/procedures that enable feedback on the team’s way of working. This could for example be to establish weekly retrospective meetings where the team has the opportunity to review our way of working.

Another obstacle to reach the next state is to establish clearer communication and collaboration guidelines on topics such as how to review other team member’s code. These guidelines should include how to handle Pull Requests in a manner that reduces the time a PR spends in review, how many people should review a PR before merging and how to formally communicate that we want additional opinions or changes.

# License

[//]: <> (TODO: Write a proper license)

# Contributions

**Tore Stenberg (HermanKassler):**

Worked on LIC-3, LIC-10, and LIC-14. Wrote the bulk of the README, added global variables and initialized them in decide.py with corresponding tests.

**Zarko Sesto (ErzaDuNord, Zarko Sesto):**

Worked on LIC-1, LIC-8, LIC-13, FUV and LAUNCH. Created tests for the aforementioned.

**Erik Smit (erikgsmit):**

Worked on functionality and testing for LIC-0, LIC-7 and LIC-12. Also implemented the final decision logic (decide function). Some other minor contributions involve setting up the requirements.txt file and PARAMETERS_T dataclass.

**Muhammad Usman (bitGatito):**

Worked on LIC-2, LIC-4, LIC-9. Created calculate_CMV to calculate the CMV. Corresponding tests.

**Ruben Socha (RubenSocha):**

CI with Github Actions, LIC 5, 6 and 11, PUM, some refactoring e.g. FUV.
