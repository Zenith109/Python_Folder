# Function to simulate a traffic light
# It is required to make 2 user defined functions trafficLight() and light().
def trafficLight():
    # Prompt the user to enter the colour of the traffic light
    signal = input("Enter the colour of the traffic light: ")
    
    # Check if the entered signal is valid
    if signal not in ("RED", "YELLOW", "GREEN"):
        print("Please enter a valid Traffic Light colour in CAPITALS")
    else:
        # Call the light function to get the corresponding action value
        value = light(signal)
        
        # Determine the action based on the value returned by light function
        if value == 0:
            print("STOP, Your Life is Precious.")
        elif value == 1:
            print("PLEASE GO SLOW.")
        else:
            print("GO!, Thank you for being patient.")
# Function ends here

# Function to return a value based on the traffic light colour
def light(colour):
    if colour == "RED":
        return 0
    elif colour == "YELLOW":
        return 1
    else:
        return 2
# Function ends here

# Call the trafficLight function to start the simulation
trafficLight()

# Print a safety message
print("SPEED THRILLS BUT KILLS")