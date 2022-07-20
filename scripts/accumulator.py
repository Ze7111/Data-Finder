import logging, os, sys # import modules

from rich.console import Console # create console object

logging.info('Accumulator Loaded Successfully') # Log accumulator load success

from classes.data_class import datacollect # import data class
from classes.rich_class import basic_UI_elements # import basic UI elements
from functions.collector import sorting_data_from_index # import sorting data from index function
import logging # import logging module

console = Console() # create console object

class variable_organizer(): # class for variable organizer
    
    def data_organizer(search_name, condition): # function to organize data
        os.system('cls') # clear screen
        
        logging.info(f'User searched for data {search_name}') # log user searched for data
        
        file_path = 'data\\data.csv' # assign file path to file
            
        index_data = datacollect.csv_to_lists(file_path)[0] # assign index data to list
        name_data = datacollect.csv_to_lists(file_path)[1] # assign name data to list
        dob_data = datacollect.csv_to_lists(file_path)[2] # assign dob data to list
        phone_data = datacollect.csv_to_lists(file_path)[3] # assign phone data to list
        email_data = datacollect.csv_to_lists(file_path)[4] # assign email data to list
        location_data = datacollect.csv_to_lists(file_path)[5] # assign location data to list
        extra_data = datacollect.csv_to_lists(file_path)[6] # assign extra data to list
        
        if file_path == 'error': # if file path is error
            basic_UI_elements.foundtable(index_data, name_data, dob_data, location_data, phone_data, email_data, extra_data) # call found table function
            return 'error' # return error
        
        if condition == 'all': # if condition is all
            basic_UI_elements.foundtable(index_data, name_data, dob_data, location_data, phone_data, email_data, extra_data) # call found table function
            return # return
        
        matching_name_index = [] # create matching name index list
            
        matching_name_index = datacollect.finding_search_index(matching_name_index, name_data, dob_data, phone_data, email_data, location_data, extra_data, search_name, condition) # call finding search index function
        
        if matching_name_index == 'none': # if matching name index is none
            logging.warning('No matching data found') # log no matching name found
            return 'none' # return none
        
        logging.info('Started sorting data from index') # log start sorting data from index
        
        index_data1 = sorting_data_from_index(matching_name_index, index_data, name_data, dob_data, phone_data, email_data, location_data, extra_data)[0] # assign index data to list
        name_data1 = sorting_data_from_index(matching_name_index, index_data, name_data, dob_data, phone_data, email_data, location_data, extra_data)[1] # call sorting data from index function 
        dob_data1 = sorting_data_from_index(matching_name_index, index_data, name_data, dob_data, phone_data, email_data, location_data, extra_data)[2] # call sorting data from index function
        phone_data1 = sorting_data_from_index(matching_name_index, index_data, name_data, dob_data, phone_data, email_data, location_data, extra_data)[3] # call sorting data from index function
        email_data1 = sorting_data_from_index(matching_name_index, index_data, name_data, dob_data, phone_data, email_data, location_data, extra_data)[4] # call sorting data from index function
        location_data1 = sorting_data_from_index(matching_name_index, index_data, name_data, dob_data, phone_data, email_data, location_data, extra_data)[5] # call sorting data from index function
        extra_data1 = sorting_data_from_index(matching_name_index, index_data, name_data, dob_data, phone_data, email_data, location_data, extra_data)[6] # call sorting data from index function
        logging.info('Finished sorting data from index') # log finish sorting data from index
        
        index_data = index_data1 # assign index data to index data 1
        name_data = name_data1 # assign name data to name data
        dob_data = dob_data1 # assign sorted data to original data
        phone_data = phone_data1 # assign new data to old data
        email_data = email_data1 # assign new data to old data
        location_data = location_data1 # assign new data to old data
        extra_data = extra_data1 # assign new data to old data
        logging.info('Finished organizing data') # log finish organizing data
        
        logging.info('Accumulator gathered all data points successfully') # Log data points gathered successfully
        total = index_data # assign total to length of index data
        
        #sys.stdout.flush() # flush stdout
        
        basic_UI_elements.foundtable(index_data, name_data, dob_data, location_data, phone_data, email_data, extra_data) # call found table function
        
        return 'success' # return success
    