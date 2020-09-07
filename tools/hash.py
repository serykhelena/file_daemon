import hashlib 

def generate_hash(data):
    return  hashlib.md5(data).hexdigest()

def get_subfolder_name(hash_val):
    """ Get name of subfolder
    
        Args:
            hash_val    - value of generated hash
        Return:
            [string]    - first two symbols of hash 
    """
    return str(hash_val[:2]) + '/'


def get_file_name(hash_val, extension='.txt'):
    """ Get file name

        Args:
            hash_val    - value of generated hash 
            extension   - extension name for file 
                          default: .txt 
        Return:
            [string]    - file name with extension 
    """
    return str(hash_val) + extension