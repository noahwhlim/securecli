# securecli

**securecli** is a lightweight command-line chat application that uses the **Diffie-Hellman key exchange** to establish a shared secret between two peers. All messages are encrypted using a simple XOR cipher with a key derived from the shared secret.

> ⚠️ **Note:** This project is intended for learning purposes. It uses small primes and a basic XOR cipher for demonstration. Do not use this in production.

---

## Features

- Pure Python — no external dependencies
- Works in **server** or **client** mode
- Diffie-Hellman key exchange for secure key agreement
- Symmetric encryption using a derived shared secret
- Interactive real-time chat over TCP

---

## How It Works

1. **Key Exchange**  
   - Server and client each generate a private key.
   - Public keys are computed using Diffie-Hellman and exchanged over the network.
   - Both parties compute the same shared secret without sending it directly.

2. **Encryption**  
   - The shared secret is hashed with SHA-256 to create a symmetric key.
   - Messages are encrypted and decrypted using a simple XOR cipher with the key.

3. **Communication**  
   - Messages are sent over a TCP connection and decrypted on the other side.

---

## Requirements

- Python 3.7 or higher
- No external libraries required

---

## Installation

Clone this repository:

```bash
git clone https://github.com/noahwhlim/securecli.git
cd securecli
