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

bulk_colour = (251/255.0,180/255.0,185/255.0) #'#FFFFFF'
face_colour = (247/255.0,104/255.0,161/255.0) #'#FF0000'
vertex_colour = (197/255.0,27/255.0,138/255.0) #'#90EE90'
edge_colour = (122/255.0,1/255.0,119/255.0) #'#ADD8E6'
none_colour = '#FFFFFF'

all_path_to_xyz_files = ['309_ish/clusters_for_paper','147_ish/clusters_for_paper']

auto_centre = False

for path_to_xyz_files in all_path_to_xyz_files:
	LargeClusterGeoFigures_Program(r_cut,elements=elements,focus_plot_with_respect_to_element=focus_plot_with_respect_to_element,path_to_xyz_files=path_to_xyz_files,add_legend=add_legend,bulk_colour=bulk_colour,face_colour=face_colour,vertex_colour=vertex_colour,edge_colour=edge_colour,none_colour=none_colour,auto_centre=auto_centre)
```

The inputs are:
* `r_cut`: The distance between atoms to be considered neighbours, synonymous as the maximum bond distance between atoms. Can give this as a number, or a dictionary between the various elements, for example: ```{'Cu': 2.8, 'Pd': 2.9, ('Cu','Pd'): 2.85}```
* `elements`: The elements that are in your set of clusters.
* `focus_plot_with_respect_to_element`: The element to focus your plots to plot about.
* `add_legend`: add a legend to your plots? ```True``` for yes, ```False``` for no.
* `bulk_colour`: The colour of points symbolising bulk atoms.
* `face_colour`: The colour of points symbolising face atoms.
* `vertex_colour`: The colour of points symbolising vertex atoms.
* `edge_colour`: The colour of points symbolising edge atoms.
* `none_colour`: The colour given if something weird happens. If you see this colour in any plots, investigate.
* `path_to_xyz_files`: This is the folder to explore, including subfolders, that contain the clusters you want to look into.
* `auto_centre`: If you would like to auto center your clusters, including wrapping your cluster if ``VASP`` has made a weird cluster due to the cluster moving over the periodic bound. ``True`` if you want to do this, ``False`` if not. Try using this if the following happens. Default: ``False``. 

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

When you execute this program by running ``python3 Run_LargeClusterGeoFigures.py`` in the terminal, LargeClusterGeoFigures will make plots that describe the distributions of bulk, face, vertex, and edge sites with respect to `focus_plot_with_respect_to_element`. 

## Output files that are created by LargeClusterGeoFigures



## Other useful programs in LargeClusterGeoFigures


## Troubleshooting

### What to do if VASP moves atoms across the periodic boundary such that the cluyster becomes split?

First, try setting the `auto_centre` tag to true and run again. Look at the exel spreadsheet that is make and see that:
* It makes the distributions and bond distances between atoms in those clusters that have this problem make more sense, and
* Dont mess up any other clusters bond distances and distributions that shouldn't have changed because they dont have this issue. 

If this doesn't work, in the same folder as your cluster's `OUTCAR` and (or) `CONTCAR` write a `xyz` file called `LCGF_look_at.xyz`, where you have made any corrections to this cluster to. LargeClusterGeoFigures will not look at your  `OUTCAR` or `CONTCAR` files and instead only look at this `LCGF_look_at.xyz` file. 

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
