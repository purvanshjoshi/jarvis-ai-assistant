# Installation Guide - J.A.R.V.I.S

This guide will help you install and set up the J.A.R.V.I.S Advanced AI Assistant System on your computer.

## System Requirements

Before you begin, make sure your system meets the following requirements:

### Minimum Requirements
- **OS**: Windows 10/11, macOS 10.14+, or Linux (Ubuntu 20.04+)
- **Python**: 3.8 or higher
- **RAM**: 4GB minimum (8GB recommended for optimal performance)
- **Disk Space**: 500MB for installation + dependencies
- **Internet Connection**: Required for API services and initial setup
- **Webcam**: Optional but recommended for camera features
- **Microphone**: Required for voice control features

### Recommended Requirements
- **OS**: Windows 11 or latest Linux distribution
- **Python**: 3.10 or higher
- **RAM**: 8GB or more
- **GPU**: NVIDIA GPU with CUDA support for accelerated processing
- **Disk Space**: 1GB+ SSD for better performance

## Installation Steps

### Step 1: Clone the Repository

```bash
# Clone the repository from GitHub
git clone https://github.com/purvanshjoshi/jarvis-ai-assistant.git

# Navigate to the project directory
cd jarvis-ai-assistant
```

### Step 2: Create a Virtual Environment

A virtual environment isolates your project dependencies from your system Python:

#### On Windows:
```bash
python -m venv venv
venv\\Scripts\\activate
```

#### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt, indicating the virtual environment is active.

### Step 3: Install Dependencies

```bash
# Upgrade pip to the latest version
pip install --upgrade pip

# Install all required packages
pip install -r requirements.txt
```

This will install all necessary dependencies including:
- GUI frameworks (PyQt5, tkinter)
- Speech recognition libraries
- Image processing tools
- System monitoring utilities
- And more...

### Step 4: Configure Environment Variables

1. **Copy the example environment file**:
   ```bash
   cp .env.example .env
   ```

2. **Edit the `.env` file** with your preferred editor:
   - Open `.env` in any text editor
   - Set your configuration values
   - Save the file

3. **Key configurations to set**:
   - `APP_NAME`: Your preferred application name
   - `DEBUG`: Set to False for production
   - `VOICE_ENABLED`: Enable/disable voice control
   - `CAMERA_ENABLED`: Enable/disable camera features
   - `API_KEYS`: Add your OpenAI/Google API keys if using external services

### Step 5: Verify Installation

```bash
# Check Python version
python --version

# Check pip packages
pip list | grep -E "PyQt5|opencv|numpy"

# Test imports
python -c "import src.jarvis_gui; print('J.A.R.V.I.S imported successfully')"
```

## Running J.A.R.V.I.S

### Start the Application

Make sure your virtual environment is activated, then run:

```bash
# Navigate to the project directory
cd jarvis-ai-assistant

# Activate virtual environment (if not already activated)
# On Windows: venv\\Scripts\\activate
# On macOS/Linux: source venv/bin/activate

# Run the main application
python -m src.jarvis_gui
```

The J.A.R.V.I.S GUI should launch in a new window.

### First Run Setup

On first run, you may be prompted to:
1. Configure system permissions
2. Authorize microphone access
3. Set up camera device
4. Configure voice settings
5. Complete memory system initialization

## Troubleshooting

### Common Issues and Solutions

#### Issue: "Python not found" or "command not recognized"
**Solution**: 
- Ensure Python is installed and added to your system PATH
- On Windows, check "Add Python to PATH" during installation
- Restart your terminal after installing Python

#### Issue: "Module not found" errors
**Solution**:
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt` again
- Delete `.venv` folder and recreate it

#### Issue: Permission denied errors on Linux/macOS
**Solution**:
```bash
chmod +x src/*.py
sudo chown -R $USER jarvis-ai-assistant
```

#### Issue: Camera/Microphone not detected
**Solution**:
- Check device is properly connected
- Verify permissions in system settings
- Update audio/video drivers
- Check `.env` configuration

#### Issue: GUI won't start
**Solution**:
- Ensure PyQt5 is installed: `pip install PyQt5==5.15.7`
- Try running in debug mode for error messages
- Check display settings on Linux: `export DISPLAY=:0`

### Getting Help

If you encounter issues:
1. Check the [GitHub Issues](https://github.com/purvanshjoshi/jarvis-ai-assistant/issues) page
2. Review existing discussions in GitHub Discussions
3. Check error logs in the `logs/` directory
4. Create a new issue with detailed error information

## Updating J.A.R.V.I.S

To update to the latest version:

```bash
# Pull the latest code
git pull origin main

# Update dependencies
pip install -r requirements.txt --upgrade

# Restart the application
```

## Uninstalling J.A.R.V.I.S

To remove J.A.R.V.I.S:

```bash
# Deactivate virtual environment
deactivate

# Remove the project directory
rm -rf jarvis-ai-assistant  # On Windows: rmdir /s jarvis-ai-assistant
```

## Next Steps

After installation, you may want to:
- Read the [README.md](README.md) for feature overview
- Check [CONTRIBUTING.md](CONTRIBUTING.md) to contribute
- Review the configuration guide in [.env.example](.env.example)
- Explore the source code in the `src/` directory

## Support

For issues or questions:
- Create an issue on GitHub
- Check existing documentation
- Review the CONTRIBUTING guidelines

---

**Happy using J.A.R.V.I.S! 🔖**
