# Contributing Guidelines

[← Back to Main README](README.md)

Thank you for your interest in contributing to the Mechatronics Card Sorting System! This document provides guidelines for contributing to the project.

---

## 🌟 Ways to Contribute

- 🐛 **Report bugs** and issues
- 💡 **Suggest new features** or improvements
- 📝 **Improve documentation**
- 🔧 **Submit bug fixes**
- ✨ **Add new features**
- 🧪 **Write tests**
- 🎨 **Improve UI/UX**

---

## 🚀 Getting Started

### 1. Fork the Repository

Click the "Fork" button at the top right of the repository page.

### 2. Clone Your Fork

```bash
git clone https://github.com/your-username/Mechatronics-card-sorting-system.git
cd Mechatronics-card-sorting-system
```

### 3. Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt
```

### 4. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

**Branch naming conventions:**
- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation updates
- `refactor/` - Code refactoring
- `test/` - Adding tests

---

## 💻 Development Workflow

### Making Changes

1. **Write clean, readable code**
   - Follow PEP 8 style guide for Python
   - Use meaningful variable names
   - Add comments for complex logic

2. **Test your changes**
   ```bash
   # Run tests
   pytest tests/
   
   # Run specific test
   pytest tests/test_vision.py
   
   # Run with coverage
   pytest --cov=src tests/
   ```

3. **Update documentation**
   - Update relevant .md files
   - Add docstrings to new functions
   - Update README if needed

### Code Style

We follow PEP 8 with these additional guidelines:

```python
# Good: Clear, descriptive names
def detect_card_suit(image, threshold=127):
    """
    Detect the suit of a playing card from an image.
    
    Args:
        image (np.ndarray): Input image of card
        threshold (int): Binary threshold value (0-255)
        
    Returns:
        str: Detected suit ('hearts', 'diamonds', 'clubs', 'spades')
        or None if detection failed
    """
    # Implementation
    pass

# Bad: Unclear names, no documentation
def dcs(img, t=127):
    pass
```

**Import Organization:**
```python
# Standard library imports
import os
import sys
from typing import Optional, List

# Third-party imports
import cv2
import numpy as np

# Local imports
from src.vision import CardDetector
from src.motion import GantryController
```

### Running Linters

```bash
# Check code style
flake8 src/

# Auto-format code
black src/

# Sort imports
isort src/

# Type checking
mypy src/
```

---

## 🧪 Testing

### Writing Tests

Place tests in the `tests/` directory:

```python
# tests/test_vision.py
import pytest
from src.vision import CardDetector

def test_card_detection():
    """Test basic card detection functionality."""
    detector = CardDetector()
    # Load test image
    test_image = cv2.imread('tests/fixtures/test_card.jpg')
    
    # Detect card
    result = detector.detect(test_image)
    
    # Assert expected behavior
    assert result is not None
    assert result['suit'] == 'hearts'
    assert result['rank'] == 'A'
    assert result['confidence'] > 0.9

def test_invalid_image():
    """Test handling of invalid input."""
    detector = CardDetector()
    
    with pytest.raises(ValueError):
        detector.detect(None)
```

### Test Coverage

Aim for >80% code coverage:

```bash
pytest --cov=src --cov-report=html tests/
# Open htmlcov/index.html to view report
```

---

## 📝 Commit Guidelines

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

**Examples:**

```
feat(vision): add support for joker card detection

Implemented detection algorithm for joker cards using
template matching. Includes tests and documentation.

Closes #123
```

```
fix(motion): correct Z-axis homing direction

Z-axis was homing in wrong direction due to inverted
limit switch logic. Fixed by updating config parser.

Fixes #456
```

### Commit Best Practices

- ✅ **DO:** Make small, focused commits
- ✅ **DO:** Write clear commit messages
- ✅ **DO:** Reference issue numbers
- ❌ **DON'T:** Commit unfinished features
- ❌ **DON'T:** Commit commented-out code
- ❌ **DON'T:** Include large binary files

---

## 🔄 Pull Request Process

### Before Submitting

1. **Update your branch**
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Run all tests**
   ```bash
   pytest tests/
   ```

3. **Check code style**
   ```bash
   flake8 src/
   black --check src/
   ```

4. **Update documentation**
   - Add/update docstrings
   - Update relevant .md files
   - Add to CHANGELOG.md

### Submitting Pull Request

1. **Push your branch**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create Pull Request on GitHub**
   - Go to your fork on GitHub
   - Click "New Pull Request"
   - Fill out PR template

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Testing
- [ ] Tests pass locally
- [ ] Added new tests
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] No breaking changes (or documented)

## Screenshots (if applicable)
[Add screenshots for UI changes]

## Related Issues
Closes #123
```

