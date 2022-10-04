# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 13:22:13 2022

@author: Nehal
"""

import os
import streamlit as st

#Custom Imports
from multipage import MultiPage
from pagesOCT import Decentraland_OCT,MetaverseSummaryGraph_OCT

# Create an instance of the app 
app = MultiPage()

# Title of the main page

#col2.title("Data Storyteller Application")

# Add all your application here
app.add_page("Map - Area Average Price", Decentraland_OCT.app)
app.add_page("Summary", MetaverseSummaryGraph_OCT.app)


# The main app
app.run()