import socket
import sys
import random
import hashlib

# ------------------------------
# Diffie-Hellman Parameters
# ------------------------------
PRIME = 23
GENERATOR = 5

# ------------------------------
# Key Exchange Functions
# ------------------------------
def generate_private_key():
    # return a random private key (integer)
    return random.randint(2, PRIME - 2)

def compute_public_key(private_key):
    # compute g^private_key mod p
    return (GENERATOR ** private_key) % PRIME

def compute_shared_secret(received_public, private_key):
    # compute shared secret
    return (received_public ** private_key) % PRIME

def derive_key(shared_secret):
    # hash the shared secret and return a symmetric key
    secret_bytes = shared_secret.to_bytes((shared_secret.bit_length() + 7) // 8, 'big')
    hashed = hashlib.sha256(secret_bytes).digest()
    return hashed

# ------------------------------
# Simple XOR Encryption (placeholder for real cipher)
# ------------------------------
def encrypt_message(message, key):
    """Encrypt message using XOR."""
    msg_bytes = message.encode()
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(msg_bytes)])

def decrypt_message(ciphertext, key):
    """Decrypt message using XOR."""
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(ciphertext)]).decode()

# ------------------------------
# Server Mode
# ------------------------------
def server_mode(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv: 
        # AF_INET -> IPv4 address family, SOCK_STREAM -> socket type TCP
        srv.bind(("0.0.0.0", port))
        
        # max 1 pending connection can be queued
        srv.listen(1) 
        
        print(f"Server listening on port {port}...")
        
        # accept() returns a tuple
        conn, addr = srv.accept()
        
        with conn:
            print(f"Connected by {addr}")
            
            # generate keys
            private_key = generate_private_key()
            public_key = compute_public_key(private_key)
            
            # send public key
            # sendall takes bytes, use encode to convert
            conn.sendall(str(public_key).encode())
            
            # receive client key
            client_pub = int(conn.recv(1024).decode())
            
            # compute shared key
            shared_secret = compute_shared_secret(client_pub, private_key)
            key = derive_key(shared_secret)
            print(f"Shared key established: {shared_secret}")
            
            # chat loop
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                decrypted = decrypt_message(data, key)
                print(f"Client: {decrypted}")
                reply = input("You: ")
                conn.sendall(encrypt_message(reply, key))
            

# ------------------------------
# Client Mode
# ------------------------------
def client_mode(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((host, port))
        
        private_key = generate_private_key()
        public_key = compute_public_key(private_key)
        
        server_pub = int(client.recv(1024).decode())
        
        client.sendall(str(public_key).encode())
        
        shared_secret = compute_shared_secret(server_pub, private_key)
        key = derive_key(shared_secret)
        print(f"Shared key established: {shared_secret}")
        
        while True:
            msg = input("You: ")
            client.sendall(encrypt_message(msg, key))
            data = client.recv(1024)
            if not data:
                break
            decrypted = decrypt_message(data, key)
            print(f"Server: {decrypted}")
        
# ------------------------------
# Entry Point
# ------------------------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Server: python secure_chat.py server <port>")
        print("  Client: python secure_chat.py client <host> <port>")
        sys.exit(1)

    mode = sys.argv[1]

    if mode == "server" and len(sys.argv) == 3:
        server_mode(int(sys.argv[2]))
    elif mode == "client" and len(sys.argv) == 4:
        client_mode(sys.argv[2], int(sys.argv[3]))
    else:
        print("Invalid arguments")
