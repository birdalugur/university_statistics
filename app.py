from tables import Table2021, Tuma2021
from OLS import write_OLS
from plot import plot_OLS

y = Tuma2021.genel_memnuniyet_puani

all_x = [Table2021.burslu_ogrenci_orani,
         Table2021.ogrenci_basina_kutuphane_alani,
         Table2021.toplam_arge_harcamalari]

x_title = [
    "Burslu Öğrenci Oranı",
    "Öğrenci Başına Kütüphane Alanı",
    "Toplam Arge Harcamaları"
]


for x, title in zip(all_x, x_title):
    print(title)
    data = y.merge(x, on='code', how='inner', suffixes=('_y', '_x')) \
        .sort_values('value_y', ascending=False).drop('university_x', axis=1)

    Y = data['value_y']
    X = data['value_x']

    write_OLS(Y, X, title)

    plot_OLS(data, 'university_y', 'bilgi', title)
