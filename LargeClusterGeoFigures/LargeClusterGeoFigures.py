import os
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

	def analyse_cluster_data(self,cluster_information):
		analysed_cluster_information = []
		for name, element_number_of_neighbours, all_number_of_neighbours, cluster in cluster_information:
			# ---------------------------------------------------------------------
			analysed_element_number_of_neighbours = {}
			for number_of_neighbours, indices in element_number_of_neighbours.items():
				if number_of_neighbours >= 12:
					element_type_name = 'bulk'
				elif 9 <= number_of_neighbours <= 11:
					element_type_name = 'face'
				elif 7 <= number_of_neighbours <= 8:
					element_type_name = 'edge'
				elif number_of_neighbours <= 6:
					element_type_name = 'vertex'
				else:
					exit('Huh?')
				add_to_dictionary_list(analysed_element_number_of_neighbours,element_type_name,indices)
			# ---------------------------------------------------------------------
			analysed_all_number_of_neighbours = {}
			for number_of_neighbours, indices in all_number_of_neighbours.items():
				if number_of_neighbours >= 12:
					element_type_name = 'bulk'
				elif 9 <= number_of_neighbours <= 11:
					element_type_name = 'face'
				elif 7 <= number_of_neighbours <= 8:
					element_type_name = 'edge'
				elif number_of_neighbours <= 6:
					element_type_name = 'vertex'
				else:
					exit('Huh?')
				add_to_dictionary_list(analysed_all_number_of_neighbours,element_type_name,indices)
			# ---------------------------------------------------------------------
			analysed_cluster_information.append((name, analysed_element_number_of_neighbours, analysed_all_number_of_neighbours, cluster))
		return analysed_cluster_information

	def record_to_excel(self, analysed_cluster_information):

		workbook = Workbook()
		worksheet = workbook.active

		# pink, red, blue, green
		colours = {'bulk': 'FFC0CB', 'face': 'FF0000', 'edge': 'ADD8E6', 'vertex': '90EE90', 'None': 'FFFFFF'}
		def get_colour_name(name):
			for colour_name in colours.keys():
				if colour_name in name:
					return colour_name
			return 'None'

		other_namings = [[type_of_NN+': element', type_of_NN+': all', type_of_NN+': percent'] for type_of_NN in self.types_of_NNs]
		naming = [str(tuple(self.elements))]+list(itertools.chain.from_iterable(other_namings))
		for index in range(len(naming)):
			name = naming[index]
			worksheet.cell(column=index+1, row=1, value=str(name))
			worksheet.cell(column=index+1, row=1).fill = PatternFill("solid", fgColor=colours[get_colour_name(name)])

		for index_aci in range(len(analysed_cluster_information)):
			cluster_name, analysed_element_number_of_neighbours, analysed_all_number_of_neighbours, cluster = analysed_cluster_information[index_aci]
			worksheet.cell(column=1, row=index_aci+2, value=str(cluster_name))
			for index2 in range(len(self.types_of_NNs)):
				types_of_NN = self.types_of_NNs[index2]
				element_NN = len(analysed_element_number_of_neighbours[types_of_NN]) if (types_of_NN in analysed_element_number_of_neighbours) else 0
				all_NN     = len(analysed_all_number_of_neighbours[types_of_NN]) if (types_of_NN in analysed_all_number_of_neighbours) else 0

				worksheet.cell(column=index2+2, row=index_aci+2, value=str(element_NN))
				worksheet.cell(column=index2+2, row=index_aci+2).fill = PatternFill("solid", fgColor=colours[get_colour_name(types_of_NN)])

				worksheet.cell(column=index2+3, row=index_aci+2, value=str(all_NN))
				worksheet.cell(column=index2+3, row=index_aci+2).fill = PatternFill("solid", fgColor=colours[get_colour_name(types_of_NN)])

				percentage = (float(element_NN)/float(all_NN))*100.0
				worksheet.cell(column=index2+4, row=index_aci+2, value=str(percentage))
				worksheet.cell(column=index2+4, row=index_aci+2).fill = PatternFill("solid", fgColor=colours[get_colour_name(types_of_NN)])
		# Save the file
		workbook.save("LargeClusterGeo_Data_Path"+self.path_to_here.replace(self.original_path,'').replace('/','_')+'_focus_element_'+str(self.focus_plot_with_respect_to_element)+".xlsx")
