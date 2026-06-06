import time

def kata_manis_awal():
    print("=" * 80)
    print("     ✨ WELCOME TO HEALTHY LIFE APP BY KELOMPOK CANGGIH ✨     ")
    print("=" * 80)
    print("Halo! Terima kasih sudah peduli sama kesehatan tubuhmu.")
    print("Panduan ini dibuat agar kamu bisa memasak hidangan sehat dengan presisi.")
    print("Semangat ya, investasi terbaik adalah tubuh yang sehat! ❤️")
    print("-" * 80)
    time.sleep(1)

def tips_diet():
    print("\n💡 TIPS SUKSES DIET:")
    print("1. Minum air putih 2 gelas sebelum makan.")
    print("2. Hindari gorengan dan minuman manis.")
    print("3. Tidur cukup 7-8 jam per hari.")
    print("\n🌟 REKOMENDASI TERBAIK:\n- Dada ayam, ikan, brokoli, dan ubi jalar.")
    print("\n🔥 KATA SEMANGAT:\n'Jangan bandingkan progressmu dengan orang lain. Fokus pada versi terbaik dirimu hari ini!'")

def tips_bulking():
    print("\n💡 TIPS SUKSES BULKING:")
    print("1. Makan surplus kalori (lebih dari kebutuhan harian).")
    print("2. Konsisten latihan beban (hypertrophy).")
    print("3. Jangan takut makan karbohidrat kompleks.")
    print("\n🌟 REKOMENDASI TERBAIK:\n- Daging sapi, telur, susu gainer, dan kacang-kacangan.")
    print("\n🔥 KATA SEMANGAT:\n'Otot tidak dibangun dalam sehari. Konsistensi adalah kunci dari tubuh yang tangguh!'")

