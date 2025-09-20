#!/usr/bin/env python3
"""
Test resize-only transformation with proper coordinate scaling
"""
import requests
import json

def test_resize_only():
    print("🔧 TESTING RESIZE-ONLY TRANSFORMATION")
    
    # Simple resize-only configuration
    release_config = {
        "version_name": "resize-only-v1.0",
        "dataset_ids": ["6ec272ad-f769-4b77-9feb-07a7f6ddc4f8"],  # animal dataset
        "description": "Resize-only test - no other transformations",
        "transformations": [
            {
                "type": "resize", 
                "params": {
                    "width": 640,
                    "height": 640
                }
            }
        ],
        "multiplier": 1,  # Only original images, no augmentation
        "export_format": "YOLO",
        "task_type": "object_detection"
    }
    
    print(f"📊 Configuration:")
    print(f"   Transformations: resize only (640x640)")
    print(f"   Multiplier: 1 (original images only)")
    print(f"   Dataset: animal (3 images)")
    
    # Create release
    try:
        response = requests.post(
            "http://localhost:12000/api/v1/releases/create",
            json=release_config,
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Release created successfully!")
            print(f"   Release ID: {result.get('release_id')}")
            return result.get('release_id')
        else:
            print(f"❌ Failed to create release: {response.status_code}")
            print(f"   Response: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Error creating release: {e}")
        return None

if __name__ == "__main__":
    test_resize_only()