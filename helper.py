import logging
import pe_constants as const


logging.basicConfig(filename='log.txt', 
                    filemode='w', 
                    encoding='utf-8',
                    format='%(message)s',#format='%(levelname)s: %(message)s', 
                    level=logging.DEBUG)


def to_hex(file_path):
    with open(file_path, 'rb') as f: 
        hexdata = f.read()
    
    return hexdata


def print_structure(func):
    def wrapper_print(structure):
        logging.info(f"{structure.__class__.__name__}".center(100, '='))
        func(structure)                
        logging.info('\n')
    return wrapper_print


@print_structure
def common_print(structure):
    for item in structure._fields_:
        item_value = structure.__getattribute__(item[0])
        if item[0] == "DataDirectory":
            logging.info('\n')
            logging.info(f"DATA DIRECTORY".center(100, '='))
            counter = 0
            for i in item_value:
                logging.info(f"{const.DIRECTORY_ENTRIES[counter]}")
                print_data_directories(i)
                counter += 1
        else:
            item_value = item_value.__getattribute__("VirtualSize") if item[0] == "Misc" else item_value
            byte_value = item_value if isinstance(item_value, bytes) else ""
            hex_value = hex(item_value) if isinstance(item_value, int) else [hex(i) for i in item_value]  
            logging.info(f"[*] {item[0]:<30} {str(byte_value):<20} {str(hex_value)}") # TODO: rjust()


def iterate_print(structure):
    for i in structure:
        common_print(i)


def print_data_directories(structure):
    for item in structure._fields_:
        item_value = structure.__getattribute__(item[0])
        hex_value = hex(item_value)
        logging.info(f"[*] {item[0]:<40} {str(hex_value)}")
    logging.info('\n')