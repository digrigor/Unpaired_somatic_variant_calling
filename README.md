![alt text](https://ukeducationguide.com/wp-content/uploads/2014/10/stgeorgeslondon.jpg "St George's, University of London") 
# Unpaired somatic variant calling
Python scripts to perform somatic variant calling on unpaired samples with a Panel Of Normals (PoN) using GATK4 Mutect2
  
[St George's, University of London](https://www.sgul.ac.uk/)


## Useful Contacts: 
- [Dionysios Grigoriadis](https://github.com/digrigor), Bioinformatician, SGUL  
	[✉ dgrigori@sgul.ac.uk](mailto:dgrigori@sgul.ac.uk?subject=SGUL%2Workshop)
- [SGUL Bioinformatics Unit](http://bioinformatics.sgul.ac.uk/)
- [SGUL Genetics Centre Bioinformatics](https://github.com/sgul-genetics-centre-bioinformatics)

### Prerequisites
This pipeline has been ran and tested on a Linux server (centOS).
- Python3
- GATK tool suite (4.0.4.0 or above)
- htslib-1.9 or above
- java installed

### Run configuration:

- **dependencies.py**:  This is the configuration python script to set-up the neccessary settings, file locations and software locations. **You need to change the file locations accordingly**:
	INPUTS:
	- maindir: Full Path. This is the main directory where all the analysis directories will be found in. **You need to create this directory.**
	- inbamsdir: Full path. maindir subdirectory. This is the directory that contains the BAM files which will be used to generate a Panel of Normals (PoN). Each BAM file should be included in a separate (and separately-named) subdirectory inside the inbamsdir. **You need to create this directory and move/link the BAM files inside it (each into a separate directory).**
	- call_bams: Full path. maindir subdirectory. This is the directory that contains the BAM files which you want to perform the somatic calling on. Each BAM file should be included in a separate (and separately-named) subdirectory inside the call_bams. **You need to create this directory and move/link the BAM files inside it (each into a separate directory).**
	
	OUTPUTS:
	- ponvcf: Full path. maindir subdirectory. This is the directory where the PoN VCFs will be created. 
	- ponjointvcf: Full path. maindir subdirectory. This is the directory where the collated PoN VCF will be created.
	- mutect2out: Full path. maindir subdirectory. This is the directory where the VCF file with the raw mutect calls will be created.
	- filtmutect2out: Full path. maindir subdirectory. This is the directory where the VCF file with the filtered mutect calls will be created.
	
	SOFTWARE:
	Please specify the paths to the required software.
	
	REFERENCES:
	Please specify the paths to the required reference files.

### Main Script file:
- **somatic_calling.py**: This is the core script of the analysis. It performs:
	1) Directory handling.
	2) Identifies the BAM files specified for PanelOfNormals (PON) and creates one VCF for each BAM file.
	3) Collate sites present in the previously created individual PoN VCFs into a sites-only VCF file.
	4) Run mutect2 on the files specified in the call_bams directory.
	5) Filter the mutect2 calls.
	
	**You don't need to change anything to run it**

### Supplementary scripts:
These are supplementary scripts containing definitions of functions utilised by the main somatic_calling.py script.
- **utils.py**
