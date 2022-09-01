opsi = input('Pilih salah satu operasi matematika yang ingin anda lakukan! (+ , -, *, /) --> ')


def klkrtr(operasi):
    if operasi == '+':
        result = a + b
    elif operasi == '-':
        result = a - b
    elif operasi == '*':
        result = a * b
    else:
        result = a / b
    return result


if opsi == '+' or opsi == '-' or opsi == '*' or opsi == '/':
    a = float(input('Masukkan angka pertama : '))
    b = float(input('Masukkan angka kedua : '))
    hsil = klkrtr(opsi)
    print(a, opsi, b, '=', hsil)
else:
    print('Mohon input operasi yang sesuai :(')