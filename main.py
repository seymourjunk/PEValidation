import helper as helper
from pe_builder import PE_Builder

file_path = ""

def parse_pe_file():
    hex_view = helper.to_hex(file_path)
    pe_file = PE_Builder(bytearray(hex_view))
    pe_file.print_all_structures()
    pe_file.validate_pe_file()


if __name__ == '__main__':
    parse_pe_file()