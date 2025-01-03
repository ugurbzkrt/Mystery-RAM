def get_meminfo():
    with open('/proc/meminfo', 'r') as f:
        lines = f.readlines()
    meminfo = {}
    for line in lines:
        parts = line.split(':')
        meminfo[parts[0].strip()] = int(parts[1].strip().split()[0]) * 1024
    return meminfo

if __name__ == "__main__":
    meminfo = get_meminfo()
    print("Buff/Cache Analizi:")
    print(f"Buffers: {meminfo['Buffers'] / 1024**2:.2f} MB")
    print(f"Cached: {meminfo['Cached'] / 1024**2:.2f} MB")
