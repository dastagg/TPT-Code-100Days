# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
from datetime import datetime
from datetime import timedelta

# %%
t = timedelta(days=4, hours=10)

# %%
type(t)

# %%
t.days

# %%
t.seconds

# %%
t.seconds / 60 / 60

# %%
t.seconds / 3600

# %%
eta = timedelta(hours = 6)

# %%
today = datetime.today()

# %%
today

# %%
eta

# %%
today + eta

# %%
str(today + eta)

# %%
