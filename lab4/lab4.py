def calculate_square_area(side):
    """Функція повертає площу квадрата за заданою стороною"""
    area = side ** 2
    return area

def main():
    s = float(input("Введіть довжину сторони квадрата: "))
    
    square_area = calculate_square_area(s)
    
    print(f"Площа квадрата зі стороною {s} дорівнює {square_area}")
 
if __name__ == "__main__":
    main()