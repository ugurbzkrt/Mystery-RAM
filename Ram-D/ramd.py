import os
import psutil

def get_memory_usage(pid):
    """Verilen PID'nin bellek kullanımını döndür."""
    try:
        process = psutil.Process(pid)
        mem_info = process.memory_info()
        return {
            "rss": mem_info.rss,  # Resident Set Size
            "vms": mem_info.vms,  # Virtual Memory Size
            "shared": mem_info.shared,
            "text": mem_info.text,
            "lib": mem_info.lib,
            "data": mem_info.data,
            "dirty": mem_info.dirty
        }
    except psutil.NoSuchProcess:
        return None

def get_system_memory():
    """Sistemin genel bellek durumunu döndür."""
    mem = psutil.virtual_memory()
    return {
        "total": mem.total,
        "available": mem.available,
        "used": mem.used,
        "free": mem.free,
        "buffers": mem.buffers,
        "cached": mem.cached
    }

if __name__ == "__main__":
    system_memory = get_system_memory()
    print("Sistem Belleği:")
    for key, value in system_memory.items():
        print(f"{key}: {value / 1024**2:.2f} MB")

    pid = os.getpid()  # Bu scriptin PID'si
    memory_usage = get_memory_usage(pid)
    print("\nMevcut Script'in Bellek Kullanımı:")
    for key, value in memory_usage.items():
        print(f"{key}: {value / 1024**2:.2f} MB")
