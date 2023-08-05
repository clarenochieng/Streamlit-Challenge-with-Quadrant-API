!pip install streamlit
!pip install qdrant-client

import streamlit as st
from streamlit.connections import ExperimentalBaseConnection
from qdrant_client import QdrantClient
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from google.cloud import bigquery

connection = st.experimental_connection()

