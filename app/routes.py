from flask import Blueprint, render_template, request, send_file, redirect, url_for, flash
from file_encryption import encrypt_file, decrypt_file, password_to_fernet_key
import tempfile
import os
from cryptography.fernet import InvalidToken

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/process', methods=['POST'])
def process_file():
    if 'file' not in request.files or 'key' not in request.form or 'mode' not in request.form:
        flash("Missing file, key, or mode!")
        return redirect(url_for('main.index'))

    file = request.files['file']
    password = request.form['key']
    mode = request.form['mode']

    if file.filename == '':
        flash("No file selected!")
        return redirect(url_for('main.index'))

    try:
        # Converting password to key
        key = password_to_fernet_key(password)
        file_data = file.read()

        if mode == 'encrypt':
            # Encrypting the file
            processed_data = encrypt_file(file_data, key)
            filename = f"{file.filename}.enc"
            flash("File encrypted successfully!")
        elif mode == 'decrypt':
            try:
                # Decrypting the file
                processed_data = decrypt_file(file_data, key)
                filename = file.filename.replace('.enc', '') or 'decrypted_file'
                flash("File decrypted successfully!")
            except InvalidToken:
                # Specific error message for decryption failure
                flash("Decryption failed: Invalid key or corrupted file!")
                return redirect(url_for('main.index'))
        else:
            flash("Invalid mode!")
            return redirect(url_for('main.index'))

        # Debug: Showing the file contents for debugging (optional, for large files this might not be ideal)
        print(f"Processed data (first 100 bytes): {processed_data[:100]}")

        # Creating a temporary file to send back
        temp = tempfile.NamedTemporaryFile(delete=False)
        temp.write(processed_data)
        temp.flush()
        temp.close()

        # Return the processed file for download
        return send_file(temp.name, as_attachment=True, download_name=filename)

    except Exception as e:
        # General exception handler
        flash(f"An error occurred: {e}")
        return redirect(url_for('main.index'))
