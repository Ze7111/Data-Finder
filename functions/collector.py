import logging # import logging

completed = False # set completed to false

if completed == False: # if completed is false
    logging.info('Collector Loaded Successfully') # log successful load of collector

def sorting_data_from_index(matching_name_index, index_data, name_data, dob_data, phone_data, email_data, location_data, extra_data): # function to get data from index
    
    global completed # set global variable
    index_data = ['0'] # assign index data to list
    index_data1 = [] # assign index data to list
    name_data1 = [] # assign name data to list
    dob_data1 = [] # assign dob data to list
    phone_data1 = [] # assign phone data to list
    email_data1 = [] # assign email data to list
    location_data1 = [] # assign location data to list
    extra_data1 = [] # assign extra data to list
    listindex = 0 # assign list index to 0
    count = 0 # assign count to 0
    
    if completed == False: # if completed is false
        logging.info('Set up data lists') # log set up data lists for sorting
    
    for i in matching_name_index: # for each index in matching name index
        
        m = matching_name_index[listindex] # assign matching name index to m
        
        count += 1 # add 1 to count
        
        if completed == False: # if completed is false
            completed = True # set completed to true
            logging.info(f'Started adding data to lists matching name index = {m}') # log start adding data to lists
        
        try:
            index_data1.append(str(count))
            name_data1.append(name_data[m])
            dob_data1.append(dob_data[m])
            phone_data1.append(phone_data[m])
            email_data1.append(email_data[m])
            location_data1.append(location_data[m])
            
        except:
            if completed == False:
                completed = True
                logging.warning(f'FAILED AT POINT OR OTHERWISE = {m}', exc_info=True) # log failed at point or otherwise
            return 'error', 'error', 'error', 'error', 'error', 'error', 'error' # return error
        
        listindex += 1
        extra_data1.append(extra_data[m])
        
        if completed == False:
            logging.info(f'Added data to lists matching name index = {m}') # log added data to lists

    completed = True
    
    return index_data1, name_data1, dob_data1, phone_data1, email_data1, location_data1, extra_data1