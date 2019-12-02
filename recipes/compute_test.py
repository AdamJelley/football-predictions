# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu



# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

test_df = ... # Compute a Pandas dataframe to write into test


# Write recipe outputs
test = dataiku.Dataset("test")
test.write_with_schema(test_df)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
print('testing123')

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
print('it works!')