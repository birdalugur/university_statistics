import pandas as pd
from dataclasses import dataclass

all_paths = []

uni_names = pd.Series()

uni_kw = ['Üniversite', 'ÜNİVERSİTE**', 'ÜNİVERSİTE/MYO', 'üniversite', 'ÜNİVERSİTE', 'ÜNİVERSİTE / MYO',
          'ÜNİVERSİTE/ MYO**']

other_kw = []

for path in all_paths:
    df = pd.read_csv(path)
    for kw in uni_kw:
        if kw in df.columns:
            uni_names = uni_names.append(df[kw])

            break
    else:
        other_kw.append(path)

unicodes = pd.read_csv("all_uni - all_uni.csv")

unique_codes = pd.read_csv("unique_codes.csv", index_col='code')


def _read_from_colname(df, col):
    uni_col = []
    for kw in uni_kw:
        if kw in df.columns:
            uni_col.append(kw)
            break
    else:
        print(df.columns)
        raise Exception("Üniversite sütunu bulunamadı!")

    uni_col = uni_col[0]
    default_column = [(uni_col, 'Unnamed: 1_level_1')]

    col.extend(default_column)

    data = df[col]
    data = data.droplevel(1, axis=1)
    data[uni_col] = data[uni_col].str.lower()
    data = data.merge(unicodes, how='left', left_on=uni_col,
                      right_on='university')

    select_col = [col[0][0]]
    select_col.extend(['university', 'code'])

    data = data[select_col]
    data = data.rename({select_col[0]: "value"}, axis=1)
    data = data.dropna()
    data['university'] = unique_codes.loc[data.code.values]['uni'].values
    return data


@dataclass
class Tuma2018:
    file_path = "Tuma Sıralamaları/2018 Vakıf Üniversitelerinin Memnuniyet Alanlarına Göre Sıralamaları.xlsx"

    df = pd.read_excel(file_path, header=[0, 1])

    genel_memnuniyet_puani = _read_from_colname(df, [('Genel Memnuniyet Puanı', 'Unnamed: 2_level_1')])

    yerleske_ve_yasamin_doyuruculugu = _read_from_colname(df, [('Yerleşke ve Yaşamının Doyuruculuğu', 'Puan')])

    ogrenim_deneyiminin_tatminkarligi = _read_from_colname(df, [('Öğrenim Deneyiminin Tatminkârlığı', 'Puan')])

    akademik_destek = _read_from_colname(df, [('Akademik Destek ve İlgi', 'Puan')])

    kurumun_yonetim_ve_isleyisinden_memnuniyeti = _read_from_colname(df, [
        ('Kurumun Yönetim ve İşleyişinden Memnuniyet', 'Puan')])

    ogrenme_imkan_ve_kaynak_zenginligi = _read_from_colname(df, [('Öğrenme İmkân ve Kaynaklarının Zenginliği', 'Puan')])

    kisisel_gelisim_ve_kariyer_destegi = _read_from_colname(df, [('Kişisel Gelişim ve Kariyer Desteği', 'Puan')])


@dataclass
class Tuma2019:
    file_path = "Tuma Sıralamaları/2019 VAKIF ÜNİVERSİTELERİNİN MEMNUNİYET ALANLARINA GÖRE SIRALAMALARI.xlsx"

    df = pd.read_excel(file_path, header=[0, 1])

    genel_memnuniyet_puani = _read_from_colname(df, [('Genel Memnuniyet Puanı', 'Unnamed: 2_level_1')])

    yerleske_ve_yasamin_doyuruculugu = _read_from_colname(df, [('Yerleşke ve Yaşamının Doyuruculuğu', 'Puan')])

    ogrenim_deneyiminin_tatminkarligi = _read_from_colname(df, [('Öğrenim Deneyiminin Tatminkârlığı', 'Puan')])

    akademik_destek = _read_from_colname(df, [('Akademik Destek ve İlgi', 'Puan')])

    kurumun_yonetim_ve_isleyisinden_memnuniyeti = _read_from_colname(df, [
        ('Kurumun Yönetim ve İşleyişinden Memnuniyet', 'Puan')])

    ogrenme_imkan_ve_kaynak_zenginligi = _read_from_colname(df, [('Öğrenme İmkân ve Kaynaklarının Zenginliği', 'Puan')])

    kisisel_gelisim_ve_kariyer_destegi = _read_from_colname(df, [('Kişisel Gelişim ve Kariyer Desteği', 'Puan')])


