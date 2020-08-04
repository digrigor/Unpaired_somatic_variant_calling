![alt text](https://ukeducationguide.com/wp-content/uploads/2014/10/stgeorgeslondon.jpg "St George's, University of London") 
# Unpaired somatic variant calling
Python scripts to perform somatic variant calling on unpaired samples with a Panel Of Normals (PoN) using GATK4 Mutect2
  
[St George's, University of London](https://www.sgul.ac.uk/)


## Useful Contacts: 
- [Dionysios Grigoriadis](https://github.com/digrigor), Bioinformatician, SGUL  
	[✉ dgrigori@sgul.ac.uk](mailto:dgrigori@sgul.ac.uk?subject=SGUL%2Workshop)
- [SGUL Bioinformatics Unit](http://bioinformatics.sgul.ac.uk/)
- [SGUL Genetics Centre Bioinformatics](https://github.com/sgul-genetics-centre-bioinformatics)

## Getting Started

Configure the run:
- **dependencies.py**:  This is the configuration python script to set-up the neccessary settings, file locations and software locations. **You need to change the file locations accordingly**

Main Script file:
- **somatic_calling.py**: This is the core script of the analysis. It performs:
	1) Directory handling.
	2) Identifies the BAM files specified for PanelOfNormals (PON) and creates one VCF for each BAM file.
	3) Collate sites present in the previously created individual PoN VCFs into a sites-only VCF file.
	4) Run mutect2 on the files specified in the call_bams directory.
	5) Filter the mutect2 calls.
	
	**You don't need to change anything to run it**

