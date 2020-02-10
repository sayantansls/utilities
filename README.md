### The scripts in this directory are as follows:

#### Script "pp_csv.py"

This script consumes a CSV (comma separated) file and pretty prints into the following format:
	
	Row Number : 1
	Column header 1 : Value1
	Column header 2 : Value2
	Column header 3 : Value3
	
	Command : pp_csv <filename>

#### Script "pp_tsv.py"

This script consumes a TSV (tab separated) file and pretty prints into the following format:

	Row Number : 1
	Column header 1 : Value1
	Column header 2 : Value2
	Column header 3 : Value3

	Command : pp_tsv <filename>

#### Script "pp_json.py"

[This script is still under construction]

#### Script "pp_vcf.py"

This script consumes a StrandOmics VCF (variant calling format) file and pretty prints into the following format:

	Variant number : 46
	#CHROM : chrX
	POS : 19377575
	ID : rs143035002
	REF : TAAAACCTTTTACACTGTTACCTAA
	ALT : T
	QUAL : .
	FILTER : PASS
	INFO : .
	FORMAT : GT:GQ:DP:SR:VR:VA:SB:ABQ:AMQ
	STRAN-398_S2_DMiSeq01-Run0071 : 0/1:1000.00:694:75.22:75.22:0:0.20:37.07:254.00

	Command : pp_vcf <filename>

#### How to add python script to path?

	Make a directory ~/bin
	Make the python script executable -- chmod +x pp_csv.py
	Add the following line to the /.bashrc file -- export PATH="$PATH:$HOME/bin"
	Link the script to a command -- ln -s $HOME/utilities/pp_csv.py $HOME/bin/pp_csv
	Repeat the above steps for pp_tsv and pp_json