@dataclass
class Tuma2020:
    file_path = "Tuma Sıralamaları/2020. Vakıf Üniversitelerinin Memnuniyet Alanlarına Göre Sıralaması.xlsx"

    df = pd.read_excel(file_path, header=[0, 1])

    genel_memnuniyet_puani = _read_from_colname(df, [('Genel Memnuniyet Puanı', 'Unnamed: 2_level_1')])

    yerleske_ve_yasamin_doyuruculugu = _read_from_colname(df, [('Yerleşke ve Yaşamının Doyuruculuğu', 'Puan')])

    ogrenim_deneyiminin_tatminkarligi = _read_from_colname(df, [('Öğrenim Deneyiminin Tatminkârlığı', 'Puan')])

    akademik_destek = _read_from_colname(df, [('Akademik Destek ve İlgi', 'Puan')])

    kurumun_yonetim_ve_isleyisinden_memnuniyeti = _read_from_colname(df, [
        ('Kurumun Yönetim ve İşleyişinden Memnuniyet', 'Puan')])

    ogrenme_imkan_ve_kaynak_zenginligi = _read_from_colname(df, [('Öğrenme İmkân ve Kaynaklarının Zenginliği', 'Puan')])

    kisisel_gelisim_ve_kariyer_destegi = _read_from_colname(df, [('Kişisel Gelişim ve Kariyer Desteği', 'Puan')])


@dataclass
class Tuma2021:
    file_path = "Tuma Sıralamaları/2021 Vakıf Üniversitelerinin Memnuniyet Alanlarına Göre Sıralaması.xlsx"

    df = pd.read_excel(file_path, header=[0, 1])

    genel_memnuniyet_puani = _read_from_colname(df, [('Genel Memnuniyet Puanı', 'Unnamed: 2_level_1')])

    uzaktan_egitim_altyapisi = _read_from_colname(df, [('Uzaktan Eğitim Alt Yapısı', 'Puan')])

    ogrenim_deneyiminin_tatminkarligi = _read_from_colname(df, [('Öğrenim Deneyiminin Tatminkârlığı', 'Puan')])

    akademik_destek = _read_from_colname(df, [('Akademik Destek ve İlgi', 'Puan')])

    kurumun_yonetim_ve_isleyisinden_memnuniyeti = _read_from_colname(df, [
        ('Kurumun Yönetim ve İşleyişinden Memnuniyet', 'Puan')])

    ogrenme_imkan_ve_kaynak_zenginligi = _read_from_colname(df, [('Öğrenme İmkân ve Kaynaklarının Zenginliği', 'Puan')])

    kisisel_gelisim_ve_kariyer_destegi = _read_from_colname(df, [('Kişisel Gelişim ve Kariyer Desteği', 'Puan')])


@dataclass
class Tuma2022:
    file_path = "Tuma Sıralamaları/2022 Vakıf Üniversitelerinin Memnuniyet Alanlarına Göre Sıralaması.xlsx"

    df = pd.read_excel(file_path, header=[0, 1])

    genel_memnuniyet_puani = _read_from_colname(df, [('Genel Memnuniyet Puanı', 'Unnamed: 2_level_1')])

    ogrenim_deneyiminin_tatminkarligi = _read_from_colname(df, [('Öğrenim Deneyiminin Tatminkârlığı', 'Puan')])

    yerleske_ve_yasamin_doyuruculugu = _read_from_colname(df, [('Yerleşke ve Yaşamının Doyuruculuğu', 'Puan')])

    akademik_destek = _read_from_colname(df, [('Akademik Destek ve İlgi', 'Puan')])

    kurumun_yonetim_ve_isleyisinden_memnuniyeti = _read_from_colname(df, [
        ('Kurumun Yönetim ve İşleyişinden Memnuniyet', 'Puan')])

    ogrenme_imkan_ve_kaynak_zenginligi = _read_from_colname(df, [('Öğrenme İmkân ve Kaynaklarının Zenginliği', 'Puan')])

    kisisel_gelisim_ve_kariyer_destegi = _read_from_colname(df, [('Kişisel Gelişim ve Kariyer Desteği', 'Puan')])


