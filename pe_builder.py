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


    def get_image_file_header(self):
        return const.IMAGE_FILE_HEADER.from_buffer_copy(self.bytearray_file[65:])



    def print_image_dos_header(self):
        print("***** IMAGE_DOS_HEADER *****")
        print(f"e_magic     : {self.image_dos_header.e_magic}, {self.image_dos_header.e_magic.hex()}")
        print(f"e_cblp      : {self.image_dos_header.e_cblp}, {hex(self.image_dos_header.e_cblp)}")
        print(f"e_cp        : {self.image_dos_header.e_cp      }, {hex(self.image_dos_header.e_cp      )}")
        print(f"e_crlc      : {self.image_dos_header.e_crlc    }, {hex(self.image_dos_header.e_crlc    )}")
        print(f"e_cparhdr   : {self.image_dos_header.e_cparhdr }, {hex(self.image_dos_header.e_cparhdr )}")
        print(f"e_minalloc  : {self.image_dos_header.e_minalloc}, {hex(self.image_dos_header.e_minalloc)}")
        print(f"e_maxalloc  : {self.image_dos_header.e_maxalloc}, {hex(self.image_dos_header.e_maxalloc)}")
        print(f"e_ss        : {self.image_dos_header.e_ss      }, {hex(self.image_dos_header.e_ss      )}")
        print(f"e_pp        : {self.image_dos_header.e_pp      }, {hex(self.image_dos_header.e_pp      )}")
        print(f"e_csum      : {self.image_dos_header.e_csum    }, {hex(self.image_dos_header.e_csum    )}")
        print(f"e_ip        : {self.image_dos_header.e_ip      }, {hex(self.image_dos_header.e_ip      )}")
        print(f"e_cs        : {self.image_dos_header.e_cs      }, {hex(self.image_dos_header.e_cs      )}")
        print(f"e_lfarlc    : {self.image_dos_header.e_lfarlc  }, {hex(self.image_dos_header.e_lfarlc  )}")
        print(f"e_ovno      : {self.image_dos_header.e_ovno    }, {hex(self.image_dos_header.e_ovno    )}")
        ##print(f"e_res       : {self.image_dos_header.e_res  },    {hex(self.image_dos_header.e_res  )}"")
        print(f"e_oemid     : {self.image_dos_header.e_oemid   }, {hex(self.image_dos_header.e_oemid   )}")
        print(f"e_oeminfo   : {self.image_dos_header.e_oeminfo }, {hex(self.image_dos_header.e_oeminfo )}")
        #print(f"e_res2      : {self.image_dos_header.e_res2}, {hex(self.image_dos_header.e_res2)}"")
        print(f"e_lfanew    : {self.image_dos_header.e_lfanew  }, {hex(self.image_dos_header.e_lfanew  )}")


    def print_all_structures(self):
        self.print_image_dos_header()