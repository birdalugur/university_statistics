import pandas as pd
import plotly.express as px
from plotly.offline import plot

from tables import Table2021, Table2019, Table2020, Table2018


def extract_uni(data: list, uni_code: int):
    extracted_data = []

    for arge in data:
        arge_sort = arge.sort_values("value", ascending=False)
        bilgi_arge = arge_sort[arge_sort["code"] == uni_code]
        extracted_data.append(bilgi_arge)

    return pd.concat(extracted_data)


def concat_data_by_year(data_list: [pd.DataFrame], years: list[int]):
    list_of_data = list()
    for data, year in zip(data_list, years):
        list_of_data.append(data.assign(year=year))
    return pd.concat(list_of_data)


arge_list = [Table2021.toplam_arge_harcamalari,
             Table2020.toplam_arge_harcamalari,
             Table2019.toplam_arge_harcamalari
             ]

arge_bilgi = extract_uni(data=arge_list, uni_code=98)

arge_bilgi = arge_bilgi.assign(year=[2021, 2020, 2019]).reset_index()

fig = px.bar(arge_bilgi, x='year', y='index')
plot(fig)

concat_data_by_year(arge_list, [2021, 2020, 2019])
