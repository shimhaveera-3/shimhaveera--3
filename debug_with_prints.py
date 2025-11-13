#!/usr/bin/env python3
"""
DEBUG: Test with comprehensive print statements
Generate only original images (multiplier=1) to see debug output clearly
"""
import requests
import json
import sys

def debug_with_prints():
    print("🔍 DEBUGGING WITH COMPREHENSIVE PRINT STATEMENTS")
    print("=" * 80)
    
    # Test configuration - ONLY ORIGINAL IMAGES (multiplier=1)
    release_config = {
        "version_name": "debug-prints-v1.0",
        "dataset_ids": ["6ec272ad-f769-4b77-9feb-07a7f6ddc4f8"],  # animal dataset
        "description": "Debug with comprehensive print statements - original images only",
        "transformations": [
            {
                "type": "resize", 
                "params": {
                    "width": 500,
                    "height": 500,
                    "resize_mode": "stretch_to"  # This is what UI uses
                }
            }
        ],
        "multiplier": 1,  # ONLY ORIGINAL IMAGES - no augmentation
        "export_format": "YOLO",
        "task_type": "object_detection"
    }
    
    print(f"📊 CONFIGURATION:")
    print(f"   Resize: 800x600 → 500x500")
    print(f"   Mode: stretch_to (non-uniform scaling)")
    print(f"   Multiplier: 1 (original images only)")
    print(f"   Expected scale factors: sx={500/800:.3f}, sy={500/600:.3f}")
    print()
    
    # Create release with debug
    try:
        print("🚀 Sending request to backend...")
        response = requests.post(
            "http://localhost:12000/api/v1/releases/create",
            json=release_config,
            timeout=120  # Longer timeout for debug output
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Release created: {result.get('release_id')}")
            print(f"📁 Check backend logs for detailed debug output!")
            return result.get('release_id')
        else:
            print(f"❌ Failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

if __name__ == "__main__":
    release_id = debug_with_prints()
    if release_id:
        print(f"\n🎯 SUCCESS! Now check the backend terminal for detailed debug output.")
        print(f"   Look for lines starting with 🚀, 🔍, 📦, 🎯, ✅")
        print(f"   This will show you EXACTLY what's happening to each annotation!")
    else:
        print(f"\n❌ Failed to create release. Check backend logs for errors.")