def _read_from_sheet(excel_file, sheet_name, cols):
    data = pd.read_excel(excel_file, sheet_name)
    uni_col = []
    for kw in uni_kw:
        if kw in data.columns:
            uni_col.append(kw)
            break
    else:
        print(data.columns)
        raise Exception("Üniversite sütunu bulunamadı!")

    uni_col = uni_col[0]
    data[uni_col] = data[uni_col].str.lower()
    data = data.merge(unicodes, how='left', left_on=uni_col, right_on='university')
    cols.extend(['university', 'code'])
    data = data[cols]
    data = data.rename({cols[0]: "value"}, axis=1)
    data = data.dropna()
    data['university'] = unique_codes.loc[data.code.values]['uni'].values

    return data


@dataclass
class Table2021:
    yok = pd.ExcelFile("Yök Raporları/2021.ods")

    toplam_ogrenci_sayisi = _read_from_sheet(
        yok,
        "Toplam Öğrenci Sayılarına Göre Vakıf Üniversiteleri",
        ["TOPLAM ÖĞRENCİ SAYISI"]
    )

    kadrolu_ogretim_uyesi_basina_ogrenci_sayisi = _read_from_sheet(
        yok,
        "Kadrolu Öğretim Üyesi Sayılarına Göre Vakıf Üniversiteleri",
        ["KADROLU ÖĞRETİM ÜYESİ BAŞINA ÖĞRENCİ SAYISI"]
    )

    doktora_program_sayisi = _read_from_sheet(
        yok,
        "Doktora Öğrenci Sayılarına Göre Vakıf Üniversiteleri",
        ["DOKTORA PROGRAM SAYISI***"]
    )

    ogrenci_basina_kapali_alan = _read_from_sheet(
        yok,
        "Öğrenci Başına Düşen Kapalı Alan Dağılımına Göre Vakıf Yükseköğretim Kurumları",
        ["ÖĞRENCİ BAŞINA KAPALI ALAN**"]
    )

    ogrenci_basina_acik_alan = _read_from_sheet(
        yok,
        "Öğrenci Başına Düşen Açık Alan Dağılımına Göre Vakıf Yükseköğretim Kurumları",
        ["ÖĞRENCİ BAŞINA AÇIK ALAN**"]
    )

    yabanci_uyruklu_ogrencilerin_toplam_ogrenci_icerisindeki_orani = _read_from_sheet(
        yok,
        "Yabancı Uyruklu Öğrenci Sayısına Göre Vakıf Yükseköğretim Kurumları",
        ["YABANCI UYRUKLU ÖĞRENCİLERİN TOPLAM ÖĞRENCİ İÇERİSİNDEKİ ORANI (%)"]
    )

    toplam_ogrenci_icinde_gelen_ogrenci_orani = _read_from_sheet(
        yok,
        "2020-2021 Dönemi Yatay Geçiş ile Giden ve Gelen Öğrenci Sayısına Göre Vakıf Üniversiteleri",
        ["TOPLAM ÖĞRENCİ İÇERİSİNDE GELEN ÖĞRENCİ ORANI (%)"]
    )

    toplam_ogrenci_icinde_giden_ogrenci_orani = _read_from_sheet(
        yok,
        "2020-2021 Dönemi Yatay Geçiş ile Giden ve Gelen Öğrenci Sayısına Göre Vakıf Üniversiteleri",
        ["TOPLAM ÖĞRENCİ İÇERİSİNDE GİDEN ÖĞRENCİ ORANI (%)"]
    )

    gelen_ogrencinin_giden_ogrenciye_orani = _read_from_sheet(
        yok,
        "2020-2021 Dönemi Yatay Geçiş ile Gelen ve Giden Öğrenci Oranına Göre Vakıf Üniversiteleri",
        ["GELEN ÖĞRENCİNİN GİDEN ÖĞRENCİYE ORANI"]
    )

    yurt_disindan_gelen_ogrenci_sayisi = _read_from_sheet(
        yok,
        "2020-2021 Dönemi Yatay Geçiş ile Giden ve Gelen Öğrenci Sayısına Göre Vakıf Üniversiteleri",
        ["YURT DIŞINDAN GELEN ÖĞRENCİ SAYISI"]
    )

    doluluk_orani = _read_from_sheet(
        yok,
        "Vakıf Yükseköğretim Kurumlarının Doluluk Oranı",
        ["DOLULUK ORANI (%)"]
    )

    ogrenci_basi_cari_gider = _read_from_sheet(
        yok,
        "Öğrenci Başına Cari Gider Miktarına Göre Vakıf Üniversiteleri",
        ["ÖĞRENCİ BAŞINA CARİ GİDER (TL)"]
    )

    burslu_ogrenci_orani = _read_from_sheet(
        yok,
        "YKS Kontenjanları Bursluluk Oranlarına Göre Vakıf Yükseköğretim Kurumları",
        ["BURSLU ÖĞRENCİ ORANI (%)"]
    )

    toplam_arge_harcamalari = _read_from_sheet(
        yok,
        "Toplam Ar-Ge Harcamalarına Göre Vakıf Üniversiteleri",
        ["TOPLAM AR-GE HARCAMASI** (TL)"]
    )

    reklam_harcamalari = _read_from_sheet(
        yok,
        "Reklam ve Tanıtım Harcamalarına Göre Vakıf Yükseköğretim Kurumları",
        ["REKLAM-TANITIM HARCAMASI (TL)"]
    )

    kutuphane_harcamalari = _read_from_sheet(
        yok,
        "Kütüphane Harcamalarına Göre Vakıf Yükseköğretim Kurumları",
        ["KÜTÜPHANEYE YAPILAN HARCAMA (TL)"]
    )

    egitim_ve_ogretim_gelirleri = _read_from_sheet(
        yok,
        "Eğitim ve Öğretim Geliri ve Öğrencilere Verilen Burslar Dahil Vakıf Yükseköğretim Kurumları",
        ["EĞİTİM VE ÖĞRETİM GELİRLERİ** (TL)"]
    )

    ogrencilere_verilen_burslar = _read_from_sheet(
        yok,
        "Eğitim ve Öğretim Geliri ve Öğrencilere Verilen Burslar Dahil Vakıf Yükseköğretim Kurumları",
        ["ÖĞRENCİLERE VERİLEN BURSLAR***"]
    )

    ogrencilere_verilen_burslarin_egitim_ve_ogretim_gelirlerine_orani = _read_from_sheet(
        yok,
        "Eğitim ve Öğretim Geliri ve Öğrencilere Verilen Burslar Dahil Vakıf Yükseköğretim Kurumları",
        ["ÖĞRENCİLERE VERİLEN BURSLARIN EĞİTİM VE ÖĞRETİM GELİRLERİNE ORANI"]
    )

    toplam_gelir = _read_from_sheet(
        yok,
        "Gelir ve Giderlerine Göre Vakıf Yükseköğretim Kurumları",
        ["TOPLAM GELİR (TL)"]
    )

    toplam_gider = _read_from_sheet(
        yok,
        "Gelir ve Giderlerine Göre Vakıf Yükseköğretim Kurumları",
        ["TOPLAM GİDER (TL)"]
    )

    toplam_ogretim_elemani_sayisi = _read_from_sheet(
        yok,
        "Öğretim Elemanlarına Ödenen Ücretlerin Toplamına Göre Vakıf Yükseköğretim Kurumları",
        ["TOPLAM ÖĞRETİM ELEMANI SAYISI**"]
    )

    urap_toplam_puan = _read_from_sheet(
        yok,
        "2020-2021 URAP Genel Puan Tablosuna Göre Vakıf Üniversiteleri",
        ["TOPLAM"]
    )

    ogrenci_basina_kutuphane_alani = _read_from_sheet(
        yok,
        "Öğrenci Başına Kütüphane Alanına Göre Vakıf Yükseköğretim Kurumları",
        ["ÖĞRENCİ BAŞINA KÜTÜPHANE ALANI** (m2)"]
    )

    ardeb_destekleri = _read_from_sheet(
        yok,
        "Vakıf Yükseköğretim Kurumlarının 2020 Yılı TÜBİTAK- ARDEB Destek İstatistiklerine Göre Sıralamaları",
        ["YÜRÜRLÜKTEKİ  PROJELERE 2020 YILI  İÇİNDE AKTARILAN  TUTAR-CARİ"]
    )

    ogretim_elemanlarina_odenen_ucretler_toplami = _read_from_sheet(
        yok,
        "Öğretim Elemanlarına Ödenen Ücretlerin Toplamına Göre Vakıf Yükseköğretim Kurumları",
        ["ÖĞRETİM ELEMANLARINA ÖDENEN ÜCRETLER TOPLAMI (TL)"]
    )

    ogretim_elemanlarina_odenen_ucretlerin_toplam_gidere_orani = _read_from_sheet(
        yok,
        "Öğretim Elemanlarına Ödenen Ücretlerin Toplamına Göre Vakıf Yükseköğretim Kurumları",
        ["ÖĞRETİM ELEMANINA ÖDENEN ÜCRETLERİN TOPLAM GİDERE ORANI (%)"]
    )


