'''
mengimport modul Transaction, sehingga semua fungsi dan variabel 
yang didefinisikan di dalamnya dapat digunakan dalam skrip yang sedang dikerjakan
'''
from transaction import Transaction

trnsct_123 = Transaction() # membuat objek Transaction yang disimpan dalam variabel trnsct_123

def main(): # meminta pengguna untuk memasukkan nama, jumlah, dan harga item dan menambahkan item ke dalam objek Transaction menggunakan metode add_item
    print("=== Selamat datang di Self-Service Kasir ===")
    
    while True:
        name = input("\nMasukkan nama item ['0' jika selesai input] : ")
        if name == '0':
            try:
                raise order()
            except Exception as e:
                print(e)
            break
        qty = input("Masukkan jumlah item\t: ")
        price = input("Masukkan harga per item\t: ")
        if qty == "":
            trnsct_123.add_item([name, 0, float(price)])
            continue
        elif price == "":
            trnsct_123.add_item([name, int(qty), 0.0])
            continue
        elif qty == "" and price == "":
            trnsct_123.add_item([name, 0, 0.0])
            continue
        trnsct_123.add_item([name, int(qty), float(price)])
        
        
    
def order(): # menampilkan pesanan dan menawarkan opsi kepada customer untuk mengupdate, menghapus, atau membayar pesanan.
    print(f"\nBerikut order-an anda\n")
    trnsct_123.print_receipt()
    
    cek = True
    while cek:
        print("\n1. Update")
        print("2. Delete")
        print("3. Bayar")
        choice = int(input("Pilihan anda ['0' untuk exit]: "))
        if choice<0 or choice>3:
            pass
        else:
            cek = False
            if choice == 1:
                cek2 = True
                while cek2:
                    name = input("\nMasukkan nama item yang mau diupdate\t: ")
                    if trnsct_123.cek_item_name(name) == True:
                        cek3 = True
                        while cek3:
                            print("\n1. Update nama")
                            print("2. Update jumlah")
                            print("3. Update harga")
                            update = int(input("Pilihan anda: "))
                            print()
                            if (update ==1 or update == 2 or update == 3):
                                if update == 1:
                                    new_name = input("Masukkan nama baru item : ")
                                    trnsct_123.update_item_name(name, new_name)
                                    raise order()
                                elif update == 2:
                                    new_qty = int(input("Masukkan jumlah baru : "))
                                    trnsct_123.update_item_qty(name, new_qty)
                                    raise order()
                                elif update == 3:
                                    new_price = float(input("Masukkan harga baru: "))
                                    trnsct_123.update_item_price(name, new_price)
                                    raise order()
                                cek3 = False
                            else:
                                print("Input tidak benar")

                        cek2 = False
                    else:
                        print("Tidak ada nama item tersebut dalam order-an anda")

            elif choice == 2:
                print("\n1. Hapus salah satu item")
                print("2. Hapus semua")
                hapus = int(input("Pilihan anda: "))
                if hapus == 1:
                    name = input("\nMasukkan nama item yang mau dihapus\t: ")
                    if trnsct_123.cek_item_name(name) != True:
                        print(f"'{name}' tidak ada dalam order-an.")
                        continue
                    confirm = input(f"Yakin ingin hapus '{name}'?[Y/N] : ")
                   
                    if confirm == 'Y' or confirm == 'y':
                        trnsct_123.delete_item(name)
                        raise order()
                    elif confirm == 'N' or confirm == 'n':
                        print("Penghapusan dibatalkan")
                        continue
                    else:
                        print("Input hanya Y atau N !")
                   
                elif hapus == 2:
                    confirm = input("Yakin ingin hapus semua order-an?[Y/N] : ")
         
                    if confirm == 'Y' or confirm == 'y':
                        trnsct_123.reset_transaction()
                        raise order()
                    elif confirm == 'N' or confirm == 'n':
                        print("Penghapusan dibatalkan")
                        continue
                    else:
                        print("Input hanya Y atau N !")
                else:
                    print("Input hanya 1 atau 2 !")
                    
            elif choice == 3:
                print()
                trnsct_123.check_order()
                print(f"\nTransaksi ID {trnsct_123.id}")
                trnsct_123.total_price()
                print(f"\nTerimakasih telah berbelanja")
                break
                
            elif choice == 0:
                print("Terima kasih telah menggunakan program ini")
                break

main()