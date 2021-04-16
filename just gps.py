# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 11:52:03 2021

@author: justf
"""

#print("Start simulator (SITL)")
#import dronekit_sitl
#sitl = dronekit_sitl.start_default()
#connection_string = sitl.connection_string()
import dronekit
import socket



try:
    dronekit.connect('REPLACE_connection_string_for_your_vehicle', heartbeat_timeout=15)

# Bad TCP connection
except socket.error:
    print ('No server exists!')

'''# Bad TTY connection
except exceptions.OSError as e:
    print ('No serial exists!')'''

'''# API Error
except dronekit.APIException:
    print ('Timeout!')'''



# Import DroneKit-Python
from dronekit import connect, VehicleMode

# Connect to the Vehicle.
print("Connecting to vehicle on: %s" % ('com6',))
vehicle = connect('com6', wait_ready=True, baud=57600)

# Get some vehicle attributes (state)
print ("Get some vehicle attribute values:")
while(True):
    print (" GPS: %s" % vehicle.gps_0)
    print ("Global Location: %s" % vehicle.location.global_frame)
     # settable

# Close vehicle object before exiting script
vehicle.close()

# Shut down simulator
#sitl.stop()
print("Completed")

