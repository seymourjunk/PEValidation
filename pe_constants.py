import ctypes

# Mapping of the Microsoft types to ctypes
WORD        = ctypes.c_ushort
DWORD       = ctypes.c_uint
LONG        = ctypes.c_uint
BYTE        = ctypes.c_ubyte
CHAR        = ctypes.c_char

class IMAGE_DOS_HEADER(ctypes.Structure): # 64 bytes
    _fields_ = [
        ("e_magic",     CHAR*2),      # magic number
        ("e_cblp",      WORD),
        ("e_cp",        WORD),
        ("e_crlc",      WORD),
        ("e_cparhdr",   WORD),
        ("e_minalloc",  WORD),
        ("e_maxalloc",  WORD),
        ("e_ss",        WORD),
        ("e_pp",        WORD),
        ("e_csum",      WORD),
        ("e_ip",        WORD),
        ("e_cs",        WORD),
        ("e_lfarlc",    WORD),
        ("e_ovno",      WORD),
        ("e_res",       WORD*4),
        ("e_oemid",     WORD),
        ("e_oeminfo",   WORD),
        ("e_res2",      WORD*10),
        ("e_lfanew",    LONG),      # file address of new exe header
    ]

DIRECTORY_ENTRIES = ["IMAGE_DIRECTORY_ENTRY_EXPORT", "IMAGE_DIRECTORY_ENTRY_IMPORT", "IMAGE_DIRECTORY_ENTRY_RESOURCE", 
                     "IMAGE_DIRECTORY_ENTRY_EXCEPTION", "IMAGE_DIRECTORY_ENTRY_SECURITY", "IMAGE_DIRECTORY_ENTRY_BASERELOC", 
                     "IMAGE_DIRECTORY_ENTRY_DEBUG", "IMAGE_DIRECTORY_ENTRY_COPYRIGHT", "IMAGE_DIRECTORY_ENTRY_ARCHITECTURE", 
                     "IMAGE_DIRECTORY_ENTRY_GLOBALPTR", "IMAGE_DIRECTORY_ENTRY_TLS", "IMAGE_DIRECTORY_ENTRY_LOAD_CONFIG", 
                     "IMAGE_DIRECTORY_ENTRY_BOUND_IMPORT", "IMAGE_DIRECTORY_ENTRY_IAT", "IMAGE_DIRECTORY_ENTRY_DELAY_IMPORT", "IMAGE_DIRECTORY_ENTRY_COM_DESCRIPTOR"]

class IMAGE_DATA_DIRECTORY(ctypes.Structure):
    _fields_ = [
        ("VirtualAddress",  DWORD),
        ("Size",            DWORD)
    ]

# https://learn.microsoft.com/en-us/windows/win32/debug/pe-format
class IMAGE_FILE_HEADER(ctypes.Structure): # 20 bytes
    _fields_ = [
        ("Machine",                 WORD),   # The number that identifies the type of target machine
        ("NumberOfSections",        WORD),
        ("TimeDateStamp",           LONG),
        ("PointerToSymbolTable",    LONG),   # The file offset of the COFF symbol table, or zero if no COFF symbol table is present
        ("NumberOfSymbols",         LONG),
        ("SizeOfOptionalHeader",    WORD),
        ("Characteristics",         WORD)
    ]

class IMAGE_OPTIONAL_HEADER(ctypes.Structure): # 224 bytes, the size isn't fixed > look at "SizeOfOptionalHeader" in IMAGE_FILE_HEADER
    _fields_ = [
        ("Magic",                       WORD),  # PE32 or PE32+
        ("MajorLinkerVersion",          BYTE),
        ("MinorLinkerVersion",          BYTE),
        ("SizeOfCode",                  DWORD), # The size of the code (text) section
        ("SizeOfInitializedData",       DWORD),
        ("SizeOfUninitializedData",     DWORD),
        ("AddressOfEntryPoint",         DWORD),
        ("BaseOfCode",                  DWORD),
        ("BaseOfData",                  DWORD),
        ("ImageBase",                   DWORD),
        ("SectionAlignment",            DWORD),
        ("FileAlignment",               DWORD),
        ("MajorOperatingSystemVersion", WORD),
        ("MinorOperatingSystemVersion", WORD),
        ("MajorImageVersion",           WORD),
        ("MinorImageVersion",           WORD),
        ("MajorSubsystemVersion",       WORD),
        ("MinorSubsystemVersion",       WORD),
        ("Win32VersionValue",           DWORD),
        ("SizeOfImage",                 DWORD),
        ("SizeOfHeaders",               DWORD),
        ("CheckSum",                    DWORD),
        ("Subsystem",                   WORD),
        ("DllCharacteristics",          WORD),
        ("SizeOfStackReserve",          DWORD),
        ("SizeOfStackCommit",           DWORD),
        ("SizeOfHeapReserve",           DWORD),
        ("SizeOfHeapCommit",            DWORD),
        ("LoaderFlags",                 DWORD),
        ("NumberOfRvaAndSizes",         DWORD),
        ("DataDirectory",               IMAGE_DATA_DIRECTORY * 16)
    ]

class IMAGE_NT_HEADERS(ctypes.Structure):   # 248 bytes
    _fields_ = [ 
        ("Signature",       CHAR * 4),
        ("FileHeader",      IMAGE_FILE_HEADER),
        ("OptionalHeader",  IMAGE_OPTIONAL_HEADER) 
    ]

class Misc(ctypes.Union):
    _fields_ = [
        ("PhysicalAddress", DWORD),
        ("VirtualSize",     DWORD)  #for exe
    ]


class IMAGE_SECTION_HEADER(ctypes.Structure):   #40 bytes
    _fields_ = [
        ("Name",                    CHAR * 8),
        ("Misc",                    Misc),
        ("VirtualAddress",          DWORD),
        ("SizeOfRawData",           DWORD),
        ("PointerToRawData",        DWORD),
        ("PointerToRelocations",    DWORD),
        ("PointerToLinenumbers",    DWORD),
        ("NumberOfRelocations",     WORD),
        ("NumberOfLinenumbers",     WORD),
        ("Characteristics",         DWORD)
    ]


