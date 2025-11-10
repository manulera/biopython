"""
blah
"""

from Bio.Align import Alignment
import numpy as np


reference_str = "ACGT"
seq1_str = "ACGGT"
seq2_str = "AT"
seq3_str = "ACT"

# Coordinates for each alignment
coords1 = np.array([[0, 1, 2, 3, 3, 4], [0, 1, 2, 3, 4, 5], [0, 1, 1, 1, 1, 2]])

coords2 = np.array([[0, 2, 3, 4], [0, 2, 2, 3]])

# Generate input alignments
alignment1 = Alignment([reference_str, seq1_str, seq2_str], coords1)
alignment2 = Alignment([reference_str, seq3_str], coords2)

# Use the method being tested
msa = Alignment.from_alignments_with_same_reference([alignment2, alignment1])
