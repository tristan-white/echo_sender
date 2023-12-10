#!/usr/bin/python3
import sys, os, time, tqdm

WAIT_TIME = 0.1     # seconds to wait between printing a cmd

if len(sys.argv) != 3:
    print(f"Usage: python3 {sys.argv[0]} SOURCE DEST")
    exit(0)

def get_cmd(data: bytes):
    return b'echo -ne "' + data + b'" >> ' + sys.argv[2].encode() + b' \n'

try:
    src = open(sys.argv[1], "rb")
except:
    print(f"{sys.argv[1]} does not exist.")
    exit(0)

src_size = os.path.getsize(sys.argv[1])

# Read, format, and write bytes in 16 byte increments
for _ in range(src_size // 16):
    data = b''
    for i in src.read(16):
        data += f"\\x{i:02x}".encode()
    cmd = get_cmd(data)
    sys.stdout.buffer.write(cmd)
    time.sleep(WAIT_TIME)

# Read, format, and write remaining bytes
data = b''
for _ in range(src_size % 16):
    b = src.read(1)
    i = int.from_bytes(b)
    data += f"\\x{i:02x}".encode()
sys.stdout.buffer.write( get_cmd(data) )
