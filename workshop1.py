kullanici_bilgisi=list()
for i in range(10):
    userName=input("Kullanici bilgisi giriniz")
    kullanici_bilgisi.append(userName)

    for user in kullanici_bilgisi:
        print(user)
