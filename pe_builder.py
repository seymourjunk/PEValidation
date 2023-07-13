import pe_constants as const

class PE_Builder:
    def __init__(self, _bytearray_file):
        self.bytearray_file = _bytearray_file
        self.PE_signature_address = None
        self.image_file_header = None
        self.image_optional_header = None
        self.PE_signature = None
        self.image_dos_header = self.get_image_dos_header()
        self.NT_image_header = self.get_NT_image_header()

        
    def get_image_dos_header(self):
        return const.IMAGE_DOS_HEADER.from_buffer_copy(self.bytearray_file[:64])
    
    def get_NT_image_header(self):
        self.PE_signature_address = self.image_dos_header.e_lfanew
        self.PE_signature = self.bytearray_file[self.PE_signature_address:self.PE_signature_address+4]
        self.image_file_header = const.IMAGE_FILE_HEADER.from_buffer_copy(self.bytearray_file[self.PE_signature_address+4:self.PE_signature_address+24])
        self.image_optional_header = const.IMAGE_OPTIONAL_HEADER.from_buffer_copy(self.bytearray_file[self.PE_signature_address+24:self.PE_signature_address+248])
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
        self.print_structure(self.image_file_header)
        self.print_structure(self.image_optional_header)

    def validate_pe_file(self):
        if self.image_dos_header.e_magic == b'MZ':
            print("CORRECT: e_magic is 'MZ'")
        else:
            raise ValueError(f"FAIL: e_magic isn't 'MZ' but {self.image_dos_header.e_magic}")
        
        if self.NT_image_header.Signature == b'PE':
            print("CORRECT: signature is 'PE'")
        else:
            raise ValueError(f"FAIL: sirnature isn't 'PE' but {self.NT_image_header.Signature}")