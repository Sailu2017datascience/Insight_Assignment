import os
import operator
import csv
import sys, getopt
from pathlib import Path

#Make sure the desired files are given as inputs"
if(len(sys.argv)!=4):
        print("Invalid number of arguments.\n 1. FileName.py\n 2. Input csv File\n 3. Output SOC_Name File.txt\n 4. Output States File.txt") 
else:
        input_File = Path(sys.argv[1])
        output_FileName_prof = Path(sys.argv[2])
        output_FileName_state = Path(sys.argv[3])

        try:
                h1bfile = open(input_File, "r", encoding="utf-8")
                
        except FileNotFoundError:
                print("Input file doesn't exist. Please check")
                exit
        results_Prof_file = open(output_FileName_prof,"w") 
        results_State_file = open(output_FileName_state,"w")                
        
        #Read the file
        soc_Dict = {}
        socName = []
        certified_applications =0
        state_Dict={}

        #initialize variables to determine the index of columns
        firstRow = 0
        case_index = 0
        state_index = 0
        prof_index = 0

        for line in h1bfile:
                
        #first row contains the headings to search for key columns.
                fields=line.split(";")
                
                if(firstRow == 0):
                        for i in range(len(fields)):
                                if(fields[i].find("STATUS")>=0):
                                        case_index = i
                                if((fields[i].find("_STATE")>=0)and(fields[i].find("_STATE")>=0)):
                                        state_index = i
                                if(fields[i].find("SOC_NAME")>=0):
                                        prof_index = i
                                i=i+1
                        firstRow = firstRow+1
        #Read the relevant fields
                if(len(fields)>1):        
                        case_status = fields[case_index].strip('\"')
                        app_State = fields[state_index].strip('\"')
                        prof_Name = fields[prof_index].strip('\"')
                                
                #filter for records which are only certified (CASE_STATUS = "CERTIFIED").
                #Create State and SOC_Name dictionaries.
                        if(case_status == "CERTIFIED" and prof_Name != ""):
                                certified_applications = certified_applications + 1
                                state_Val = soc_Dict.setdefault(prof_Name,None)
                                if(state_Val == None):
                                        soc_Dict[prof_Name]=1
                                else:
                                        soc_Dict[prof_Name] = state_Val+1

                                if(app_State!=""):
                                        aState_Val = state_Dict.setdefault(app_State,None)
                                        if(aState_Val == None):
                                                state_Dict[app_State]=1
                                        else:
                                                state_Dict[app_State] = aState_Val+1
         
                       

        #Sort decreasing by SOC_NAME on Count of CASES and pick the top 10 records
        sorted_soc_Dict = dict(sorted(soc_Dict.items(), key = operator.itemgetter(1),reverse=True)[:10])
        # sort for duplicate values and keys in alphabetical order
        sorted_soc_Dict = dict(sorted(sorted_soc_Dict.items(), key = operator.itemgetter(0), reverse=False)[:10])
        #sort again by certified cases to get the desired sort.
        sorted_soc_Dict = dict(sorted(sorted_soc_Dict.items(), key = operator.itemgetter(1), reverse=True)[:10])

        #create the File
                
        results_Prof_file.write("TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE"+"\n")

        #pick the top 10 and extract the following columns: SOC_NAME, NUMBER_CERTIFIED, PERCENTAGE_OF_TOTAL

        for k,l in (sorted_soc_Dict.items()):
                textToWrite = k+";"+ str(l)+";"+ (str(round((l*100)/certified_applications,1))+"%")
                results_Prof_file.write(textToWrite+"\n")

        results_Prof_file.close()

        #Repeat process for State sorting

        #Sort decreasing by SOC_NAME on Count of CASES
        sorted_state_Dict = dict(sorted(state_Dict.items(), key = operator.itemgetter(1), reverse=True)[:10])
        sorted_state_Dict = dict(sorted(sorted_state_Dict.items(), key = operator.itemgetter(0), reverse=False)[:10])
        sorted_state_Dict = dict(sorted(sorted_state_Dict.items(), key = operator.itemgetter(1), reverse=True)[:10])



        #sorted_state_Dict.sort(key = operator.itemgetter(1,0))

        #create the File

         
         
        results_State_file.write("TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE"+"\n")

        #pick the top 10 and extract the following columns: SOC_NAME, NUMBER_CERTIFIED, PERCENTAGE_OF_TOTAL
        topTenRecords = 0
        for k,l in (sorted_state_Dict.items()):
                textToWrite = k+";"+ str(l)+";"+ (str(round((l*100)/certified_applications,1))+"%")
                results_State_file.write(textToWrite+"\n")
                
        results_State_file.close()

         
