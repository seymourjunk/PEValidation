import logging

logging.basicConfig(filename='log.txt', 
                    filemode='w', 
                    encoding='utf-8',
                    format='%(message)s',#format='%(levelname)s: %(message)s', 
                    level=logging.DEBUG)

def to_hex(file_path):
    with open(file_path, 'rb') as f: 
        hexdata = f.read()
    
    return hexdata

def print_structure(structure):
    logging.info(f"===== {structure.__class__.__name__} =====")
    for item in structure._fields_:
        item_value = structure.__getattribute__(item[0])
        dec_value = item_value if isinstance(item_value, int) else [i for i in item_value]
        hex_value = hex(item_value) if isinstance(item_value, int) else [hex(i) for i in item_value]
        logging.info(f"[*] {item[0]}: {dec_value}, {hex_value}") # TODO: rjust() 
    logging.info('\n')