#Install dependencies
pip install streamlit
pip install qdrant-client

import streamlit as st
from streamlit.connections import ExperimentalBaseConnection
from qdrant_client import QdrantClient
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from google.cloud import bigquery

connection = st.experimental_connection()

class MyConnection(ExperimentalBaseConnection[connection.MyConnection]):
  def _connect(self, **kwargs) -> MyConnection:
    return connection.connect(**self._secrets, **kwargs)
  def cursor(self, **kwargs):
    return self._instance(cursor)
  ttl = 900
  @st.cache_data(ttl = ttl)
  def query(self, query: str, ttl = ttl, **kwargs):
    return self._instance.query(query)

st.title('Streamlit Challenge with Qdrant API')
