import socket

# Create socket
client = socket.socket()

# Connect to server
client.connect(("127.0.0.1", 5555))

# Save file name
save_name = input("Enter name to save file: ")

# Receive data
data = client.recv(1000000)

# Save file
with open(save_name, "wb") as file:
    file.write(data)

print("File received successfully")

# Close connection
client.close()