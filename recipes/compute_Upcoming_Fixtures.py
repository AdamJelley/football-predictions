# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
leagues_prepared_filtered = dataiku.Dataset("Leagues_prepared_filtered")
leagues_prepared_filtered_df = leagues_prepared_filtered.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

upcoming_Fixtures_df = leagues_prepared_filtered_df # For this sample code, simply copy input to output


# Write recipe outputs
upcoming_Fixtures = dataiku.Dataset("Upcoming_Fixtures")
upcoming_Fixtures.write_with_schema(upcoming_Fixtures_df)