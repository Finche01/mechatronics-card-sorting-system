# API Reference

[← Back to Main README](README.md)

---

## 📦 Module Overview

The Mechatronics Card Sorting System consists of several main modules:

- **Vision**: Card detection and classification
- **Motion**: Gantry control and path planning
- **PLC**: Hardware communication
- **GUI**: User interface components

---

## 🎴 Vision Module

### CardDetector

Detects playing cards in images using computer vision.

```python
from src.vision import CardDetector

detector = CardDetector(config)
```

#### Methods

##### `detect(image) -> Optional[Dict]`

Detects a single card in the image.

**Parameters:**
- `image` (np.ndarray): Input image (BGR format)

**Returns:**
- `dict` or `None`: Card information or None if no card detected
  ```python
  {
      'bbox': (x, y, width, height),  # Bounding box
      'contour': np.ndarray,           # Card contour
      'angle': float,                  # Rotation angle
      'area': int                      # Contour area
  }
  ```

**Example:**
```python
import cv2

# Load image
image = cv2.imread('card.jpg')

# Detect card
result = detector.detect(image)

if result:
    x, y, w, h = result['bbox']
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
```

##### `detect_multiple(image, max_cards=10) -> List[Dict]`

Detects multiple cards in a single image.

**Parameters:**
- `image` (np.ndarray): Input image
- `max_cards` (int): Maximum number of cards to detect

**Returns:**
- `list`: List of detected cards (same format as `detect()`)

**Example:**
```python
cards = detector.detect_multiple(image, max_cards=5)
print(f"Found {len(cards)} cards")
```

---

### CardClassifier

Classifies card suit and rank.

```python
from src.vision import CardClassifier

classifier = CardClassifier(model_path='models/classifier.pkl')
```

#### Methods

##### `classify(card_image) -> Dict`

Classifies a card image.

**Parameters:**
- `card_image` (np.ndarray): Cropped card image

**Returns:**
- `dict`: Classification results
  ```python
  {
      'suit': str,        # 'hearts', 'diamonds', 'clubs', 'spades'
      'rank': str,        # 'A', '2'-'10', 'J', 'Q', 'K'
      'confidence': float # 0.0 to 1.0
  }
  ```

**Example:**
```python
result = classifier.classify(card_image)

if result['confidence'] > 0.9:
    print(f"Detected: {result['rank']} of {result['suit']}")
else:
    print("Low confidence detection")
```

##### `train(training_data, labels) -> None`

Train the classifier on new data.

**Parameters:**
- `training_data` (np.ndarray): Array of card images
- `labels` (list): Corresponding labels

**Example:**
```python
# Load training data
X_train, y_train = load_training_data('data/cards/')

# Train classifier
classifier.train(X_train, y_train)

# Save model
classifier.save('models/new_classifier.pkl')
```

---

## 🤖 Motion Module

### GantryController

Controls the 3-axis gantry system.

```python
from src.motion import GantryController

gantry = GantryController(config, plc_client)
```

#### Methods

##### `home() -> bool`

Homes all axes to limit switches.

**Returns:**
- `bool`: True if homing successful

**Example:**
```python
if gantry.home():
    print("Homing complete")
else:
    print("Homing failed")
```

##### `move_to(x, y, z, speed=None) -> bool`

Move to absolute position.

**Parameters:**
- `x` (float): X position in mm
- `y` (float): Y position in mm
- `z` (float): Z position in mm
- `speed` (float, optional): Speed in mm/s

**Returns:**
- `bool`: True if movement successful

**Example:**
```python
# Move to pickup position
success = gantry.move_to(100, 200, 50, speed=150)

# Wait for motion to complete
gantry.wait_until_idle()
```

##### `move_relative(dx, dy, dz) -> bool`

Move relative to current position.

**Parameters:**
- `dx` (float): X offset in mm
- `dy` (float): Y offset in mm
- `dz` (float): Z offset in mm

**Example:**
```python
# Move 10mm to the right
gantry.move_relative(10, 0, 0)
```

##### `get_position() -> Tuple[float, float, float]`

Get current position.

**Returns:**
- `tuple`: Current (x, y, z) position in mm

**Example:**
```python
x, y, z = gantry.get_position()
print(f"Current position: X={x}, Y={y}, Z={z}")
```

##### `set_speed(speed) -> None`

Set movement speed for all axes.

**Parameters:**
- `speed` (float): Speed in mm/s (max defined in config)

##### `emergency_stop() -> None`

Immediately stop all motion.

