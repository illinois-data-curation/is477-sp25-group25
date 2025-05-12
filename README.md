# is477-sp25-group25
Eric Zhang and Gregory Peng

[![DOI](https://zenodo.org/badge/948292320.svg)](https://doi.org/10.5281/zenodo.15384905)

# Reproducibility Instructions

1. Clone this repository.
2. Download data from Box: https://uofi.app.box.com/s/xpdb4v0tc4ou6dc3v4bw4oaj1cq6tjd6
3. Place the data into `results/merged.csv` and any other folders as instructed in Box.
4. Run `pip install -r requirements.txt` to install dependencies.
5. Run `snakemake --cores 1` to reproduce outputs.
6. All outputs will be generated in `results/` folder.
