# 🚁 Propeller Performance & Basic Noise Simulation

This project provides a Python script to perform a simplified Blade Element Momentum Theory (BEMT) calculation for a N-bladed propeller and then generate a basic audio file simulating its dominant noise signature. It's a conceptual tool for understanding how propeller design parameters influence both aerodynamic performance and perceived sound.

## ✨ Features

* **Blade Element Momentum Theory (BEMT)**: Calculates thrust, torque, and power for a N-bladed propeller based on geometric and flight parameters.

* **Basic Noise Estimation**: Estimates the fundamental Blade Passing Frequency (BPF) and uses a simplified approach to scale the amplitude of the generated sound based on calculated power.

* **Sound File Generation**: Creates a `.wav` audio file that simulates the propeller's hum, including the fundamental BPF and its first few harmonics, along with a basic broadband noise component.

* **Customizable Parameters**: Easily modify propeller dimensions, RPM, and flight conditions.

## ⚙️ How It Works

1.  **BEMT Calculation**:

    * The propeller blade is divided into small radial elements.

    * For each element, the local angle of attack is iteratively calculated, considering induced velocities.

    * Lift and drag forces are determined using simplified airfoil characteristics.

    * These forces are then integrated across all blade elements to find the total thrust, torque, and power.

2.  **Noise Generation**:

    * The primary tonal noise frequency (Blade Passing Frequency - BPF) is calculated directly from the number of blades and RPM.

    * The amplitude of the generated sound is scaled proportionally to the calculated power required by the propeller (a simplified assumption).

    * A sine wave at the BPF, along with its first few harmonics, is synthesized.

    * A basic "broadband" noise (simulating turbulence) is added as white noise.

    * All components are combined and saved as a 16-bit WAV audio file.

## 🚀 Installation

1.  **Clone the repository (or copy the code)**:

    ```
    git clone https://github.com/hrasityilmaz/blade_analysis
    cd blade_analysis

    ```

2.  **Install Python**: Ensure you have Python 3.x installed.

3.  **Install Dependencies**:

    ```
    pip install numpy scipy

    ```

    *(Optional: For direct audio playback in Python, you might need `pydub` and `simpleaudio`)*

    ```
    pip install pydub simpleaudio

    ```

## 🎮 Usage

1.  **Open the Python script**:
    Locate the Python file (e.g., `blade.py`) in your text editor.

2.  **Adjust Parameters**:
    Modify the `BEMT Results (Example values)` section at the top of the script to change propeller parameters (e.g., `B`, `RPM`, `R`, `Power_Required`, `Total_Thrust_Propeller`). You can also adjust the `amplitude_scale` in the sound generation section to fine-tune the relative loudness.

3.  **Run the script**:

    ```
    python blade.py
    python sound.py

    ```

The script will print the calculated thrust, torque, and power to the console. if you want to check sound will be how -> use sound.py also

## 📊 Output

* **Console Output**:

    ```
    --- BEMT Results (for 2 blades)---
  Total Thrust: 5.611 N
  Total Torque: 0.003 Nm
  Power Required: 1.874 W
  Efficiency: N/A (Hover Condition)
  Propeller Efficiency: N/A (Hover Condition)
    
  Blade Passing Frequency (BPF): 233.33 Hz
  Target amplitude for sine wave: 1 (out of 32767)
  Sound file 'drone_propeller_sound.wav' created successfully.

    ```

* **`drone_propeller_sound.wav`**: An audio file that you can play using any media player to hear the simulated propeller noise.

## ⚠️ Limitations

This project is intended for conceptual understanding and basic demonstration. It has several simplifications:

* **Simplified Airfoil Data**: The `get_CL_CD` function uses a very basic approximation. Real airfoil data is much more complex.

* **Basic BEMT Implementation**: A full BEMT solver would include more robust convergence criteria, root/tip loss models, and more detailed blade element properties.

* **Highly Simplified Acoustic Model**:

    * The relationship between power/thrust and sound amplitude is a rough estimate, not based on rigorous aeroacoustic equations.

    * Broadband noise is simulated as simple white noise, not actual turbulent flow noise.

    * Harmonic amplitudes are arbitrary.

    * It does **not** account for complex phenomena like vortex shedding noise, blade-vortex interaction, or directivity (how sound changes with listening angle).

    * Environmental factors (air absorption, ground reflection) are not considered.

* **No Psychoacoustic Metrics**: The output is a raw sound file; it doesn't provide metrics like loudness (Sones), sharpness, or annoyance.

For accurate propeller design and noise prediction, specialized commercial or research-grade CFD and aeroacoustic software is required.

## 💡 Future Enhancements

* Implement a more robust BEMT solver with proper convergence and tip/root loss models.

* Integrate actual airfoil data lookup tables.

* Explore more advanced empirical noise models for better amplitude and broadband noise characteristics.

* Add a simple GUI (probably flutter or java) for easier interaction.

* Allow customization of the number of blade elements for BEMT.

* Add options for different propeller geometries (e.g., swept blades).

## 🤝 Contributing

Contributions are welcome! If you have ideas for improvements, bug fixes, or want to add more advanced features, please feel free to Fork the repository.

## 📄 License

This project is licensed under the MIT License