@dataclass
class Table2020:
    yok = pd.ExcelFile("Yök Raporları/2020.ods")

    toplam_ogrenci_sayisi = _read_from_sheet(
        yok,
        "Öğrenci Sayılarına Göre Vakıf Üniversiteleri",
        ["TOPLAM ÖĞRENCİ SAYISI"]
    )

    kadrolu_ogretim_uyesi_basina_ogrenci_sayisi = _read_from_sheet(
        yok,
        "Kadrolu Öğretim Üyesi Başına Düşen Öğrenci Sayısı",
        ["KADROLU ÖĞRETİM ÜYESİ BAŞINA ÖĞRENCİ SAYISI"]
    )

    doktora_program_sayisi = _read_from_sheet(
        yok,
        "Doktora Programı Başına Düşen Öğrenci Sayısına Göre Vakıf Üniversiteleri",
        ["DOKTORA PROGRAM SAYISI**"]
    )

    ogrenci_basina_kapali_alan = _read_from_sheet(
        yok,
        "Öğrenci Başına Düşen Kapalı Alana Göre Vakıf Yükseköğretim Kurumları",
        ["ÖĞRENCİ BAŞINA KAPALI ALAN**"]
    )

    ogrenci_basina_acik_alan = _read_from_sheet(
        yok,
        "Öğrenci Başına Düşen Açık Alana Göre Vakıf Yükseköğretim Kurumları",
        ["ÖĞRENCİ BAŞINA AÇIK ALAN**"]
    )

    yabanci_uyruklu_ogrencilerin_toplam_ogrenci_icerisindeki_orani = _read_from_sheet(
        yok,
        "Yabancı Uyruklu Öğrenci   Sayısına Göre Vakıf Yükseköğretim Kurumları",
        ["YABANCI UYRUKLU ÖĞRENCİLERİN TOPLAM ÖĞRENCİ İÇERİSİNDEKİ ORANI (%)"]
    )

    toplam_ogrenci_icinde_gelen_ogrenci_orani = _read_from_sheet(
        yok,
        "2019-2020 Eğitim Öğretim Döneminde Yatay Geçiş ile Gelen Öğrenci Sayısına Göre Vakıf Üniversiteleri.",
        ["TOPLAM ÖĞRENCİ İÇERİSİNDE YATAY GEÇİŞ İLE GELEN ÖĞRENCİ ORANI (%)"]
    )

    toplam_ogrenci_icinde_giden_ogrenci_orani = _read_from_sheet(
        yok,
        "2019-2020 Eğitim Öğretim Döneminde Yatay Geçiş ile Giden Öğrenci Sayısına Göre Vakıf Üniversiteleri",
        ["TOPLAM ÖĞRENCİ İÇERİSİNDE YATAY GEÇİŞ İLE GİDEN ÖĞRENCİ ORANI (%)"]
    )

    giden_ogrenci_sayisi = _read_from_sheet(
        yok,
        "2019-2020 Eğitim Öğretim Döneminde Yatay Geçiş ile Giden Öğrenci Sayısına Göre Vakıf Üniversiteleri",
        ["YATAY GEÇİŞ İLE GİDEN ÖĞRENCİ SAYISI"]
    )

    gelen_ogrenci_sayisi = _read_from_sheet(
        yok,
        "2019-2020 Eğitim Öğretim Döneminde Yatay Geçiş ile Gelen Öğrenci Sayısına Göre Vakıf Üniversiteleri.",
        ["YATAY GEÇİŞ İLE GELEN ÖĞRENCİ SAYISI"]
    )

    yurt_disindan_gelen_ogrenci_sayisi = _read_from_sheet(
        yok,
        "2019-2020 Döneminde Yatay Geçiş ile Yurt Dışından Gelen Öğrenci Sayısına Göre Vakıf Üniversiteler",
        ["YURT DIŞINDAN YATAY GEÇİŞ İLE GELEN ÖĞRENCİ SAYISI"]
    )

    doluluk_orani = _read_from_sheet(
        yok,
        "2019 YKS Kontenjanları Doluluk Oranlarına Göre Vakıf Yükseköğretim Kurumları",
        ["DOLULUK ORANI (%)"]
    )

    ogrenci_basi_cari_gider = _read_from_sheet(
        yok,
        "Öğrenci Başına Cari Gider Miktarına Göre Vakıf Üniversiteleri",
        ["ÖĞRENCİ BAŞINA CARİ GİDER** (TL)"]
    )

    burslu_ogrenci_orani = _read_from_sheet(
        yok,
        "YKS Kontenjanları Tam Bursluluk Oranlarına Göre Vakıf Yükseköğretim Kurumları",
        ["TAM BURSLU ÖĞRENCİ ORANI (%)"]
    )

    toplam_arge_harcamalari = _read_from_sheet(
        yok,
        "Toplam Araştırma Proje Bütçelerine Göre Vakıf Üniversiteleri",
        ["TOPLAM ARAŞTIRMA PROJE HARCAMASI** (TL)"]
    )

    reklam_harcamalari = _read_from_sheet(
        yok,
        "Reklam-Tanıtım Harcamalarına Göre Vakıf Yükseköğretim Kurumları",
        ["REKLAM-TANITIM HARCAMASI (TL)"]
    )

    kutuphane_harcamalari = _read_from_sheet(
        yok,
        "Kütüphane Harcamalarına Göre Vakıf Yükseköğretim Kurumları",
        ["KÜTÜPHANEYE YAPILAN HARCAMA (TL)"]
    )

    egitim_ve_ogretim_gelirleri = _read_from_sheet(
        yok,
        "Eğitim-Öğretim Hizmet Geliri ve Öğrencilere Verilen Burs ve Yardım Vakıf Yükseköğretim Kurumları",
        ["EĞİTİM-ÖĞRETİM HİZMET GELİRLERİ** (TL)"]
    )

    ogrencilere_verilen_burslar = _read_from_sheet(
        yok,
        "Eğitim-Öğretim Hizmet Geliri ve Öğrencilere Verilen Burs ve Yardım Vakıf Yükseköğretim Kurumları",
        ["ÖĞRENCİLERE VERİLEN BURS, YARDIM VB. HARCAMALAR TOPLAMI*** (TL)"]
    )

    ogrencilere_verilen_burslarin_egitim_ve_ogretim_gelirlerine_orani = _read_from_sheet(
        yok,
        "Eğitim-Öğretim Hizmet Geliri ve Öğrencilere Verilen Burs ve Yardım Vakıf Yükseköğretim Kurumları",
        ["ÖĞRENCİLERE VERİLEN BURS YARDIM VB. HARCAMALARIN EĞİTİM ÖĞRETİM GELİRİNE ORANI"]
    )

    toplam_gelir = _read_from_sheet(
        yok,
        "Gelir, Gider",
        ["TOPLAM GELİR (SUAM DAHİL, TL)"]
    )

    toplam_gider = _read_from_sheet(
        yok,
        "Gelir, Gider",
        ["TOPLAM GİDER (SUAM DAHİL, TL)"]
    )

    toplam_ogretim_elemani_sayisi = _read_from_sheet(
        yok,
        "Öğretim Elemanlarına Ödenen Ücret Toplamına Göre Vakıf Yükseköğretim Kurumları",
        ["TOPLAM ÖĞRETİM ELEMANI SAYISI"]
    )

    urap_toplam_puan = _read_from_sheet(
        yok,
        "2019-2020 URAP Genel Puan Tablosuna Göre Vakıf Üniversiteleri",
        ["TOPLAM"]
    )
    ardeb_destekleri = _read_from_sheet(
        yok,
        "TÜBİTAK-ARDEB Proje Bütçelerine Göre Vakıf Yükseköğretim Kurumları",
        ["DEVAM EDEN PROJELERE YIL İÇİNDE AKTARILAN TUTAR (MİLYON TL)"]
    )
    ogretim_elemanlarina_odenen_ucretler_toplami = _read_from_sheet(
        yok,
        "Öğretim Elemanlarına Ödenen Ücret Toplamına Göre Vakıf Yükseköğretim Kurumları",
        ["ÖĞRETİM ELEMANLARINA ÖDENEN ÜCRETLER TOPLAMI (TL)"]
    )

    ogretim_elemanlarina_odenen_ucretlerin_toplam_gidere_orani = _read_from_sheet(
        yok,
        "Öğretim Elemanlarına Ödenen Ücret Toplamına Göre Vakıf Yükseköğretim Kurumları",
        ["ÖĞRETİM ELEMANINA ÖDENEN ÜCRETİN TOPLAM GİDERE ORANI (%)"]
    )


