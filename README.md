# Project-X: Anomaly Detection (in collaboration)

Experiments on video-based anomaly detection built on top of
[Gate-Shift Networks for Video Action Recognition](http://openaccess.thecvf.com/content_CVPR_2020/papers/Sudhakaran_Gate-Shift_Networks_for_Video_Action_Recognition_CVPR_2020_paper.pdf)
(GSM, Sudhakaran, Escalera, Lanz, CVPR 2020). The code is derived from the
authors' GSM codebase (BSD 2-Clause, Copyright (c) 2019 FBK; see `LICENSE`) and
adds a Kanji-based dataset pipeline (frame extraction, benchmarks) used in our
experiments. Run logs and result tables are kept in
[`docs/EXPERIMENTS.md`](docs/EXPERIMENTS.md).

## Repository structure

```
gsm/                      Python package (model, data, training / testing)
  main.py                   training entry point
  test_models.py            evaluation entry point
  models.py, gsm.py         video model and Gate-Shift Module
  dataset.py, datasets_video.py, transforms.py, opts.py, CosineAnnealingLR.py
  ops/                      consensus module and basic ops
  model_zoo/                BNInception / InceptionV3 (+GSM) definitions, yaml specs
scripts/                  shell wrappers and standalone scripts
  train_rgb.sh, test_rgb.sh
  eval/                     evaluation shell scripts
  slurm/                    SLURM jobs (cluster-specific paths)
  data_scripts/             frame extraction / list-file generation
  average_scores.py, download_models.py, tds_benchmarks.py
data/                     Kuzushiji-Kanji .npz files (kkanji-*)
docs/                     experiment log, original GSM README
third_party/
  tensorflow_models/        vendored copy of tensorflow/models (not used by the code)
```

## Installation

The original GSM code targets Python 3.5 and PyTorch 1.2.

```
pip install -r requirements.txt
```

## Usage

Run all commands from the repository root.

Training:
```
python -m gsm.main something-v1 RGB --arch BNInception \
    --num_segments 8 --consensus_type avg --batch-size 16 --iter_size 2 \
    --dropout 0.5 --lr 0.01 --warmup 10 --epochs 60 --eval-freq 5 \
    --gd 20 --run_iter 1 -j 16 --npb --gsm
```
(`bash scripts/train_rgb.sh` runs the InceptionV3 / 16 segment configuration.)

Testing:
```
bash scripts/test_rgb.sh        # or any script in scripts/eval/
```
Checkpoints are expected in `models/` (see `scripts/download_models.py`).

## Data

- Something-Something-v1 and Diving48: see `docs/GSM_original_README.md` and
  `scripts/data_scripts/process_dataset_*.py`, `extract_frames_diving48.py`.
- Kanji: `data/kkanji-*.npz`, processed with `scripts/data_scripts/extract_frames_kanji.py`
  and `extract_frames_MovingKanji.py`. Several of these scripts contain absolute
  paths from the original cluster (`/m100_work/...`) that must be adapted.

## Credits

- GSM: Swathikiran Sudhakaran, Sergio Escalera, Oswald Lanz, "Gate-Shift Networks
  for Video Action Recognition", CVPR 2020. `gsm/model_zoo` derives from
  tensorflow-model-zoo.torch.
- `third_party/tensorflow_models`: copy of TensorFlow Models (Apache-2.0, see its LICENSE).

## License

BSD 2-Clause (see `LICENSE`).
