import random
import datetime
from customer import Customer
from atm_card import ATMCard

bank_abc = Customer(id=1)

# Melakukan input pin sekaligus pengecekan PIN ATM apakah sudah benar atau belum
while True:
    id = int(input("Masukkan pin anda: "))
    trial = 0

    while (id != int(bank_abc.pin_atm()) and trial < 12):
        id = int(input("Pin anda salah. Silakan Masukkan lagi: "))

        trial += 1

        if trial == 3:
            print("Error. Silakan ambil kartu dan coba lagi..")
            quit()

# Melakukan pengulangan untuk MENU
    pilihan ='y'
    while (pilihan == 'y'):
        print('                   SELAMAT DATANG                   ')
        print('                                                    ')
        print('========  PILIH TRANSAKSI YANG ANDA INGINKAN =======')
        print('====================================================')
        print('           TEKAN (CANCEL) UNTUK PEMBATALAN          ')
        print('1. ---------------------------             CEK SALDO')
        print('2. ---------------------------                 DEBET')
        print('3. ---------------------------                SIMPAN')
        print('4. ---------------------------             GANTI PIN')
        print('5. ---------------------------                KELUAR')
        print('                                                    ')
# Mengeluarkan informasi untuk menu 1
        saldo_user = bank_abc.checkBalance()
        first_menu = int(input('Silakan pilih menu yang anda inginkan: '))
        if first_menu == 1:
            print('                                                    ')
            print('                                                    ')
            print('=========             CEK SALDO           ==========')
            print('====================================================')
            print('                                                    ')
            print('                                                    ')
            print(f'     SALDO ANDA SAAT INI ADALAH: {saldo_user}      ')
            print('                                                    ')
            print('                                                    ')
            print('                                                    ')
            print('                                                    ')

            pilihan = input('Apakah anda ingin melanjutkan program? (y/n): ')
# Mengeluarkan informasi untuk menu 2
        elif first_menu == 2:

            nominal_debet = int(input(" MASUKKAN JUMLAH UANG:         "))
            sisa_saldo = bank_abc.withdrawBalance(nominal=nominal_debet)

            if nominal_debet < saldo_user:
                print('                                                    ')
                print('                                                    ')
                print('=========         INFORMASI SALDO         ==========')
                print('                                                    ')
                print('                                                    ')
                print(f' SISA SALDO: RP.                    {sisa_saldo}   ')
                print('                                                    ')
                print('                                                    ')
                print('                                                    ')
                print('                                                    ')
                print('                                                    ')              
            else:
                print('                                                    ')
                print('                                                    ')
                print('                                                    ')
                print('                                                    ')
                print('             MAAF SALDO ANDA TIDAK CUKUP            ')
                print('                                                    ')
                print('                                                    ')
                print('                                                    ')
                print('                                                    ')

            pilihan = input('Apakah anda ingin melanjutkan program? (y/n): ')
# Mengeluarkan informasi untuk menu 3
        elif first_menu == 3:

            nominal_simpan = int(input("MASUKKAN JUMLAH UANG:         "))
            saldo = bank_abc.depositBalance(nominal=nominal_simpan)

            print('                                                    ')
            print('                                                    ')
            print('=========         INFORMASI SALDO         ==========')
            print('                                                    ')
            print('                                                    ')
            print(f' SALDO ANDA ADALAH RP.                    {saldo}  ')
            print('                                                    ')
            print('                                                    ')
            print('                                                    ')
            print('                                                    ')
            print('                                                    ')
   
            pilihan = input('Apakah anda ingin melanjutkan program? (y/n): ')

# Mengeluarkan informasi untuk menu 4
        elif first_menu == 4:

            perbarui_pin = int(input('Masukkan 4 digit pin baru anda:     '))
            pin_saat_ini = bank_abc.pin_atm()
            pin_baru = bank_abc.new_pin(newpin=perbarui_pin)

            if perbarui_pin == pin_saat_ini:
                print('                                                    ')
                print('                                                    ')
                print('                                                    ')
                print('                                                    ')
                print('               PIN ANDA BELUM DIPERBARUI            ')
                print('                                                    ')
                print('                                                    ')
                print('                                                    ')
                print('                                                    ')
            else:
                print('                                                    ')
                print('                                                    ')
                print('                                                    ')
                print('                                                    ')
                print(f'         SELAMAT PIN ANDA SUDAH DIPERBARUI         ')
                print('                                                    ')
                print('                                                    ')
                print('                                                    ')
                print('                                                    ')

            pilihan = input('Apakah anda ingin melanjutkan program? (y/n): ')

# Mengeluarkan informasi untuk menu 5
        elif first_menu == 5: 

            nomor_record = random.randint(100000,1000000)
            date = datetime.datetime.now()

            print('                                                       ')
            print('                       BANK ABC                        ')
            print('=======================================================')
            print(f' TANGGAL                     {date}                   ')
            print('                                                       ')
            print(f' RECORD  NO.                            {nomor_record}')
            print('                                                       ')
            print('                                                       ')
            print(f' SALDO ANDA :                             {saldo_user}')
            print('                                                       ')
            quit()
        else:
            print('           MAAF SILAKAN ULANGI TRANSAKSI ANDA          ')    
            quit()   