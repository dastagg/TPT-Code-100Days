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

# %%
from datetime import date

# %%
datetime.today()

# %%
today = datetime.today()

# %%
type(today)

# %%
todaydate = date.today()

# %%
todaydate

# %%
type(todaydate)

# %%

# %%

# %%

# %%
todaydate.month

# %%
todaydate.day

# %%
todaydate.year

# %%
christmas = date(2022, 12, 25)

# %%
christmas

# %%
christmas - todaydate

# %%
(christmas - todaydate).days

# %%
if christmas != todaydate:
    print("Sorry, there are still " + str((christmas-todaydate).days) + " days until Christmas")
else:
    print("Yay, it's Christmas!")
        

# %%
