# Contributing to J.A.R.V.I.S

Thank you for your interest in contributing to the J.A.R.V.I.S Advanced AI Assistant System! We welcome contributions from the community to help improve this project.

## How to Contribute

### Reporting Bugs

1. **Check existing issues** before reporting a bug to avoid duplicates
2. **Use the bug report template** when creating a new issue
3. **Provide detailed information**:
   - System specifications (OS, Python version)
   - Steps to reproduce
   - Expected vs. actual behavior
   - Error messages or logs
   - Screenshots if applicable

### Requesting Features

1. **Check existing feature requests** first
2. **Provide clear use cases** for your feature request
3. **Explain the expected behavior** and benefits
4. **Consider implementation complexity** and alternatives

### Submitting Pull Requests

#### Before You Start

1. **Fork the repository** on GitHub
2. **Create a new branch** with a descriptive name:
   ```
   git checkout -b feature/your-feature-name
   git checkout -b fix/your-bug-fix
   ```
3. **Make sure you have the latest code**:
   ```
   git pull upstream main
   ```

#### Development Setup

1. **Clone your fork**:
   ```
   git clone https://github.com/YOUR_USERNAME/jarvis-ai-assistant.git
   cd jarvis-ai-assistant
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

#### Making Changes

1. **Keep commits atomic and meaningful** - one feature or fix per commit
2. **Write clear commit messages**:
   ```
   [Feature] Add voice recognition enhancement
   [Fix] Resolve memory leak in camera module
   [Docs] Update installation guide
   ```

3. **Follow the existing code style**:
   - Use descriptive variable names
   - Add comments for complex logic
   - Follow PEP 8 style guidelines

4. **Test your changes**:
   - Test on multiple systems if possible
   - Verify no regressions in existing features
   - Include test output in PR description

#### Submitting the Pull Request

1. **Push your branch**:
   ```
   git push origin feature/your-feature-name
   ```

2. **Create a Pull Request** with:
   - Clear title and description
   - Reference to related issues
   - List of changes made
   - Testing information
   - Screenshots for UI changes

3. **Address review feedback**:
   - Respond to comments professionally
   - Make requested changes in new commits
   - Re-request review after making changes

## Code of Conduct

This project adheres to the Contributor Covenant Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

### Our Pledge

- We are committed to providing a welcoming and inclusive environment
- We respect all contributors regardless of background
- We treat all feedback with consideration

## Project Structure

```
jarvis-ai-assistant/
├── src/                 # Main source code
│   ├── jarvis_gui.py    # GUI implementation
│   ├── Jarvis_prompts.py # Command processor
│   ├── Jarvis_window_CTRL.py # Window control
│   └── Jarvis_file_opner.py  # File management
├── memory/              # Memory system storage
├── screenshots/         # Screenshot storage
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
└── .env.example         # Configuration template
```

## Testing

- Test your changes thoroughly before submitting
- Include test results in the PR description
- Report any system-specific issues

## Documentation

- Update README.md if your changes affect usage
- Add docstrings to new functions
- Document configuration changes in .env.example

## Questions?

If you have questions about contributing, feel free to:
- Open a discussion in the GitHub Discussions tab
- Check existing documentation in the repo
- Review closed PRs for similar changes

## Recognition

All contributors will be recognized in the project documentation. Thank you for helping make J.A.R.V.I.S better!

---

**Happy Contributing! 🚀**
