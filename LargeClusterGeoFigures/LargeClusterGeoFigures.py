import os, shutil
import numpy as np
import matplotlib.colors as mcolors

from ase.io import read, write
from ase.visualize import view

#from ase.data import atomic_numbers, chemical_symbols
#from asap3.analysis.rdf import RadialDistributionFunction

from collections import Counter

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

from LargeClusterGeoFigures.No_Of_Neighbours import No_Of_Neighbours

from openpyxl import Workbook
from openpyxl.styles import Border, Side, PatternFill, Font, GradientFill, Alignment

import itertools

def add_to_dictionary_list(analysed_element_number_of_neighbours,element_type_name,indices):
	analysed_element_number_of_neighbours[element_type_name] = analysed_element_number_of_neighbours.get(element_type_name,[]) + indices

def get_distance(distance1,distance2):
	dist_xx = distance1[0] - distance2[0]
	dist_yy = distance1[1] - distance2[1]
	dist_zz = distance1[2] - distance2[2]
	distance = (dist_xx**2.0 + dist_yy**2.0 + dist_zz**2.0) ** 0.5
	return distance

class LargeClusterGeoFigures_Program:
	def __init__(self, r_cut, elements=['Cu','Pd'],focus_plot_with_respect_to_element='Cu',path_to_here='.',add_legend=False):
		self.path_to_here = os.path.abspath(path_to_here)
		self.r_cut = r_cut
		self.elements = elements
		self.focus_plot_with_respect_to_element = focus_plot_with_respect_to_element
		self.add_legend = add_legend

		self.original_path = os.getcwd()
		self.types_of_NNs = ['bulk', 'face', 'edge', 'vertex']

		self.run()

	def run(self):
		print('--------------------------------------')
		print('Processing: '+str(self.path_to_here))
		print('--------------------------------------')
		print('Getting data from XYZ files')
		clusters_data = self.get_cluster_data()
		print('Finished getting data from XYZ files')
		print('--------------------------------------')
		print('Processing data')
		cluster_information = self.process_cluster_data(clusters_data)
		print('Processed data')
		print('--------------------------------------')
		print('Analysing data')
		analysed_cluster_information = self.analyse_cluster_data(cluster_information)
		print('Finished analysing data')
		print('--------------------------------------')
		print('Making excel spreadsheet')
		self.record_to_excel(analysed_cluster_information)
		print('Finished excel spreadsheet')
		print('--------------------------------------')

	def get_cluster_data(self):
		clusters_data = []
		for root, dirs, files in os.walk(self.path_to_here):
			for file in files:
				if file.endswith('OUTCAR'):
					name = root.replace(self.original_path,'')
					cluster = read(root+'/'+file)
					clusters_data.append((cluster,name))
					dirs[:] = []
		clusters_data.sort(key=lambda x:len(x[0]))
		return clusters_data

	def process_cluster_data(self,clusters_data):
		cluster_information = self.process_NN_1(clusters_data)
		return cluster_information

	def process_NN_1(self, clusters_data):
		cluster_information = []
		for cluster, name in clusters_data:
			nl = No_Of_Neighbours([self.r_cut/2.0]*len(cluster))
			nl.update(cluster)
			all_number_of_neighbours = {}
			element_number_of_neighbours = {}
			for index in range(len(cluster)):
				indices, offsets = nl.get_neighbors(index)
				number_of_neighbours = len(indices)
				all_number_of_neighbours.setdefault(number_of_neighbours,[]).append(index)
				if cluster[index].symbol == self.focus_plot_with_respect_to_element:
					element_number_of_neighbours.setdefault(number_of_neighbours,[]).append(index)
			cluster_information.append((name, element_number_of_neighbours, all_number_of_neighbours, cluster))
		return cluster_information

	def get_nn_type(self,number_of_neighbours):
		if number_of_neighbours >= 12:
			nn_type = 0
		elif 9 <= number_of_neighbours <= 11:
			nn_type = 1
		elif 7 <= number_of_neighbours <= 8:
			nn_type = 2
		elif number_of_neighbours <= 6:
			nn_type = 3
		else:
			exit('Huh?')
		return nn_type

	def analyse_cluster_data(self,cluster_information):
		analysed_cluster_information = []
		for name, element_number_of_neighbours, all_number_of_neighbours, cluster in cluster_information:
			# ---------------------------------------------------------------------
			analysed_element_number_of_neighbours = {}
			for number_of_neighbours, indices in element_number_of_neighbours.items():
				element_type_name = self.types_of_NNs[self.get_nn_type(number_of_neighbours)]
				add_to_dictionary_list(analysed_element_number_of_neighbours,element_type_name,indices)
			# ---------------------------------------------------------------------
			analysed_all_number_of_neighbours = {}
			for number_of_neighbours, indices in all_number_of_neighbours.items():
				element_type_name = self.types_of_NNs[self.get_nn_type(number_of_neighbours)]
				add_to_dictionary_list(analysed_all_number_of_neighbours,element_type_name,indices)
			# ---------------------------------------------------------------------
			analysed_cluster_information.append((name, analysed_element_number_of_neighbours, analysed_all_number_of_neighbours, cluster))
		return analysed_cluster_information

	def record_to_excel(self, analysed_cluster_information):

		workbook = Workbook()
		worksheet = workbook.active
		worksheet.title = 'Info'

		# pink, red, blue, green
		colours = {'bulk': 'FFC0CB', 'face': 'FF0000', 'edge': 'ADD8E6', 'vertex': '90EE90', 'None': 'FFFFFF'}
		def get_colour_name(name):
			for colour_name in colours.keys():
				if colour_name in name:
					return colour_name
			return 'None'

		other_namings = [[type_of_NN+': element', type_of_NN+': all', type_of_NN+': percent'] for type_of_NN in self.types_of_NNs]
		naming = ['name', str(tuple(self.elements)), 'No of atoms']+list(itertools.chain.from_iterable(other_namings))
		for index in range(len(naming)):
			name = naming[index]
			worksheet.cell(column=index+1, row=1, value=str(name))
			worksheet.cell(column=index+1, row=1).fill = PatternFill("solid", fgColor=colours[get_colour_name(name)])

		analysed_cluster_information.sort(key=lambda x: (len(x[3]),tuple(value for key, value in sorted(Counter(x[3].get_chemical_symbols()).items()))))

		for index_aci in range(len(analysed_cluster_information)):
			cluster_name, analysed_element_number_of_neighbours, analysed_all_number_of_neighbours, cluster = analysed_cluster_information[index_aci]
			worksheet.cell(column=1, row=index_aci+2, value=str(cluster_name))
			worksheet.cell(column=2, row=index_aci+2, value=str(cluster.get_chemical_formula()))
			worksheet.cell(column=3, row=index_aci+2, value=str(len(cluster)))

			for index2 in range(len(self.types_of_NNs)):
				types_of_NN = self.types_of_NNs[index2]
				element_NN = len(analysed_element_number_of_neighbours[types_of_NN]) if (types_of_NN in analysed_element_number_of_neighbours) else 0
				all_NN     = len(analysed_all_number_of_neighbours[types_of_NN]) if (types_of_NN in analysed_all_number_of_neighbours) else 0

				worksheet.cell(column=3*index2+4, row=index_aci+2, value=str(element_NN))
				worksheet.cell(column=3*index2+4, row=index_aci+2).fill = PatternFill("solid", fgColor=colours[get_colour_name(types_of_NN)])

				worksheet.cell(column=3*index2+5, row=index_aci+2, value=str(all_NN))
				worksheet.cell(column=3*index2+5, row=index_aci+2).fill = PatternFill("solid", fgColor=colours[get_colour_name(types_of_NN)])

				percentage = (float(element_NN)/float(all_NN))*100.0
				worksheet.cell(column=3*index2+6, row=index_aci+2, value=str(percentage))
				worksheet.cell(column=3*index2+6, row=index_aci+2).fill = PatternFill("solid", fgColor=colours[get_colour_name(types_of_NN)])
		# write distances into excel
		print('Writing bond distance data to excel')
		workbook_name = "LargeClusterGeo_Data_Path"+self.path_to_here.replace(self.original_path,'').replace('/','_')+'_focus_element_'+str(self.focus_plot_with_respect_to_element)
		workbook_cluster_folder = workbook_name+'_clusters'
		if os.path.exists(workbook_cluster_folder):
			shutil.rmtree(workbook_cluster_folder)
		os.makedirs(workbook_cluster_folder)
		for index_aci in range(len(analysed_cluster_information)):
			cluster_path, analysed_element_number_of_neighbours, analysed_all_number_of_neighbours, cluster = analysed_cluster_information[index_aci]
			cluster_name = str(len(cluster))+'_'+str(cluster.get_chemical_formula())+'_'+cluster_path.split('/')[-1]
			print(str(index_aci+1)+' out of '+str(len(analysed_cluster_information))+' ('+str(cluster_name)+')')
			worksheet = workbook.create_sheet()
			worksheet.title = str(cluster_name)
			worksheet.cell(row=1, column=1).value = 'r_cut = '
			worksheet.cell(row=1, column=2).value = str(self.r_cut)
			symbols = cluster.get_chemical_symbols()
			for index1 in range(len(cluster)):
				worksheet.cell(row=4+index1, column=1).value = worksheet.cell(row=1, column=4+index1).value = str(symbols[index1])
				worksheet.cell(row=4+index1, column=3).value = worksheet.cell(row=3, column=4+index1).value = str(index1)
			no_of_nearest_neighbours_per_atom = {index: 0 for index in range(len(cluster))}
			cluster_positions = cluster.get_positions()
			for index1 in range(len(cluster)):
				for index2 in range(index1+1,len(cluster)):
					distance = get_distance(cluster_positions[index1],cluster_positions[index2])
					worksheet.cell(row=4+index1, column=4+index2).value = worksheet.cell(row=4+index2, column=4+index1).value = str(round(distance,3))
					if distance <= self.r_cut:
						no_of_nearest_neighbours_per_atom[index1] += 1
						no_of_nearest_neighbours_per_atom[index2] += 1
						worksheet.cell(row=4+index1, column=4+index2).fill = worksheet.cell(row=4+index2, column=4+index1).fill = PatternFill("solid", fgColor='FFC0CB')
					else:
						worksheet.cell(row=4+index1, column=4+index2).fill = worksheet.cell(row=4+index2, column=4+index1).fill = PatternFill("solid", fgColor='90EE90')
				worksheet.cell(row=4+index1, column=2).value = worksheet.cell(row=2, column=4+index1).value = str(no_of_nearest_neighbours_per_atom[index1])
			# The number of neighbours on each atom
			nn_atoms = [nn for index, nn in sorted(no_of_nearest_neighbours_per_atom.items())]
			cluster.set_tags(nn_atoms)
			xyz_file_name = cluster_name+'_no_of_neighbours'
			write(workbook_cluster_folder+'/'+xyz_file_name+'.xyz',cluster)
			# The types of vertices on each atom
			type_of_nn_atoms = [self.get_nn_type(nn) for index, nn in sorted(no_of_nearest_neighbours_per_atom.items())]
			cluster.set_tags(type_of_nn_atoms)
			xyz_file_name = cluster_name+'_nn_type'
			write(workbook_cluster_folder+'/'+xyz_file_name+'.xyz',cluster)
			with open(workbook_cluster_folder+'/filenames_to_paths.txt','a') as xyz_names_to_path:
				xyz_names_to_path.write(str(cluster_name)+': '+str(cluster_path)+'\n')
		# Save the file
		print('Saving excel file')
		workbook.save(workbook_name+".xlsx")
		print('Done saving excel file')