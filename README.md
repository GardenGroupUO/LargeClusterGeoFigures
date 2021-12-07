# LargeClusterGeoFigures: Obtaining Plots about Geometric Properties of Nanoclusters and Other Chemical Systems

[![PyPI - Python Version](https://img.shields.io/badge/Python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)](https://docs.python.org/3/)
[![Citation](https://img.shields.io/badge/Citation-click%20here-green.svg)](https://dx.doi.org/10.1021/acs.jcim.0c01128)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/GardenGroupUO/LargeClusterGeoFigures)](https://github.com/GardenGroupUO/LargeClusterGeoFigures)
[![Licence](https://img.shields.io/github/license/GardenGroupUO/LargeClusterGeoFigures)](https://www.gnu.org/licenses/agpl-3.0.en.html)
[![LGTM Grade](https://img.shields.io/lgtm/grade/python/github/GardenGroupUO/LargeClusterGeoFigures)](https://lgtm.com/projects/g/GardenGroupUO/LargeClusterGeoFigures/context:python)

Authors: Geoffrey R. Weal, Caitlin A. Casey-Stevens and Dr. Anna L. Garden (University of Otago, Dunedin, New Zealand)

Group page: https://blogs.otago.ac.nz/annagarden/

Page to cite with work from: *XXX*; XXX; 

## What is this Program?



## Pre-Requisite Programs

LargeClusterGeoFigures requires the following programs before it can be used:

* Atomic Simulation Environment (ASE): https://wiki.fysik.dtu.dk/ase/
* ASAP3: https://wiki.fysik.dtu.dk/asap
* Packaging

The easiest way to install these is through pip. Type the following two lines into the terminal: 

.. code-block:: bash

	pip3 install --upgrade --user ase packaging
	pip3 install --upgrade --user asap3==3.11.10

See https://pip.pypa.io/en/stable/installation/ if you do not have pip installed on your computer. 

## Installation

To install this program on your computer, pop open your terminal, ``cd`` to where you want to place this program on your computer, and clone the program to your computer by typing the following into your terminal:

```
git clone https://github.com/GardenGroupUO/LargeClusterGeoFigures
```

If you do not have ``git`` installed on your computer, see https://www.atlassian.com/git/tutorials/install-git

Once you have done this, type ``pwd`` into the terminal and copy this path into your ``~\.bashrc`` in the following format:

```bash
#####################################################################################
# These lines will allow python to locate this program on your computer.
export PATH_TO_ClusterGeoFigures='/PATH_GIVEN_BY_THE_PWD_COMMAND/LargeClusterGeoFigures'
export PYTHONPATH="$PATH_TO_ClusterGeoFigures":$PYTHONPATH
#####################################################################################
```

This will allow your computer to run this program through your terminal on python3.

## How to Run LargeClusterGeoFigures

An example of the script used to run this program is given below, called ``Run_ClusterGeoFigures.py``.

```python
from LargeClusterGeoFigures import LargeClusterGeoFigures_Program

r_cut = 2.9
elements = ['Cu','Pd']
focus_plot_with_respect_to_element = 'Pd'
add_legend = False

all_path_to_xyz_files = ['309_ish/clusters_for_paper','147_ish/clusters_for_paper']

for path_to_xyz_files in all_path_to_xyz_files:
	LargeClusterGeoFigures_Program(r_cut,elements,focus_plot_with_respect_to_element,path_to_xyz_files,add_legend)
```

When you execute this program by running ``python3 Run_LargeClusterGeoFigures.py`` in the terminal, LargeClusterGeoFigures will 

## What will LargeClusterGeoFigures do when you run the ``Run_LargeClusterGeoFigures.py`` script?

This will make excel spreadsheets that include the number of atoms in your clusters that have been counted as:

	* vertex: number_of_neighbours <= 6
	* edge: 7 <= number_of_neighbours <= 8
	* face: 9 <= number_of_neighbours <= 11
	* bulk: number_of_neighbours >= 12

The excel spreadsheets will also include the distances between atoms in each cluster. 

A folder will also contain xyz files of clusters, where:

	* cluster_name+'_no_of_neighbours.xyz': This is the number of neighbours that each atom in the cluster contains for the r_cut value that is given
	* cluster_name+'_nn_type.xyz': This is the type of atom that each atom has been cast as being:

The types of atoms that you can have are (with its given tag for cluster_name+'nn_type.xyz'):

	* bulk (tag = 0)
	* face (tag = 1)
	* edge (tag = 2)
	* vertex (tag = 3)

## Output files that are created by LargeClusterGeoFigures



## Other useful programs in LargeClusterGeoFigures



## About

<div align="center">

| Python        | [![PyPI - Python Version](https://img.shields.io/badge/Python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)](https://docs.python.org/3/) | 
|:-------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| Repositories  | [![GitHub release (latest by date)](https://img.shields.io/github/v/release/GardenGroupUO/LargeClusterGeoFigures)](https://github.com/GardenGroupUO/LargeClusterGeoFigures) |
| Documentation | [![GitHub release (latest by date)](https://img.shields.io/github/v/release/GardenGroupUO/LargeClusterGeoFigures)](https://github.com/GardenGroupUO/LargeClusterGeoFigures) | 
| Citation      | [![Citation](https://img.shields.io/badge/Citation-click%20here-green.svg)](https://dx.doi.org/10.1021/acs.jcim.0c01128) | 
| Tests         | [![LGTM Grade](https://img.shields.io/lgtm/grade/python/github/GardenGroupUO/LargeClusterGeoFigures)](https://lgtm.com/projects/g/GardenGroupUO/LargeClusterGeoFigures/context:python)
| License       | [![Licence](https://img.shields.io/github/license/GardenGroupUO/LargeClusterGeoFigures)](https://www.gnu.org/licenses/agpl-3.0.en.html) |
| Authors       | Geoffrey R. Weal, Caitlin A. Casey-Stevens, and Dr. Anna L. Garden |
| Group Website | https://blogs.otago.ac.nz/annagarden/ |

</div>
