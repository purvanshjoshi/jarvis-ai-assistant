"""
J.A.R.V.I.S Configuration Settings Module

This module contains default configuration settings for the J.A.R.V.I.S system.
Edit these values to customize the behavior and features of the application.
"""

import os
from pathlib import Path

# ============================================================================
# APPLICATION SETTINGS
# ============================================================================

# Application name and version
APP_NAME = "J.A.R.V.I.S"
APP_VERSION = "1.0.0"

# Debug mode (set to False in production)
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

# Logging level: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

# ============================================================================
# DISPLAY AND THEME SETTINGS
# ============================================================================

# GUI Theme (default, dark, light)
THEME = os.getenv('THEME', 'dark')

# Window dimensions
WINDOW_WIDTH = int(os.getenv('WINDOW_WIDTH', 1200))
WINDOW_HEIGHT = int(os.getenv('WINDOW_HEIGHT', 800))

# Animation speed (milliseconds)
ANIMATION_SPEED = int(os.getenv('ANIMATION_SPEED', 300))

# Glow effect intensity (0.0 to 1.0)
GLOW_INTENSITY = float(os.getenv('GLOW_INTENSITY', 0.8))

# ============================================================================
# VOICE AND AUDIO SETTINGS
# ============================================================================

# Enable/disable voice control
VOICE_ENABLED = os.getenv('VOICE_ENABLED', 'True').lower() == 'true'

# Speech recognition language
SPEECH_RECOGNITION_LANGUAGE = os.getenv('SPEECH_LANGUAGE', 'en-US')

# Speech recognition engine: 'google', 'wit', 'bing'
SPEECH_ENGINE = os.getenv('SPEECH_ENGINE', 'google')

# Text-to-speech enabled
TTS_ENABLED = os.getenv('TTS_ENABLED', 'True').lower() == 'true'

# TTS Voice rate (0.5 to 2.0)
TTS_RATE = float(os.getenv('TTS_RATE', 1.0))

# ============================================================================
# CAMERA SETTINGS
# ============================================================================

# Enable/disable camera features
CAMERA_ENABLED = os.getenv('CAMERA_ENABLED', 'True').lower() == 'true'

# Camera device index (0 = default camera)
CAMERA_DEVICE = int(os.getenv('CAMERA_DEVICE', 0))

# Camera FPS (frames per second)
CAMERA_FPS = int(os.getenv('CAMERA_FPS', 30))

# Camera resolution
CAMERA_RESOLUTION_WIDTH = int(os.getenv('CAMERA_RESOLUTION_WIDTH', 640))
CAMERA_RESOLUTION_HEIGHT = int(os.getenv('CAMERA_RESOLUTION_HEIGHT', 480))

# Enable face detection
FACE_DETECTION = os.getenv('CAMERA_FACE_DETECTION', 'True').lower() == 'true'

# ============================================================================
# SYSTEM MONITORING SETTINGS
# ============================================================================

# Enable CPU monitoring
MONITOR_CPU = os.getenv('MONITOR_CPU', 'True').lower() == 'true'

# Enable memory monitoring
MONITOR_MEMORY = os.getenv('MONITOR_MEMORY', 'True').lower() == 'true'

# Enable disk monitoring
MONITOR_DISK = os.getenv('MONITOR_DISK', 'True').lower() == 'true'

# Enable temperature monitoring
MONITOR_TEMPERATURE = os.getenv('MONITOR_TEMPERATURE', 'True').lower() == 'true'

# Enable battery monitoring
MONITOR_BATTERY = os.getenv('MONITOR_BATTERY', 'True').lower() == 'true'

# Enable network monitoring
MONITOR_NETWORK = os.getenv('MONITOR_NETWORK', 'True').lower() == 'true'

# Update interval in milliseconds
MONITOR_UPDATE_INTERVAL = int(os.getenv('MONITOR_UPDATE_INTERVAL', 1000))

# ============================================================================
# MEMORY SYSTEM SETTINGS
# ============================================================================

# Enable memory system
MEMORY_ENABLED = os.getenv('MEMORY_ENABLED', 'True').lower() == 'true'

# Memory file path
MEMORY_FILE = os.getenv('MEMORY_FILE', 'memory/memory.json')

# Memory debug log path
MEMORY_DEBUG_LOG = os.getenv('MEMORY_DEBUG_LOG', 'memory/memory_debug.log')

# Enable memory backup
MEMORY_BACKUP_ENABLED = os.getenv('MEMORY_BACKUP_ENABLED', 'True').lower() == 'true'

# Backup interval (seconds)
MEMORY_BACKUP_INTERVAL = int(os.getenv('MEMORY_BACKUP_INTERVAL', 3600))

# ============================================================================
# FILE STORAGE PATHS
# ============================================================================

# Screenshot directory
SCREENSHOT_DIR = os.getenv('SCREENSHOT_DIR', 'screenshots/')

# Logs directory
LOG_DIR = os.getenv('LOG_DIR', 'logs/')

# Configuration directory
CONFIG_DIR = os.getenv('CONFIG_DIR', 'config/')

# ============================================================================
# SECURITY SETTINGS
# ============================================================================

# Enable memory encryption
ENCRYPT_MEMORY = os.getenv('ENCRYPT_MEMORY', 'False').lower() == 'true'

# Allow remote commands
ALLOW_REMOTE_COMMANDS = os.getenv('ALLOW_REMOTE_COMMANDS', 'False').lower() == 'true'

# Require authentication
REQUIRE_AUTHENTICATION = os.getenv('REQUIRE_AUTHENTICATION', 'False').lower() == 'true'

# ============================================================================
# API KEYS (Set these in .env file, not here)
# ============================================================================

# OpenAI API Key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')

# Google API Key
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY', '')

# ============================================================================
# PERFORMANCE SETTINGS
# ============================================================================

# Maximum processes to display
MAX_PROCESSES_DISPLAY = int(os.getenv('MAX_PROCESSES_DISPLAY', 10))

# Refresh rate (Hz)
REFRESH_RATE = int(os.getenv('REFRESH_RATE', 60))

# Enable GPU acceleration (if available)
GPU_ACCELERATION = os.getenv('GPU_ACCELERATION', 'False').lower() == 'true'


# ============================================================================
# CONFIGURATION CLASS
# ============================================================================

class Config:
    """Configuration class for accessing and updating settings."""
    
    def __init__(self):
        """Initialize configuration with default values."""
        self.app_name = APP_NAME
        self.app_version = APP_VERSION
        self.debug = DEBUG
        self.log_level = LOG_LEVEL
        self.theme = THEME
        self.voice_enabled = VOICE_ENABLED
        self.camera_enabled = CAMERA_ENABLED
        self.memory_enabled = MEMORY_ENABLED
    
    def get(self, key, default=None):
        """Get configuration value by key."""
        return globals().get(key, default)
    
    def set(self, key, value):
        """Set configuration value."""
        globals()[key] = value
    
    def to_dict(self):
        """Convert configuration to dictionary."""
        config_dict = {}
        for key, value in globals().items():
            if not key.startswith('_') and key.isupper():
                config_dict[key] = value
        return config_dict


# ============================================================================
# DEFAULT CONFIGURATION INSTANCE
# ============================================================================

config = Config()


if __name__ == '__main__':
    # Print configuration for debugging
    print(f"{APP_NAME} v{APP_VERSION} - Configuration Settings")
    print("=" * 50)
    print(config.to_dict())
