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

all_path_to_files = ['309_ish/clusters_for_paper','147_ish/clusters_for_paper']
record_all_files = False

auto_centre = False
record_bond_distance = False

for path_to_files in all_path_to_files:
	LargeClusterGeoFigures_Program(r_cut,elements=elements,focus_plot_with_respect_to_element=focus_plot_with_respect_to_element,path_to_files=path_to_files,record_all_files=record_all_files,add_legend=add_legend,bulk_colour=bulk_colour,face_colour=face_colour,vertex_colour=vertex_colour,edge_colour=edge_colour,none_colour=none_colour,auto_centre=auto_centre,record_bond_distance=record_bond_distance)