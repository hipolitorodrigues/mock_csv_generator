from typing import Dict, List
import tkinter as tk
from tkinter import ttk, messagebox
from dataclasses import dataclass
import json
import csv
import random
from pathlib import Path
from abc import ABC, abstractmethod

@dataclass
class ColumnConfig:
    """Represents the configuration for a single column."""
    header: str
    values: List[str]

class ConfigurationManager(ABC):
    """Abstract base class for configuration management."""
    @abstractmethod
    def save_config(self, config: Dict[str, List[str]]) -> None:
        pass

    @abstractmethod
    def load_config(self) -> Dict[str, List[str]]:
        pass

class JsonConfigurationManager(ConfigurationManager):
    """Handles saving and loading configuration from JSON file."""
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
    """Handles CSV file generation."""
    def generate_csv(self, filename: str, config: Dict[str, List[str]], num_rows: int) -> None:
        headers = list(config.keys())
        
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            
            for _ in range(num_rows):
                row = [random.choice(config[header]) for header in headers]
                writer.writerow(row)

class ColumnFrame(ttk.LabelFrame):
    """Frame component for a single column configuration."""
    def __init__(self, parent, column_number: int, **kwargs):
        super().__init__(parent, text=f"Column {column_number}", **kwargs)
        self.column_number = column_number
        
        # Configure frame size
        self.configure(width=300, height=400)
        
        # Header
        header_frame = ttk.Frame(self)
        header_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(header_frame, text="Header:").pack(side=tk.LEFT)
        self.header_entry = ttk.Entry(header_frame)
        self.header_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 0))
        
        # Values
        values_frame = ttk.LabelFrame(self, text="Values")
        values_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Create canvas and scrollbar for values
        self.canvas = tk.Canvas(values_frame, height=300)
        scrollbar = ttk.Scrollbar(values_frame, orient="vertical", command=self.canvas.yview)
        
        # Create frame for value entries
        self.scrollable_frame = ttk.Frame(self.canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        # Create window inside canvas
        self.canvas_frame = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.bind('<Configure>', self._on_canvas_configure)
        
        # Configure canvas scroll
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack canvas and scrollbar
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Add value entries
        self.value_entries = []
        for i in range(12):
            entry = ttk.Entry(self.scrollable_frame)
            entry.pack(pady=2, fill=tk.X, padx=5)
            self.value_entries.append(entry)
        
        # Configure canvas scroll region
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def _on_canvas_configure(self, event):
        """Handle canvas resize event."""
        self.canvas.itemconfig(self.canvas_frame, width=event.width)

    def get_config(self) -> ColumnConfig:
        """Get the current column configuration."""
        header = self.header_entry.get().strip()
        values = [entry.get().strip() for entry in self.value_entries]
        return ColumnConfig(header=header, values=[v for v in values if v])

    def set_config(self, header: str, values: List[str]) -> None:
        """Set the column configuration."""
        self.header_entry.delete(0, tk.END)
        self.header_entry.insert(0, header)
        
        for entry, value in zip(self.value_entries, values + [''] * (12 - len(values))):
            entry.delete(0, tk.END)
            entry.insert(0, value)

class CsvGeneratorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Mock CSV Generator")
        
        # Get screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        # Calculate window size (80% of screen)
        window_width = int(screen_width * 0.5)
        window_height = int(screen_height * 0.8)
        
        # Center the window
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        self.config_manager = JsonConfigurationManager()
        self.csv_generator = CsvGenerator()
        
        self.create_widgets()
        self.create_menu()
        self.load_initial_config()

    def create_menu(self):
        """Create menu bar with configuration options."""
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        
        # Create Configuration menu
        config_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Configuration", menu=config_menu)
        
        config_menu.add_command(label="Load from JSON", command=self.load_json_config)
        config_menu.add_command(label="Load from DATA_CONFIG.py", command=self.load_data_config)
        config_menu.add_separator()
        config_menu.add_command(label="Save Configuration", command=self.save_config)
        config_menu.add_command(label="Clear All", command=self.clear_all)

    def create_widgets(self):
        """Create all GUI widgets."""
        # Main container
        main_container = ttk.Frame(self)
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create notebook for column pages
        self.notebook = ttk.Notebook(main_container)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Create pages for columns
        self.column_frames = []
        for i in range(8):
            frame = ttk.Frame(self.notebook)
            self.notebook.add(frame, text=f"Column {i+1}")
            
            column_frame = ColumnFrame(frame, i + 1)
            column_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
            self.column_frames.append(column_frame)

        # Bottom controls
        controls_frame = ttk.Frame(main_container)
        controls_frame.pack(fill=tk.X, pady=10)

        # Number of rows entry
        ttk.Label(controls_frame, text="Number of rows:").pack(side=tk.LEFT, padx=5)
        self.rows_entry = ttk.Entry(controls_frame, width=10)
        self.rows_entry.insert(0, "500")
        self.rows_entry.pack(side=tk.LEFT, padx=5)

        # Buttons
        ttk.Button(controls_frame, text="Generate CSV", command=self.generate_csv).pack(side=tk.RIGHT, padx=5)
        ttk.Button(controls_frame, text="Save Configuration", command=self.save_config).pack(side=tk.RIGHT, padx=5)

    def load_initial_config(self):
        """Load initial configuration from DATA_CONFIG."""
        try:
            from data_config import DATA_CONFIG
            for frame, (header, values) in zip(self.column_frames, DATA_CONFIG.items()):
                frame.set_config(header, values)
        except ImportError:
            pass

    def load_json_config(self):
        """Load configuration from JSON file."""
        try:
            config = self.config_manager.load_config()
            if not config:
                messagebox.showwarning("Warning", "No saved configuration found in JSON file.")
                return
                
            self.clear_all()  # Clear current configuration
            
            for i, (header, values) in enumerate(config.items()):
                if i < len(self.column_frames):
                    self.column_frames[i].set_config(header, values)
            
            messagebox.showinfo("Success", "Configuration loaded from JSON successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load JSON configuration: {str(e)}")

    def load_data_config(self):
        """Load configuration from DATA_CONFIG.py."""
        try:
            from data_config import DATA_CONFIG
            
            self.clear_all()  # Clear current configuration
            
            for frame, (header, values) in zip(self.column_frames, DATA_CONFIG.items()):
                frame.set_config(header, values)
                
            messagebox.showinfo("Success", "Configuration loaded from DATA_CONFIG.py successfully!")
            
        except ImportError:
            messagebox.showerror("Error", "DATA_CONFIG.py not found or invalid.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load DATA_CONFIG.py: {str(e)}")

    def clear_all(self):
        """Clear all column configurations."""
        for frame in self.column_frames:
            frame.set_config("", [""] * 12)

    def save_config(self):
        """Save current configuration."""
        config = {}
        for frame in self.column_frames:
            column_config = frame.get_config()
            if column_config.header and column_config.values:  # Only save if header and values exist
                config[column_config.header] = column_config.values

        if not config:
            messagebox.showerror("Error", "At least one column must be configured")
            return

        self.config_manager.save_config(config)
        messagebox.showinfo("Success", "Configuration saved successfully!")

    def generate_csv(self):
        """Generate CSV file with current configuration."""
        try:
            num_rows = int(self.rows_entry.get())
            if num_rows <= 0:
                raise ValueError("Number of rows must be positive")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        config = {}
        for frame in self.column_frames:
            column_config = frame.get_config()
            if column_config.header and column_config.values:  # Only include if header and values exist
                config[column_config.header] = column_config.values

        if not config:
            messagebox.showerror("Error", "At least one column must be configured")
            return

        try:
            self.csv_generator.generate_csv("mokup-00.csv", config, num_rows)
            messagebox.showinfo("Success", "CSV file generated successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate CSV: {str(e)}")

if __name__ == "__main__":
    app = CsvGeneratorGUI()
    app.mainloop()