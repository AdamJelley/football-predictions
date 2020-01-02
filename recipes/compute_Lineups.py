# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
fixtures_prepared = dataiku.Dataset("Fixtures_prepared")
fixtures_prepared_df = fixtures_prepared.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

lineups_df = fixtures_prepared_df # For this sample code, simply copy input to output


# Write recipe outputs
lineups = dataiku.Dataset("Lineups")
lineups.write_with_schema(lineups_df)
