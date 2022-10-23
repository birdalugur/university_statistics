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


toplam_gelirin_ogrenci_sayisina_orani = toplam_gelir/toplam_ogrenci_sayisi

toplam_giderin_ogrenci_sayisina_orani = toplam_gider/toplam_ogrenci_sayisi

net_gelirin_ogrenci_sayisina_orani = (toplam_gelir-toplam_gider) / toplam_ogrenci_sayisi

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


ales_sayisal = pd.concat(
    [
        tables.Table2021.ales_sayisal.assign(year=2021),
        tables.Table2020.ales_sayisal.assign(year=2020),
        tables.Table2019.ales_sayisal.assign(year=2019),
        tables.Table2018.ales_sayisal.assign(year=2018)
    ]
).pivot(index='year', columns='university', values='value')



ales_ea = pd.concat(
    [
        tables.Table2021.ales_esit_agirlik.assign(year=2021),
        tables.Table2020.ales_esit_agirlik.assign(year=2020),
        tables.Table2019.ales_esit_agirlik.assign(year=2019),
        tables.Table2018.ales_esit_agirlik.assign(year=2018)
    ]
).pivot(index='year', columns='university', values='value')


ales_sozel = pd.concat(
    [
        tables.Table2021.ales_sozel.assign(year=2021),
        tables.Table2020.ales_sozel.assign(year=2020),
        tables.Table2019.ales_sozel.assign(year=2019),
        tables.Table2018.ales_sozel.assign(year=2018)
    ]
).pivot(index='year', columns='university', values='value')


writer = pd.ExcelWriter("variables.xlsx")

def write_excel(var, name):
    var = var.T
    var.index.name = None
    var.to_excel(writer, sheet_name=name)


write_excel(toplam_ogrenci_sayisi, "toplam_ogrenci_sayisi")
write_excel(onlisans_ogrenci_sayisi, "onlisans_ogrenci_sayisi")
write_excel(doktora_ogrenci_sayisi, "doktora_ogrenci_sayisi")
write_excel(lisans_ogrenci_sayisi, "lisans_ogrenci_sayisi")
write_excel(lisansustu_ogrenci_sayisi, "lisansustu_ogrenci_sayisi")
write_excel(yabanci_uyruklu_ogrenci_sayisi,"yabanci_uyruklu_ogrenci_sayisi")
write_excel(gelen_ogrencinin_giden_ogrenciye_orani,"gelen_ogrencinin_giden_ogrenciye_orani")
write_excel(ogrenci_basi_cari_gider,"ogrenci_basi_cari_gider")
write_excel(toplam_arge_harcamalari,"toplam_arge_harcamalari")
write_excel(reklam_harcamalari,"reklam_harcamalari")
write_excel(kutuphane_harcamalari,"kutuphane_harcamalari")
write_excel(ogrencilere_verilen_burslarin_egitim_ve_ogretim_gelirlerine_orani,"ogrencilere_verilen_burslarin_egitim_ve_ogretim_gelirlerine_orani")
write_excel(toplam_gelir,"toplam_gelir")
write_excel(toplam_gider,"toplam_gider")
write_excel(toplam_gelirin_ogrenci_sayisina_orani,"toplam_gelirin_ogrenci_sayisina_orani")
write_excel(toplam_giderin_ogrenci_sayisina_orani,"toplam_giderin_ogrenci_sayisina_orani")
write_excel(net_gelirin_ogrenci_sayisina_orani,"net_gelirin_ogrenci_sayisina_orani")
write_excel(ogretim_elemanlarina_odenen_ucretlerin_toplam_gidere_orani, "ogretim_elemanlarina_odenen_ucretlerin_toplam_gidere_orani")
write_excel(kadrolu_ogretim_uyesi_basina_ogrenci_sayisi,"kadrolu_ogretim_uyesi_basina_ogrenci_sayisi")
write_excel(ales_sayisal,"ales_sayisal")
write_excel(ales_sozel, "ales_sozel")
write_excel(ales_ea, "ales_ea")

writer.save()
writer.close()



