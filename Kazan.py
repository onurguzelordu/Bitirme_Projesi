import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Örnek bir DataFrame oluşturma
import pandas as pd

# CSV dosyasının yolunu belirleyin
dosya_yolu = r'C:\Veriler\2005-2015_verileri\Kazan1.csv'  

# CSV dosyasını oku ve DataFrame oluştur
df = pd.read_csv(dosya_yolu)

# DataFrame'i görüntüle
print(df)


# Basit bir grafik çizme
print(df.columns)




plt.plot(df['Yil'], df['Sicaklik'], label='Sicaklik')
plt.plot(df['Yil'], df['Cig_Noktasi'], label='Cig Noktasi')
plt.plot(df['Yil'], df['Ruzgar_Hizi'], label='Ruzgar_Hizi')
plt.plot(df['Yil'], df['Basinc'], label='Basinc')

plt.xlabel('Yil')
plt.ylabel('Değerler')
plt.title('Hava Durumu Grafiği')
plt.yticks(range(-35, 100, 5))
plt.legend()  # Efsane eklemek için
plt.show()
