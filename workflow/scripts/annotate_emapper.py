#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python 2.7
# -*- coding: utf-8 -*-
"""
Created by Jacob Musser
modified by Natasha Picciani
Jan 2023

Annotating proteins with eggNOG mapper

usage: annotate_emapper.py proteins.fasta outputDirectory
"""

import re
import subprocess
from pathlib import PurePosixPath
import sys
import argparse
from Bio import SeqIO

# Path to programs and files
gonames_file = "/home/nnp9/local/datasets/go_terms_2019.txt"  # GO Terms IDs and their corresponding names from 2019 GO release


# User inputs
proteinFile = sys.argv[1]  # protein file
outDir = sys.argv[2]  # output directory
python = sys.argv[3]
emapper = sys.argv[4]
basename = PurePosixPath(proteinFile).stem

# Functionally annotating the protein sequences with eggNOG-mapper
subprocess.call(
    [
        python,
        emapper,
        "-i",
        proteinFile,
        "-m",
        "diamond",
        "-o",
        basename,
        "--cpu",
        "40",
        "--output_dir",
        outDir,
        "--dmnd_ignore_warnings"
    ]
)