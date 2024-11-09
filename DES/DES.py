PC_1 = [28, 38, 26, 29, 12, 36, 39, 46, 17, 44, 5, 56, 9, 6, 22, 47, 4, 62, 23, 53, 41, 0, 14, 43,8, 58, 40, 37, 31, 48, 50, 20, 21, 15, 34, 11, 35, 13, 52, 49, 2, 25, 51, 57, 30, 19, 1, 54, 7, 60, 3, 10, 32, 42, 59, 27]
shift_bit = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
PC_2 = [3, 15, 37, 52, 44, 49, 8, 39, 12, 48, 28, 42, 21, 5, 27, 54, 9, 20, 22, 26, 0, 43, 34, 53, 19, 47, 16, 51, 11, 6, 31, 4, 50, 40, 46, 35, 36, 24, 23, 2, 13, 10, 1, 25, 33, 41, 30, 55]
E=[28, 13, 15, 6, 19, 3, 22, 4, 5, 7, 26, 5, 2, 11, 27, 5, 29, 23, 1, 25, 3, 21, 23, 20, 22, 9,29, 16, 14, 16, 1, 17, 18, 8, 0, 27, 29, 29, 10, 8, 26, 31, 7, 24, 12, 14, 13, 30]
P=[17, 8, 6, 16, 9, 14, 18, 12, 22, 7, 29, 4, 5, 20, 23, 27, 26, 1, 15, 24, 11, 3, 30, 0, 2, 25,10, 31, 21, 28, 13, 19]

