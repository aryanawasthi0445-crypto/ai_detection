import math
from config.settings import VIOLENCE_PROXIMITY_THRESHOLD, VIOLENCE_RAPID_MOVEMENT_THRESHOLD

class ViolenceDetector:
    """
    Analyzes spatio-temporal dynamics of persons to determine violence.
    Looks for:
    1. Multiple persons in close proximity
    2. Rapid/Eratic movement indicating struggle
    """
    def __init__(self):
        # We store the previous centers of detected persons to calculate velocity
        self.previous_centers = []

    @staticmethod
    def _calculate_center(box):
        return (box['x1'] + box['x2']) / 2, (box['y1'] + box['y2']) / 2

    @staticmethod
    def _calculate_distance(pt1, pt2):
        return math.sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)

    def analyze(self, persons):
        """
        Determines violence alerts based on multiple variables.
        """
        alerts = []
        
        if len(persons) < 2:
            self.previous_centers = [self._calculate_center(p) for p in persons]
            return alerts

        current_centers = [self._calculate_center(p) for p in persons]
        
        # 1. Proximity Check
        persons_in_proximity = False
        for i in range(len(current_centers)):
            for j in range(i + 1, len(current_centers)):
                dist = self._calculate_distance(current_centers[i], current_centers[j])
                if dist < VIOLENCE_PROXIMITY_THRESHOLD:
                    persons_in_proximity = True
                    break

        # 2. Rapid Movement Check
        rapid_movement_detected = False
        
        # Basic heuristic: Check if any current center has moved significantly
        # from ANY previous center (simplistic tracking, suitable for basic violence logic)
        for cur in current_centers:
            for prev in self.previous_centers:
                velocity = self._calculate_distance(cur, prev)
                if velocity > VIOLENCE_RAPID_MOVEMENT_THRESHOLD:
                    rapid_movement_detected = True
                    break
        
        # 3. Decision Logic
        # It's an active struggle if they are close AND moving rapidly
        if persons_in_proximity and rapid_movement_detected:
            alerts.append("Violence Detected")
        # Else if they are just very close, it's a potential risk 
        elif persons_in_proximity:
             pass # For now do nothing, just people hugging/close

        # Update cache
        self.previous_centers = current_centers
        
        return alerts
