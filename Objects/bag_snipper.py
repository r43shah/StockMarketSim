# bag_snipper.py
# by Raj Shah
# Winter 2018
#
# Purpose: Creating a new bag within a specified start and end time
# by cropping a sequence of bags selected by the user
#
# To call the script: python bag_snipper.py start_time end_time


import rosbag
import sys
import Tkinter
import tkFileDialog

# purpose: collect the bag filepaths and the time period of interest
def collect_inputs():
	filepaths=[]
	start=0
	end=0
	filepaths=get_files()
	start=float(sys.argv[1])
	end=float(sys.argv[2])
	return filepaths,start,end

# purpose: ask user for the filepaths of the bags
def get_files():
	Tkinter.Tk().withdraw()
	filepaths=tkFileDialog.askopenfilenames()
	return filepaths

# purpose: parses through all the bags and writes all the relevant
# data in a new bag
def parse_data(filepaths,start,end):
	write_bag=rosbag.Bag('snipped_bag.bag','w') #initialize new bag
	try:
		n=0
		while n<len(filepaths): #loop through all bags
			print filepaths[n]
			read_bag=rosbag.Bag(filepaths[n]) #read next bag
			start_check=False
			end_check=False
			for topic,msg,t in read_bag.read_messages():
				#check if timestamp is within time period of interest, and set flag as required
				if t.to_sec()>end:
					end_check=True
				if t.to_sec()>=start:
					start_check=True

				#if time period of interest has passed, return
				if end_check==True:
					return

				#write data in new bag if timestamp is within time period of interest
				if start_check==True:
					write_bag.write(topic,msg,t)
			n+=1
		
	finally:
		write_bag.close()
	return

def main():
	filepaths,start,end=collect_inputs()
	parse_data(filepaths,start,end)
	return
	
main()