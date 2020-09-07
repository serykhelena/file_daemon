import logging
import os


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

STORAGE_FOLDER = 'store/'


def create_folder(directory):
    """ Create specified folders
        
        Args:
            directory   - directory, path. 
                          format: [subfolder/]
    """
    if not os.path.exists(STORAGE_FOLDER + directory):
        logger.debug(f"Folders {directory} don't exist")
        try:
            os.mkdir(STORAGE_FOLDER + directory)
            logger.debug(f"Folder '{STORAGE_FOLDER + directory}' was successfully created")
        except OSError as err:
            logger.error(f"Creation of the directore '{STORAGE_FOLDER + directory}' failed\n{err}")
    else:
        logger.debug(f"Folder '{STORAGE_FOLDER + directory}' already exist")


def save_file(path, name, data):
    full_path = STORAGE_FOLDER + path + name 
    create_folder(path)
    with open(full_path, 'wb+') as new_file:
        new_file.write(data)
        logger.debug(f"File {full_path} was saved succesfully")

