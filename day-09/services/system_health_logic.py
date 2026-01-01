import psutil

def system_health():
    """
        This API gets the System Metrics(CPU, Memory, Disk, System Health)
        Based on a CPU Threshold i.e 10 (Configurable)
    """    
    current_cpu = psutil.cpu_percent(interval=1)
    current_mem = psutil.virtual_memory().percent
    current_disk = psutil.disk_usage('/').percent

    cpu_thres=10

    status="High cpu" if current_cpu>cpu_thres else "Healthy"

    return {
        "CPU":current_cpu,
        "MEM":current_mem,
        "DISK":current_mem,
        "Threshold":cpu_thres,
        "Sys_Status":status
    }