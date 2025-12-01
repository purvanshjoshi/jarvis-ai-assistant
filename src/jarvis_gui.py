# J.A.R.V.I.S - Advanced GUI Interface
# Main HUD Display System v2.2
# Features: Real-time monitoring, live camera, voice control integration

import sys
import os
from datetime import datetime

try:
    from PySide6.QtCore import Qt, QTimer
    from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
    from PySide6.QtGui import QFont, QColor
except ImportError:
    print("PySide6 not installed. Install with: pip install PySide6")
    sys.exit(1)

import psutil


class JarvisHUD(QMainWindow):
    """Main J.A.R.V.I.S HUD Interface"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("J.A.R.V.I.S - Advanced AI Assistant System v2.2")
        self.setGeometry(100, 100, 1280, 800)
        self.setup_ui()
        self.setup_timers()
        
    def setup_ui(self):
        """Setup the main UI components"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout(central_widget)
        
        # Title
        title = QLabel("J.A.R.V.I.S - VISION INTERFACE v2.2")
        title.setFont(QFont("Segoe UI", 24, QFont.Bold))
        title.setStyleSheet("color: #00D4FF; background: rgba(10, 14, 20, 200);")
        layout.addWidget(title)
        
        # System Status
        self.status_label = QLabel("Initializing systems...")
        self.status_label.setFont(QFont("Consolas", 12))
        self.status_label.setStyleSheet("color: #DCECFB;")
        layout.addWidget(self.status_label)
        
        # Time
        self.time_label = QLabel()
        self.time_label.setFont(QFont("Consolas", 14, QFont.Bold))
        self.time_label.setStyleSheet("color: #EAF6FF;")
        layout.addWidget(self.time_label)
        
        layout.addStretch()
        
        # Set dark background
        central_widget.setStyleSheet("background-color: rgb(10, 14, 20);")
        
    def setup_timers(self):
        """Setup timers for updates"""
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_status)
        self.timer.start(1000)  # Update every second
        
    def update_status(self):
        """Update system status display"""
        try:
            cpu_percent = psutil.cpu_percent(interval=0.1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            status_text = f"CPU: {cpu_percent}% | Memory: {memory.percent}% | Disk: {disk.percent}%"
            self.status_label.setText(status_text)
            
            current_time = datetime.now().strftime("%H:%M:%S")
            self.time_label.setText(current_time)
            
        except Exception as e:
            self.status_label.setText(f"Error: {str(e)}")


def main():
    """Main entry point for the Jarvis GUI"""
    app = QApplication(sys.argv)
    hud = JarvisHUD()
    hud.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
