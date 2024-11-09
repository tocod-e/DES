import numpy as np

class DES:
    # Class-level constants
    PC_1 = [28, 38, 26, 29, 12, 36, 39, 46, 17, 44, 5, 56, 9, 6, 22, 47, 4, 62, 23, 53, 41, 0, 14, 43, 8, 58, 40, 37, 31, 48, 50, 20, 21, 15, 34, 11, 35, 13, 52, 49, 2, 25, 51, 57, 30, 19, 1, 54, 7, 60, 3, 10, 32, 42, 59, 27]
    shift_bit = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    PC_2 = [3, 15, 37, 52, 44, 49, 8, 39, 12, 48, 28, 42, 21, 5, 27, 54, 9, 20, 22, 26, 0, 43, 34, 53, 19, 47, 16, 51, 11, 6, 31, 4, 50, 40, 46, 35, 36, 24, 23, 2, 13, 10, 1, 25, 33, 41, 30, 55]
    E = [28, 13, 15, 6, 19, 3, 22, 4, 5, 7, 26, 5, 2, 11, 27, 5, 29, 23, 1, 25, 3, 21, 23, 20, 22, 9, 29, 16, 14, 16, 1, 17, 18, 8, 0, 27, 29, 29, 10, 8, 26, 31, 7, 24, 12, 14, 13, 30]
    P = [17, 8, 6, 16, 9, 14, 18, 12, 22, 7, 29, 4, 5, 20, 23, 27, 26, 1, 15, 24, 11, 3, 30, 0, 2, 25, 10, 31, 21, 28, 13, 19]
    IP = [32, 34, 15, 6, 19, 3, 22, 4, 5, 36, 53, 42, 2, 11, 45, 17, 16, 23, 1, 62, 49, 21, 25, 20, 44, 47, 9, 38, 52, 28, 41, 43, 14, 51, 18, 56, 0, 57, 40, 61, 59, 10, 60, 54, 31, 7, 24, 12, 50, 63, 30, 46, 35, 48, 33, 27, 58, 55, 37, 29, 8, 39, 26, 13]
    IP_1 = [36, 18, 12, 5, 7, 8, 3, 45, 60, 26, 41, 13, 47, 63, 32, 2, 16, 15, 34, 4, 23, 21, 6, 17, 46, 22, 62, 55, 29, 59, 50, 44, 0, 54, 1, 52, 9, 58, 27, 61, 38, 30, 11, 31, 24, 14, 51, 25, 53, 20, 48, 33, 28, 10, 43, 57, 35, 37, 56, 40, 42, 39, 19, 49]

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

    def __init__(self, key):
        self.key = self.hex_to_bin(key)
        self.round_keys = self.generate_round_keys()

    @staticmethod
    def hex_to_bin(hex_num):
        return [int(bit) for bit in bin(int(hex_num, 16))[2:].zfill(len(hex_num) * 4)]

    @staticmethod
    def bin_to_hex(bits):
        return hex(int("".join(map(str, bits)), 2))[2:]

    @staticmethod
    def permutation(bits, table):
        return [bits[i] for i in table]

    def generate_round_keys(self):
        """Generate all 16 round keys."""
        initial_key = self.permutation(self.key, DES.PC_1)
        left, right = initial_key[:28], initial_key[28:]
        key_schedule = []
        for shift in DES.shift_bit:
            left, right = self.shift_left(left, shift), self.shift_left(right, shift)
            combined_key = left + right
            round_key = self.permutation(combined_key, DES.PC_2)
            key_schedule.append(round_key)
        return key_schedule

    @staticmethod
    def shift_left(block, shifts):
        return block[shifts:] + block[:shifts]

    def f_function(self, Ri, Ki):
        expanded_Ri = self.permutation(Ri, DES.E)
        xor_result = [b1 ^ b2 for b1, b2 in zip(expanded_Ri, Ki)]
        sbox_input = [xor_result[i:i+6] for i in range(0, len(xor_result), 6)]
        sbox_output = []
        for i, sbox in enumerate(DES.sboxen):
            row = (sbox_input[i][0] << 1) | sbox_input[i][5]
            col = int("".join(map(str, sbox_input[i][1:5])), 2)
            binary_value = bin(sbox[row][col])[2:].zfill(4)
            sbox_output.extend(int(bit) for bit in binary_value)
        return self.permutation(sbox_output, DES.P)

    def encrypt_block(self, plain_text):
        plain_bits = self.hex_to_bin(plain_text)
        permuted_plain = self.permutation(plain_bits, DES.IP)
        left, right = permuted_plain[:32], permuted_plain[32:]
        
        for round_key in self.round_keys:
            new_right = [l ^ f for l, f in zip(left, self.f_function(right, round_key))]
            left, right = right, new_right
        
        final_permutation = self.permutation(right + left, DES.IP_1)
        return self.bin_to_hex(final_permutation)

    def f_function_result(self, Ri_1, Ki):
        """Calculate specific f-function output for given inputs."""
        Ki_bin = self.hex_to_bin(Ki)
        Ri_1_bin = self.hex_to_bin(Ri_1)
        f_result = self.f_function(Ri_1_bin, Ki_bin)
        return self.bin_to_hex(f_result)
    
    def run(self, plain_text, Ri_1, Ki):
        """Executes the encryption process and f-function calculation, displaying results."""
        print("Das Ergebnis der f-Funktion in hexa:", self.f_function_result(Ri_1, Ki))
        print("Verschlüsselter Text:", self.encrypt_block(plain_text))

# Usage example
Key = "aff263f5eba068b2"
Plain_Text='d51d8da24285ff85'
Ri = "c9308881"
Ki= "850bff0a66ed"

des = DES(Key)
des.run(Plain_Text,Ri, Ki)
