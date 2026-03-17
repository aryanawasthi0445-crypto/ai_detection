from utils.visualization import Visualizer
import json

def test_json_output_generation():
    persons = [{'x1': 10, 'y1': 10, 'x2': 50, 'y2': 50, 'conf': 0.85}]
    weapons = [{'x1': 60, 'y1': 60, 'x2': 80, 'y2': 80, 'conf': 0.70}]
    alerts = ["Weapon Detected"]
    
    json_str = Visualizer.generate_json_output(persons, weapons, alerts)
    data = json.loads(json_str)
    
    assert len(data["detections"]["persons"]) == 1
    assert data["detections"]["persons"][0]["confidence"] == 0.85
    assert "Weapon Detected" in data["alerts"]
