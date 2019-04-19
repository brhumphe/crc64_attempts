import crc32c

if __name__ == '__main__':
    hashed = crc32c.crc32(b'{NAMELIST}')
    print(hex(hashed))
