
# Insight_Assignment
Welcome! These files were built as part of a coding challenge for Project for Insight valuation.

This file is specifically built to be used to do the H1B approval analysis on an yearly basis. Python3 file takes three parameters as inputs 
	a. Source file should be in semicolon(;) separated format. 
	b. Output File: Occupations.txt - lists the top 10 occupations that have been approved with total count and approval percentage 
	c. Output File: States.txt - Lists the top 10 states that have largest number of H1B workers based and working there. 
	
	please make sure that all the folders and files exist in the desired format for the program to run properly. You can change the path by editing the shell file and providing details in the arguments.
	
	Even though github doesn't support the uploading of large data files, they have been run on the local directories and the program does work fine and produce the desired output.
	
	Program looks and reads the source file first line for header data which is later used for filtering purposes. program does parametrize it and small filter changes can be performed to handle other filters as well. For status it looks for the header row to have "STATUS" text. similarly for Work State and SOC Name.
	
	It runs filters on Certified records and creates dictionaries and tuples to perform sorting initially based on number of certified applications followed by SOC_Name or State depending on the output file.
	It creates two different files and file handling through Path makes it platform independent.
	
	Thanks for giving us an opportunity to participate in the coding challenge
