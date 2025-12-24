import psutil

def system_health():
    print("---- System health threshold status ----")

    # take threshold values from user input
    cpu_thresh = float(input("Enter the cpu threshold: "))
    mem_thresh = float(input("Enter the mem threshold: "))
    disk_thresh = float(input("Enter the disk threshold: "))

    print("\nfetching the current sys status now using psutil...")
    
    # get current metrics using psutil
    current_cpu = psutil.cpu_percent(interval=1)
    current_mem = psutil.virtual_memory().percent
    current_disk = psutil.disk_usage('/').percent

    print("-" * 30)
    print(f"CPU:  {current_cpu}% (Threshold: {cpu_thresh}%)")
    print(f"MEM:  {current_mem}% (Threshold: {mem_thresh}%)")
    print(f"DISK: {current_disk}% (Threshold: {disk_thresh}%)")
    print("-" * 30)

    # compare metrics against thresholds and print results
    if current_cpu > cpu_thresh:
        print(f" ALERT: CPU usage is too high! ({current_cpu}%)")
    else:
        print(" CPU is healthy.")

    if current_mem > mem_thresh:
        print(f" ALERT: Memory usage is too high! ({current_mem}%)")
    else:
        print(" Memory is healthy.")

    if current_disk > disk_thresh:
        print(f" ALERT: Disk space is running low! ({current_disk}%)")
    else:
        print(" Disk space is healthy.")

# call function
system_health()