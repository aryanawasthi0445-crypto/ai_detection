from fastapi import FastAPI, UploadFile, File, HTTPException, Request
from pydantic import BaseModel
import time
import logging
from utils.api_utils import setup_logging, decode_image_bytes, decode_image_base64
from model_wrapper import AIInferenceWrapper

# Initialize Logger
logger = setup_logging()

# Initialize API and Model
app = FastAPI(title="AI Violence Detection API", version="1.0.0")
inference_service = AIInferenceWrapper()
inference_service.warmup()

class Base64Request(BaseModel):
    image_base64: str

@app.post("/predict")
async def predict(
    file: UploadFile = File(None),
    request: Request = None,
    confidence: Optional[float] = None
):
    start_time = time.time()
    
    try:
        # 1. Image Data Extraction
        frame = None
        
        # Check if it's a JSON request (base64)
        if request.headers.get("content-type") == "application/json":
            body = await request.json()
            if "image_base64" in body:
                frame = decode_image_base64(body["image_base64"])
            else:
                raise HTTPException(status_code=400, detail="Missing 'image_base64' in JSON body")
        
        # Check if it's a file upload
        elif file:
            contents = await file.read()
            frame = decode_image_bytes(contents)
            
        else:
            raise HTTPException(status_code=400, detail="No image provided (File or Base64)")

        if frame is None:
            raise HTTPException(status_code=400, detail="Could not decode image")

        # 2. Inference
        result = inference_service.predict_frame(frame, threshold=confidence)
        
        # 3. Finalize Response
        process_time = (time.time() - start_time) * 1000
        result["processing_time_ms"] = round(process_time, 2)
        
        # Log Prediction
        logger.info(f"PREDICTION: {result['prediction']} | CONF: {result['confidence']:.2f} | TIME: {result['processing_time_ms']}ms")
        
        return result

    except HTTPException as he:
        raise he
    except Exception as e:
        logger.error(f"Prediction Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    return {"status": "healthy", "timestamp": time.time()}
