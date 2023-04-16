# Super-Cashier-Project
Sistem kasih self-service yang mana customer bisa langsung memasukkan item yang dibeli, jumlah item yang dibeli, harga item yang dibeli dan fitur yang lain

# Requirements
1. Pengguna harus dapat memilih produk yang ingin dibeli dan menempatkan produk tersebut ke dalam keranjang belanja secara mandiri.
2. Pengguna harus dapat melakukan operasi delete dan update pada data item dalam keranjang belanja.
3. Program harus dapat menghitung total harga pembelian dari produk yang dipilih dan perolehan diskon untuk total belanja tertentu.
4. Program dapat mengecek kesalahan input (invalid)
5. Program harus memiliki antarmuka pengguna yang mudah dipahami dan digunakan oleh pengguna tanpa bantuan dari kasir.
6. Program harus dapat berjalan dengan stabil dan efisien, tanpa terjadi kesalahan atau kerusakan yang mengganggu proses transaksi.

# Alur Program
1. Program akan memulai dengan menampilkan pesan "Selamat datang di Self-Service Kasir"
2. Pengguna akan diminta untuk memasukkan nama, jumlah, dan harga item yang akan dibeli lalu akan dimasukkan ke dalam keranjang belanja.
3. Setelah itu, program akan menampilkan keranjang belanja item yang akan dibeli beserta total harga belanjaan sejauh ini.
4. Jika pengguna ingin menghapus atau mengubah item yang telah ditambahkan, pengguna dapat memilih opsi "Update" atau "Hapus" dan memasukkan nama, jumlah, dan harga item yang baru.
5. Pengguna keluar dari program dengan memasukkan kode '0'.
6. Jika sudah yakin dengan belanjaan yang ingin dibeli, pengguna dapat memilih menu "Bayar". program akan menampilkan list item pada keranjang belanja serta total harga keseluruhan.
7. Setelah selesai, program akan menampilkan pesan "Terima kasih telah menggunakan program ini".

# Hasil Test Case
1. Transaksi input item

    ![image](https://user-images.githubusercontent.com/91892470/232286741-a304058f-ef4e-4cd6-9dbe-bcb370daa980.png)

2. Mengupdate item

    ![image](https://user-images.githubusercontent.com/91892470/232286458-a32a6d3a-94f2-4e86-beff-0d29ac54ad4e.png)

3. Menghapus item

    a. Menghapus salah satu item
    
      ![image](https://user-images.githubusercontent.com/91892470/232287014-af6fd8f6-c3f6-4d40-9ecf-14be9d704c74.png)
      
       

    b. Menghapus semua item

      ![image](https://user-images.githubusercontent.com/91892470/232286511-9e5fa1e3-b38e-4d79-8b09-c112a79985c2.png)
      

4. Pembayaran

    ![image](https://user-images.githubusercontent.com/91892470/232288108-9b7a6b62-6675-432a-9c00-2c2e74b1d5e4.png)
    
# Future Work

1. Membuat program terbagi kebeberap file .py dan class.
2. Perbaikan lainnya yang mungkin ditemukan setelah program digunakan oleh beberapa user.
