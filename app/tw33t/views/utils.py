import os

'''
Support log information about each search into file
'''

def log_search(user_screen, result, folder_name='log_search', mode='a'):

    # Create folder to store if it not exist
    if not os.path.isdir(folder_name):
        try:
            os.makedirs(folder_name)
        except:
            pass

    # Log info into a file
    if os.path.isdir(folder_name):
        output = _process_result(result)
        try:
            with open(folder_name + '/logging.txt', mode) as f:
                f.write(user_screen + '\n\n')
                f.write(output + '\n')
                f.write('----------------------------------------\n')
        except:
            pass

# Convert list of string to string
def _process_result(result):
    out = ''
    for elem in result:
        out += elem['creation_date'] + '\n'
        out += elem['content'] + '\n'

    return out
