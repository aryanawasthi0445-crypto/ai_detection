import cv2
import json

class Visualizer:
    """
    Utility class for drawing bounding boxes, text alerts, and outputting JSON logs.
    """
    
    # Colors (BGR)
    COLOR_PERSON = (255, 178, 102)     # Light Blue
    COLOR_WEAPON = (0, 0, 255)         # Red
    COLOR_ALERT_BG = (0, 0, 150)       # Dark Red
    COLOR_TEXT = (255, 255, 255)       # White

    @staticmethod
    def draw_bbox(frame, box, label, color, confidence=None):
        """Draws a standardized bounding box with label logic."""
        x1, y1, x2, y2 = box
        
        # Bounding Box
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        
        # Label config
        text = f"{label}" if confidence is None else f"{label} {confidence:.2f}"
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.6
        thickness = 2
        
        # Text Background
        (text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, thickness)
        cv2.rectangle(frame, (x1, y1 - text_height - baseline - 5), (x1 + text_width, y1), color, -1)
        
        # Text
        cv2.putText(frame, text, (x1, y1 - 5), font, font_scale, Visualizer.COLOR_TEXT, thickness)


    @staticmethod
    def display_fps(frame, fps):
        """Overlays the FPS counter on the top left corner."""
        cv2.putText(frame, f"FPS: {fps:.1f}", (20, 40), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    @staticmethod
    def display_alerts(frame, alerts):
        """Draws high-visibility red alerts for violence or weapons."""
        y_offset = 80
        for alert in alerts:
            # Emphasize text with a background box
            text = alert.upper()
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 1.0
            thickness = 2
            
            (tw, th), bl = cv2.getTextSize(text, font, font_scale, thickness)
            cv2.rectangle(frame, (15, y_offset - th - 5), (15 + tw + 10, y_offset + bl), Visualizer.COLOR_ALERT_BG, -1)
            cv2.putText(frame, text, (20, y_offset), font, font_scale, Visualizer.COLOR_TEXT, thickness)
            
            y_offset += (th + bl + 15)

    @staticmethod
    def generate_json_output(persons, weapons, alerts):
        """Formats the current frame detections into the required JSON struct."""
        
        def box_to_dict(b):
            return {
                "bbox": [b['x1'], b['y1'], b['x2'], b['y2']],
                "confidence": round(float(b['conf']), 2)
            }
            
        output = {
            "detections": {
                "persons": [box_to_dict(p) for p in persons],
                "weapons": [box_to_dict(w) for w in weapons]
            },
            "alerts": alerts
        }
        return json.dumps(output)
