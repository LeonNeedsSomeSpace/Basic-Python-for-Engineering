#Calculate Voltages, Currents and Resistances using Ohm's Law
#Define a function that calculates voltage
def compute_voltage(current, resistance):
    return current * resistance
#Define a function that calculates voltage
#Resistance cannot equal to 0 here!
def compute_current(voltage, resistance):
    if resistance != 0:
        return voltage / resistance
    else:
        return None
#Define a function that calculates resistance
#Current cannot equal to 0 here!
def compute_resistance(voltage, current):
    if current != 0:
        return voltage / current
    else:
        return None

#Define the main function
def main():
    print("Ohm's Law Calculator\n")
    print("Type V for Voltage, I for Current, R for Resistance, and press enter\n")

#Depending on what the input is (V, I or R), the program will initiate different calculations
    choice = input("Enter (V/I/R): \n").strip().upper()

    if choice == 'V':
        try:
            I = float(input("Enter current (I in amperes): "))
            R = float(input("Enter resistance (R in ohms): "))
            V = compute_voltage(I, R)
            print(f"Voltage (V) = {V:.2f} V")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    elif choice == 'I':
        try:
            V = float(input("Enter voltage (V in volts): "))
            R = float(input("Enter resistance (R in ohms): "))
            I = compute_current(V, R)
            if I is not None:
                print(f"Current (I) = {I:.2f} A")
            else:
                print("Error: Resistance cannot be zero.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    elif choice == 'R':
        try:
            V = float(input("Enter voltage (V in volts): "))
            I = float(input("Enter current (I in amperes): "))
            R = compute_resistance(V, I)
            if R is not None:
                print(f"Resistance (R) = {R:.2f} Ohms")
            else:
                print("Error: Current cannot be zero.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    else:
        print("Invalid choice. Please enter V, I, or R.")

#main function needs to be called
if __name__ == "__main__":
    main()





