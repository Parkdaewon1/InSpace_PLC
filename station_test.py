from pymodbus.client.sync import ModbusTcpClient
import requests
import json

PLC_IP = "192.168.0.200"
Station_id = "2"
Web_IP = "http://127.0.0.1:50000/station/"

countForprint = 0

c = ModbusTcpClient(PLC_IP, port=502)
c.connect()

print('Connecting....')
print('Client Start')


while 1:
    ServerResponse = requests.get(Web_IP+Station_id).json()
    if ServerResponse["command"] == "CONTROL_COMMAND_OPEN":
        if countForprint == 1:
            requests.patch(Web_IP+Station_id, json = {'runningStatus':'CONTROL_STATUS_OPEN'})
            print("command =", requests.get(Web_IP+Station_id).json()["command"])
            print("station status =", requests.get(Web_IP+Station_id).json()["runningStatus"])
        countForprint = 0
        c.write_coil(16,True)
        
    if ServerResponse["command"] == "CONTROL_COMMAND_CLOSE":
        if countForprint == 0:
            requests.patch(Web_IP+Station_id, json = {'runningStatus':'CONTROL_STATUS_CLOSE'})
            print("command =", requests.get(Web_IP+Station_id).json()["command"])
            print("station status =", requests.get(Web_IP+Station_id).json()["runningStatus"])
        countForprint = 1
        c.write_coil(16,False)
        
    if c.read_coils(0,8).bits[0] == False:
        print("Emergency Stop")
        exit()

c.close()
