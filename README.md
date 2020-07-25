# Utility Scripts

## Script "pp_csv.py"

This script consumes a CSV (comma separated) file and pretty prints into the following format:
	
	Row Number : 1
	Column header 1 : Value1
	Column header 2 : Value2
	Column header 3 : Value3
	
	Command : pp_csv <filename>

## Script "pp_tsv.py"

This script consumes a TSV (tab separated) file and pretty prints into the following format:

	Row Number : 1
	Column header 1 : Value1
	Column header 2 : Value2
	Column header 3 : Value3

	Command : pp_tsv <filename>

## Script "pp_json.py"

[This script is still under construction]

## Script "pp_vcf.py"

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

## Script "pp_progenity_vcf.py"

This script consumes a Progenity VCF (variant calling format) file and pretty prints into the following format:

	Variant number : 1351
	INFO : 
		Progenity HGVS : HGVSg=NC_000023.11:g.154863151C>T;HGVSc=NM_000132.3:c.6506G>A;HGVSp=NP_000123.1:p.Arg2169His
		SnpEff Annotations :
			Annotation number : 1
			|missense_variant|MODERATE|F8|F8|transcript|NM_000132.3|protein_coding|23/26|NM_000132.3:c.6506G>A|NP_000123.1:p.Arg2169His|6677/9036|6506/7056|2169/2351||
			Annotation number : 2
			|missense_variant|MODERATE|F8|F8|transcript|NM_019863.2|protein_coding|2/5|NM_019863.2:c.101G>A|NP_063916.1:p.Arg34His|246/2605|101/651|34/216||
	SAMPLE : 0/1
	FORMAT : GT
	POS : 154863151
	FILTER : .
	QUAL : .
	#CHROM : chrX
	ALT : T
	REF : C
	ID : VSYTWGIITQ

	Command : pp_progenity_vcf <filename>


## How to add python script to path?

	Make a directory ~/bin
	Make the python script executable -- chmod +x pp_csv.py
	Add the following line to the /.bashrc file -- export PATH="$PATH:$HOME/bin"
	Link the script to a command -- ln -s $HOME/utilities/pp_csv.py $HOME/bin/pp_csv
	Repeat the above steps for pp_tsv and pp_json

## Contact

Author : Sayantan Ghosh (sayantan.ghosh@strandls.com)