menu_diet_db = {
    "1": {"nama": "Oatmeal Mangga Spesial", "kalori": "320 Kcal", "cara": "PERSIAPAN:\n- Alat: Panci, spatula, mangkuk\n- Bahan: 40g oatmeal, 200ml susu almond, 1 mangga\n\nLANGKAH MEMASAK:\n1. Rebus susu hingga berbuih kecil\n2. Masukkan oatmeal, aduk 5 menit hingga kental\n3. Tuang ke mangkuk\n4. Potong mangga dadu, tata di atasnya"},
    "2": {"nama": "Dada Ayam Panggang", "kalori": "410 Kcal", "cara": "PERSIAPAN:\n- Alat: Teflon, pisau\n- Bahan: 150g dada ayam, lada, garam, olive oil\n\nLANGKAH MEMASAK:\n1. Marinasi ayam dengan lada & garam\n2. Panaskan teflon dengan olive oil\n3. Panggang 6 menit tiap sisi hingga cokelat\n4. Sajikan dengan sayuran rebus"},
    "3": {"nama": "Salad Telur Rebus", "kalori": "250 Kcal", "cara": "PERSIAPAN:\n- Alat: Panci, mangkuk\n- Bahan: 2 telur, selada, tomat, jeruk nipis\n\nLANGKAH MEMASAK:\n1. Rebus telur 9 menit\n2. Cuci selada & tomat, potong-potong\n3. Kupas telur, belah dua\n4. Campur semua, beri perasan jeruk"},
    "4": {"nama": "Smoothie Alpukat", "kalori": "290 Kcal", "cara": "PERSIAPAN:\n- Alat: Blender\n- Bahan: 1/2 alpukat, bayam, 150ml air\n\nLANGKAH MEMASAK:\n1. Masukkan alpukat & bayam ke blender\n2. Tambahkan air\n3. Blender hingga halus\n4. Tuang ke gelas"},
    "5": {"nama": "Salmon Panggang", "kalori": "430 Kcal", "cara": "PERSIAPAN:\n- Alat: Teflon\n- Bahan: 1 slice salmon, jeruk nipis, lada\n\nLANGKAH MEMASAK:\n1. Lumuri salmon dengan jeruk\n2. Tabur lada\n3. Panggang 5 menit per sisi\n4. Sajikan dengan kentang rebus"},
    "6": {"nama": "Tumis Tahu Tempe", "kalori": "280 Kcal", "cara": "PERSIAPAN:\n- Alat: Wajan\n- Bahan: 100g tahu, 100g tempe, bawang, kecap\n\nLANGKAH MEMASAK:\n1. Potong tahu tempe\n2. Tumis bawang hingga harum\n3. Masukkan tahu tempe, beri kecap\n4. Aduk hingga matang"},
    "7": {"nama": "Sup Ayam Bening", "kalori": "310 Kcal", "cara": "PERSIAPAN:\n- Alat: Panci\n- Bahan: 100g ayam, wortel, kentang\n\nLANGKAH MEMASAK:\n1. Rebus ayam hingga kaldu keluar\n2. Masukkan wortel & kentang\n3. Masak hingga empuk\n4. Tambahkan seledri"},
    "8": {"nama": "Pepes Ikan Mas", "kalori": "260 Kcal", "cara": "PERSIAPAN:\n- Alat: Pengukus, daun pisang\n- Bahan: 1 ikan mas, bumbu kuning\n\nLANGKAH MEMASAK:\n1. Lumuri ikan dengan bumbu\n2. Bungkus daun pisang\n3. Kukus 40 menit\n4. Sajikan hangat"},
    "9": {"nama": "Orak-arik Putih Telur", "kalori": "240 Kcal", "cara": "PERSIAPAN:\n- Alat: Teflon\n- Bahan: 3 putih telur, daun bawang\n\nLANGKAH MEMASAK:\n1. Masukkan putih telur ke teflon\n2. Orak-arik dengan daun bawang\n3. Masak hingga padat\n4. Sajikan dengan roti gandum"},
    "10": {"nama": "Greek Yogurt Berry", "kalori": "190 Kcal", "cara": "PERSIAPAN:\n- Alat: Mangkuk\n- Bahan: 1 cup greek yogurt, buah beri\n\nLANGKAH MEMASAK:\n1. Tuang yogurt ke mangkuk\n2. Cuci beri\n3. Potong kecil buah\n4. Campur dan aduk rata"},
    "11": {"nama": "Tumis Buncis Daging", "kalori": "270 Kcal", "cara": "PERSIAPAN:\n- Alat: Wajan\n- Bahan: 100g buncis, 50g daging iris\n\nLANGKAH MEMASAK:\n1. Tumis daging hingga berubah warna\n2. Masukkan buncis\n3. Beri saus tiram\n4. Aduk hingga layu"},
    "12": {"nama": "Capcay Kuah", "kalori": "200 Kcal", "cara": "PERSIAPAN:\n- Alat: Panci\n- Bahan: Brokoli, wortel, kembang kol\n\nLANGKAH MEMASAK:\n1. Rebus air, masukkan sayuran\n2. Masak hingga empuk\n3. Beri lada & garam\n4. Sajikan hangat"},
    "13": {"nama": "Ikan Kembung Bakar", "kalori": "350 Kcal", "cara": "PERSIAPAN:\n- Alat: Teflon\n- Bahan: 1 ikan kembung, kecap\n\nLANGKAH MEMASAK:\n1. Bersihkan ikan\n2. Olesi kecap\n3. Bakar hingga matang\n4. Sajikan dengan lalapan"},
    "14": {"nama": "Sup Jamur Kancing", "kalori": "150 Kcal", "cara": "PERSIAPAN:\n- Alat: Panci\n- Bahan: 100g jamur, kaldu ayam\n\nLANGKAH MEMASAK:\n1. Tumis bawang bombay\n2. Masukkan jamur\n3. Tuang kaldu, didihkan\n4. Beri seledri"},
    "15": {"nama": "Sate Dada Ayam", "kalori": "300 Kcal", "cara": "PERSIAPAN:\n- Alat: Tusuk sate, teflon\n- Bahan: Dada ayam, kecap\n\nLANGKAH MEMASAK:\n1. Potong ayam kotak\n2. Tusuk ayam\n3. Bakar di teflon\n4. Sajikan dengan kecap"},
    "16": {"nama": "Urap Sayur", "kalori": "180 Kcal", "cara": "PERSIAPAN:\n- Alat: Kukusan\n- Bahan: Bayam, tauge, kelapa parut\n\nLANGKAH MEMASAK:\n1. Rebus sayur\n2. Sangrai kelapa dengan bumbu\n3. Campur sayur\n4. Sajikan"},
    "17": {"nama": "Udang Rebus Jahe", "kalori": "220 Kcal", "cara": "PERSIAPAN:\n- Alat: Panci\n- Bahan: 100g udang, jahe\n\nLANGKAH MEMASAK:\n1. Rebus air & jahe\n2. Masukkan udang\n3. Masak hingga berubah warna\n4. Sajikan"},
    "18": {"nama": "Oatmeal Cokelat", "kalori": "300 Kcal", "cara": "PERSIAPAN:\n- Alat: Panci\n- Bahan: 40g oatmeal, cocoa powder\n\nLANGKAH MEMASAK:\n1. Masak oatmeal dengan air\n2. Masukkan bubuk cokelat\n3. Aduk rata\n4. Sajikan hangat"},
    "19": {"nama": "Salad Tuna", "kalori": "280 Kcal", "cara": "PERSIAPAN:\n- Alat: Mangkuk\n- Bahan: 1 kaleng tuna, selada\n\nLANGKAH MEMASAK:\n1. Tiriskan tuna\n2. Potong selada\n3. Campur keduanya\n4. Beri perasan lemon"},
    "20": {"nama": "Brokoli Kukus", "kalori": "120 Kcal", "cara": "PERSIAPAN:\n- Alat: Kukusan\n- Bahan: 1 brokoli, bawang putih\n\nLANGKAH MEMASAK:\n1. Kukus brokoli 5 menit\n2. Tumis bawang putih\n3. Siram bawang ke brokoli\n4. Sajikan"}
}

