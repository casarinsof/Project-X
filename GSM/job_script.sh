#!/bin/bash
#SBATCH -A IscrB_SRL4V
#SBATCH -p m100_usr_prod
#SBATCH --time 24:00:00 # format: HH:MM:SS
#SBATCH -N 1 # 1 node
#SBATCH --ntasks-per-node=1 # 8 tasks out of 128
#SBATCH --cpus-per-task=8
#SBATCH --gres=gpu:1 # 1 gpus per node out of 4
#SBATCH --mem=100000 # memory per node out of 246000MB
#SBATCH --job-name=cugwu-nogsm



module load anaconda/2020.11
module load cuda/11.0
module load cmake
module load profile/deeplrn

source /cineca/prod/opt/tools/anaconda/2020.11/none/etc/profile.d/conda.sh

conda activate ai
cd /m100/home/userexternal/cugwu000/Python\ Scripts/GSM

python main.py kanji RGB --split 1 --arch BNInception --num_segments 8 --consensus_type avg \
                           --batch-size 16 --iter_size 2 --dropout 0.5 --lr 0.01 --warmup 10 --epochs 60 \
                           --eval-freq 5 --gd 20 --run_iter 1 -j 8 --npb --gsm

wait
conda deactivate


