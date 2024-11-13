def enkripsi(plain_text, shift):
    cipher_text =""
    for char in plain_text:
        #Huruf Besar
        if char.isupper():
            cipher_text += chr((ord(char) + shift - 65) % 26 +65)
        #Huruf Kecil
        elif char.islower():
            cipher_text += chr((ord(char) + shift - 97) % 26 +97)
        else:
        #Karakter selain huruf tetap    
            cipher_text += char
    return cipher_text


def deskripsi(cipher_text, shift):
    plain_text =""
    for char in cipher_text:
        #Huruf besar
        if char.isupper():
             plain_text += chr((ord(char) - shift - 65) % 26 +65)
        #Huruf Kecil
        elif char.islower():
            plain_text+= chr((ord(char) - shift - 97) % 26 +97)
        else:
        #Karakter selain huruf tetap    
            plain_text += char
    return plain_text



# interface pengguna
def main():
    print("Selamat datang di program Kriptografi Caesar")
    plain_text = input("Masukkan teks asli (plaintext): ")
    shift = int(input("Masukkan shift (1-25): "))

    #panggil fungsi  enkripsi 
    cipher_text = enkripsi (plain_text, shift)
    print("Teks terenkripsi: ", cipher_text)


    #panggil fungsi deskripsi
    deskripsi_text = deskripsi(cipher_text, shift)
    print("Teks terdeskripsi: ", deskripsi_text)


if __name__ == "__main__":
    main()