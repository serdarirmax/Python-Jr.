Morsalfabe={
            'A': '.-',
            'B': '-...',
            'C': '-.-.',
            'D': '-..',
            'E': '.',
            'F': '..-.',
            'G': '--.',
            'H': '....',
            'I': '..',
            'J': '.---',
            'K': '-.-',
            'L': '.-..',
            'M': '--',
            'N': '-.',
            'O': '---',
            'P': '.--.',
            'R': '.-.',
            'S': '...',
            'T': '-',
            'U': '..-',
            'V': '...-',
            'Y': '-.--',
            'Z': '--..',
            '.': '.-.-.-',
            ' ': ' ',    # kelimeleri ayırmak için ekleme yaptım.
}
veri=input("Mors Alfabesine çevrilmesini istediğiniz cümleyi [türkçe karakterler olmadan] giriniz : ").upper()
cevir=""
for i in range(len(veri)):
    indeksiAl=veri[i]
    cevir+=Morsalfabe.get(indeksiAl)
print(cevir)