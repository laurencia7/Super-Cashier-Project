import uuid # Mengimpor modul uuid. 

class Transaction:
    def __init__(self):
        self.id = uuid.uuid4().hex # uuid (Universally Unique Identifier) adalah standar yang digunakan untuk membuat ID unik secara acak.
        self.items = []
        self.total = 0
        
    def add_item(self, item): # menambahkan item ke dalam pesanan
        name, qty, price = item
        item_dict = {"name": name, "qty": qty, "price": price}
        self.items.append(item_dict)
        self.total += qty * price
        print("Item telah ditambahkan ke pesanan")
        
    def delete_item(self, name): # menghapus item dari pesanan
        for item in self.items:
            if item["name"] == name:
                self.total -= item["qty"] * item["price"]
                self.items.remove(item)
        print("Item telah dihapus")
                
    def reset_transaction(self): # menghapus semua pesanan 
        self.items = []
        self.total = 0
        
    def cek_item_name(self, old_name):  # mengecek apakah item tertentu ada dalam pesanan
        for item in self.items:
            if item["name"] == old_name:
                return True
                
        return False
                
    def update_item_name(self, old_name, new_name): # mengupdate nama item dalam pesanan
        for item in self.items:
            if item["name"] == old_name:
                item["name"] = new_name
        
        print("Nama telah diupdate")
                
    def update_item_qty(self, name, new_qty): # mengupdate jumlah item dalam pesanan
        for item in self.items:
            if item["name"] == name:
                self.total -= item["qty"] * item["price"]
                item["qty"] = new_qty
                self.total += new_qty * item["price"]
        
        print("Jumlah telah diupdate")
                
    def update_item_price(self, name, new_price): # mengupdate harga item dalam pesanan
        for item in self.items:
            if item["name"] == name:
                self.total -= item["qty"] * item["price"]
                item["price"] = new_price
                self.total += item["qty"] * new_price
                
        print("Harga telah diupdate")
        
    def check_order(self): # memeriksa kesalahan dalam pesanan.
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
            print("\nPemesanan sudah benar")
        else:
            print("Terdapat eror dalam pemesanan:")
            for error in errors:
                print(error)
                
    def print_receipt(self): # menampilkan pesanan
        print("| No | Nama Item | Jumlah Item | Harga/Item | Total Harga |")
        print("|----|-----------|-------------|------------|-------------|")
        for i, item in enumerate(self.items, 1):
            total_item = item["qty"] * item["price"]
            print(f"| {i:2} | {item['name']:9} | {item['qty']:11} | {item['price']:10} | {total_item:11} |")
        print(f"\nTotal : Rp{self.total},-")

    def total_price(self): # menghitung total harga pesanan
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