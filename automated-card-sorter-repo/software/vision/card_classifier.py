#!/usr/bin/env python3
"""
Automated Card Sorting System - Vision Classifier
==================================================

This module handles card classification using OpenCV template matching.
Communicates with Node-RED via MQTT.

Authors: Josh Craven, Jae Park
Course: TPJ653NAA - Mechatronics Engineering
Institution: Seneca College
Date: March 2026
"""

import cv2
import numpy as np
import paho.mqtt.client as mqtt
import json
import yaml
import logging
from datetime import datetime
from pathlib import Path

# =============================================================================
# Configuration
# =============================================================================

class Config:
    """Load and store configuration from config.yaml"""
    
    def __init__(self, config_path="config.yaml"):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
    
    @property
    def camera_index(self):
        return self.config['camera']['index']
    
    @property
    def mqtt_broker(self):
        return self.config['mqtt']['broker']
    
    @property
    def mqtt_port(self):
        return self.config['mqtt']['port']
    
    @property
    def topic_request(self):
        return self.config['mqtt']['topic_request']
    
    @property
    def topic_result(self):
        return self.config['mqtt']['topic_result']
    
    @property
    def confidence_threshold(self):
        return self.config['classification']['confidence_threshold']
    
    @property
    def flip_index(self):
        return self.config['classification']['flip_index']
    
    @property
    def scan_request_index(self):
        return self.config['classification']['scan_request_index']


# =============================================================================
# Logging Setup
# =============================================================================

def setup_logging():
    """Configure logging to file and console"""
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_dir / "classifications.log"),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)


# =============================================================================
# Template Manager
# =============================================================================

class TemplateManager:
    """Load and manage card rank/suit templates"""
    
    def __init__(self, ranks_dir="templates/ranks", suits_dir="templates/suits"):
        self.ranks_dir = Path(ranks_dir)
        self.suits_dir = Path(suits_dir)
        self.rank_templates = {}
        self.suit_templates = {}
        self.load_templates()
    
    def load_templates(self):
        """Load all template images"""
        # Rank templates (A, 2-10, J, Q, K)
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for rank in ranks:
            template_path = self.ranks_dir / f"{rank}.png"
            if template_path.exists():
                self.rank_templates[rank] = cv2.imread(str(template_path), 0)
                logger.info(f"Loaded rank template: {rank}")
        
        # Suit templates (♠, ♥, ♦, ♣)
        suits = {'spades': '♠', 'hearts': '♥', 'diamonds': '♦', 'clubs': '♣'}
        for suit_name, suit_symbol in suits.items():
            template_path = self.suits_dir / f"{suit_name}.png"
            if template_path.exists():
                self.suit_templates[suit_symbol] = cv2.imread(str(template_path), 0)
                logger.info(f"Loaded suit template: {suit_symbol}")


# =============================================================================
# Vision Classifier
# =============================================================================

class CardClassifier:
    """Main card classification engine"""
    
    def __init__(self, config):
        self.config = config
        self.camera = cv2.VideoCapture(config.camera_index)
        self.templates = TemplateManager()
        
        # Set camera properties
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        self.camera.set(cv2.CAP_PROP_FPS, 30)
    
    def capture_frame(self):
        """Capture image from camera"""
        ret, frame = self.camera.read()
        if not ret:
            logger.error("Failed to capture frame from camera")
            return None
        return frame
    
    def preprocess_image(self, image):
        """Preprocess image for classification"""
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Apply Gaussian blur to reduce noise
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
        # Adaptive thresholding for better contrast
        thresh = cv2.adaptiveThreshold(
            blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
            cv2.THRESH_BINARY, 11, 2
        )
        
        return thresh
    
    def extract_rank_roi(self, image):
        """Extract region of interest for rank detection"""
        # TODO: Implement ROI extraction based on card position
        # Typically top-left corner of card
        h, w = image.shape[:2]
        roi = image[int(h*0.05):int(h*0.25), int(w*0.05):int(w*0.25)]
        return roi
    
    def extract_suit_roi(self, image):
        """Extract region of interest for suit detection"""
        # TODO: Implement ROI extraction based on card position
        # Typically below rank in top-left corner
        h, w = image.shape[:2]
        roi = image[int(h*0.25):int(h*0.45), int(w*0.05):int(w*0.25)]
        return roi
    
    def template_match(self, image, templates):
        """
        Match image against templates using OpenCV template matching
        
        Returns:
            tuple: (best_match, confidence)
        """
        best_match = None
        best_score = 0
        
        for name, template in templates.items():
            # Resize template to multiple scales for robustness
            for scale in [0.8, 1.0, 1.2]:
                resized_template = cv2.resize(
                    template, 
                    (int(template.shape[1] * scale), int(template.shape[0] * scale))
                )
                
                # Template matching
                result = cv2.matchTemplate(image, resized_template, cv2.TM_CCOEFF_NORMED)
                _, max_val, _, _ = cv2.minMaxLoc(result)
                
                if max_val > best_score:
                    best_score = max_val
                    best_match = name
        
        return best_match, best_score
    
    def detect_orientation(self, image):
        """
        Detect if card is upside-down
        
        Returns:
            bool: True if card is right-side up, False if inverted
        """
        # TODO: Implement orientation detection
        # Simple approach: check if rank is detected in top-left vs bottom-right
        return True
    
    def classify_card(self):
        """
        Main classification routine
        
        Returns:
            dict: {
                'rank': str,
                'suit': str,
                'confidence': float,
                'needs_flip': bool,
                'timestamp': str
            }
        """
        # Capture frame
        frame = self.capture_frame()
        if frame is None:
            return None
        
        # Preprocess
        processed = self.preprocess_image(frame)
        
        # Extract ROIs
        rank_roi = self.extract_rank_roi(processed)
        suit_roi = self.extract_suit_roi(processed)
        
        # Classify rank
        rank, rank_conf = self.template_match(rank_roi, self.templates.rank_templates)
        
        # Classify suit
        suit, suit_conf = self.template_match(suit_roi, self.templates.suit_templates)
        
        # Overall confidence (average)
        confidence = (rank_conf + suit_conf) / 2
        
        # Check orientation
        is_right_side_up = self.detect_orientation(processed)
        
        # Determine if flip needed
        needs_flip = (not is_right_side_up) or (confidence < self.config.confidence_threshold)
        
        result = {
            'rank': rank if rank else 'UNKNOWN',
            'suit': suit if suit else 'UNKNOWN',
            'confidence': float(confidence),
            'needs_flip': needs_flip,
            'timestamp': datetime.now().isoformat()
        }
        
        logger.info(f"Classification: {rank} of {suit} (confidence: {confidence:.2f})")
        
        return result
    
    def release(self):
        """Release camera resources"""
        self.camera.release()


