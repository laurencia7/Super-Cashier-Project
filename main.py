import uuid
class Transaction:
    def __init__(self):
        self.id = uuid.uuid4().hex
        self.items = []
        self.total = 0
        
    def add_item(self, item):
        name, qty, price = item
        item_dict = {"name": name, "qty": qty, "price": price}
        self.items.append(item_dict)
        self.total += qty * price
        print(item_dict)
        print("Item telah ditambahkan ke pesanan")
        
    def delete_item(self, name):
        for item in self.items:
            if item["name"] == name:
                self.total -= item["qty"] * item["price"]
                self.items.remove(item)
        print("Item telah dihapus")
                
    def reset_transaction(self):
        self.items = []
        self.total = 0
        
    def cek_item_name(self, old_name):
        for item in self.items:
            if item["name"] == old_name:
                return True
                
        return False
                
    def update_item_name(self, old_name, new_name):
        for item in self.items:
            if item["name"] == old_name:
                item["name"] = new_name
        
        print("Nama telah diupdate")
                
    def update_item_qty(self, name, new_qty):
        for item in self.items:
            if item["name"] == name:
                self.total -= item["qty"] * item["price"]
                item["qty"] = new_qty
                self.total += new_qty * item["price"]
        
        print("Jumlah telah diupdate")
                
    def update_item_price(self, name, new_price):
        for item in self.items:
            if item["name"] == name:
                self.total -= item["qty"] * item["price"]
                item["price"] = new_price
                self.total += item["qty"] * new_price
                
        print("Harga telah diupdate")
        
    def check_order(self):
        errors = []
        for item in self.items:
            if "name" not in item or "qty" not in item or "price" not in item:
                errors.append(f"Error: Informasi item '{item.get('name', 'Unknown')}' kurang lengkap")
            if not isinstance(item.get("qty"), int) or item["qty"] <= 0:
                errors.append(f"Error: Invalid jumlah item '{item.get('name', 'Unknown')}'")
            if not isinstance(item.get("price"), (int, float)) or item["price"] <= 0:
                errors.append(f"Error: Invalid harga item '{item.get('name', 'Unknown')}'")
        
        if not errors:
            self.print_receipt()
            print("Pemesanan sudah benar")
        else:
            print("Terdapat eror dalam pemesanan:")
            for error in errors:
                print(error)
                
    def print_receipt(self):
        print("| No | Nama Item | Jumlah Item | Harga/Item | Total Harga |")
        print("|----|-----------|-------------|------------|-------------|")
        for i, item in enumerate(self.items, 1):
            total_item = item["qty"] * item["price"]
            print(f"| {i:2} | {item['name']:9} | {item['qty']:11} | {item['price']:10} | {total_item:11} |")
        print(f"\nTotal : Rp{self.total},-")

    def total_price(self):
        if self.total > 500000:
            print("Diskon 10%")
            print(f"Total pembayaran: Rp{self.total-(self.total*0.1)},-")
        elif self.total > 300000 and self.total <= 500000:
            print("Diskon 8%")
            print(f"Total pembayaran: Rp{self.total-(self.total*0.08)},-")
        elif self.total > 200000 and self.total <= 300000:
            print("Diskon 5%")
            print(f"Total pembayaran : Rp{self.total-(self.total*0.05)},-")
        else:
            print(f"Total pembayaran: Rp{self.total},-")


trnsct_123 = Transaction()

def main():
    print("=== Selamat datang di Self-Service Kasir ===")
    
    while True:
        name = input("\nMasukkan nama item ['0' jika selesai input] : ")
        if name == '0':
            order()
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
        
        
    
def order():
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
                    try:
                        if confirm == 'Y' or confirm == 'y':
                            trnsct_123.delete_item(name)
                            raise order()
                        elif confirm == 'N' or confirm == 'n':
                            print("Penghapusan dibatalkan")
                            continue
                        else:
                            print("Input hanya Y atau N !")
                    except:
                        print("Input error")
                
                elif hapus == 2:
                    confirm = input("Yakin ingin hapus semua order-an?[Y/N] : ")
                    try:
                        if confirm == 'Y' or confirm == 'y':
                            trnsct_123.reset_transaction()
                            raise order()
                        elif confirm == 'N' or confirm == 'n':
                            print("Penghapusan dibatalkan")
                            continue
                        else:
                            print("Input hanya Y atau N !")
                    except:
                        print("Input error")
                else:
                    print("Input hanya 1 atau 2 !")
                    
            elif choice == 3:
                trnsct_123.check_order()
                trnsct_123.print_receipt()
                print(f"\nTransaksi ID {trnsct_123.id}")
                trnsct_123.total_price()
                break
                
            elif choice == 0:
                print("Terima kasih telah menggunakan program ini")
                break

main()
    
    
    