**Example:**
```python
# In event handler
if emergency_detected:
    gantry.emergency_stop()
```

---

### PathPlanner

Plans optimal collision-free paths.

```python
from src.motion import PathPlanner

planner = PathPlanner(config)
```

#### Methods

##### `plan_path(start, goal, obstacles=None) -> List[Tuple]`

Calculate path between two points.

**Parameters:**
- `start` (tuple): Starting (x, y) position
- `goal` (tuple): Target (x, y) position
- `obstacles` (list, optional): List of obstacle rectangles

**Returns:**
- `list`: List of waypoints [(x1, y1), (x2, y2), ...]

**Example:**
```python
# Plan path avoiding obstacles
obstacles = [(150, 150, 50, 50), (300, 200, 50, 50)]
path = planner.plan_path((0, 0), (400, 300), obstacles)

# Execute path
for x, y in path:
    gantry.move_to(x, y, z=50)
    gantry.wait_until_idle()
```

---

## 🔌 PLC Module

### ModbusClient

Communicate with PLCs via Modbus TCP/RTU.

```python
from src.plc import ModbusClient

plc = ModbusClient(host='192.168.0.10', port=502)
```

#### Methods

##### `connect() -> bool`

Establish connection to PLC.

**Returns:**
- `bool`: True if connected successfully

##### `disconnect() -> None`

Close connection to PLC.

##### `read_coil(address) -> bool`

Read single coil (digital input/output).

**Parameters:**
- `address` (int): Coil address

**Returns:**
- `bool`: Coil state (True/False)

**Example:**
```python
# Read limit switch
limit_switch = plc.read_coil(1000)
if limit_switch:
    print("Limit switch activated")
```

##### `write_coil(address, value) -> bool`

Write single coil.

**Parameters:**
- `address` (int): Coil address
- `value` (bool): State to write

**Returns:**
- `bool`: True if write successful

**Example:**
```python
# Activate solenoid valve
plc.write_coil(2000, True)
time.sleep(0.5)
plc.write_coil(2000, False)
```

##### `read_register(address) -> int`

Read holding register.

**Parameters:**
- `address` (int): Register address

**Returns:**
- `int`: Register value

##### `write_register(address, value) -> bool`

Write holding register.

**Parameters:**
- `address` (int): Register address
- `value` (int): Value to write

**Example:**
```python
# Set speed setpoint
plc.write_register(4000, 200)  # 200 mm/s
```

##### `read_registers(address, count) -> List[int]`

Read multiple consecutive registers.

**Example:**
```python
# Read current position (3 registers: X, Y, Z)
position = plc.read_registers(5000, 3)
x, y, z = position
```

---

### S7Client

Communicate with Siemens S7 PLCs.

```python
from src.plc import S7Client

plc = S7Client(host='192.168.0.10', rack=0, slot=1)
```

#### Methods

Similar to ModbusClient, with S7-specific additions:

##### `read_db(db_number, start, size) -> bytes`

Read data block.

**Parameters:**
- `db_number` (int): Data block number
- `start` (int): Start byte
- `size` (int): Number of bytes

**Example:**
```python
# Read DB1 starting at byte 0, 10 bytes
data = plc.read_db(1, 0, 10)
```

##### `write_db(db_number, start, data) -> bool`

Write to data block.

**Example:**
```python
import struct

# Write float to DB1 at byte 0
value = 123.45
data = struct.pack('>f', value)  # Big-endian float
plc.write_db(1, 0, data)
```

---

## 🖥️ GUI Module

### MainWindow

Main application window.

```python
from src.gui import MainWindow

app = QApplication(sys.argv)
window = MainWindow(config)
window.show()
```

#### Signals (PyQt)

##### `start_sorting()`

Emitted when user clicks Start button.

##### `stop_sorting()`

Emitted when user clicks Stop button.

##### `emergency_stop()`

Emitted when emergency stop triggered.

#### Slots

##### `update_camera_frame(frame)`

Update camera display.

**Parameters:**
- `frame` (np.ndarray): Image to display

##### `update_status(message, level='info')`

Update status bar.

**Parameters:**
- `message` (str): Status message
- `level` (str): 'info', 'warning', or 'error'

##### `update_position(x, y, z)`

Update position display.

---

## 🎛️ Configuration

### Config Class

Manages system configuration.

```python
from src.config import Config

config = Config('config/config.yaml')
```

#### Properties

##### `camera`

Camera configuration.
```python
config.camera.index        # Camera device ID
config.camera.resolution   # (width, height)
config.camera.fps          # Frames per second
```