### Review Process

1. **Automated Checks**
   - CI/CD pipeline runs tests
   - Linters check code style
   - Coverage report generated

2. **Code Review**
   - Maintainer reviews code
   - May request changes
   - Discuss in PR comments

3. **Approval & Merge**
   - Once approved, maintainer merges
   - Branch is deleted
   - Appears in next release

---

## 🐛 Reporting Bugs

### Before Reporting

- Search existing issues
- Try latest version
- Check [Troubleshooting Guide](TROUBLESHOOTING.md)

### Bug Report Template

```markdown
## Bug Description
Clear description of the bug

## Steps to Reproduce
1. Go to '...'
2. Click on '...'
3. See error

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Environment
- OS: [e.g., Windows 10, Ubuntu 22.04]
- Python version: [e.g., 3.11.2]
- Software version: [e.g., 1.0.0]
- Hardware: [PLC model, camera model]

## Screenshots/Logs
[Attach relevant screenshots or log files]

## Additional Context
Any other relevant information
```

---

## 💡 Suggesting Features

### Feature Request Template

```markdown
## Feature Description
Clear description of the feature

## Problem It Solves
What problem does this address?

## Proposed Solution
How should it work?

## Alternatives Considered
Other approaches you've thought about

## Additional Context
Mockups, examples, references
```

---

## 📚 Documentation

### Types of Documentation

1. **Code Comments**
   - Explain WHY, not WHAT
   - Document complex algorithms
   - Add TODOs for future work

2. **Docstrings**
   - All public functions/classes
   - Google style format
   - Include examples

3. **README Files**
   - Keep updated with changes
   - Add new sections as needed

4. **Wiki Pages** (coming soon)
   - Tutorials
   - Design decisions
   - Architecture docs

### Documentation Style

```python
def calculate_optimal_path(start, end, obstacles):
    """
    Calculate the shortest collision-free path between two points.
    
    Uses A* pathfinding algorithm with obstacle avoidance. The path
    is optimized for smooth motion by minimizing direction changes.
    
    Args:
        start (tuple): Starting position (x, y) in millimeters
        end (tuple): Target position (x, y) in millimeters
        obstacles (list): List of obstacle rectangles [(x, y, w, h), ...]
        
    Returns:
        list: List of waypoints [(x1, y1), (x2, y2), ...] or
              empty list if no path found
        
    Raises:
        ValueError: If start or end is out of bounds
        
    Example:
        >>> path = calculate_optimal_path((0, 0), (100, 100), [])
        >>> print(path)
        [(0, 0), (50, 50), (100, 100)]
    """
    pass
```

---

## 🏗️ Project Structure

Understanding the codebase:

```
Mechatronics-card-sorting-system/
├── src/
│   ├── vision/              # Computer vision modules
│   │   ├── __init__.py
│   │   ├── detector.py      # Card detection
│   │   └── classifier.py    # Suit/rank classification
│   ├── motion/              # Motion control
│   │   ├── __init__.py
│   │   ├── gantry.py        # Gantry controller
│   │   └── pathplanner.py   # Path planning
│   ├── plc/                 # PLC communication
│   │   ├── __init__.py
│   │   ├── modbus.py        # Modbus implementation
│   │   └── s7comm.py        # Siemens S7 implementation
│   └── gui/                 # User interface
│       ├── __init__.py
│       └── mainwindow.py    # Main GUI
├── tests/                   # All tests
├── config/                  # Configuration files
├── docs/                    # Additional documentation
├── tools/                   # Utility scripts
└── assets/                  # Images, icons, etc.
```

---

## 🎯 Development Priorities

Current focus areas:

### High Priority
- [ ] Improve card detection accuracy
- [ ] Add support for additional PLC models
- [ ] Performance optimization

### Medium Priority
- [ ] Web-based monitoring dashboard
- [ ] Multi-deck sorting
- [ ] Advanced statistics

### Low Priority
- [ ] Mobile app
- [ ] Cloud integration
- [ ] ML model improvements

---

## 🤝 Community Guidelines

### Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Help newcomers
- No harassment or discrimination

### Communication

- **GitHub Issues:** Bug reports, feature requests
- **Pull Requests:** Code contributions, discussions
- **Discussions:** General questions, ideas

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

## 🙏 Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Credited in release notes
- Thanked in README

---

## ❓ Questions?

- Check [User Guide](USER_GUIDE.md)
- Review [Troubleshooting](TROUBLESHOOTING.md)
- Open a Discussion on GitHub

---

**Thank you for contributing! 🎉**

[← Back to Main README](README.md)
