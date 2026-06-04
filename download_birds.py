#!/usr/bin/env python3
"""
Download all 30 bird images for projectlovebirds
Run this in your projectlovebirds directory
"""

import os
import urllib.request
from pathlib import Path

# Create images directory
Path("images").mkdir(exist_ok=True)

# All 30 bird image URLs
urls = [
    ("bird-1.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Atlantic_puffin_in_flight_-_Reykjavik%2C_Iceland.jpg/480px-Atlantic_puffin_in_flight_-_Reykjavik%2C_Iceland.jpg"),
    ("bird-2.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Resplendent_Quetzal_-_male_%2836516655281%29.jpg/480px-Resplendent_Quetzal_-_male_%2836516655281%29.jpg"),
    ("bird-3.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Shoebill_Balaeniceps_rex_in_Swamp.jpg/480px-Shoebill_Balaeniceps_rex_in_Swamp.jpg"),
    ("bird-4.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Lophorina_superba_-_Superb_Bird-of-paradise_1.jpg/480px-Lophorina_superba_-_Superb_Bird-of-paradise_1.jpg"),
    ("bird-5.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Harpia_harpyja_-Belize_Zoo-8a.jpg/480px-Harpia_harpyja_-Belize_Zoo-8a.jpg"),
    ("bird-6.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Flamingos_Laguna_Colorada.jpg/480px-Flamingos_Laguna_Colorada.jpg"),
    ("bird-7.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Falco_peregrinus_-_01.jpg/480px-Falco_peregrinus_-_01.jpg"),
    ("bird-8.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Keel-billed_Toucan_Ramphastos_sulfuratus_2500px.jpg/480px-Keel-billed_Toucan_Ramphastos_sulfuratus_2500px.jpg"),
    ("bird-9.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Andean_condor_%28Vultur_gryphus%29.jpg/480px-Andean_condor_%28Vultur_gryphus%29.jpg"),
    ("bird-10.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Snowy_Owl_%28240866707%29.jpg/480px-Snowy_Owl_%28240866707%29.jpg"),
    ("bird-11.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Goura_victoria_-_Artis_-_001.jpg/480px-Goura_victoria_-_Artis_-_001.jpg"),
    ("bird-12.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Mandarin.duck.arp.jpg/480px-Mandarin.duck.arp.jpg"),
    ("bird-13.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Secretarybird_Nxai_pan.jpg/480px-Secretarybird_Nxai_pan.jpg"),
    ("bird-14.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Painted_bunting_%28Passerina_ciris%29_male.jpg/480px-Painted_bunting_%28Passerina_ciris%29_male.jpg"),
    ("bird-15.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Kakapo_on_Codfish_Island.jpg/480px-Kakapo_on_Codfish_Island.jpg"),
    ("bird-16.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Bearded_Vulture_at_Gamla.jpg/480px-Bearded_Vulture_at_Gamla.jpg"),
    ("bird-17.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Hoatzin_-_Cuyabeno_-_Ecuador.jpg/480px-Hoatzin_-_Cuyabeno_-_Ecuador.jpg"),
    ("bird-18.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Pithecophaga_jefferyi_1.jpg/480px-Pithecophaga_jefferyi_1.jpg"),
    ("bird-19.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Lyrebird_superb.jpg/480px-Lyrebird_superb.jpg"),
    ("bird-20.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Diomedea_exulans_in_flight_-_SE_Tasmania.jpg/480px-Diomedea_exulans_in_flight_-_SE_Tasmania.jpg"),
    ("bird-21.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Blue-footed_booby_-_Galapagos_%2827456523946%29.jpg/480px-Blue-footed_booby_-_Galapagos_%2827456523946%29.jpg"),
    ("bird-22.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Hoopoe_2.jpg/480px-Hoopoe_2.jpg"),
    ("bird-23.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/King_Penguin_%28Aptenodytes_patagonicus%29_in_South_Georgia.jpg/480px-King_Penguin_%28Aptenodytes_patagonicus%29_in_South_Georgia.jpg"),
    ("bird-24.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Sword-billed_Hummingbird_Ensifera_ensifera.jpg/480px-Sword-billed_Hummingbird_Ensifera_ensifera.jpg"),
    ("bird-25.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/ToucanFromTheFront.jpg/480px-ToucanFromTheFront.jpg"),
    ("bird-26.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Ribbon-tailed_Astrapia_%28Astrapia_mayeri%29_male.jpg/480px-Ribbon-tailed_Astrapia_%28Astrapia_mayeri%29_male.jpg"),
    ("bird-27.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Emu_-_Dromaius_novaehollandiae_%286821554185%29.jpg/480px-Emu_-_Dromaius_novaehollandiae_%286821554185%29.jpg"),
    ("bird-28.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Ara_macao_-Sinheriting_the_Earth%2C_Jaco%2C_Costa_Rica-8.jpg/480px-Ara_macao_-Sinheriting_the_Earth%2C_Jaco%2C_Costa_Rica-8.jpg"),
    ("bird-29.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Fregata_magnificens_-Galapagos%2C_Ecuador_-male-8.jpg/480px-Fregata_magnificens_-Galapagos%2C_Ecuador_-male-8.jpg"),
    ("bird-30.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Snowy_Owl_%28240866707%29.jpg/480px-Snowy_Owl_%28240866707%29.jpg"),
]

print("Downloading 30 bird images...\n")

for filename, url in urls:
    filepath = f"images/{filename}"
    try:
        print(f"Downloading {filename}...", end=" ")
        urllib.request.urlretrieve(url, filepath)
        print("✓")
    except Exception as e:
        print(f"✗ Failed: {e}")

print("\n✓ Done! All images are in the 'images/' folder.")
