import ctypes
lib = ctypes.cdll.LoadLibrary('./libcrc64.so')
lib.crc64.argtypes = [ctypes.c_uint64, ctypes.c_char_p, ctypes.c_uint64]
lib.crc64.restype = ctypes.c_uint64

test = b'{NAMELIST}'
out = lib.crc64(0, test, len(test))
print(hex(out))