from libs import bcolors

msd=r"""


o OPTIONS
        usage: Ignite [-h] [-f] [-u] [-i] [-g] [-s] [-d] [-p] [-c] [-l] [-e] [-x] [-R]
        The Huds CSV 2 ElasticSearch Tool (Ignite) Chidori-Edition

        optional arguments:
          -h, --help            show this help message and exit
          -f , --csvfile        CSV file with data
          -u , --username       username for elasticsearch instance, this is optional,
                                if no security ignore
          -i , --index          if specified, app will ignore the default from
                                settings.ini
          -g, --get_csv_columns
                                the tag should be used in conjuction with "-f" to list
                                and validate the columns of the csv file
          -s , --data_source_name
                                specify where the data is coming from, as in the
                                source or origin
          -d , --delimiter      specify the delimiter of the given CSV file, by
                                default the delimiter is a comma
          -p , --parce          specify together with parcer/mapping name that can be
                                found in parcer.conf e.g. -p <parcer_name/key>
          -c , --create_parce   specify template for parcer/mapper creation for a
                                specified file USAGE: -f <file_name> -c
                                <module/parcer_name>
          -l, --list_parcers    this tag will list available parcer modules, this tag
                                should be used alone
          -e, --elasticsearch   this tag will use elasticsearch as a destination
          -x, --flush           this tag should be used alone, it flush the database
                                of persistency and clears logs too
          -R, --readme          short notes on how to use app



o USE CASE 1
        This will upload to elasticsearch, the program will:
                ignite.exe -p nessus -u hud -i nessus -s nessus -f "C:\Users\dryl0\Desktop\clean\csvs\nessus_scan_ba7yyy.csv" -e

o USE CASE 2
        This will not upload to elasticsearch, but to a directory on the local disk, called _json_output which is located in the ropot directory of the application
                ignite.exe -p nessus -u hud -i nessus -s nessus -f "C:\Users\dryl0\Desktop\clean\csvs\nessus_scan_ba7yyy.csv"
                               
  Meaning of the parameters used in USE CASES 1 and 2
        -p = is the parcer mapping used to parce the given data from the CSV file (used the -p nessus to invoke the nessus parcer).        
        -u = is the username of the elasticsearch user (will select user hud, which user will authenticate to the instance).        
        -i = is the index on an elasticsearch instance the parced data will be stored. 
             (-i flag to store the data in to an index called "nessus", for production use, it is recommended to configure the index in settings.ini).        
        -s = is the name of the dataset being uploaded to elasticsearch, hence from ECS, this would be the "event.dataset" field (-s nessus to label, event.dataset to nessus).        
        -f = is the location of the CSV file to be uploaded (the csv file you will to upload, hence, C:\Users\dryl0\Desktop\clean\csvs\nessus_scan_ba7yyy.csv).       
        -e = this tell the tool to send all parced data to elasticsearch, if not specified, the data is stored on the local disk.



"""

introm="""
[+] Creator: Hud Seidu Daannaa
[+] Name:

        o Ignite (Huds CSV 2 Elasticsearch Tool)

[+] Description:

        o 
        o Automatically generate and load elasticsearch template (later version)
        o An option to generate a parcer mapping template for a given CSV file with
          label columns. This gives rise to create a parcer like mapper to which helps
          to process csv columns to elasticsearch using specific field names (ECS recommended)
        o Field normalization and validation before elasticsearch upload.
        o Ability to track fields via a logs an Option to destinate csv data to a json text file
        o The tool has the ability to keep track of uploaded files, to prevent file upload duplication
        o 
"""
introm = bcolors.OKCYAN+introm+bcolors.ENDC

success="""
\U0001F923
\U0001F606
\U0001f600
"""
cat="""
                     ."  :'. .':  ".
                  ==)  _ :  '  : _  (==
                    |>/O\   _   /O\<|
                    | \-"~` _ `~"-/ |
                   >|`===. \_/ .===`|<
             .-"-.   \==='  |  '===/   .-"-.
        .---{'. '`}---\,  .-'-.  ,/---{.'. '}---.
         )  `"---"`     `~-===-~`     `"---"`   (
        (         Huds CSV 2 ElasticSearch      )
         )                Tool                 (
        '---------------------------------------'"""
cat = bcolors.WARNING+cat+bcolors.ENDC 

inpt="""
        .--,       .--,
        ( (  \.---./  ) 
        '.__/o   o\__.'
           {=  ^  =}
            >  -  <
"""
license="""

# Copyright (c) 2021, Hud Seidu Daannaa
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#  * Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#  * Neither the name of www.daannaa.space nor the names of its contributors
#    may be used to endorse or promote products derived from this software
#    without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

"""