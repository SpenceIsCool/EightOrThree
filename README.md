# EightOrThree
Authors: Spencer Wilson and Amiy Yadav

A translator for 0 - 9 between ASL and ISL and vise-versa

This is currently the bare bones example, but there is intent to refine this code in late December 2022.

This project was completed for CSCI 5922 Neural Networks and Deep Learning course in Fall 2022 at the University of Colorado Boulder with Prof. Danna Gurari and assistance from Samreen Anjum and Lucas Hayne

For a brief demonstration of the usefulness of this product, please see our YouTube video here: https://www.youtube.com/watch?v=f9_uXm3NwQA&t=203s


## Datasets
Dataset is hosted on kaggle at: https://www.kaggle.com/datasets/spenceiscool/asl-isl-numbers-conversions


## Models
Pre-trained models are hosted on kaggle at: https://www.kaggle.com/datasets/spenceiscool/asl-isl-numbers-conversions


## Execution
- We recommend setting up a tensor-flow environment that will support your GPUs. If runnning on a Mac with x86 chip, here is a good tutorial: https://developer.apple.com/metal/tensorflow-plugin/
- Setup a kaggle account if you do not already have one and follow isntructions here: https://github.com/Kaggle/kaggle-api#download-dataset-files
- Source the provided requirements.txt file
- Run prep.py. This will take a while as it must download relatively large files.
- Activate your GPU enabled tensor-flow environment and execute `python3 tool.py`

- If you'd like to free up space on your device, execute `clean.sh`, this will remove the zip file, the datasets, models and results directory.

