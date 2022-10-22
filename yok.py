import pandas as pd

import tables

toplam_ogrenci_sayisi = pd.concat(
    [
        tables.Table2021.toplam_ogrenci_sayisi.assign(year=2021),
        tables.Table2020.toplam_ogrenci_sayisi.assign(year=2020),
        tables.Table2019.toplam_ogrenci_sayisi.assign(year=2019),
        tables.Table2018.toplam_ogrenci_sayisi.assign(year=2018)
    ]
).pivot(index='year', columns='university', values='value')


onlisans_ogrenci_sayisi = pd.concat(
    [
        tables.Table2021.onlisans_ogrenci_sayisi.assign(year=2021),
        tables.Table2020.onlisans_ogrenci_sayisi.assign(year=2020),
        tables.Table2019.onlisans_ogrenci_sayisi.assign(year=2019),
        tables.Table2018.onlisans_ogrenci_sayisi.assign(year=2018)
    ]
).pivot(index='year', columns='university', values='value')


doktora_ogrenci_sayisi = pd.concat(
    [
        tables.Table2021.doktora_ogrenci_sayisi.assign(year=2021),
        tables.Table2020.doktora_ogrenci_sayisi.assign(year=2020),
    ]
).pivot(index='year', columns='university', values='value')


lisans_ogrenci_sayisi = pd.concat(
    [
        tables.Table2021.lisans_ogrenci_sayisi.assign(year=2021),
        tables.Table2020.lisans_ogrenci_sayisi.assign(year=2020),
        tables.Table2019.lisans_ogrenci_sayisi.assign(year=2019),
        tables.Table2018.lisans_ogrenci_sayisi.assign(year=2018)
    ]
).pivot(index='year', columns='university', values='value')


lisansustu_ogrenci_sayisi = pd.concat(
    [
        tables.Table2021.lisansustu_ogrenci_sayisi.assign(year=2021),
        tables.Table2020.lisansustu_ogrenci_sayisi.assign(year=2020),
        tables.Table2019.lisansustu_ogrenci_sayisi.assign(year=2019),
        tables.Table2018.lisansustu_ogrenci_sayisi.assign(year=2018)
    ]
).pivot(index='year', columns='university', values='value')


yabanci_uyruklu_ogrenci_sayisi = pd.concat(
    [
        tables.Table2021.yabanci_uyruklu_ogrenci_sayisi.assign(year=2021),
        tables.Table2020.yabanci_uyruklu_ogrenci_sayisi.assign(year=2020),
        tables.Table2019.yabanci_uyruklu_ogrenci_sayisi.assign(year=2019)
    ]
).pivot(index='year', columns='university', values='value')


gelen_ogrencinin_giden_ogrenciye_orani = pd.concat(
    [
        tables.Table2021.gelen_ogrencinin_giden_ogrenciye_orani.assign(year=2021),
        tables.Table2020.gelen_ogrencinin_giden_ogrenciye_orani.assign(year=2020),
        tables.Table2019.gelen_ogrencinin_giden_ogrenciye_orani.assign(year=2019)
    ]
).pivot(index='year', columns='university', values='value')

ogrenci_basi_cari_gider = pd.concat(
    [
        tables.Table2021.ogrenci_basi_cari_gider.assign(year=2021),
        tables.Table2020.ogrenci_basi_cari_gider.assign(year=2020),
        tables.Table2019.ogrenci_basi_cari_gider.assign(year=2019),
        tables.Table2018.ogrenci_basi_cari_gider.assign(year=2018)
    ]
).pivot(index='year', columns='university', values='value')

toplam_arge_harcamalari = pd.concat(
    [
        tables.Table2021.toplam_arge_harcamalari.assign(year=2021),
        tables.Table2020.toplam_arge_harcamalari.assign(year=2020),
        tables.Table2019.toplam_arge_harcamalari.assign(year=2019)
    ]
).pivot(index='year', columns='university', values='value')

reklam_harcamalari = pd.concat(
    [
        tables.Table2021.reklam_harcamalari.assign(year=2021),
        tables.Table2020.reklam_harcamalari.assign(year=2020),
        tables.Table2019.reklam_harcamalari.assign(year=2019)
    ]
).pivot(index='year', columns='university', values='value')

kutuphane_harcamalari = pd.concat(
    [
        tables.Table2021.kutuphane_harcamalari.assign(year=2021),
        tables.Table2020.kutuphane_harcamalari.assign(year=2020),
        tables.Table2019.kutuphane_harcamalari.assign(year=2019)
    ]
).pivot(index='year', columns='university', values='value')



ogrencilere_verilen_burslarin_egitim_ve_ogretim_gelirlerine_orani = pd.concat(
    [
        tables.Table2021.ogrencilere_verilen_burslarin_egitim_ve_ogretim_gelirlerine_orani.assign(year=2021),
        tables.Table2020.ogrencilere_verilen_burslarin_egitim_ve_ogretim_gelirlerine_orani.assign(year=2020)
    ]
).pivot(index='year', columns='university', values='value')


toplam_gelir = pd.concat(
    [
        tables.Table2021.toplam_gelir.assign(year=2021),
        tables.Table2020.toplam_gelir.assign(year=2020)
    ]
).pivot(index='year', columns='university', values='value')


toplam_gider = pd.concat(
    [
        tables.Table2021.toplam_gider.assign(year=2021),
        tables.Table2020.toplam_gider.assign(year=2020)
    ]
).pivot(index='year', columns='university', values='value')


toplam_gelir - toplam_gider

ogretim_elemanlarina_odenen_ucretlerin_toplam_gidere_orani = pd.concat(
    [
        tables.Table2021.ogretim_elemanlarina_odenen_ucretlerin_toplam_gidere_orani.assign(year=2021),
        tables.Table2020.ogretim_elemanlarina_odenen_ucretlerin_toplam_gidere_orani.assign(year=2020)
    ]
).pivot(index='year', columns='university', values='value')


kadrolu_ogretim_uyesi_basina_ogrenci_sayisi = pd.concat(
    [
        tables.Table2021.kadrolu_ogretim_uyesi_basina_ogrenci_sayisi.assign(year=2021),
        tables.Table2020.kadrolu_ogretim_uyesi_basina_ogrenci_sayisi.assign(year=2020),
        tables.Table2020.kadrolu_ogretim_uyesi_basina_ogrenci_sayisi.assign(year=2018)
    ]
).pivot(index='year', columns='university', values='value')




