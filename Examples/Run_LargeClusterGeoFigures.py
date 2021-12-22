from LargeClusterGeoFigures import LargeClusterGeoFigures_Program

r_cut = 2.9
elements = ['Cu','Pd']
focus_plot_with_respect_to_element = 'Pd'
add_legend = False

bulk_colour = 'FFC0CB'
face_colour = 'FF0000'
vertex_colour = '90EE90'
edge_colour = 'ADD8E6'
none_colour = 'FFFFFF'

all_path_to_xyz_files = ['309_ish/clusters_for_paper','147_ish/clusters_for_paper']

for path_to_xyz_files in all_path_to_xyz_files:
	LargeClusterGeoFigures_Program(r_cut,elements=elements,focus_plot_with_respect_to_element=focus_plot_with_respect_to_element,path_to_xyz_files=path_to_xyz_files,add_legend=add_legend,bulk_colour=bulk_colour,face_colour=face_colour,vertex_colour=vertex_colour,edge_colour=edge_colour,none_colour=none_colour):
