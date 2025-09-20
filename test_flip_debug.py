#!/usr/bin/env python3

"""
🔍 TEST FLIP DEBUG
Create a release with flip transformation to see debug output
"""

import requests
import json

def test_flip_release():
    print("🧮 TESTING FLIP RELEASE CREATION")
    
    # Release configuration with flip transformation (NEW API FORMAT)
    release_config = {
        "version_name": "v1.0",
        "dataset_ids": ["6ec272ad-f769-4b77-9feb-07a7f6ddc4f8"],  # animal dataset
        "description": "Debug test for flip transformations with animal dataset",
        "transformations": [
            {
                "type": "flip",
                "params": {
                    "vertical": True
                }
            },
            {
                "type": "resize", 
                "params": {
                    "width": 640,
                    "height": 640
                }
            }
        ],
        "multiplier": 2,  # 1 original + 1 augmented = 2 total per image
        "export_format": "YOLO",
        "task_type": "object_detection"
    }
    
    print(f"📊 Release config:")
    print(f"   Transformations: {[t['type'] for t in release_config['transformations']]}")
    print(f"   Multiplier: {release_config['multiplier']}")
    print(f"   Flip vertical: {release_config['transformations'][0]['params']['vertical']}")
    
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
            print(f"   Status: {result.get('status')}")
            if 'download_url' in result:
                print(f"   Download URL: {result['download_url']}")
        else:
            print(f"❌ Release creation failed: {response.status_code}")
            print(f"   Response: {response.text}")
            
    except Exception as e:
        print(f"❌ Exception: {e}")

if __name__ == "__main__":
    test_flip_release()