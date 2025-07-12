import logging  # Import the logging module

# Corrected logger configuration
logging.basicConfig(filename='new_file.log',  # Log messages to file
                    filemode='w',            # Overwrite the file on each run
                    format='%(asctime)s - %(name)s- %(levelname)s - %(message)s',  
                    level=logging.DEBUG)  # Set logging level

def add(a, b):
    logging.debug("Addition operation is taking place")
    return a + b

logging.debug("The addition of 10 and 15 is taking place")
add(10, 15)
