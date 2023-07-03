import pe_constants as const

def to_hex(file_path):
    with open(file_path, 'rb') as f: 
        hexdata = f.read()
    
    return hexdata