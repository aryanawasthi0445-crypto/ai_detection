import requests
import os
import base64

def test_health():
    url = "http://localhost:8001/health"
    response = requests.get(url)
    print(f"Health Check: {response.status_code}")
    print(response.json())

def test_predict_file(image_path):
    url = "http://localhost:8001/predict"
    with open(image_path, "rb") as f:
        files = {"file": f}
        response = requests.post(url, files=files)
    
    print(f"Predict File: {response.status_code}")
    print(response.json())

if __name__ == "__main__":
    # Test Health
    test_health()
    
    # Try to find an image
    found_img = None
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.lower().endswith(".jpg"):
                found_img = os.path.join(root, file)
                break
        if found_img: break
    
    if found_img:
        print(f"Testing with image: {found_img}")
        test_predict_file(found_img)
    else:
        print("No image found to test.")