@dataclass
class Table2019:
    yok = pd.ExcelFile("Yök Raporları/2019.ods")

    toplam_ogrenci_sayisi = _read_from_sheet(
        yok,
        "Öğrenci  Sayılarına  Göre  Vakıf Üniversiteleri",
        ["TOPLAM ÖĞRENCİ SAYISI"]
    )

    kadrolu_ogretim_uyesi_basina_ogrenci_sayisi = _read_from_sheet(
        yok,
        "Kadrolu Öğretim Üyesi Başına Düşen Öğrenci Sayısına Göre Vakıf Yükseköğretim Kurumları",
        ["KADROLU ÖĞRETİM ÜYESİ BAŞINA ÖĞRENCİ SAYISI"]
    )

    kapali_alan = _read_from_sheet(
        yok,
        "Öğrenci Başına Düşen Alan Dağılımına Göre Vakıf Yükseköğretim Kurumları",
        ["KAPALI ALAN (m²)"]
    )

    acik_alan = _read_from_sheet(
        yok,
        "Öğrenci Başına Düşen Alan Dağılımına Göre Vakıf Yükseköğretim Kurumları",
        ["AÇIK ALAN (m²)"]
    )
    yabanci_uyruklu_ogrencilerin_toplam_ogrenci_icerisindeki_orani = _read_from_sheet(
        yok,
        "Yabancı Uyruklu Öğrenci Sayısına Göre Vakıf Yükseköğretim Kurumları",
        ["YABANCI UYRUKLU ÖĞRENCİLERİN TOPLAM ÖĞRENCİ İÇERİSİNDEKİ ORANI (%)"]
    )

    toplam_ogrenci_icinde_gelen_ogrenci_orani = _read_from_sheet(
        yok,
        "2018-2019 Döneminde Yatay Geçiş ile Gelen Öğrenci Sayısına Göre Vakıf Yükseköğretim Kurumları",
        ["TOPLAM ÖĞRENCİ İÇERİSİNDE YATAY GEÇİŞ İLE GELEN ÖĞRENCİ ORANI (%)"]
    )

    toplam_ogrenci_icinde_giden_ogrenci_orani = _read_from_sheet(
        yok,
        "2018-2019 Döneminde Yatay Geçiş ile Giden Öğrenci Sayısına Göre Vakıf Yükseköğretim Kurumları",
        ["TOPLAM ÖĞRENCİ İÇERİSİNDE YATAY GEÇİŞ İLE GİDEN ÖĞRENCİ ORANI (%)"]
    )

    giden_ogrenci_sayisi = _read_from_sheet(
        yok,
        "2018-2019 Döneminde Yatay Geçiş ile Giden Öğrenci Sayısına Göre Vakıf Yükseköğretim Kurumları",
        ["YATAY GEÇİŞ İLE GİDEN ÖĞRENCİ SAYISI"]
    )

    gelen_ogrenci_sayisi = _read_from_sheet(
        yok,
        "2018-2019 Döneminde Yatay Geçiş ile Gelen Öğrenci Sayısına Göre Vakıf Yükseköğretim Kurumları",
        ["YATAY GEŞİŞ İLE GELEN ÖĞRENCİ SAYISI"]
    )

    ogrenci_basi_cari_gider = _read_from_sheet(
        yok,
        "Öğrenci Başına Cari Gider Miktarına Göre Vakıf Yükseköğretim Kurumları",
        ["ÖĞRENCİ BAŞINA CARİ GİDER** (TL)"]
    )

    burslu_ogrenci_orani = _read_from_sheet(
        yok,
        "YKS Kontenjanları Tam Bursluluk Oranlarına Göre Vakıf Yükseköğretim Kurumları",
        ["TAM BURSLU ÖĞRENCİ ORANI (%)"]
    )

    toplam_arge_harcamalari = _read_from_sheet(
        yok,
        "Toplam Araştırma Proje Bütçelerine Göre Vakıf Yükseköğretim Kurumları",
        ["TOPLAM ARAŞTIRMA PROJELERİ BÜTÇESİ (TL)"]
    )

    reklam_harcamalari = _read_from_sheet(
        yok,
        "Reklam-Tanıtım Harcamalarına Göre Vakıf Yükseköğretim Kurumları",
        ["REKLAM-TANITIM HARCAMASI (TL)"]
    )

    kutuphane_harcamalari = _read_from_sheet(
        yok,
        "Kütüphane Harcamalarına Göre Vakıf Yükseköğretim Kurumları",
        ["KÜTÜPHANEYE YAPILAN HARCAMA (TL)"]
    )

    urap_toplam_puan = _read_from_sheet(
        yok,
        "2018-2019 URAP  Genel  Puan Tablosuna Göre Vakıf Üniversiteleri",
        ["TOPLAM"]
    )

    ardeb_destekleri = _read_from_sheet(
        yok,
        "TÜBİTAK-ARDEB Proje Bütçelerine Göre Vakıf Yükseköğretim Kurumları ",
        ["DEVAM EDEN PROJELERE YIL İÇİNDE AKTARILAN TUTAR (MİLYON TL)**"]
    )