sboxen = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
		[0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
		[4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
		[15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

		[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
		[3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
		[0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
		[13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

		[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
		[13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
		[13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
		[1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

		[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
		[13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
		[10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
		[3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

		[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
		[14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
		[4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
		[11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

		[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
		[10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
		[9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
		[4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

		[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
		[13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
		[1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
		[6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

		[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
		[1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
		[7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
		[2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]
           
    
IP=[32, 34, 15, 6, 19, 3, 22, 4, 5, 36, 53, 42, 2, 11, 45, 17, 16, 23, 1, 62, 49, 21, 25, 20, 44, 47,9, 38, 52, 28, 41, 43, 14, 51, 18, 56, 0, 57, 40, 61, 59, 10, 60, 54, 31, 7, 24, 12, 50, 63, 30, 46, 35,48, 33, 27, 58, 55, 37, 29, 8, 39, 26, 13]
IP_1 = [36, 18, 12, 5, 7, 8, 3, 45, 60, 26, 41, 13, 47, 63, 32, 2, 16, 15, 34, 4, 23, 21, 6, 17, 46, 22, 62, 55, 29, 59, 50, 44, 0, 54, 1, 52, 9, 58, 27, 61, 38, 30, 11, 31, 24, 14, 51, 25, 53, 20, 48, 33, 28, 10, 43, 57, 35, 37, 56, 40, 42, 39, 19, 49]

k = "aff263f5eba068b2"

# zahlen von hexa zu binary Umwandlung
def hex_to_bin(hex_num):
    decimal_num = int(hex_num, 16)
    str_binary_num = bin(decimal_num)[2:]
    binary_list = [int(bit) for bit in str_binary_num]
    return binary_list

# zahlen von binary zu hexa Umwandlung
def bin_to_hix(list_of_bits):
    binary_str = ''.join(str(bit) for bit in list_of_bits)
    hex_str = hex(int(binary_str, 2))[2:]  
    return hex_str

# zahlen von binary zu decimal Umwandlung
def binary_to_decimal(binary_list):
    decimal_list = []
    for binary in binary_list:
        decimal = 0
        binary_str = str(binary)
        for i in range(len(binary_str)):
            decimal += int(binary_str[i]) * (2 ** (len(binary_str) - 1 - i))
        decimal_list.append(decimal)
    return decimal_list

# zahlen von decimal zu binary Umwandlung
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:].zfill(4)  # [2:] to remove the '0b' prefix, zfill to pad with leading zeros
    return binary

Schlussel = hex_to_bin(k)
#print(Schlussel)

# (a)  Erstellen Sie eine eigene Funktion.  Initialisieren Sie ein Array mit Nullen, in dasalle Rundenschlüssel abgelegt werden können.
import numpy as np  # Wir importieren numpy, um ein NumPy-Array zu erstellen
def initialize_key_schedule():
    # Erstelle ein zweidimensionales NumPy-Array (Matrix) mit den angegebenen Dimensionen und initialisiere es mit Nullen
    key_schedule = np.zeros((16, 48), dtype=int)
    return key_schedule

# print('a',initialize_key_schedule())
# funktion um permutation zu permutieren

def permutation(key, PC, n):
    lst = [0]*n
    permuted = [key[i] for i in PC]
    return permuted

# (b)  Implementieren  Sie  die  PC-1,  die  auf  das  Eingangsargumentkangewandt  wird.
PC_1_Permotation = permutation(Schlussel, PC_1, 64)
# print('b',PC_1_Permotation)

# (c)  Zerlegen Sie das Ergebnis der PC-1 in die beiden Hälften C0 und D0.
def Schnitt(key, n):
    left = key[:n] # C0
    right = key[n:] # D0
    return [left, right] 
Schlussel_Schnitt = Schnitt(PC_1_Permotation,28)
# print('c',Schlussel_Schnitt)

#(d) Erzeugen Sie nun eine Schleife, die je nach Runde den Leftshift korrekt anwendet.
def shift_left(block, nth_shifts):
    key = []
    for i in range(nth_shifts):
        key = block[nth_shifts:] + block[:nth_shifts]
    return key

def schlussel_combination(Schlussel):
    schlussel_combination = []
    left = Schlussel[0]
    right = Schlussel[1]
    for i in range(16):
        #print("key_56bit_schnitt in Runde",i , ":" ,left, right)
        le = shift_left(left, shift_bit[i])  
        ri = shift_left(right, shift_bit[i])
        #print("key_56bit_schnitt in Runde",i ," nach Verschiebung:" ,le, ri)
        res = le + ri
        schlussel_combination.append(res)
        left = le
        right = ri
        my_array = np.array(schlussel_combination)
    return my_array

Schlussel_combinat = schlussel_combination(Schlussel_Schnitt)
#print(Schlussel_combinat)
# Anzahl der Runden

# aufgabe E
def Key_round_erg(key):
    num_rounds = len(key)
    anzahl_keys_per_round = 48
    key_schedule = initialize_key_schedule() 
    for i in range(num_rounds):
        for j in range(anzahl_keys_per_round):
            key_schedule[i][j] = key[i][PC_2[j]]
    return key_schedule

Rundenergebnisse = Key_round_erg(Schlussel_combinat)
# print('d',Rundenergebnisse)
#Rundenergebnisse

# (f) Geben Sie als Lösung für diese Aufgabe den vorletzten Rundenschlüssel k15 an, wenn folgender Schlüssel genutzt wird:
k15 = Rundenergebnisse[-2]
k15_in_hex = bin_to_hix(k15)
# print("vorletzten Rundenschlüssel k15:",k15_in_hex)
# print('f',k15,k15_in_hex)

Ki= "850bff0a66ed"
Ri_1 = "c9308881"
Ki_bin = hex_to_bin(Ki)
Ri_1_bin = hex_to_bin(Ri_1)
#len(Ri_1_bin)

# (a)  Realisieren Sie die Expansion von Ri. Nutzen Sie:
# Expandtion funcktion
def expand(input_block, n):
    output_block = []
    for i in range(n):
        output_block.append(input_block[E[i]])
    return output_block  # Eine Tabelle mit n Bits zurückgeben

# a=expand(Ri_1_bin,48)
# print('a',a,len(a))

# b) Ergebniss der Expansion mit dem Rundenschlüssel xor-verknüpfen
def f(Ri, runden_schluessel):  
    # Rundenschlüssel und Ri xor-verknüpfen
    ergebnis = np.bitwise_xor(Ri, runden_schluessel)
    # die Aufteilung in die acht Array der Größe 6, die den Eingang der S-Boxen bilden.
    ergebnis =  np.array_split(ergebnis, 8)
    return ergebnis
# b=f(a,Ki_bin)
# print('b',b,len(b))

# S_boxen Funktion
def s_box(sbox_input):
    x = 0
    sbox_output=[]
    for wert in sbox_input:
        sbox_in = []
        # Die Spalte berechnen. Die mittellere 4 Bits von rechts nach links  zusammenfügen und dann in einer Zahl umwandeln.
        spalte = 0   # column (Spalte)
        for bit in wert[1:5]:
            spalte = (spalte << 1) | bit
        # Die Zeile rausbekommen indem ich Bit 1 und Bit 6 zusammenfüge und dann in einer Zahl umwandeln 
        zeile = 0  # row (Zeile)
        for bit in [wert[0] , wert[5]]:
            zeile = (zeile << 1) | bit
        sQ=sboxen[x]
        # Umwandlung in 4-Bit-Binärcode
        binary_number = np.binary_repr(sQ[zeile][spalte], width=4)
        #Ergebnis-Bits in eine Liste speichern
        for bit in binary_number:
            sbox_in.append(int(bit))
        sbox_output.append(sbox_in)
        x = x+1
    return sbox_output

# c=s_box(b)
# print('c',c,len(c))
# (d) Setzen Sie alle Bit wieder zusammen, permutieren Sie diese und geben die Werte als Ergebnis der f-Funktion zurück.
def s_boxen_permutation(sbox_output):
    output = []     # liste um alle sboxen ausgabe zusammen zu setzen
    for i in sbox_output:
        output = output + i
    out_perm = permutation(output, P, 32)
    return out_perm # die funktion gibt die permutirte bits zuruck  
# d=s_boxen_permutation(c)
# print('d',d,len(d))

# (e)  Generieren Sie für die Lösung dieser Aufgabe die Ausgabe der  f-Funktion für folgende Eingaben: 


# 1-Schrit: Ri-1 expandieren von 32 Bits auf 48 Bits
expaned_Ri_1 =  expand(Ri_1_bin, 48)
# 2-Schritt: Rundenschlüssel mit dem expandierten rechten Hälfte (Ri_1) xor-verknüpfen
xor_result = f(expaned_Ri_1,Ki_bin)
# 3-Schritt: Das Ergebnis der XOR-Verknüfung mitells S-Box-Substitution verkleinern
sbox_result = s_box(xor_result)
# 4-Schritt: Das Ergebnis aus der S-Box mittels P-Permuation permutieren
erg = s_boxen_permutation(sbox_result)
# Ergebnis der f-Funktion in Hex umwadeln
f_result_zu_hex = bin_to_hix(erg)
print("Das Ergebnis der f-Funktion in hexa:", f_result_zu_hex)
print("================================================")

plain='d51d8da24285ff85'
plain2bin = hex_to_bin(plain)
plainPermotation = permutation(plain2bin, IP, 64)
plainSchnitt = Schnitt(plainPermotation,32)
links = plainSchnitt[0]
richts = plainSchnitt[1]
for i in range(16):
    # print('i',i)
    # print('links',links)
    # print('richts',richts)
    # print('schlussel',Rundenergebnisse[i])
    # print('-----------','\n')
    plain_text_expand = expand(richts,48)
    xOR_plain_mit_schlussel = f(plain_text_expand, Rundenergebnisse[i])
    s_boxen_ausgabe = s_box(xOR_plain_mit_schlussel)
    permutation_nach_sboxen = s_boxen_permutation(s_boxen_ausgabe)
    xor_sBoxen_mit_link = [a ^ b for a, b in zip(links, permutation_nach_sboxen)]
    links = richts
    richts = xor_sBoxen_mit_link

temp = richts
richts = links
links = temp
lis_vor_ip_1 = []
lis_vor_ip_1 = links+richts
# print("lis_vor_ip_1",lis_vor_ip_1)
# print(len(lis_vor_ip_1))

def IP_inverse_Perm(lis_vor_ip_1, IP_1):
    IP_inverse_ausgabe = [lis_vor_ip_1[i] for i in IP_1]
    return IP_inverse_ausgabe

IP_inverse = IP_inverse_Perm(lis_vor_ip_1, IP_1)
# print("IP_inverse",IP_inverse)

y = bin_to_hix(IP_inverse)
print('y',y)


# =================================================================
print("Andere Implementierung")
plain='d51d8da24285ff85'
plain2bin = hex_to_bin(plain)
plainPermotation = permutation(plain2bin, IP, 64)
plainSchnitt = Schnitt(plainPermotation,32)
links = plainSchnitt[0]
richts = plainSchnitt[1]
for i in range(16):
    plain_text_expand = expand(richts,48)
    xOR_plain_mit_schlussel = f(plain_text_expand, Rundenergebnisse[i])
    s_boxen_ausgabe = s_box(xOR_plain_mit_schlussel)
    permutation_nach_sboxen = s_boxen_permutation(s_boxen_ausgabe)
    xor_sBoxen_mit_link = [a ^ b for a, b in zip(links, permutation_nach_sboxen)]
    links = richts
    richts = xor_sBoxen_mit_link 
lis_vor_ip_1 = []
lis_vor_ip_1 = richts+links
def IP_inverse_Perm(lis_vor_ip_1, IP_1):
    IP_inverse_ausgabe = [lis_vor_ip_1[i] for i in IP_1]
    return IP_inverse_ausgabe

IP_inverse = IP_inverse_Perm(lis_vor_ip_1, IP_1)
y = bin_to_hix(IP_inverse)
print('y',y)