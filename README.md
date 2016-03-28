# FSD-Log-Parser
Python log parser of the FSD network server. 

usage: stats.py [-h] [-percent] [-start START] [-end END] type logs [logs ...]

FSD Log Statistics

positional arguments:
  type          Choose a type: clients, users, connections, dups
  logs          Provide the log file/s

optional arguments:
  -h, --help    show this help message and exit
  -percent      Compute percentages
  -start START  Provide a start date e.g. 15-03-2014
  -end END      Provide an end date e.g. 15-03-2014
