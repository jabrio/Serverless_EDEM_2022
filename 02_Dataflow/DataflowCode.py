#Dataflow EDEM Code

#Import Libraries
import argparse
import json
import logging
import time
import apache_beam as beam
from apache_beam.options.pipeline_options import (PipelineOptions, StandardOptions)
from apache_beam.transforms.combiners import MeanCombineFn
from apache_beam.transforms.combiners import CountCombineFn
from apache_beam.transforms.core import CombineGlobally
import apache_beam.transforms.window as window
from apache_beam.io.gcp.bigquery import parse_table_schema_from_json
from apache_beam.io.gcp import bigquery_tools
import datetime

#ParseJson Function
#Get data from PubSub and parse them

def parse_json_message(message):
    '''Mapping message from PubSub'''
    #DecodePubSub message in order to deal with

    #Convert string decoded in json format(element by element)

    #Add Processing Time (new column)

    #Return function
    return 

#Create DoFn Class to add Window processing time and encode message to publish into PubSub
class add_processing_time(beam.DoFn):
    def process(self, element):
        '''TO COMPLETE'''
        yield 

#Create DoFn Class to extract temperature from data
class agg_temperature(beam.DoFn):
    def process(self, element):
        '''TO COMPLETE'''
        yield 

#Create Beam pipeline
def edemData(output_table):

    #Load schema from BigQuery/schemas folder
    with open(f"schemas/{output_table}.json") as file:
        input_schema = json.load(file)

    schema = bigquery_tools.parse_table_schema_from_json(json.dumps(input_schema))

    #Create pipeline
    #First of all, we set the pipeline options
    options = PipelineOptions(save_main_session=True, streaming=True)
    with beam.Pipeline(options=options) as p:

        #Part01: we create pipeline from PubSub to BigQuery
        data = (
            #Read messages from PubSub
            p | "Read messages from PubSub" >> #TOCOMPLETE
            #Parse JSON messages with Map Function and adding Processing timestamp
              | "Parse JSON messages" >> #TOCOMPLETE
        )

        #Part02: Write proccessing message to their appropiate sink
        #Data to Bigquery
        (data | "Write to BigQuery" >> #TOCOMPLETE 
        )

        #Part03: Count temperature per minute and put that data into PubSub
        #Create a fixed window (1 min duration)
        (data 
            | "Get temperature value" >> #TOCOMPLETE
            | "WindowByMinute" >> #TOCOMPLETE
            | "MeanByWindow" >> #TOCOMPLETE
            | "Add Window ProcessingTime" >> #TOCOMPLETE
            | "WriteToPubSub" >> #TOCOMPLETE
        )

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    edemData("YOUR_BIGQUERY_TABLE_NAME")