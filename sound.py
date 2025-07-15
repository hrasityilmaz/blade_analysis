import numpy as np
import scipy.io.wavfile as wavfile


B = 2                 # Number of blades
RPM = 6000            # Propeller RPM
Total_Thrust_Propeller = 2.5 # Example N
Power_Required = 250  # Example W
R = 0.05 # Propeller radius in meters

# --- 1. Calculate Blade Passing Frequency (BPF) ---
bpf = B * (RPM / 60)
print(f"Blade Passing Frequency (BPF): {bpf:.2f} Hz")


amplitude_scale = np.sqrt(Power_Required / 100) * 0.2 

max_amplitude = 0.8 * 32767 
target_amplitude = max_amplitude * amplitude_scale

if target_amplitude > max_amplitude:
    target_amplitude = max_amplitude

print(f"Target amplitude for sine wave: {target_amplitude:.0f} (out of {max_amplitude:.0f})")

sample_rate = 44100  
duration = 3.0       
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)


tone_wave = target_amplitude * np.sin(2 * np.pi * bpf * t)

harmonic_2_wave = (target_amplitude * 0.4) * np.sin(2 * np.pi * (2 * bpf) * t) # 40% of fundamental
harmonic_3_wave = (target_amplitude * 0.2) * np.sin(2 * np.pi * (3 * bpf) * t) # 20% of fundamental


broadband_noise = (max_amplitude * 0.05) * np.random.randn(len(t)) # 5% of max amplitude random noise


combined_wave = tone_wave + harmonic_2_wave + harmonic_3_wave + broadband_noise


combined_wave = np.int16(combined_wave)

# --- 4. Save to WAV File ---
output_filename = "drone_propeller_sound.wav"
wavfile.write(output_filename, sample_rate, combined_wave)

print(f"Sound file '{output_filename}' created successfully.")
