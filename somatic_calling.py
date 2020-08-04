#Python script to perform somatic variant calling on unpaired BAM files using a Panel of normals
#Here we're using GATK4 Mutect2 tool.

#Libraries
import glob
import os

from dependencies import *
from utils import *

#Directories checking
#Check if input directories exist and create output directories
if not os.path.exists(inbamsdir):
    print("--ERROR: Sorry "+inbamsdir+" does not exist, or it's not accessible at the moment.")
    raise KeyError

ponbams = glob.glob(inbamsdir+"*/*_sorted_unique_recalibrated.bam")

if len(ponbams)==0:
    print("--ERROR: Sorry " + inbamsdir + " does not contain any BAM files, or they're not accessible at the moment.")
    raise KeyError

if not os.path.exists(ponvcf):
    os.makedirs(ponvcf)

if not os.path.exists(ponjointvcf):
    os.makedirs(ponjointvcf)

if not os.path.exists(mutect2out):
    os.makedirs(mutect2out)

if not os.path.exists(filtmutect2out):
    os.makedirs(filtmutect2out)

#STEP1: Create individual VCFs from the panel of normal BAM files.
ponbams_samples = [x.split("/")[-2] for x in ponbams]
if len(ponbams_samples)==len(ponbams):
    ponbams_dict = dict(zip(ponbams_samples,ponbams))
else:
    print("--ERROR: Sorry, your input bam file samples are not unique.")
    raise KeyError

for pdi in ponbams_dict:
    if not os.path.exists(ponvcf+pdi):
        os.makedirs(ponvcf+pdi)

bam2vcf_commands = [java+" -jar "+gatk+" Mutect2 "+\
                    "-R "+bwaindex+" "+\
                    "-I "+ponbams_dict[x]+" "+\
                    "-tumor "+x+" "+\
                    "--disable-read-filter MateOnSameContigOrNoMappedMateReadFilter "+\
                    "-L "+exometargets+" "+\
                    "-O "+ponvcf+x+"/"+x+".vcf.gz" for x in ponbams_dict]

parallel_command(bam2vcf_commands, n=ncores)

#STEP2: Collate sites present in two or more individual PoN VCFs into a sites-only VCF file.
ponvcfs = glob.glob(ponvcf+"*/*.vcf.gz")
vcf2joinvcf_command = java+" -jar "+gatk+" CreateSomaticPanelOfNormals "+\
    "--vcfs "+" --vcfs ".join([vcf for vcf in ponvcfs])+" "+\
    "-O "+ponjointvcf+"PoN.vcf.gz"

parallel_command([vcf2joinvcf_command], n=ncores)

#STEP3: Run mutect2 on the files specified in the call_bams directory
bams_tocall = glob.glob(call_bams+"*/*.bam")
sample_names = [x.split("/")[-2] for x in bams_tocall]
mutect2_commands=[]
for i in range(0,len(bams_tocall)):
    if not os.path.exists(mutect2out + "/" + sample_names[i]):
        os.makedirs(mutect2out + "/" + sample_names[i])
    mutect2_commands.append(java+" -jar "+gatk+" Mutect2 "+\
        "-R "+bwaindex+" "+\
        "-I "+bams_tocall[i]+" "+\
        "-tumor "+sample_names[i]+" "+\
        "-L "+exometargets+" "+\
        "--panel-of-normals "+ponjointvcf+"PoN.vcf.gz "+\
        "-O "+mutect2out + sample_names[i] + "/" + sample_names[i] + "_raw_mutect2.vcf " + \
        "-bamout "+mutect2out + sample_names[i] + "/" + sample_names[i] + "_bamout.bam")

parallel_command(mutect2_commands, n=ncores)

#STEP4: Filter the mutect2 calls
calledvcfs = glob.glob(mutect2out + "*/*_raw_mutect2.vcf")
vcf_sn = [x.split("/")[-2] for x in calledvcfs]
filter_commands=[]
for i in range(0,len(calledvcfs)):
    if not os.path.exists(filtmutect2out + "/" + vcf_sn[i]):
        os.makedirs(filtmutect2out + "/" + vcf_sn[i])
    filter_commands.append(java+" -jar "+gatk+" FilterMutectCalls "+\
        "-V "+calledvcfs[i]+" "+\
        "-O "+ filtmutect2out + vcf_sn[i] + "/" + vcf_sn[i] + "_filtered_mutect2.vcf")

parallel_command(filter_commands, n=ncores)