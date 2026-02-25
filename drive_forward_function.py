def drive_to_end():
    
    while k.analog() < 2500:
        for port in range(3):
            k.motor(port, 100)
    
    k.ao()
