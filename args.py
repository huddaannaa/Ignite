import argparse



pce = argparse.ArgumentParser(prog="Ignite", description="The Huds CSV 2 ElasticSearch Tool (Ignite) Chidori-Edition", epilog="www.daannaa.space ")
pce.add_argument('-f', 
                '--csvfile', 
                type=str, 
                metavar='',  
                help='CSV file with data')
pce.add_argument_group('Credentials', 
                       description="Note: A SuperUser of an Administrator level credentials are needed, leave blank if not applicable")
pce.add_argument('-u', 
                 '--username', 
                 type=str, 
                 metavar='', 
                 help='username for elasticsearch instance, this is optional, if no security ignore',)
pce.add_argument('-i', 
                 '--index', 
                 type=str, 
                 metavar='',
                 help='if specified, app will ignore the default from settings.ini',) 
pce.add_argument('-g', 
                 '--get_csv_columns', 
                 action='store_true', 
                 help='the tag should be used in conjuction with "-f" to list and validate the columns of the csv file',)
pce.add_argument('-s', 
                 '--data_source_name', 
                 type=str,
                 metavar='',
                 default='hudcsvparcer', 
                 help='specify where the data is coming from, as in the source or origin',)
pce.add_argument('-d', 
                 '--delimiter', 
                 type=str,
                 metavar='',
                 default=',', 
                 help='specify the delimiter of the given CSV file, by default the delimiter is a comma',)
pce.add_argument('-p', 
                 '--parce', 
                 type=str,
                 metavar='',
                 help='specify together with parcer/mapping name that can be found in parcer.conf e.g. -p <parcer_name/key>',)
pce.add_argument('-c', 
                 '--create_parce', 
                 type=str,
                 metavar='',
                 help='specify template for parcer/mapper creation for a specified file USAGE: -f <file_name> -c <module/parcer_name>',)
pce.add_argument('-l', 
                 '--list_parcers', 
                 action='store_true', 
                 help='this tag will list available parcer modules, this tag should be used alone',)
pce.add_argument('-e', 
                 '--elasticsearch', 
                 action='store_true', 
                 help='this tag will use elasticsearch as a destination',)
pce.add_argument('-x', 
                 '--flush', 
                 action='store_true', 
                 help='this tag should be used alone, it flush the database of persistency and clears logs too',)
pce.add_argument('-R', 
                 '--readme', 
                 action='store_true', 
                 help='short notes on how to use app',)
args = pce.parse_args()