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
            logger.error(f"Creation of the directory '{STORAGE_FOLDER + directory}' failed\n{err}")
    else:
        logger.debug(f"Folder '{STORAGE_FOLDER + directory}' already exist")


def save_file(path, name, data):
    """ Save file into specified directory
        
        Args:
            path    - directory, path. 
                      format: [subfolder/]
            name    - file name 
            data    - file data
    """
    full_path = STORAGE_FOLDER + path + name 
    create_folder(path)
    if os.path.isfile(full_path):
        logger.debug(f"File {full_path} already exists")
        return 
    with open(full_path, 'wb+') as new_file:
        new_file.write(data)
        logger.debug(f"File {full_path} was saved succesfully")

    
def get_path_to_file(hash_):
    """ Get path to file by it's hash-name
        
        Args:
            hash_   - hash value [string] 
    """
    full_path = STORAGE_FOLDER + hash_[:2] + '/' + hash_
    if os.path.isfile(full_path):
        return full_path
    logger.error(f"FILE {full_path} not found")    
    raise IOError(f'File {full_path} doesn\'t exist')


def delete_file(hash_):
    """ Delete file by it's hash-name
        
        Args:
            hash_   - hash value [string] 
    """
    full_path = STORAGE_FOLDER + hash_[:2] + '/' + hash_
    subfolder = STORAGE_FOLDER + hash_[:2]
    if os.path.isfile(full_path):
        os.remove(full_path)
        logger.debug(f"File {full_path} successfully removed!")
        try:
            os.rmdir(subfolder)
            logger.debug(f"Folder {subfolder} successfully removed!")
        except OSError:
            logger.debug(f"Folder {subfolder} is not empty")
        return True
    logger.error(f"FILE {full_path} not found")    
    raise IOError(f'File {full_path} doesn\'t exist')
