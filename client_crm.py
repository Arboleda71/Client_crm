"""Client CRM System
"""
clients = [
    {"name": "Camilo", "age": 23, "email": "camilo@gmail.com", "active": True},
    {"name": "Valentina", "age": 25, "email": "valen@outlook.com", "active": True},
    {"name": "Jose", "age": 27, "email": "jose@example.com", "active": False},
    {"name": "Elena", "age": 24, "email": "elena@hotmail.com", "active": False},
    {"name": "Luis", "age": 20, "email": "luis123@gmail.com", "active": True}
]
def show_menu():
    print("===== CLIENT CRM SYSTEM =====")
    print("1. List all clients")
    print("2. Add new client")
    print("3. Delete client by name")
    print("4. Update client info")
    print("5. Search client (name or email)")
    print("6. Show active clients")
    print("7. Show stats")
    print("8. Save to file")
    print("0. Exit")

def list_clients(clients):
    """List all clients in the system"""
    print("===== CLIENTS LIST =====")
     
    store=[]     
    for client in clients:
        if not clients:
            print("No clients found. ")  
            break
        print(f"name: {client['name']}, age: {client['age']}, email: {client['email']}, active: {client['active']}")
        
        


def add_client(clients):
    """Adding a new client with name, age, email, active"""
    

    try:
        name=input("Enter client name: ").strip().lower()
        for client in clients:
            if client["name"].strip().lower()==name:
                print("Client already exists.")
                break
            
        if len(name)<3:
                print("Name is too short.")
                return
        
        age=int(input("Enter client age: "))
        if age<0 or age>120:
                print("Invalid age, please enter a valid age.")
                return
        email=input("Enter client email:").strip().lower()
        if not "@" in email:
                print("Invalid email format.")
                return        
        if len(email)<5:
                print("Email is too short.")
                return
          
        active=input("Is the client active? (yes/no): ").strip().lower()
        if active=="yes":
               clients.append({"active": True})  
               return
        elif active=="no":
                clients.append({"active": False})
                return
        else:
            print("Invalid input, please enter (yes) or (no).").strip().lower()  
            
              
        store={"name":name, "age":age, "email":email, "active":active}
        clients.append(store)
        list_clients(clients)
        print("Client added successfully.") 
    except ValueError:
        print("Invalid input, Please enter a valid age.")

def delete_client(clients):
    """Delete a client by name"""
    original_len=len(clients)
    name=input("Enter client name to delete: ").strip().lower()
    clients[:]=[client for client in clients if client["name"].lower()!=name]
    if len(clients)<original_len:
         print(f"client {name} deleted successfully.")
    else:
         print("client not found ")
    if not clients:
        print("No clients found.")
        
def update(clients):
     """Update client for name;age;email;active or not"""
     name=input("Enter client name to update: ").strip().lower()
     for client in clients:
          if client["name.".lower()==name:
                    print("client found ")
                    ]
     





     
                



