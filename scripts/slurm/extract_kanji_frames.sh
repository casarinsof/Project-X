#!/bin/bash
#SBATCH -A IscrB_SRL4V
#SBATCH -p m100_usr_prod
#SBATCH --time 24:00:00 # format: HH:MM:SS
#SBATCH -N 1 # 1 node
#SBATCH --ntasks-per-node=1 # 8 tasks out of 128
#SBATCH --cpus-per-task=8
#SBATCH --gres=gpu:1 # 1 gpus per node out of 4
##SBATCH --mem=7100 # memory per node out of 246000MB
#SBATCH --job-name=cugwu_vtadl



module load anaconda/2020.11
module load cuda/11.0
module load cmake
module load profile/deeplrn

source /cineca/prod/opt/tools/anaconda/2020.11/none/etc/profile.d/conda.sh

conda activate ai
cd /m100/home/userexternal/cugwu000/Python\ Scripts/Project-X

python scripts/data_scripts/extract_frames_kanji.py

wait
conda deactivate