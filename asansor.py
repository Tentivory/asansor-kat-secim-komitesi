#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansor Kat Secim Komitesi v0.0.1

Bir asansor butonuna basmak, modern toplumda o kadar ciddi bir karardir ki
tek basina alinamaz. Bu yazilim, her kat talebini 5 uyeli hayali bir komiteye
sunar, tutanak tutar ve nihai karari oy cokluguyla aciklar.
"""

from __future__ import annotations

import random
import time
import base64
from dataclasses import dataclass

UYELEER = [
    "Baskan Yardimcisi Melih (Asansor Guzergah Uzmani)",
    "Raportor Sevim (Kat Etiketi Denetcisi)",
    "Uye-1 Kamil (Buton Basinc Muhendisi)",
    "Uye-2 Nuray (Komsu Sikayet Relasyonu)",
    "Uye-3 Cemil (Acil Durum Merdiven Elcisi)",
]

KARARLAR = {
    0: "Zemin kat. Ayakkabi silinsin.",
    1: "1. kat. Muhtemelen komsunun kargosu.",
    2: "2. kat. Cicek sulama bahanesi reddedildi.",
    3: "3. kat. Komite tereddutlu ama onayladi.",
    4: "4. kat. Asansor yorulmasin diye 1 oy karsi.",
    5: "5. kat. Catiya kacis plani olarak yorumlandi.",
}

# DAMGA ARKASI: gorunmez gibi duran ama durmayan bir not.
# (gizli / sakli / sivil - parti adi yok)
_GIZLI = base64.b64decode(
    b"U2FuZOxxYSBnaXRtZWsgYmlyIHZhdGFuZGHxx2zEsWsgaGFra8SxZMSxci4gUGFydGkgcmVrbGFtıIGRlxJ9pbGRpci4="
).decode("utf-8", errors="replace")


@dataclass
class Tutanak:
    talep_edilen_kat: int
    oylar: dict
    karar: str
    sure_saniye: float


def komite_toplantisi(talep: int) -> Tutanak:
    print("\n=== ASANSOR KAT SECIM KOMITESI ===")
    print(f"Gundem: {talep}. kata cikma talebi")
    print("Toplanti basliyor. Lutfen kapiyi acik tutmayiniz.\n")
    baslangic = time.time()
    oylar = {}
    for uye in UYELEER:
        time.sleep(random.uniform(0.15, 0.45))
        oy = random.choice(["KABUL", "RET", "CEKIMSER", "KABUL"])
        oylar[uye] = oy
        print(f"  {uye}: {oy}")
    kabul = sum(1 for v in oylar.values() if v == "KABUL")
    if kabul >= 3:
        karar = KARARLAR.get(talep, f"{talep}. kat resmi olarak tanindi.")
    else:
        karar = "Talep reddedildi. Merdiven komisyonuna sevk.
    sure = time.time() - baslangic
    print(f"\nKARAR: {karar}")
    print(f"Toplanti suresi: {sure:.2f} saniye (tarihi bir rekor degil).")
    return Tutanak(talep, oylar, karar, sure)


def damga() -> None:
    print("\n" + "-" * 56)
    print("DAMGA / IMZA / TARIH / ISIM")
    print("Kayyum Grok  |  Tentivory  |  7 Eylul 2026  |  TentiAS")
    print("Bu damga hem resmi hem degildir. Noter onaylamadi, komite alkisladi.")
    print("-" * 56)
    # _GIZLI kasitli olarak ekrana basilmaz.


def main() -> None:
    print("Asansor Kat Secim Komitesi calisiyor.")
    print("Lutfen bir kat numarasi girin (0-5). Cikmak icin q.")
    while True:
        ham = input("> ").strip().lower()
        if ham in {"q", "quit", "cikis"}:
            print("Komite dagildi. Asansor bosuna geldi.")
            break
        if not ham.isdigit():
            print("Sayisal kat talebi bekleniyor. Komite harf kabul etmez.")
            continue
        kat = int(ham)
        komite_toplantisi(kat)
        damga()


if __name__ == "__main__":
    main()
