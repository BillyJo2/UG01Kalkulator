def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Tidak bisa membagi dengan nol"

def main():
    while True:
        

        pilihan = input("Masukkan pilihan (+/-/*/:/Q): ")

        if pilihan == 'Q' or pilihan == 'q':
            print("Program Berhenti")
            break

        if pilihan in ['+', '-', '*', ':']:
            num1 = float(input("Masukkan angka pertama: "))
            num2 = float(input("Masukkan angka kedua: "))

            if pilihan == '+':
                print(f"Hasil: {tambah(num1, num2)}")
            elif pilihan == '-':
                print(f"Hasil: {kurang(num1, num2)}")
            elif pilihan == '*':
                print(f"Hasil: {kali(num1, num2)}")
            elif pilihan == ':':
                print(f"Hasil: {bagi(num1, num2)}")
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()