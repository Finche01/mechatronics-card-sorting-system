# Contributing to Automated Card Sorting System

Thank you for your interest in contributing to this project! This document provides guidelines for contributing improvements, bug fixes, and enhancements.

## 🎯 Project Context

This is an **educational project** developed as part of the Mechatronics Engineering program at Seneca College. While we welcome contributions, please understand that:

- This represents completed coursework (March 2026)
- The physical system may not be actively maintained
- Major architectural changes should be discussed first

## 🤝 Ways to Contribute

### 1. Bug Reports
If you find issues with the code or documentation:

- **Search existing issues** first to avoid duplicates
- Use the issue template when creating new reports
- Include:
  - Clear description of the problem
  - Steps to reproduce
  - Expected vs actual behavior
  - System information (PLC model, Python version, etc.)
  - Relevant logs or screenshots

### 2. Documentation Improvements
Documentation contributions are highly valued:

- Fix typos or unclear explanations
- Add missing procedures or troubleshooting steps
- Improve code comments
- Translate documentation to other languages
- Add diagrams or visual aids

### 3. Code Contributions

**Good First Issues**:
- Vision system template improvements
- Node-RED dashboard enhancements
- Additional safety checks
- Better error handling
- Code cleanup and refactoring

**Substantial Changes**:
- New sorting algorithms
- Alternative communication protocols
- Multi-card pickup capability
- Advanced vision features (OCR, custom cards)

## 📋 Contribution Process

### 1. Fork & Clone

```bash
# Fork the repository on GitHub
# Clone your fork
git clone https://github.com/YOUR_USERNAME/automated-card-sorter.git
cd automated-card-sorter

# Add upstream remote
git remote add upstream https://github.com/ORIGINAL_OWNER/automated-card-sorter.git
```

### 2. Create a Branch

```bash
# Create a feature branch
git checkout -b feature/your-feature-name

# Or a bugfix branch
git checkout -b bugfix/issue-number-description
```

**Branch Naming**:
- `feature/` - New features or enhancements
- `bugfix/` - Bug fixes
- `docs/` - Documentation updates
- `refactor/` - Code refactoring
- `test/` - Test additions or improvements

### 3. Make Changes

**Code Style**:

**Python** (PEP 8):
```python
# Use 4 spaces for indentation
# Descriptive variable names
# Docstrings for functions

def classify_card(image, templates):
    """
    Classify a playing card using template matching.
    
    Args:
        image: OpenCV image array of card
        templates: Dictionary of rank/suit templates
        
    Returns:
        tuple: (rank, suit, confidence)
    """
    # Implementation
```

**JavaScript/Node-RED**:
```javascript
// Use camelCase for variables
// Semicolons required
// Comments for complex logic

function processMqttMessage(topic, payload) {
    const data = JSON.parse(payload);
    // Handle classification result
}
```

**Ladder Logic/PLC**:
- Descriptive rung comments
- Logical grouping of functions
- Consistent addressing scheme

**Testing**:
- Add tests for new features
- Verify existing tests still pass
- Test on actual hardware if possible (or document simulation)

### 4. Commit Changes

```bash
# Stage your changes
git add .

# Commit with descriptive message
git commit -m "Add feature: description of what was added"
```

**Commit Message Format**:
```
<type>: <short summary>

<detailed description>

Fixes #<issue-number>
```

Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`

Examples:
```
feat: Add automatic suction cup cleaning sequence

Implements periodic cleaning after every 100 cycles using 
a stationary brush at coordinate (200, 200, 5). Reduces 
manual maintenance requirements.

Fixes #42
```

```
fix: Correct photoelectric sensor chatter issue

Added 100ms debounce timer to prevent rapid switching
during Z-axis descent. Improves reliability of slowdown logic.

Fixes #18
```

### 5. Push & Pull Request

```bash
# Push to your fork
git push origin feature/your-feature-name
```

**On GitHub**:
1. Navigate to your fork
2. Click "Compare & pull request"
3. Fill out the PR template:
   - Clear title
   - Description of changes
   - Related issue numbers
   - Testing performed
   - Screenshots/videos if applicable

## ✅ Pull Request Checklist

Before submitting:

- [ ] Code follows project style guidelines
- [ ] Comments added for complex logic
- [ ] Documentation updated (if needed)
- [ ] Tests added/updated (if applicable)
- [ ] Existing tests pass
- [ ] No breaking changes (or clearly documented)
- [ ] Commit messages are clear and descriptive
- [ ] PR description explains the "why" not just the "what"

## 🔍 Review Process

1. **Automated Checks**: Linting and tests run automatically
2. **Code Review**: Maintainers review for quality and fit
3. **Discussion**: Feedback and requested changes
4. **Approval**: Once approved, PR will be merged

**Review Timeline**: We aim to respond within 1 week, but as this is an academic project, response times may vary.

## 🎨 Specific Contribution Areas

### Vision System Improvements
**Location**: `software/vision/`

Ideas:
- Better template matching algorithms
- Support for custom card decks
- Multi-card detection
- Confidence threshold tuning
- Alternative classification methods (neural networks)

**Requirements**:
- Maintain compatibility with existing MQTT interface
- Preserve JSON message format
- Update documentation

### PLC Programming Enhancements
**Location**: `software/plc/`

Ideas:
- Optimized motion profiles
- Additional safety interlocks
- Error recovery routines
- Diagnostic counters

**Requirements**:
- Maintain Modbus register map
- Document all changes to control logic
- Test thoroughly on simulator before hardware

### Node-RED Dashboard
**Location**: `software/node-red/`

Ideas:
- Enhanced data visualization
- Historical performance tracking
- Email/SMS alerts for errors
- Remote monitoring capabilities

**Requirements**:
- Backward compatible with existing flows
- Responsive design for mobile
- Maintain existing MQTT/Modbus structure

### Hardware Modifications
**Location**: `hardware/`

Ideas:
- Alternative end-effector designs
- Cable management improvements
- Sensor mounting solutions
- Enclosure designs

**Requirements**:
- Full CAD models provided
- Bill of materials
- Assembly instructions
- Integration notes

## 🐛 Bug Fix Priority

**High Priority**:
- Safety-related issues
- Data loss or corruption
- System crashes or hangs
- Incorrect motion commands

**Medium Priority**:
- Incorrect classifications
- UI bugs
- Performance degradation
- Documentation errors

**Low Priority**:
- Minor UI inconsistencies
- Code style issues
- Nice-to-have features

## 📞 Questions?

If you're unsure about:
- Whether a feature fits the project scope
- How to implement something
- Best practices for the system

**Contact**:
- Open a GitHub Discussion
- Email: jcraven@myseneca.ca or jpark83@myseneca.ca

We're happy to help guide contributions!

## 📜 Code of Conduct

Be respectful and professional:
- Constructive feedback only
- No harassment or discrimination
- Assume good intentions
- Help newcomers learn

## 🙏 Recognition

All contributors will be acknowledged in:
- README.md Contributors section
- Release notes for substantial contributions
- Project documentation

Thank you for helping improve this project! 🎉

---

**Last Updated**: March 2026
