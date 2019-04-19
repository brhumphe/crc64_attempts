import crcmod

# crc64 = crcmod.mkCrcFun(0xad93d23594c935a9)
crc64 = crcmod.predefined.mkPredefinedCrcFun('crc-64-jones')
print(hex(crc64(b'123456789')))
print(hex(crc64(b'{NAMELIST}')))