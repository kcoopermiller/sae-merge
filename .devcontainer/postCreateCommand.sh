#!/bin/bash

# Install dependencies
pip install git+https://github.com/callummcdougall/eindex.git
pip install -qU huggingface_hub
pip install -q transformer_lens sae-lens==0.1.0 wandb accelerate

# Install mergekit dependencies inside venv
git clone -q https://github.com/cg123/mergekit.git
python -m venv ./mergekit/venv
source ./mergekit/venv/bin/activate
pip install -e ./mergekit
deactivate