#!/usr/bin/env python3
"""
DEBUG: Trace complete annotation transformation flow
Map all functions and understand the story step by step
"""
import requests
import json
import sys

def debug_annotation_flow():
    print("🔍 DEBUGGING ANNOTATION TRANSFORMATION FLOW")
    print("=" * 60)
    
    # Test configuration that matches UI behavior
    release_config = {
        "version_name": "debug-flow-v1.0",
        "dataset_ids": ["6ec272ad-f769-4b77-9feb-07a7f6ddc4f8"],  # animal dataset
        "description": "Debug annotation transformation flow",
        "transformations": [
            {
                "type": "resize", 
                "params": {
                    "width": 500,
                    "height": 500,
                    "resize_mode": "stretch_to"  # This is the key!
                }
            }
        ],
        "multiplier": 1,  # Only original images
        "export_format": "YOLO",
        "task_type": "object_detection"
    }
    
    print(f"📊 CONFIGURATION:")
    print(f"   Resize: 800x600 → 500x500")
    print(f"   Mode: stretch_to (non-uniform scaling)")
    print(f"   Expected scale factors: sx={500/800:.3f}, sy={500/600:.3f}")
    print()
    
    # Create release with debug
    try:
        response = requests.post(
            "http://localhost:12000/api/v1/releases/create",
            json=release_config,
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Release created: {result.get('release_id')}")
            return result.get('release_id')
        else:
            print(f"❌ Failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def analyze_results(release_id):
    """Analyze the transformation results"""
    print("\n🔬 ANALYZING TRANSFORMATION RESULTS")
    print("=" * 60)
    
    # Check the generated files
    import os
    import zipfile
    
    zip_path = f"projects/gevis/releases/debug-flow-v1.0_yolo.zip"
    
    if not os.path.exists(zip_path):
        print(f"❌ Release file not found: {zip_path}")
        return
    
    # Extract and analyze annotations
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Read annotations
        try:
            annotations_data = zip_ref.read('metadata/annotations.json')
            annotations = json.loads(annotations_data)
            
            print("📋 ANNOTATION RESULTS:")
            for image_path, anns in annotations.items():
                print(f"\n🖼️  {image_path}:")
                if not anns:
                    print("   ❌ NO ANNOTATIONS")
                    continue
                    
                for i, ann in enumerate(anns):
                    bbox = ann['bbox']
                    class_id = ann['class_id']
                    
                    # Convert from YOLO format (cx, cy, w, h) to absolute
                    cx, cy, w, h = bbox
                    x_min = (cx - w/2) * 500  # 500 = target width
                    y_min = (cy - h/2) * 500  # 500 = target height
                    x_max = (cx + w/2) * 500
                    y_max = (cy + h/2) * 500
                    
                    print(f"   Ann {i+1}: class_id={class_id}")
                    print(f"           YOLO: cx={cx:.4f}, cy={cy:.4f}, w={w:.4f}, h={h:.4f}")
                    print(f"           ABS:  x_min={x_min:.1f}, y_min={y_min:.1f}, x_max={x_max:.1f}, y_max={y_max:.1f}")
                    
                    # Check bounds
                    if cx < 0 or cx > 1 or cy < 0 or cy > 1 or w < 0 or w > 1 or h < 0 or h > 1:
                        print(f"           ⚠️  OUT OF BOUNDS!")
                    else:
                        print(f"           ✅ Within bounds")
                        
        except Exception as e:
            print(f"❌ Error reading annotations: {e}")

if __name__ == "__main__":
    release_id = debug_annotation_flow()
    if release_id:
        analyze_results(release_id)