##### `motion`

Motion configuration.
```python
config.motion.steps_per_mm_x   # X-axis steps/mm
config.motion.max_speed        # Maximum speed mm/s
config.motion.x_min            # X-axis minimum limit
```

##### `plc`

PLC configuration.
```python
config.plc.type    # 'modbus', 'snap7', 'pycomm3'
config.plc.ip      # PLC IP address
config.plc.port    # Communication port
```

#### Methods

##### `save(filepath=None)`

Save configuration to file.

##### `reload()`

Reload configuration from file.

---

## 🎯 Complete Example

### Basic Sorting Operation

```python
import cv2
from src.vision import CardDetector, CardClassifier
from src.motion import GantryController
from src.plc import ModbusClient
from src.config import Config

# Load configuration
config = Config('config/config.yaml')

# Initialize components
plc = ModbusClient(config.plc.ip, config.plc.port)
plc.connect()

gantry = GantryController(config, plc)
detector = CardDetector(config)
classifier = CardClassifier()

# Initialize camera
cap = cv2.VideoCapture(config.camera.index)

# Home system
print("Homing...")
gantry.home()

# Main sorting loop
try:
    while True:
        # Move to pickup position
        gantry.move_to(*config.positions.pickup)
        gantry.wait_until_idle()
        
        # Capture image
        ret, frame = cap.read()
        if not ret:
            break
        
        # Detect card
        card = detector.detect(frame)
        if card is None:
            print("No card detected")
            continue
        
        # Crop card region
        x, y, w, h = card['bbox']
        card_image = frame[y:y+h, x:x+w]
        
        # Classify card
        result = classifier.classify(card_image)
        
        if result['confidence'] < 0.9:
            print("Low confidence, skipping")
            continue
        
        print(f"Detected: {result['rank']} of {result['suit']}")
        
        # Pick up card
        plc.write_coil(2000, True)  # Activate gripper
        gantry.move_to(*config.positions.pickup[:2], 
                      z=config.positions.pickup[2] - 2)
        time.sleep(0.3)  # Grip delay
        gantry.move_to(*config.positions.pickup[:2], 
                      z=config.positions.pickup[2] + 50)
        
        # Move to appropriate bin
        bin_position = config.positions.sort_positions[result['suit']]
        gantry.move_to(*bin_position)
        gantry.wait_until_idle()
        
        # Release card
        plc.write_coil(2000, False)  # Deactivate gripper
        time.sleep(0.2)
        
except KeyboardInterrupt:
    print("Stopping...")
finally:
    cap.release()
    gantry.emergency_stop()
    plc.disconnect()
```

---

## 📊 Data Types

### Position

```python
Position = Tuple[float, float, float]  # (x, y, z) in mm
```

### BoundingBox

```python
BoundingBox = Tuple[int, int, int, int]  # (x, y, width, height)
```

### CardInfo

```python
CardInfo = {
    'suit': str,         # 'hearts', 'diamonds', 'clubs', 'spades'
    'rank': str,         # 'A', '2'-'10', 'J', 'Q', 'K'
    'confidence': float, # 0.0 to 1.0
    'bbox': BoundingBox,
    'angle': float,      # Rotation in degrees
}
```

---

## ⚠️ Error Handling

### Exceptions

#### `ConnectionError`

Raised when PLC connection fails.

```python
try:
    plc.connect()
except ConnectionError as e:
    print(f"Failed to connect: {e}")
```

#### `HomingError`

Raised when homing sequence fails.

```python
try:
    gantry.home()
except HomingError as e:
    print(f"Homing failed: {e}")
    # Check limit switches
```

#### `PositionError`

Raised when position is out of bounds.

```python
try:
    gantry.move_to(1000, 1000, 1000)  # Out of bounds
except PositionError as e:
    print(f"Invalid position: {e}")
```

#### `VisionError`

Raised when card detection/classification fails critically.

---

## 🔍 Debugging

### Enable Debug Mode

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('card_sorter')

# All component operations will be logged
```

### Performance Profiling

```python
import time

start = time.time()
result = classifier.classify(card_image)
elapsed = time.time() - start

print(f"Classification took {elapsed*1000:.2f}ms")
```

---

## 📚 Additional Resources

- [User Guide](USER_GUIDE.md) - Operating instructions
- [Hardware Setup](HARDWARE.md) - Hardware documentation
- [Troubleshooting](TROUBLESHOOTING.md) - Common issues

---

[← Back to Main README](README.md)
