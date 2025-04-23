# Cryptify - Secure File Encryption Tool

Cryptify is a **secure and scalable file encryption web app** built with **Flask** and the **AES encryption algorithm**. This project aims to provide an easy-to-use interface for encrypting and decrypting files, ensuring the confidentiality of sensitive data.

## Features
- AES-based encryption for strong data security.
- Simple and clean UI for user-friendly interaction.
- Secure file upload and download.
- Easy-to-use decryption tool for previously encrypted files.

## Technologies Used
- **Backend**: Flask (Python)
- **Encryption**: AES (Advanced Encryption Standard)
- **Frontend**: HTML, CSS (Flask templates)
- **Libraries**: PyCryptodome for AES encryption

## Installation

To get started, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/barsha59/Cryptify.git
    ```

2. Navigate into the project directory:
    ```bash
    cd Cryptify
    ```

3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:
    - **On Windows**:
        ```bash
        .\venv\Scripts\activate
        ```
    - **On macOS/Linux**:
        ```bash
        source venv/bin/activate
        ```

5. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

6. Run the Flask app:
    ```bash
    python app.py
    ```

7. Open your browser and navigate to `http://127.0.0.1:5000` to start using Cryptify.

## How It Works
- **File Encryption**: Upload a file, choose your encryption key, and the app will generate an encrypted version of the file.
- **File Decryption**: Upload the encrypted file, provide the same key, and the app will decrypt it for you.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## Acknowledgements
- Thanks to **Flask** and **PyCryptodome** for their amazing libraries!
- Inspired by a desire to explore secure data handling and encryption.

