class DoubleStackCalculator:
    def __init__(self, max_size):
        self.max_size = max_size
        self.num_stack = [None] * max_size  # Stack untuk angka
        self.op_stack = [None] * max_size   # Stack untuk operator
        self.top_num = -1                   # Pointer untuk stack angka
        self.top_op = -1                    # Pointer untuk stack operator

    # Operasi push untuk stack angka
    def push_num(self, num):
        if self.top_num < self.max_size - 1:
            self.top_num += 1
            self.num_stack[self.top_num] = num
        else:
            print("Num Stack Overflow!")

    # Operasi push untuk stack operator
    def push_op(self, op):
        if self.top_op < self.max_size - 1:
            self.top_op += 1
            self.op_stack[self.top_op] = op
        else:
            print("Op Stack Overflow!")

    # Operasi pop untuk stack angka
    def pop_num(self):
        if self.top_num >= 0:
            num = self.num_stack[self.top_num]
            self.top_num -= 1
            return num
        else:
            print("Num Stack Underflow!")
            return None

    # Operasi pop untuk stack operator
    def pop_op(self):
        if self.top_op >= 0:
            op = self.op_stack[self.top_op]
            self.top_op -= 1
            return op
        else:
            print("Op Stack Underflow!")
            return None

    # Fungsi untuk mengevaluasi ekspresi
    def evaluate(self):
        while self.top_op != -1:
            operator = self.pop_op()
            right_operand = self.pop_num()
            left_operand = self.pop_num()

            result = self.apply_operator(left_operand, right_operand, operator)
            self.push_num(result)

        # Hasil akhir ada di top_num
        return self.pop_num()

    # Fungsi untuk menerapkan operator
    def apply_operator(self, left, right, operator):
        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        elif operator == '/':
            return left / right
        else:
            raise ValueError(f"Operator tidak valid: {operator}")


# Fungsi untuk menjalankan kalkulator
def run_calculator(expression):
    calc = DoubleStackCalculator(10)  # Ukuran stack bisa disesuaikan
    i = 0

    while i < len(expression):
        if expression[i].isdigit():
            # Jika menemukan angka, masukkan ke stack angka
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            calc.push_num(num)
        elif expression[i] in "+-*/":
            # Jika menemukan operator, masukkan ke stack operator
            calc.push_op(expression[i])
            i += 1
        else:
            i += 1  # Abaikan karakter yang tidak dikenal (misalnya spasi)

    # Evaluasi ekspresi
    return calc.evaluate()


# Contoh penggunaan kalkulator
expression = "7+6*2-4/20"  # Harus menghasilkan 10.0
result = run_calculator(expression)
print(f"Hasil dari {expression} adalah: {result}")