# Photodetector Data Analysis (Python)

A comprehensive Python-based toolkit for analyzing photodetector (optoelectronic) characterization data. This repository includes scripts for processing raw data and calculating key figures of merit (FOMs) for photodetectors.

## 📊 Modules & Features

- **`Photodetector_IV_Analyzer.py`**: Analyzes Current-Voltage (I-V) characteristics under dark and illuminated conditions.
- **`Responsivity_Analysis.py`**: Calculates the responsivity (\(R = I_{ph} / P_{inc}\)) of the device.
- **`Detectivity_Analysis.py`**: Calculates specific detectivity (\(D^*\)) taking into account the noise current.
- **`Noise_analysis.py`**: Processes noise data to evaluate the signal-to-noise ratio.
- **`Stability_Rise_Decay_Time.py`**: Extracts rise time and decay time from transient photocurrent measurements.
- **`Photocurrent_sensitivity.py`**: Analyzes photocurrent and sensitivity metrics.

## 📁 Repository Structure
- `data/`: Contains raw experimental data (Excel/CSV files).
- `results/`: Output directory for generated plots and analyzed data.
- `*.py`: Individual Python scripts for specific analyses.
- `requirements.txt`: Required Python dependencies.

## 🛠 Technologies Used
- **Python 3**
- **Pandas**, **NumPy** (Data manipulation & numerical analysis)
- **Matplotlib**, **Seaborn** (Data visualization)
- **SciPy** (Curve fitting & signal processing)

## 🚀 How to Run
1. Clone the repository:
   `git clone https://github.com/Shadi-Ghafari/Photodetector-Data-Analysis.git`
2. Install dependencies:
   `pip install -r requirements.txt`
3. Place your raw data in the `data/` folder.
4. Run the desired script:
   `python Responsivity_Analysis.py`
**Shadi Ghafari** (Materials Scientist / Optoelectronics Researcher)
*Expert in UV-Vis, XRD, and Photodetector characterization data analysis.*
