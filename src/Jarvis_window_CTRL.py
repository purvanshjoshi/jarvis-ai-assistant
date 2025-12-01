# Jarvis Window and Application Control Module
# Manages application launching, window focusing, and system control

import os
import subprocess
import logging
import sys

try:
    import pygetwindow as gw
except ImportError:
    gw = None

try:
    import pyautogui
except ImportError:
    pyautogui = None

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Application command mappings
APP_MAPPINGS = {
    'notepad': 'notepad',
    'calculator': 'calc',
    'chrome': r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    'vlc': r'C:\Program Files\VLC\vlc.exe',
    'cmd': 'cmd',
    'powershell': 'powershell',
    'vs code': r'C:\Users\%USERNAME%\AppData\Local\Programs\Microsoft VS Code\Code.exe',
}


class WindowManager:
    """Manages application windows and focus"""
    
    def __init__(self):
        self.window_cache = {}
    
    def focus_window(self, window_title):
        """Focus a window by title"""
        if not gw:
            logger.warning("pygetwindow not available")
            return False
        
        window_title = window_title.lower().strip()
        
        for window in gw.getAllWindows():
            if window_title in window.title.lower():
                if window.isMinimized:
                    window.restore()
                window.activate()
                return True
        
        return False
    
    def open_application(self, app_name):
        """Open an application by name"""
        app_name = app_name.lower().strip()
        
        if app_name in APP_MAPPINGS:
            command = APP_MAPPINGS[app_name]
            try:
                if sys.platform == 'win32':
                    os.startfile(command)
                else:
                    subprocess.Popen(['open', command])
                
                logger.info(f"Opened application: {app_name}")
                return True
            except Exception as e:
                logger.error(f"Failed to open {app_name}: {str(e)}")
                return False
        
        logger.warning(f"Unknown application: {app_name}")
        return False
    
    def close_window(self, window_title):
        """Close a window by title"""
        if not gw:
            logger.warning("pygetwindow not available")
            return False
        
        window_title = window_title.lower().strip()
        
        for window in gw.getAllWindows():
            if window_title in window.title.lower():
                window.close()
                logger.info(f"Closed window: {window_title}")
                return True
        
        return False
    
    def list_windows(self):
        """List all open windows"""
        if not gw:
            return []
        
        return [w.title for w in gw.getAllWindows()]


class CommandExecutor:
    """Executes system commands and operations"""
    
    def __init__(self):
        self.window_manager = WindowManager()
    
    def execute(self, command):
        """Execute a command"""
        command = command.lower().strip()
        
        if command.startswith('open '):
            app = command.replace('open ', '').strip()
            return self.window_manager.open_application(app)
        
        elif command.startswith('close '):
            window = command.replace('close ', '').strip()
            return self.window_manager.close_window(window)
        
        elif command == 'list windows':
            windows = self.window_manager.list_windows()
            logger.info(f"Open windows: {len(windows)}")
            return True
        
        else:
            logger.warning(f"Unknown command: {command}")
            return False


if __name__ == "__main__":
    executor = CommandExecutor()
    print("Window Control Module Initialized")
    print("Available commands: open [app], close [window], list windows")
