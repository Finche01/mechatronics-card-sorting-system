# Changelog

All notable changes to the Mechatronics Card Sorting System will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Planned Features
- Web-based remote monitoring dashboard
- Multi-deck sorting capability
- Machine learning model improvements
- Mobile app for system control
- Real-time statistics and analytics
- Support for custom card designs

---

## [1.0.0] - 2024-XX-XX

### Initial Release

#### Added
- **Vision System**
  - Card detection using OpenCV
  - Suit and rank classification
  - Real-time image processing
  - Confidence scoring for classifications
  - Support for standard playing cards

- **Motion Control**
  - 3-axis gantry control via PLC
  - Automated homing sequence
  - Path planning with obstacle avoidance
  - Soft limits and collision detection
  - Adjustable speed and acceleration

- **PLC Communication**
  - Modbus TCP support
  - Siemens S7 protocol support (via SNAP7)
  - Allen-Bradley support (via pycomm3)
  - Robust error handling and reconnection

- **User Interface**
  - Live camera feed display
  - Real-time position monitoring
  - System status indicators
  - Manual jog controls
  - Automatic and manual operating modes

- **Configuration**
  - YAML-based configuration file
  - Easy position teaching
  - Adjustable vision parameters
  - Customizable sorting rules

- **Safety Features**
  - Emergency stop integration
  - Soft limit enforcement
  - Collision detection
  - Error logging and recovery

- **Documentation**
  - Comprehensive README
  - Hardware setup guide
  - Software installation guide
  - User guide with calibration procedures
  - API reference
  - Troubleshooting guide
  - Contributing guidelines

#### Hardware Support
- Stepper motor control (NEMA 23)
- USB camera integration (1080p)
- Pneumatic gripper control
- Limit switch monitoring
- Emergency stop circuit

#### Performance
- Sorting speed: Up to 60 cards/minute
- Detection accuracy: >98%
- Positioning accuracy: ±0.5mm
- Processing time: <100ms per card

---

## Version History Format

### [X.Y.Z] - YYYY-MM-DD

#### Added
- New features

#### Changed
- Changes to existing functionality

#### Deprecated
- Soon-to-be removed features

#### Removed
- Removed features

#### Fixed
- Bug fixes

#### Security
- Security updates

---

## Future Roadmap

### Version 1.1.0 (Q2 2024)
- [ ] Web dashboard for monitoring
- [ ] Enhanced statistics and reporting
- [ ] Support for additional card types
- [ ] Improved error recovery
- [ ] Performance optimizations

### Version 1.2.0 (Q3 2024)
- [ ] Multi-deck sorting
- [ ] Advanced path planning
- [ ] Machine learning improvements
- [ ] Cloud integration
- [ ] API for external integrations

### Version 2.0.0 (Q4 2024)
- [ ] Complete UI redesign
- [ ] Mobile application
- [ ] Advanced analytics dashboard
- [ ] Multi-user support
- [ ] Remote diagnostics

---

## Versioning Strategy

This project uses Semantic Versioning:

- **MAJOR** version (X.0.0): Incompatible API changes
- **MINOR** version (0.X.0): New functionality (backwards compatible)
- **PATCH** version (0.0.X): Bug fixes (backwards compatible)

---

## How to Update

To upgrade to the latest version:

```bash
# Pull latest code
git pull origin main

# Update dependencies
pip install -r requirements.txt --upgrade

# Check for breaking changes in this file
# Run migration scripts if provided

# Test system
python tests/test_installation.py
```

---

## Migration Guides

### From Pre-1.0 to 1.0.0

**Configuration Changes:**
- New YAML format (convert old configs)
- Motion parameters now in mm instead of steps
- Vision threshold range changed to 0-255

**API Changes:**
- `GantryController.moveTo()` → `GantryController.move_to()`
- Position units changed from steps to millimeters
- New required config sections added

**Migration Script:**
```bash
python tools/migrate_config_to_v1.py old_config.cfg config.yaml
```

---

## Support

For questions about changes or upgrades:
- Check [User Guide](USER_GUIDE.md)
- Review [API Reference](API.md)
- Open [GitHub Issue](https://github.com/yourusername/Mechatronics-card-sorting-system/issues)

---

[← Back to Main README](README.md)
