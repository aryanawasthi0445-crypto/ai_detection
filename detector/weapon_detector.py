import math
from config.settings import WEAPON_PROXIMITY_THRESHOLD

class WeaponDetector:
    """
    Analyzes YOLO outputs specifically for weapons and their relation to humans.
    """
    
    @staticmethod
    def _calculate_center(box):
        """Calculate the center coordinate of a bounding box."""
        cx = (box['x1'] + box['x2']) / 2
        cy = (box['y1'] + box['y2']) / 2
        return cx, cy

    @staticmethod
    def _calculate_distance(pt1, pt2):
        """Calculate Euclidean distance between two points."""
        return math.sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)

    def analyze(self, persons, weapons):
        """
        Checks if a detected weapon is near any detected person.
        Returns a list of alerts.
        """
        alerts = []
        
        if not weapons:
            return alerts
            
        alerts.append("Weapon Detected")
        
        # Check weapon proximity to persons to determine intent
        weapon_held = False
        for weapon in weapons:
            w_center = self._calculate_center(weapon)
            
            for person in persons:
                p_center = self._calculate_center(person)
                dist = self._calculate_distance(w_center, p_center)
                
                if dist < WEAPON_PROXIMITY_THRESHOLD:
                    weapon_held = True
                    break
            
            if weapon_held:
                break
                
        if weapon_held:
            # We add an extra alert to signify urgency
            alerts.append("WEAPON IN PROXIMITY TO HUMAN")

        return alerts
