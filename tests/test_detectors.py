import pytest
from detector.violence_detector import ViolenceDetector
from detector.weapon_detector import WeaponDetector

def test_violence_detector_low_proximity_fast_movement():
    detector = ViolenceDetector()
    
    # Person 1
    p1_v1 = {'x1': 100, 'y1': 100, 'x2': 150, 'y2': 150, 'conf': 0.9}
    # Person 2
    p2_v1 = {'x1': 110, 'y1': 110, 'x2': 160, 'y2': 160, 'conf': 0.9}
    
    # Initialization call
    detector.analyze([p1_v1, p2_v1])
    
    # Person 1 moved slightly
    p1_v2 = {'x1': 105, 'y1': 105, 'x2': 155, 'y2': 155, 'conf': 0.9}
    # Person 2 moved significantly (Rapid Movement)
    p2_v2 = {'x1': 200, 'y1': 200, 'x2': 250, 'y2': 250, 'conf': 0.9}
    
    alerts = detector.analyze([p1_v2, p2_v2])
    
    assert "Violence Detected" in alerts

def test_violence_detector_no_persons():
    detector = ViolenceDetector()
    alerts = detector.analyze([])
    assert len(alerts) == 0

def test_weapon_detector_not_held():
    detector = WeaponDetector()
    persons = [{'x1': 0, 'y1': 0, 'x2': 10, 'y2': 10}]
    weapons = [{'x1': 100, 'y1': 100, 'x2': 110, 'y2': 110}] # Far away
    
    alerts = detector.analyze(persons, weapons)
    assert "Weapon Detected" in alerts
    assert "WEAPON IN PROXIMITY TO HUMAN" not in alerts

def test_weapon_detector_held():
    detector = WeaponDetector()
    persons = [{'x1': 100, 'y1': 100, 'x2': 200, 'y2': 200}]
    weapons = [{'x1': 150, 'y1': 150, 'x2': 160, 'y2': 160}] # Inside person box
    
    alerts = detector.analyze(persons, weapons)
    assert "Weapon Detected" in alerts
    assert "WEAPON IN PROXIMITY TO HUMAN" in alerts
