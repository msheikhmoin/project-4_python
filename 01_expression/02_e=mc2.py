
C = 299792458  

while True:
    
    try:
        m = float(input("\nEnter kilos of mass: "))
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        continue
    E = m * C**2
    print("\ne = m * C^2...\n")
    print(f"m = {m} kg")
    print(f"C = {C} m/s")
    print(f"{E} joules of energy!\n")

    again = input("Do you want to calculate again? (yes/no): ").strip().lower()
    if again != "yes":
        break
