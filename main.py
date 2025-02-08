import tkinter as tk
from tkinter import ttk, messagebox
from dataclasses import dataclass
import json
import csv
import random
from typing import Dict, List
from abc import ABC, abstractmethod

#===========================================
# MODEL
#===========================================
@dataclass
class ColumnConfig:
    """Defines the configuration structure for each column"""
    header: str
    values: List[str]

class ConfigurationManager(ABC):
    """Interface for configuration management"""
    @abstractmethod
    def save_config(self, config: Dict[str, List[str]]) -> None:
        pass

    @abstractmethod
    def load_config(self) -> Dict[str, List[str]]:
        pass

class JsonConfigurationManager(ConfigurationManager):
    """Implements saving/loading configurations in JSON"""
    def __init__(self, filename: str = "column_config.json"):
        self.filename = filename

    def save_config(self, config: Dict[str, List[str]]) -> None:
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4)

    def load_config(self) -> Dict[str, List[str]]:
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

class CsvGenerator:
    """Responsible for CSV file generation"""
    def generate_csv(self, filename: str, config: Dict[str, List[str]], num_rows: int) -> None:
        headers = list(config.keys())
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            for _ in range(num_rows):
                row = [random.choice(config[header]) for header in headers]
                writer.writerow(row)

#===========================================
# VIEW
#===========================================
class ColumnFrame(ttk.LabelFrame):
    """Frame for individual column configuration"""
    def __init__(self, parent, column_number: int, **kwargs):
        super().__init__(parent, text=f"Column {column_number}", **kwargs)
        self.column_number = column_number
        self.configure(width=300, height=400)
        self._create_widgets()

    def _create_widgets(self):
        """Creates all widgets for the column frame"""
        self._create_header_frame()
        self._create_values_frame()
        self._create_scrollable_values()

    def _create_header_frame(self):
        """Creates the frame for column header"""
        header_frame = ttk.Frame(self)
        header_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(header_frame, text="Header:").pack(side=tk.LEFT)
        self.header_entry = ttk.Entry(header_frame)
        self.header_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 0))

    def _create_values_frame(self):
        """Creates the frame for column values"""
        self.values_frame = ttk.LabelFrame(self, text="Values")
        self.values_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def _create_scrollable_values(self):
        """Creates scrollable area for values"""
        self.canvas = tk.Canvas(self.values_frame, height=300)
        scrollbar = ttk.Scrollbar(self.values_frame, orient="vertical", command=self.canvas.yview)
        
        self.scrollable_frame = ttk.Frame(self.canvas)
        self.scrollable_frame.bind("<Configure>", 
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        
        self.canvas_frame = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.bind('<Configure>', self._on_canvas_configure)
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.value_entries = []
        for _ in range(12):
            entry = ttk.Entry(self.scrollable_frame)
            entry.pack(pady=2, fill=tk.X, padx=5)
            self.value_entries.append(entry)

    def _on_canvas_configure(self, event):
        """Adjusts canvas frame width"""
        self.canvas.itemconfig(self.canvas_frame, width=event.width)

    def get_config(self) -> ColumnConfig:
        """Gets current column configuration"""
        header = self.header_entry.get().strip()
        values = [entry.get().strip() for entry in self.value_entries]
        return ColumnConfig(header=header, values=[v for v in values if v])

    def set_config(self, header: str, values: List[str]) -> None:
        """Sets column configuration"""
        self.header_entry.delete(0, tk.END)
        self.header_entry.insert(0, header)
        
        for entry, value in zip(self.value_entries, values + [''] * (12 - len(values))):
            entry.delete(0, tk.END)
            entry.insert(0, value)

class MainView(tk.Tk):
    """Main application window"""
    def __init__(self):
        super().__init__()
        self.title("Mock CSV Generator")
        self._configure_window()
        self.column_frames = []

    def _configure_window(self):
        """Configures window size and position"""
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = int(screen_width * 0.5)
        window_height = int(screen_height * 0.8)
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def create_widgets(self, controller):
        """Creates all interface widgets"""
        self._create_main_container()
        self._create_notebook()
        self._create_controls(controller)
        self._create_menu(controller)

    def _create_main_container(self):
        """Creates main container"""
        self.main_container = ttk.Frame(self)
        self.main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def _create_notebook(self):
        """Creates notebook with column tabs"""
        self.notebook = ttk.Notebook(self.main_container)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        for i in range(8):
            frame = ttk.Frame(self.notebook)
            self.notebook.add(frame, text=f"Column {i+1}")
            column_frame = ColumnFrame(frame, i + 1)
            column_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
            self.column_frames.append(column_frame)

    def _create_controls(self, controller):
        """Creates bottom controls"""
        controls_frame = ttk.Frame(self.main_container)
        controls_frame.pack(fill=tk.X, pady=10)

        ttk.Label(controls_frame, text="Number of rows:").pack(side=tk.LEFT, padx=5)
        self.rows_entry = ttk.Entry(controls_frame, width=10)
        self.rows_entry.insert(0, "500")
        self.rows_entry.pack(side=tk.LEFT, padx=5)

        ttk.Button(controls_frame, text="Generate CSV", 
                  command=controller.generate_csv).pack(side=tk.RIGHT, padx=5)
        ttk.Button(controls_frame, text="Save Configuration", 
                  command=controller.save_config).pack(side=tk.RIGHT, padx=5)

    def _create_menu(self, controller):
        """Creates menu bar"""
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        
        config_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Configuration", menu=config_menu)
        
        config_menu.add_command(label="Load from JSON", command=controller.load_json_config)
        config_menu.add_separator()
        config_menu.add_command(label="Save Configuration", command=controller.save_config)
        config_menu.add_command(label="Clear All", command=controller.clear_all)

#===========================================
# CONTROLLER
#===========================================
class CsvGeneratorController:
    """Main application controller"""
    def __init__(self):
        self.model = {
            'config_manager': JsonConfigurationManager(),
            'csv_generator': CsvGenerator()
        }
        self.view = MainView()
        self.view.create_widgets(self)

    def run(self):
        """Starts the application"""
        self.view.mainloop()

    def load_json_config(self):
        """Loads configuration from JSON file"""
        try:
            config = self.model['config_manager'].load_config()
            if not config:
                messagebox.showwarning("Warning", "No saved configuration found in JSON file.")
                return
            
            self.clear_all()
            for i, (header, values) in enumerate(config.items()):
                if i < len(self.view.column_frames):
                    self.view.column_frames[i].set_config(header, values)
            
            messagebox.showinfo("Success", "Configuration loaded from JSON successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load JSON configuration: {str(e)}")

    def clear_all(self):
        """Clears all configurations"""
        for frame in self.view.column_frames:
            frame.set_config("", [""] * 12)

    def save_config(self):
        """Saves current configuration"""
        config = {}
        for frame in self.view.column_frames:
            column_config = frame.get_config()
            if column_config.header and column_config.values:
                config[column_config.header] = column_config.values

        if not config:
            messagebox.showerror("Error", "At least one column must be configured")
            return

        self.model['config_manager'].save_config(config)
        messagebox.showinfo("Success", "Configuration saved successfully!")

    def generate_csv(self):
        """Generates CSV file with current configuration"""
        try:
            num_rows = int(self.view.rows_entry.get())
            if num_rows <= 0:
                raise ValueError("Number of rows must be positive")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        config = {}
        for frame in self.view.column_frames:
            column_config = frame.get_config()
            if column_config.header and column_config.values:
                config[column_config.header] = column_config.values

        if not config:
            messagebox.showerror("Error", "At least one column must be configured")
            return

        try:
            self.model['csv_generator'].generate_csv("mokup-00.csv", config, num_rows)
            messagebox.showinfo("Success", "CSV file generated successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate CSV: {str(e)}")

if __name__ == "__main__":
    app = CsvGeneratorController()
    app.run()