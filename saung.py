import streamlit as st
import pandas as pd

# Definisikan menu dengan gambar
menu = {
    "Nasi Goreng": {"price": 20000, "image": "nasi_goreng.jpg"},
    "Mie Goreng": {"price": 15000, "image": "mie_goreng.jpg"},
    "Ayam Penyet": {"price": 25000, "image": "ayam_penyet.jpg"},
    "Es Teh": {"price": 5000, "image": "es_teh.jpg"},
    "Kopi": {"price": 10000, "image": "kopi.jpg"},
    "Jus Mangga": {"price": 8000, "image": "jus_mangga.jpg"}
}

# Judul aplikasi
st.title("Aplikasi Kasir Restoran")

# Inisialisasi keranjang belanja
order_items = []

# Menampilkan menu dengan layout samping-sampingan
st.header("Menu")
st.write("Pilih item dan masukkan jumlah yang diinginkan:")

# Membuat kolom untuk setiap item menu
columns = st.columns(2)  # Membuat 2 kolom

for index, (item, details) in enumerate(menu.items()):
    with columns[index % 2]:  # Menggunakan modulus untuk mengatur kolom
        st.image(details["image"], caption=item, width=100)  # Menampilkan gambar
        st.write(f"**{item}**")
        st.write(f"Rp {details['price']}")
        qty = st.number_input(f"Jumlah {item}", min_value=0, value=0, key=item)
        if qty > 0:
            order_items.append((item, qty, details["price"]))

# Menampilkan keranjang belanja dalam bentuk tabel
st.header("Keranjang Belanja")
if order_items:
    # Membuat DataFrame dari order_items
    df_order = pd.DataFrame(order_items, columns=["Nama Menu", "Jumlah", "Harga Satuan"])
    df_order["Total Harga"] = df_order["Jumlah"] * df_order["Harga Satuan"]  # Menghitung total harga per item
    
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