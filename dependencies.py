#RUN CONFIGURATION
maindir="/homedirs-porthos/sgul/shares/incc/porthos/Genetics_Centre_Bioinformatics/mosaic_calling/dgrigoriadis/take2/"
inbamsdir=maindir+"panel_of_normals_BAMs/"
ponvcf=maindir+"panel_of_normals_vcfs/"
ponjointvcf=maindir+"panel_of_normals_joint_vcfs/"
mutect2out=maindir+"raw_somatic_caller_only/"
filtmutect2out=maindir+"filtered_somatic_calls/"
call_bams = maindir+"call_bams/"

#SOFTWARE
resources="/homedirs_APittman/sgul/shares/Mimir/Genetics_Centre_Bioinformatics_Mimir/resources/"
vcftools=resources+"vcftools/bin/vcftools"
plink=resources+"plink_linux_x86_64/plink"
tabix=resources+"htslib-1.9/tabix"
bgzip=resources+"htslib-1.9/tabixbgzip"
vcf_concat=resources+"vcftools/bin/vcf-concat"
java="java"
gatk=resources+"gatk-4.0.4.0/gatk-package-4.0.4.0-local.jar"
bwaindex=resources+"Genome_reference_files/human_g1k_v37.fasta"
exometargets=resources+"Genome_reference_files/BroadExACExomeIntervlas.bed"

#SETTINGS
ncores=6


