# securecli

**securecli** is a lightweight command-line chat application that uses the **Diffie-Hellman key exchange** to establish a shared secret between two peers. All messages are encrypted using a simple XOR cipher with a key derived from the shared secret.

> ⚠️ **Note:** This project is intended for learning purposes. It uses small primes and a basic XOR cipher for demonstration. Do not use this in production.

---

## Features

* Pure Python — no external dependencies
* Works in **server** or **client** mode
* Diffie-Hellman key exchange for secure key agreement
* Symmetric encryption using a derived shared secret
* Interactive real-time chat over TCP

---

## How It Works

1. **Key Exchange**

   * Server and client each generate a private key.
   * Public keys are computed using Diffie-Hellman and exchanged over the network.
   * Both parties compute the same shared secret without sending it directly.

2. **Encryption**

   * The shared secret is hashed with SHA-256 to create a symmetric key.
   * Messages are encrypted and decrypted using a simple XOR cipher with the key.

3. **Communication**

   * Messages are sent over a TCP connection and decrypted on the other side.

---

## Requirements

* Python 3.7 or higher
* No external libraries required

---

## Installation

Clone this repository:

```bash
git clone https://github.com/noahwhlim/securecli.git
cd securecli
```

---

## Starting the App

**1. Start the Server**

Open a terminal and run:

```bash
python main.py server <port>
```

Replace `<port>` with the port number you want the server to listen on (e.g., `5000`).

**Example:**

```bash
python main.py server 5000
```

**2. Start the Client**

Open another terminal and run:

```bash
python main.py client <server_host> <port>
```

Replace `<server_host>` with the server's IP address (`127.0.0.1` if local) and `<port>` with the same port the server is listening on.

**Example:**

```bash
python main.py client 127.0.0.1 5000
```

**3. Chat**

* Type your messages and press **Enter** to send.
* Type `/quit` to exit the chat.

---

## Example

**Server Terminal**

```
Server listening on port 5000...
Connected by ('127.0.0.1', 60312)
Shared key established: 2
Client: Hello from client!
You: Hi there!
```

**Client Terminal**

```
Shared key established: 2
You: Hello from client!
Server: Hi there!
```

---

## Security Notes

* This demo uses a **very small prime** for simplicity.
* XOR encryption is **not secure** for real-world use.
* In a production-ready version, you would:

  * Use a large prime and generator for Diffie-Hellman.
  * Replace XOR with AES or ChaCha20.
  * Implement proper authentication and replay attack prevention.

---

## License

MIT License — feel free to use and modify.