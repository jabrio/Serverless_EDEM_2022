#EDEM SERVERLESS PART 02

#Cloud Function triggered by PubSub Event
#When a temperature over 25ºC or under 17ºC is received, a IoT Core command will be throw.

#Import libraries
import base64, json, sys, os
from google.cloud import iot_v1
import random

#Read from PubSub
def pubsub_to_iot(event, context):
    #Read message from Pubsub (decode from Base64)
    '''https://cloud.google.com/functions/docs/calling/pubsub#functions_calling_pubsub-python'''

    #Load json
    
    #Dealing with environment variables
    project_id = os.environ['PROJECT_ID']
    cloud_region = os.environ['REGION_ID']
    registry_id = os.environ['REGISTRY_ID']
    device_id = os.environ['DEVICE_ID']

    #Logic for incoming data
    room_temperature = range(17,23)

    if message['aggTemperature'] in room_temperature:
        print("Temperature OK. Nothing to set.")
        pass
    else:

        #IoT Client
        client = iot_v1.DeviceManagerClient()
        
        #Send Command to IoT Device
        '''https://cloud.google.com/iot/docs/how-tos/commands#api'''

        #Check for last version updated
        '''https://cloud.google.com/iot/docs/how-tos/config/configuring-devices#iot-core-get-config-python'''

        #Update device configuration
        '''https://cloud.google.com/iot/docs/how-tos/config/configuring-devices#iot-core-update-config-python'''
