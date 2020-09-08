import hashlib 


def generate_hash(data):
    """ Get hash value of file 
    
        Args:
            data    - binary file data
        Return:
            [string]- hexadecimal hash sum 
    """
    return  hashlib.md5(data).hexdigest()


def get_subfolder_name(hash_):
    """ Get name of subfolder
    
        Args:
            hash_    - value of generated hash
        Return:
            [string]    - first two symbols of hash 
    """
    return hash_[:2] + '/'