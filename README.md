# Mock CSV Generator

**Mock CSV Generator** is a desktop application, developed in Python and Tkinter, that allows you to create custom CSV files based on user-defined configurations. It's ideal for generating mock data for testing and prototyping.

![alt text]()

## Features

1. **Custom CSV Generation**:
   - Configure columns with custom headers and values.
   - Define the number of rows to generate.

2. **Configuration Management**:
   - **Save Configurations**: Save the current configuration (headers and column values) to a JSON file.
   - **Load Configurations**: Load previously saved configurations from a JSON file or the `DATA_CONFIG.py` module.
   - **Clear Configurations**: Reset all columns to their initial state.

3. **User-Friendly GUI**:
   - Intuitive interface built with Tkinter.
   - Supports up to 8 configurable columns.

## How It Works

1. **Column Configuration**:
   - Add a header for each column.
   - Populate possible values for each column.

2. **CSV Generation**:
   - Enter the desired number of rows.
   - Click "Generate CSV" to create the `mokup-00.csv` file in the same directory as the program.

3. **Configuration Management**:
   - Use the "Configuration" menu to save or load your settings:
     - "Load from JSON" to load from the JSON file.
     - "Load from DATA_CONFIG.py" to load from a Python module (if available).
     - "Save Configuration" to save the current setup.
     - "Clear All" to reset all configurations.

## How to Run

1. **Prerequisites**:
   - Python 3.8 or higher.
   - Standard libraries (`tkinter`, `json`, `csv`).

2. **Execution**:
   - Download the code.
   - Run the `main.py` file:
     ```bash
     python main.py
     ```

3. **Generated Files**:
   - Saved configurations will be stored in `column_config.json`.
   - The generated CSV file will be saved as `mokup-00.csv`.

## Technologies Used

- **Python 3.13.1**: Logic and backend.
- **Tkinter**: Simple and responsive graphical interface.

## Project Structure

- `main.py`: Main application code.
- `column_config.json`: (optional) Stores user-saved configurations.
- `DATA_CONFIG.py`: (optional) Allows loading custom configurations via a Python module.

## Autor

- **Desenvolvedor**: Hipolito Rodrigues
- **Data de Criação**: 23/01/2025
- **Última Atualização**: 27/01/2025
- **Versão Atual**: 1.3.4

---

## Licença

This project is licensed under the [CC0 1.0 Universal (Public Domain)](https://creativecommons.org/publicdomain/zero/1.0/) license. This means you can copy, modify, distribute, and perform the work, even for commercial purposes, all without asking permission.
```
