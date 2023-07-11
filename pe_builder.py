import pe_constants as const

class PE_Builder:
    def __init__(self, _bytearray_file):
        self.bytearray_file = _bytearray_file
        self.PE_signature_address = None
        self.image_dos_header = self.get_image_dos_header()
        self.NT_image_header = self.get_NT_image_header()
        self.image_file_header = self.get_image_file_header()

        
    def get_image_dos_header(self):
        return const.IMAGE_DOS_HEADER.from_buffer_copy(self.bytearray_file[:64])
    
    def get_NT_image_header(self):
        self.PE_signature_address = self.image_dos_header.e_lfanew
        #print(self.bytearray_file[240:242])
        return const.IMAGE_NT_HEADERS.from_buffer_copy(self.bytearray_file[self.PE_signature_address:self.PE_signature_address+248])


    def get_image_file_header(self): #TODO: check for correct values
        return const.IMAGE_FILE_HEADER.from_buffer_copy(self.bytearray_file[65:])

    def print_structure(self, structure):
        print(f"===== {structure.__class__.__name__} =====")
        for item in structure._fields_:
            item_value = structure.__getattribute__(item[0])
            dec_value = item_value if isinstance(item_value, int) else [i for i in item_value]
            hex_value = hex(item_value) if isinstance(item_value, int) else [hex(i) for i in item_value]
            print(f"[*] {item[0]}: {dec_value}, {hex_value}") # TODO: rjust() 
        print('')

    def print_all_structures(self):
        self.print_structure(self.image_dos_header)
        #self.print_structure(self.NT_image_header)