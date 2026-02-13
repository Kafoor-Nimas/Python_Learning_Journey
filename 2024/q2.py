class Product:
    def __init__(self,name,quntity,price):
        self.name=name
        self.quntity=quntity
        self.price=price

    @staticmethod
    def add_product(name,quntity,price):
        with open('inventory.txt','a')as file:
            file.write(f"{name},{quntity},{price}\n")
        print("Product added successfully.")

    @staticmethod
    def view_inventory():
        try:
            with open("inventory.txt","r")as file:
                print("\nInventory List:")
                for line in file:
                    name,quntity,price =line.strip().split(",")
                    print(f"Name: {name}, Quantity: {quntity}, Price: {price}")
        except FileNotFoundError:
            print("Inventory file not found.")

    @staticmethod
    def update_quntity(name,new_qunatity):
        try:
            updated_lines =[]
            found = False

            with open("inventory.txt","r") as file:
                for line in file:
                    product_name,quantity,price =line.strip().split(",")
                    if product_name == name:
                        quantity =str(new_qunatity)
                        found=True
                    updated_lines.append(f"{product_name},{quantity},{price}\n")

            with open("inventory.txt","w")as file:
                file.writelines(updated_lines)
            
            if found:
                print("Quantity updated successfully.")
            else:
                print("Product not found")

        except FileNotFoundError:
            print("Inventory file not found.")


Product.add_product("Pen",50,20)
Product.add_product("Book",30,150)

Product.view_inventory()

Product.update_quntity("Pen",100)

Product.view_inventory()