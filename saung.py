import streamlit as st
import pandas as pd

# Definisikan menu dengan harga per satuan dan harga per kilogram
menu_satuan = {
    "Nasi Goreng": {"price": 20000, "image": "nasi_goreng.jpg"},
    "Mie Goreng": {"price": 15000, "image": "mie_goreng.jpg"},
    "Ayam Penyet": {"price": 25000, "image": "ayam_penyet.jpg"},
    "Es Teh": {"price": 5000, "image": "es_teh.jpg"},
    "Kopi": {"price": 10000, "image": "kopi.jpg"},
    "Jus Mangga": {"price": 8000, "image": "jus_mangga.jpg"}
}

menu_ikan = {
    "Ikan Salmon": 150000,  # harga per kg
    "Ikan Tuna": 120000,
    "Ikan Gurame": 80000,
    "Ikan Lele": 60000
}

# Judul aplikasi
st.title("Aplikasi Kasir Saung Bukit Cikuasa")

# Inisialisasi keranjang belanja
order_items = []

# Menampilkan menu makanan dengan harga per satuan
st.header("Menu Makanan")
st.write("Pilih item dan masukkan jumlah yang diinginkan:")

columns = st.columns(2)  # Membuat 2 kolom untuk menu makanan

for index, (item, details) in enumerate(menu_satuan.items()):
    with columns[index % 2]:  # Menggunakan modulus untuk mengatur kolom
        st.image(details["image"], caption=item, width=100)  # Menampilkan gambar
        st.write(f"**{item}**")
        st.write(f"Rp {details['price']}")
        qty = st.number_input(f"Jumlah {item}", min_value=0, value=0, key=item)
        if qty > 0:
            total_harga = qty * details["price"]
            order_items.append((item, qty, details["price"], total_harga))

# Menampilkan menu ikan dengan harga per kilogram
st.header("Menu Ikan")
st.write("Masukkan berat ikan yang diinginkan (dalam kg):")

for ikan, harga_per_kg in menu_ikan.items():
    berat = st.number_input(f"Berat {ikan} (kg)", min_value=0.0, value=0.0, step=0.1, key=ikan)
    if berat > 0:
        total_harga = berat * harga_per_kg
        order_items.append((ikan, berat, harga_per_kg, total_harga))

# Menampilkan keranjang belanja dalam bentuk tabel
st.header("Keranjang Belanja")
if order_items:
    # Membuat DataFrame dari order_items
    df_order = pd.DataFrame(order_items, columns=["Nama Menu", "Jumlah/Berat", "Harga Satuan", "Total Harga"])
    
    # Menampilkan tabel
    st.table(df_order)

    # Menghitung total keseluruhan
    total = df_order["Total Harga"].sum()
    st.write(f"Total Keseluruhan: Rp {total}")

    # Fitur pembayaran
    if st.button("Bayar"):
        st.success("Pembayaran berhasil!")
        order_items.clear()  # Mengosongkan keranjang setelah pembayaran
else:
    st.write("Keranjang kosong")