@dataclass
class Table2018:
    yok = pd.ExcelFile("Yök Raporları/2018.ods")

    toplam_ogrenci_sayisi = _read_from_sheet(
        yok,
        "Vakıf Üniversiteleri Öğrenci Sayıları",
        ["TOPLAM ÖĞRENCİ SAYISI"]
    )

    kapali_alan = _read_from_sheet(
        yok,
        "Vakıf Yükseköğretim Kurumlarının Öğrenci Başına Düşen Alan Dağılımı",
        ["KAPALI ALAN (m²)"]
    )

    acik_alan = _read_from_sheet(
        yok,
        "Vakıf Yükseköğretim Kurumlarının Öğrenci Başına Düşen Alan Dağılımı",
        ["AÇIK ALAN (m²)"]
    )

    ogrenci_basi_cari_gider = _read_from_sheet(
        yok,
        "Vakıf Yükseköğretim Kurumlarında Öğrenci Başına Cari Gider Miktarı",
        ["ÖĞRENCİ BAŞINA CARİ GİDER** (TL)"]
    )

    burslu_ogrenci_orani = _read_from_sheet(
        yok,
        "Vakıf Yükseköğretim Kurumlarının Tam Bursluluk Oranı",
        ["TAM BURSLU ÖĞRENCİ ORANI %"]
    )

    urap_toplam_puan = _read_from_sheet(
        yok,
        "Vakıf Üniversiteleri 2017-2018 URAP Genel Puan Tablosu",
        ["TOPLAM"]
    )

    ogrenci_basina_kutuphane_alani = _read_from_sheet(
        yok,
        "Vakıf Yükseköğretim Kurumlarının Öğrenci Başına Düşen Kütüphane Alanı",
        ["ÖĞRENCİ BAŞINA DÜŞEN KÜTÜPHANE ALANI (m²)"]
    )

    ardeb_destekleri = _read_from_sheet(
        yok,
        "Vakıf Üniversitelerinin TÜBİTAK- ARDEB Proje Bütçeleri (2017)",
        ["PROJELERE YIL İÇİNDE AKTARILAN TUTAR (MİLYON TL)**"]
    )