# =============================================================================
# MQTT Communication
# =============================================================================

class MQTTHandler:
    """Handle MQTT communication with Node-RED"""
    
    def __init__(self, config, classifier):
        self.config = config
        self.classifier = classifier
        self.client = mqtt.Client()
        
        # Set callbacks
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
    
    def on_connect(self, client, userdata, flags, rc):
        """Callback when connected to MQTT broker"""
        logger.info(f"Connected to MQTT broker with result code {rc}")
        # Subscribe to vision request topic
        client.subscribe(self.config.topic_request)
        logger.info(f"Subscribed to topic: {self.config.topic_request}")
    
    def on_message(self, client, userdata, msg):
        """Callback when message received"""
        try:
            payload = json.loads(msg.payload.decode())
            index = payload.get('index', 0)
            
            logger.info(f"Received request with index: {index}")
            
            # Check if this is a vision request (index 999)
            if index == self.config.scan_request_index:
                # Classify card
                result = self.classifier.classify_card()
                
                if result:
                    # Send result back
                    self.publish_result(result)
                else:
                    logger.error("Classification failed")
            
        except Exception as e:
            logger.error(f"Error processing message: {e}")
    
    def publish_result(self, result):
        """Publish classification result to MQTT"""
        # Determine bin index based on classification
        if result['needs_flip']:
            bin_index = self.config.flip_index  # 77 = needs flip
        else:
            # Map rank/suit to bin index (0-21)
            # TODO: Implement actual bin mapping logic
            bin_index = 0
        
        payload = {
            'rank': result['rank'],
            'suit': result['suit'],
            'confidence': result['confidence'],
            'bin_index': bin_index,
            'timestamp': result['timestamp']
        }
        
        self.client.publish(
            self.config.topic_result, 
            json.dumps(payload)
        )
        
        logger.info(f"Published result: Bin {bin_index}")
    
    def connect(self):
        """Connect to MQTT broker"""
        self.client.connect(self.config.mqtt_broker, self.config.mqtt_port, 60)
    
    def start(self):
        """Start MQTT loop"""
        self.client.loop_forever()


# =============================================================================
# Main
# =============================================================================

def main():
    """Main entry point"""
    global logger
    logger = setup_logging()
    
    logger.info("=" * 60)
    logger.info("Automated Card Sorting System - Vision Classifier")
    logger.info("=" * 60)
    
    # Load configuration
    config = Config()
    
    # Initialize classifier
    classifier = CardClassifier(config)
    
    # Initialize MQTT handler
    mqtt_handler = MQTTHandler(config, classifier)
    
    try:
        # Connect to MQTT broker
        mqtt_handler.connect()
        logger.info("MQTT connected. Waiting for classification requests...")
        
        # Start MQTT loop (blocking)
        mqtt_handler.start()
        
    except KeyboardInterrupt:
        logger.info("Shutdown requested by user")
    
    except Exception as e:
        logger.error(f"Fatal error: {e}")
    
    finally:
        # Cleanup
        classifier.release()
        logger.info("Vision system shutdown complete")


if __name__ == "__main__":
    main()
