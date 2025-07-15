import numpy as np

# --- 1. Define Parameters ---
B = 2  # Number of blades
R = 0.1  # Propeller radius in meters
N_elements = 20  # Number of blade elements
r_elements = np.linspace(0.01 * R, R, N_elements) # Radii for each element, avoiding the hub center


def get_chord(r):
    return 0.02 # Example: constant chord

def get_blade_angle(r):
    return np.deg2rad(15) # Example: constant 15 degrees pitch


def get_CL_CD(alpha):
    CL = 2 * np.pi * alpha 
    CD = 0.01 + 0.02 * alpha**2 
    return CL, CD

RPM = 6000 #
Omega = RPM * (2 * np.pi / 60) 
V_inf = 0 
rho = 1.225

# --- 2. Iterative Calculation for Each Blade Element ---
total_thrust = 0
total_torque = 0

for i, r_i in enumerate(r_elements):
    dr = r_elements[i] - (r_elements[i-1] if i > 0 else 0)
    if i == 0: # For the first element, approximate dr
        dr = r_elements[1] - r_elements[0]

   
    a = 0.1 
    a_prime = 0.01 
    tolerance = 1e-4
    max_iterations = 100

    for iteration in range(max_iterations):
        phi_old = np.arctan((V_inf * (1 + a)) / (Omega * r_i * (1 - a_prime)))
        alpha_old = get_blade_angle(r_i) - phi_old
        CL, CD = get_CL_CD(alpha_old)

        W_old = np.sqrt((V_inf * (1 + a))**2 + (Omega * r_i * (1 - a_prime))**2)

        # Differential forces based on current a, a_prime
        dL = 0.5 * rho * W_old**2 * get_chord(r_i) * CL * dr
        dD = 0.5 * rho * W_old**2 * get_chord(r_i) * CD * dr

        # Convert to thrust and torque components
        dT_element = dL * np.cos(phi_old) - dD * np.sin(phi_old)
        dQ_element = (dL * np.sin(phi_old) + dD * np.cos(phi_old)) * r_i

    
        break # Remove this in a real iterative solver


    total_thrust += dT_element
    total_torque += dQ_element

# --- 3. Summing Up for Total Propeller Performance ---
Total_Thrust_Propeller = B * total_thrust
Total_Torque_Propeller = B * total_torque
Power_Required = Total_Torque_Propeller * Omega

if V_inf > 0:
    Efficiency = (Total_Thrust_Propeller * V_inf) / Power_Required
else:
    Efficiency = "N/A (Hover Condition)" # Or calculate figure of merit

print(f"Total Thrust: {Total_Thrust_Propeller:.3f} N")
print(f"Total Torque: {Total_Torque_Propeller:.3f} Nm")
print(f"Power Required: {Power_Required:.3f} W")
print(f"Efficiency: {Efficiency}")