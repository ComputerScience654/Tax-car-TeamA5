"""
นายจิณณวัตร ปัจฉิม  465415241002 
นายวรรธนัย กิ่งไทร   465415241012
CSS46541N
"""
def calculate_tax_car(cc,car_age):
    # คำนวณภาษีรถแบบปกติตาม cc
    if cc == 1200:
        base_tax = (600 * 0.5) + (600 * 1.5)
    elif cc == 1900:
        base_tax = (600 * 0.5) + (1200 * 1.5) + (100 * 4)
    elif cc == 2000:
        base_tax = (600 * 0.5) + (1200 * 1.5) + (200 * 4)
    elif cc == 3000:
        base_tax = (600 * 0.5) + (1200 * 1.5) + (1200 * 4)
    else:
        print("Not this choice,please choose again.")
    
    # การลดหย่อนภาษี
    if 6 <= car_age <= 10:
        discount_rate = (car_age - 5) * 10  
        tax = base_tax * (100 - discount_rate) / 100
    else:
        tax = base_tax

    return tax
# แสดงตัวเลือก
def main():
    print("Program calculate tax_car")
    print("You choose your cc car")
    print("1. 1200 cc")
    print("2. 1900 cc")
    print("3. 2000 cc")
    print("4. 3000 cc")

    choice = int(input("You enter 1/2/3/4: "))

    cc_car = {1:1200, 2:1900, 3:2000, 4:3000} # กำหนดให้ choice 1 = 1200 cc เป็นต้น 
    if choice in cc_car:
        car_age = int(input("Enter your car's age (in years): ")) # กรอกอายุรถเพื่อเช็คว่าลดหย่อนภาษีได้เท่าไร
        if car_age < 0: # เช็คว่ามีีการกรอกอายุรถน้อยกว่า 0 หรือไม่
            print("Error: Age of car must be non-negative.") 
        else:
            tax = calculate_tax_car(cc_car[choice],car_age)
            print(f"Your car tax = {tax:.2f} baht")
    else:
        print("This option is not available yet!")

if __name__ == "__main__":
    main()  