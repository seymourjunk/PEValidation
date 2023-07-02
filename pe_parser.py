import ctypes
import struct


# Mapping of the Microsoft types to ctypes
WORD        = ctypes.c_ushort
# DWORD       = ctypes.c_ulong
# BYTE        = ctypes.c_ubyte
# LPBYTE      = ctypes.POINTER(ctypes.c_ubyte)
# LPTSTR      = ctypes.POINTER(ctypes.c_char) 
# HANDLE      = ctypes.c_void_p
# PVOID       = ctypes.c_void_p
# ULONG_PTR   = ctypes.POINTER(ctypes.c_ulong) # ctypes.c_ulong
# LPVOID      = ctypes.c_void_p
LONG        = ctypes.c_long

class IMAGE_DOS_HEADER(ctypes.Structure):
    _fields_ = [
        ("e_magic",     WORD),
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
        ("e_lfanew",    LONG),
    ]
