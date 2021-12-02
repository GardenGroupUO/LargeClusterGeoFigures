from LargeClusterGeoFigures import LargeClusterGeoFigures_Program

r_cut = 2.9
elements = ['Cu','Pd']
focus_plot_with_respect_to_element = 'Pd'
add_legend = False

all_path_to_xyz_files = ['309_ish/clusters_for_paper','147_ish/clusters_for_paper']

for path_to_xyz_files in all_path_to_xyz_files:
	LargeClusterGeoFigures_Program(r_cut,elements,focus_plot_with_respect_to_element,path_to_xyz_files,add_legend)
