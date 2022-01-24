import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from keras.utils import np_utils

# Veri dosya üzerinden okunur.
data = pd.read_csv('ekg.data')
giriş = "kalbin hızlı çalışması"
print ("artışı_girin :\n")
artışı_girin:

girin_artısı = input ()
0.45
if float(artış_değeri) >= 0.70:
    giriş = giriş + "koşu"
elif float(artış_değeri) >= 0.60:
    giriş = giriş + "yüzme"
elif float(artış_değeri) >= 0.50:
    giriş = giriş + "bisklet"
elif float(artış_değeri) >= 0.40:
    giriş = giriş + "voleybol"
elif float(artış_değeri) >= 0.30:
    giriş = giriş + "basketbol"
elif float(artış_değeri) >= 0.20:
    giriş = giriş + "futbol"
elif float(artış_değeri) >= 0.10:
    giriş = giriş + "yürüme"
else:
    giriş = giriş + "golf"