menu_bulking_db = {
    "1": {"nama": "Roti Gandum Selai Kacang", "kalori": "650 Kcal", "cara": "PERSIAPAN:\n- Alat: Pisau oles, teflon\n- Bahan: 2 roti gandum, selai kacang, 3 telur\n\nLANGKAH MEMASAK:\n1. Oles selai pada roti\n2. Masak 3 telur mata sapi\n3. Sajikan telur di samping roti\n4. Siap disantap"},
    "2": {"nama": "Semur Daging Sapi", "kalori": "780 Kcal", "cara": "PERSIAPAN:\n- Alat: Panci, wajan\n- Bahan: 150g daging, kecap, nasi\n\nLANGKAH MEMASAK:\n1. Tumis daging\n2. Masukkan kecap & air\n3. Masak hingga empuk\n4. Sajikan dengan 2 centong nasi"},
    "3": {"nama": "Susu Gainer & Pisang", "kalori": "580 Kcal", "cara": "PERSIAPAN:\n- Alat: Shaker, piring\n- Bahan: 3 scoop gainer, 2 pisang\n\nLANGKAH MEMASAK:\n1. Kocok gainer dengan air\n2. Siapkan pisang\n3. Makan pisang\n4. Minum susu gainer"},
    "4": {"nama": "Ayam Goreng & Mash Potato", "kalori": "690 Kcal", "cara": "PERSIAPAN:\n- Alat: Teflon, panci\n- Bahan: 150g ayam, tepung, kentang\n\nLANGKAH MEMASAK:\n1. Goreng ayam tepung\n2. Rebus & hancurkan kentang\n3. Campur kentang dengan susu/mentega\n4. Sajikan"},
    "5": {"nama": "Nasi Goreng Gila", "kalori": "820 Kcal", "cara": "PERSIAPAN:\n- Alat: Wajan\n- Bahan: Nasi, sosis, bakso, 2 telur\n\nLANGKAH MEMASAK:\n1. Tumis sosis & bakso\n2. Masukkan nasi & kecap\n3. Buat telur dadar\n4. Sajikan"},
    "6": {"nama": "Sate Ayam & Lontong", "kalori": "670 Kcal", "cara": "PERSIAPAN:\n- Alat: Panggangan\n- Bahan: Ayam, lontong, bumbu kacang\n\nLANGKAH MEMASAK:\n1. Bakar sate ayam\n2. Potong lontong\n3. Siram bumbu kacang\n4. Sajikan"},
    "7": {"nama": "Spaghetti Bolognese", "kalori": "710 Kcal", "cara": "PERSIAPAN:\n- Alat: Panci, wajan\n- Bahan: Spaghetti, daging cincang\n\nLANGKAH MEMASAK:\n1. Rebus spaghetti\n2. Tumis daging\n3. Campur saus bolognese\n4. Sajikan"},
    "8": {"nama": "Sup Buntut Sapi", "kalori": "740 Kcal", "cara": "PERSIAPAN:\n- Alat: Presto, panci\n- Bahan: Buntut sapi, wortel, nasi\n\nLANGKAH MEMASAK:\n1. Presto buntut\n2. Masukkan sayur\n3. Beri bumbu sup\n4. Sajikan dengan nasi"},
    "9": {"nama": "Omelet Makaroni Keju", "kalori": "620 Kcal", "cara": "PERSIAPAN:\n- Alat: Teflon\n- Bahan: Makaroni, 3 telur, keju\n\nLANGKAH MEMASAK:\n1. Rebus makaroni\n2. Kocok telur & keju\n3. Goreng di teflon\n4. Sajikan"},
    "10": {"nama": "Jus Alpukat Jumbo", "kalori": "530 Kcal", "cara": "PERSIAPAN:\n- Alat: Blender\n- Bahan: 2 alpukat, susu cokelat\n\nLANGKAH MEMASAK:\n1. Blender alpukat & susu\n2. Hias gelas dengan cokelat\n3. Tuang jus\n4. Siap minum"}
}

def tampilkan_detail(db, pilihan, tipe):
    if pilihan in db:
        print("\n" + "✨" * 60)
        print(f"📋 MENU: {db[pilihan]['nama']}")
        print(f"🔥 KALORI: {db[pilihan]['kalori']}")
        print(f"\n🍳 CARA MEMBUAT DETAIL:")
        print(f"{db[pilihan]['cara']}")
        print("✨" * 60)
        if tipe == "diet": tips_diet()
        else: tips_bulking()
    else:
        print("\nMaaf, pilihan tidak ada.")

def proses_kategori(tipe, db):
    print(f"\n--- [ DAFTAR MENU {tipe.upper()} ] ---")
    for k, v in db.items(): print(f"[{k}] {v['nama']}")
    pilihan = input("\nPilih nomor menu: ").strip()
    tampilkan_detail(db, pilihan, tipe)

def main():
    kata_manis_awal()
    print("1. Menurunkan berat badan (Diet)")
    print("2. Meningkatkan massa otot (Bulking)")
    kegiatan = input("\nPilihanmu (1 atau 2): ").strip()
    if kegiatan == "1": proses_kategori("diet", menu_diet_db)
    elif kegiatan == "2": proses_kategori("bulking", menu_bulking_db)

if __name__ == "__main__":
    main()
