### The scripts in this directory are as follows:

#### Script "pp_csv.py"

This script consumes a CSV (comma separated) file and pretty prints into the following format:
	
	Key1 : Value1
	Key2 : Value2
	Key3 : Value3

	pp_csv <filename>

#### Script "pp_tsv.py"

This script consumes a TSV (tab separated) file and pretty prints into the following format:

	Key1 : Value1
	Key2 : Value2
	Key3 : Value3

	pp_tsv <filename>

#### Script "pp_json.py"

[This script is still under construction]

#### How to add python script to path?

	Make a directory ~/bin
	Make the python script executable -- chmod +x pp_csv.py
	Add the following line to the /.bashrc file -- export PATH="$PATH:$HOME/bin"
	Link the script to a command -- ln -s $HOME/utilities/pp_csv.py $HOME/bin/pp_csv
	Repeat the above steps for pp_tsv and pp_json
