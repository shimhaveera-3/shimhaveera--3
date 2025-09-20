
=== 🔍 TRANSFORMATIONS DEBUG :: cat.jpg ===
transformations variable: [{'type': 'resize', 'params': {'width': 500, 'height': 500}}, {'type': 'flip', 'params': {'vertical': True}}]
transformations type: <class 'list'>
transformations bool: True
🎯 COMPLEX TRANSFORMATIONS for cat.jpg
🖼️ Original image dims: (800, 600)
🎯 ORIGINAL IMAGE: Applying ONLY resize (baseline behavior)
🖼️ Resized to: (500, 500) using mode: stretch_to

🔍 TRACKING FUNCTION INPUT:
   Transformations: [{'type': 'resize', 'params': {'width': 500, 'height': 500}}]
   Original dims: (800, 600)
   Final dims: (500, 500)
🎯 RESIZE CONFIG ALREADY EXISTS: {'enabled': True, 'width': 500, 'height': 500}

📍 ANNOTATION TRACKING ORDER: ['resize']
🔧 GEOMETRIC TRANSFORMS ORDER: ['resize']
🔍 TRANSFORMATION CONFIG DETAILS: {'resize': {'enabled': True, 'width': 500, 'height': 500}}

🎯 TRACKING FUNCTION OUTPUT:
   transformation_config: {'resize': {'enabled': True, 'width': 500, 'height': 500}}
   Has geometric transforms: True
   Geometric transforms: [{'type': 'resize', 'params': {'width': 500, 'height': 500}, 'index': 0}]       
🎯 ORIGINAL IMAGE BASELINE: Applied resize-only, augmented images will get full combinations!
🎯 RELEASES.PY: Using NEW FUNCTIONS with internal transformation!
   📊 Tracking data: {'transformation_sequence': [{'index': 0, 'type': 'resize', 'params': {'width': 500, 'height': 500}, 'is_geometric': True, 'is_photometric': False}], 'transformation_config': {'resize': {'enabled': True, 'width': 500, 'height': 500}}, 'original_dims': (800, 600), 'final_dims': (500, 500), 'debug_transformation_order': {'annotation_config_order': ['resize'], 'geometric_transforms_order': ['resize'], 'orders_match': True, 'duplicate_resize_detected': False}, 'has_geometric_transforms': True, 'geometric_transforms': [{'type': 'resize', 'params': {'width': 500, 'height': 500}, 'index': 0}], 'photometric_transforms': [], 'total_transforms': 1, 'geometric_count': 1, 'photometric_count': 0}
🎯 NEW DETECTION FUNCTION CALLED!
   Annotations: 3
   Final dims: 500x500
   Has transform_config: True
   Original dims: (800, 600)
🔧 TRANSFORMING ANNOTATIONS: (800, 600) → 500x500
   Original: 3 → Transformed: 3
🔍 ANNOTATIONS BEFORE YOLO CONVERSION:
   Ann 1: BBox(107.50, 40.50, 760.50, 583.50)
           Canvas: 500x500
           ⚠️  OUT OF BOUNDS!
   Ann 2: BBox(317.50, 204.50, 372.50, 254.50)
           Canvas: 500x500
   Ann 3: BBox(429.50, 201.50, 483.50, 251.50)
           Canvas: 500x500
🔍 Processing annotation 1/3
   📦 BBox: (107.50, 40.50, 760.50, 583.50)
   📏 Normalized: cx=0.8680, cy=0.6240, w=1.3060, h=1.0860
   ⚠️  CLIPPED: Out of bounds values normalized
      Original: cx=0.8680, cy=0.6240, w=1.3060, h=1.0860
      Clipped:  cx=0.8680, cy=0.6240, w=1.0000, h=1.0000
   ✅ SUCCESS: Added to YOLO: 0 0.868000 0.624000 1.000000 1.000000
🔍 Processing annotation 2/3
   📦 BBox: (317.50, 204.50, 372.50, 254.50)
   📏 Normalized: cx=0.6900, cy=0.4590, w=0.1100, h=0.1000
   ✅ SUCCESS: Added to YOLO: 1 0.690000 0.459000 0.110000 0.100000
🔍 Processing annotation 3/3
   📦 BBox: (429.50, 201.50, 483.50, 251.50)
   📏 Normalized: cx=0.9130, cy=0.4530, w=0.1080, h=0.1000
   ✅ SUCCESS: Added to YOLO: 1 0.913000 0.453000 0.108000 0.100000
✅ NEW DETECTION FUNCTION RESULT: 3 lines

🖼️ IMAGE GENERATION ORDER: ['flip', 'resize']

🔍 TRACKING FUNCTION INPUT:
   Transformations: [{'type': 'flip', 'params': {'vertical': True}}, {'type': 'resize', 'params': {'width': 500, 'height': 500}}]
   Original dims: (800, 600)
   Final dims: (500, 500)
🎯 RESIZE CONFIG ALREADY EXISTS: {'enabled': True, 'width': 500, 'height': 500}

📍 ANNOTATION TRACKING ORDER: ['flip', 'resize']
🔧 GEOMETRIC TRANSFORMS ORDER: ['flip', 'resize']
🔍 TRANSFORMATION CONFIG DETAILS: {'flip': {'enabled': True, 'vertical': True}, 'resize': {'enabled': True, 'width': 500, 'height': 500}}

🎯 TRACKING FUNCTION OUTPUT:
   transformation_config: {'flip': {'enabled': True, 'vertical': True}, 'resize': {'enabled': True, 'width': 500, 'height': 500}}
   Has geometric transforms: True
   Geometric transforms: [{'type': 'flip', 'params': {'vertical': True}, 'index': 0}, {'type': 'resize', 'params': {'width': 500, 'height': 500}, 'index': 1}]
🎯 RELEASES.PY: Using ADVANCED transformation system for annotations!
   📊 Tracking data: {'transformation_sequence': [{'index': 0, 'type': 'flip', 'params': {'vertical': True}, 'is_geometric': True, 'is_photometric': False}, {'index': 1, 'type': 'resize', 'params': {'width': 500, 'height': 500}, 'is_geometric': True, 'is_photometric': False}], 'transformation_config': {'flip': {'enabled': True, 'vertical': True}, 'resize': {'enabled': True, 'width': 500, 'height': 500}}, 'original_dims': (800, 600), 'final_dims': (500, 500), 'debug_transformation_order': {'annotation_config_order': ['flip', 'resize'], 'geometric_transforms_order': ['flip', 'resize'], 'orders_match': True, 'duplicate_resize_detected': False}, 'has_geometric_transforms': True, 'geometric_transforms': [{'type': 'flip', 'params': {'vertical': True}, 'index': 0}, {'type': 'resize', 'params': {'width': 500, 'height': 500}, 'index': 1}], 'photometric_transforms': [], 'total_transforms': 2, 'geometric_count': 2, 'photometric_count': 0}    

=== 🔍 TRANSFORMATIONS DEBUG :: car.jpg ===
transformations variable: [{'type': 'resize', 'params': {'width': 500, 'height': 500}}, {'type': 'flip', 'params': {'vertical': True}}]
transformations type: <class 'list'>
transformations bool: True
🎯 COMPLEX TRANSFORMATIONS for car.jpg
🖼️ Original image dims: (800, 600)
🎯 ORIGINAL IMAGE: Applying ONLY resize (baseline behavior)
🖼️ Resized to: (500, 500) using mode: stretch_to

🔍 TRACKING FUNCTION INPUT:
   Transformations: [{'type': 'resize', 'params': {'width': 500, 'height': 500}}]
   Original dims: (800, 600)
   Final dims: (500, 500)
🎯 RESIZE CONFIG ALREADY EXISTS: {'enabled': True, 'width': 500, 'height': 500}

📍 ANNOTATION TRACKING ORDER: ['resize']
🔧 GEOMETRIC TRANSFORMS ORDER: ['resize']
🔍 TRANSFORMATION CONFIG DETAILS: {'resize': {'enabled': True, 'width': 500, 'height': 500}}

🎯 TRACKING FUNCTION OUTPUT:
   transformation_config: {'resize': {'enabled': True, 'width': 500, 'height': 500}}
   Has geometric transforms: True
   Geometric transforms: [{'type': 'resize', 'params': {'width': 500, 'height': 500}, 'index': 0}]       
🎯 ORIGINAL IMAGE BASELINE: Applied resize-only, augmented images will get full combinations!
🎯 RELEASES.PY: Using NEW FUNCTIONS with internal transformation!
   📊 Tracking data: {'transformation_sequence': [{'index': 0, 'type': 'resize', 'params': {'width': 500, 'height': 500}, 'is_geometric': True, 'is_photometric': False}], 'transformation_config': {'resize': {'enabled': True, 'width': 500, 'height': 500}}, 'original_dims': (800, 600), 'final_dims': (500, 500), 'debug_transformation_order': {'annotation_config_order': ['resize'], 'geometric_transforms_order': ['resize'], 'orders_match': True, 'duplicate_resize_detected': False}, 'has_geometric_transforms': True, 'geometric_transforms': [{'type': 'resize', 'params': {'width': 500, 'height': 500}, 'index': 0}], 'photometric_transforms': [], 'total_transforms': 1, 'geometric_count': 1, 'photometric_count': 0}
🎯 NEW DETECTION FUNCTION CALLED!
   Annotations: 2
   Final dims: 500x500
   Has transform_config: True
   Original dims: (800, 600)
🔧 TRANSFORMING ANNOTATIONS: (800, 600) → 500x500
   Original: 2 → Transformed: 2
🔍 ANNOTATIONS BEFORE YOLO CONVERSION:
   Ann 1: BBox(132.50, 108.50, 594.50, 598.50)
           Canvas: 500x500
           ⚠️  OUT OF BOUNDS!
   Ann 2: BBox(454.50, 288.50, 502.50, 324.50)
           Canvas: 500x500
           ⚠️  OUT OF BOUNDS!
🔍 Processing annotation 1/2
   📦 BBox: (132.50, 108.50, 594.50, 598.50)
   📏 Normalized: cx=0.7270, cy=0.7070, w=0.9240, h=0.9800
   ✅ SUCCESS: Added to YOLO: 2 0.727000 0.707000 0.924000 0.980000
🔍 Processing annotation 2/2
   📦 BBox: (454.50, 288.50, 502.50, 324.50)
   📏 Normalized: cx=0.9570, cy=0.6130, w=0.0960, h=0.0720
   ✅ SUCCESS: Added to YOLO: 3 0.957000 0.613000 0.096000 0.072000
✅ NEW DETECTION FUNCTION RESULT: 2 lines

🖼️ IMAGE GENERATION ORDER: ['flip', 'resize']

🔍 TRACKING FUNCTION INPUT:
   Transformations: [{'type': 'flip', 'params': {'vertical': True}}, {'type': 'resize', 'params': {'width': 500, 'height': 500}}]
   Original dims: (800, 600)
   Final dims: (500, 500)
🎯 RESIZE CONFIG ALREADY EXISTS: {'enabled': True, 'width': 500, 'height': 500}

📍 ANNOTATION TRACKING ORDER: ['flip', 'resize']
🔧 GEOMETRIC TRANSFORMS ORDER: ['flip', 'resize']
🔍 TRANSFORMATION CONFIG DETAILS: {'flip': {'enabled': True, 'vertical': True}, 'resize': {'enabled': True, 'width': 500, 'height': 500}}

🎯 TRACKING FUNCTION OUTPUT:
   transformation_config: {'flip': {'enabled': True, 'vertical': True}, 'resize': {'enabled': True, 'width': 500, 'height': 500}}
   Has geometric transforms: True
   Geometric transforms: [{'type': 'flip', 'params': {'vertical': True}, 'index': 0}, {'type': 'resize', 'params': {'width': 500, 'height': 500}, 'index': 1}]
🎯 RELEASES.PY: Using ADVANCED transformation system for annotations!
   📊 Tracking data: {'transformation_sequence': [{'index': 0, 'type': 'flip', 'params': {'vertical': True}, 'is_geometric': True, 'is_photometric': False}, {'index': 1, 'type': 'resize', 'params': {'width': 500, 'height': 500}, 'is_geometric': True, 'is_photometric': False}], 'transformation_config': {'flip': {'enabled': True, 'vertical': True}, 'resize': {'enabled': True, 'width': 500, 'height': 500}}, 'original_dims': (800, 600), 'final_dims': (500, 500), 'debug_transformation_order': {'annotation_config_order': ['flip', 'resize'], 'geometric_transforms_order': ['flip', 'resize'], 'orders_match': True, 'duplicate_resize_detected': False}, 'has_geometric_transforms': True, 'geometric_transforms': [{'type': 'flip', 'params': {'vertical': True}, 'index': 0}, {'type': 'resize', 'params': {'width': 500, 'height': 500}, 'index': 1}], 'photometric_transforms': [], 'total_transforms': 2, 'geometric_count': 2, 'photometric_count': 0}    

=== 🔍 TRANSFORMATIONS DEBUG :: dog.jpg ===
transformations variable: [{'type': 'resize', 'params': {'width': 500, 'height': 500}}, {'type': 'flip', 'params': {'vertical': True}}]
transformations type: <class 'list'>
transformations bool: True
🎯 COMPLEX TRANSFORMATIONS for dog.jpg
🖼️ Original image dims: (800, 600)
🎯 ORIGINAL IMAGE: Applying ONLY resize (baseline behavior)
🖼️ Resized to: (500, 500) using mode: stretch_to

🔍 TRACKING FUNCTION INPUT:
   Transformations: [{'type': 'resize', 'params': {'width': 500, 'height': 500}}]
   Original dims: (800, 600)
   Final dims: (500, 500)
🎯 RESIZE CONFIG ALREADY EXISTS: {'enabled': True, 'width': 500, 'height': 500}

📍 ANNOTATION TRACKING ORDER: ['resize']
🔧 GEOMETRIC TRANSFORMS ORDER: ['resize']
🔍 TRANSFORMATION CONFIG DETAILS: {'resize': {'enabled': True, 'width': 500, 'height': 500}}

🎯 TRACKING FUNCTION OUTPUT:
   transformation_config: {'resize': {'enabled': True, 'width': 500, 'height': 500}}
   Has geometric transforms: True
   Geometric transforms: [{'type': 'resize', 'params': {'width': 500, 'height': 500}, 'index': 0}]       
🎯 ORIGINAL IMAGE BASELINE: Applied resize-only, augmented images will get full combinations!
🎯 RELEASES.PY: Using NEW FUNCTIONS with internal transformation!
   📊 Tracking data: {'transformation_sequence': [{'index': 0, 'type': 'resize', 'params': {'width': 500, 'height': 500}, 'is_geometric': True, 'is_photometric': False}], 'transformation_config': {'resize': {'enabled': True, 'width': 500, 'height': 500}}, 'original_dims': (800, 600), 'final_dims': (500, 500), 'debug_transformation_order': {'annotation_config_order': ['resize'], 'geometric_transforms_order': ['resize'], 'orders_match': True, 'duplicate_resize_detected': False}, 'has_geometric_transforms': True, 'geometric_transforms': [{'type': 'resize', 'params': {'width': 500, 'height': 500}, 'index': 0}], 'photometric_transforms': [], 'total_transforms': 1, 'geometric_count': 1, 'photometric_count': 0}
🎯 NEW DETECTION FUNCTION CALLED!
   Annotations: 1
   Final dims: 500x500
   Has transform_config: True
   Original dims: (800, 600)
🔧 TRANSFORMING ANNOTATIONS: (800, 600) → 500x500
   Original: 1 → Transformed: 1
🔍 ANNOTATIONS BEFORE YOLO CONVERSION:
   Ann 1: BBox(179.50, 37.50, 704.50, 597.50)
           Canvas: 500x500
           ⚠️  OUT OF BOUNDS!
🔍 Processing annotation 1/1
   📦 BBox: (179.50, 37.50, 704.50, 597.50)
   📏 Normalized: cx=0.8840, cy=0.6350, w=1.0500, h=1.1200
   ⚠️  CLIPPED: Out of bounds values normalized
      Original: cx=0.8840, cy=0.6350, w=1.0500, h=1.1200
      Clipped:  cx=0.8840, cy=0.6350, w=1.0000, h=1.0000
   ✅ SUCCESS: Added to YOLO: 2 0.884000 0.635000 1.000000 1.000000
✅ NEW DETECTION FUNCTION RESULT: 1 lines

🖼️ IMAGE GENERATION ORDER: ['flip', 'resize']

🔍 TRACKING FUNCTION INPUT:
   Transformations: [{'type': 'flip', 'params': {'vertical': True}}, {'type': 'resize', 'params': {'width': 500, 'height': 500}}]
   Original dims: (800, 600)
   Final dims: (500, 500)
🎯 RESIZE CONFIG ALREADY EXISTS: {'enabled': True, 'width': 500, 'height': 500}

📍 ANNOTATION TRACKING ORDER: ['flip', 'resize']
🔧 GEOMETRIC TRANSFORMS ORDER: ['flip', 'resize']
🔍 TRANSFORMATION CONFIG DETAILS: {'flip': {'enabled': True, 'vertical': True}, 'resize': {'enabled': True, 'width': 500, 'height': 500}}

🎯 TRACKING FUNCTION OUTPUT:
   transformation_config: {'flip': {'enabled': True, 'vertical': True}, 'resize': {'enabled': True, 'width': 500, 'height': 500}}
   Has geometric transforms: True
   Geometric transforms: [{'type': 'flip', 'params': {'vertical': True}, 'index': 0}, {'type': 'resize', 'params': {'width': 500, 'height': 500}, 'index': 1}]
🎯 RELEASES.PY: Using ADVANCED transformation system for annotations!
   📊 Tracking data: {'transformation_sequence': [{'index': 0, 'type': 'flip', 'params': {'vertical': True}, 'is_geometric': True, 'is_photometric': False}, {'index': 1, 'type': 'resize', 'params': {'width': 500, 'height': 500}, 'is_geometric': True, 'is_photometric': False}], 'transformation_config': {'flip': {'enabled': True, 'vertical': True}, 'resize': {'enabled': True, 'width': 500, 'height': 500}}, 'original_dims': (800, 600), 'final_dims': (500, 500), 'debug_transformation_order': {'annotation_config_order': ['flip', 'resize'], 'geometric_transforms_order': ['flip', 'resize'], 'orders_match': True, 'duplicate_resize_detected': False}, 'has_geometric_transforms': True, 'geometric_transforms': [{'type': 'flip', 'params': {'vertical': True}, 'index': 0}, {'type': 'resize', 'params': {'width': 500, 'height': 500}, 'index': 1}], 'photometric_transforms': [], 'total_transforms': 2, 'geometric_count': 2, 'photometric_count': 0}    

=== 📋 WRITING ANNOTATIONS.JSON ===
Total images with annotations: 6
   images\train\cat.jpg: 3 annotations
      First annotation: {'class_id': 0, 'bbox': [0.868, 0.624, 1.0, 1.0]}
   images\train\cat_flip_vertical.jpg: 0 annotations
   images\val\car.jpg: 2 annotations
      First annotation: {'class_id': 2, 'bbox': [0.727, 0.707, 0.924, 0.98]}
   images\val\car_flip_vertical.jpg: 0 annotations
   images\test\dog.jpg: 1 annotations
      First annotation: {'class_id': 2, 'bbox': [0.884, 0.635, 1.0, 1.0]}
   images\test\dog_flip_vertical.jpg: 0 annotations
INFO:     127.0.0.1:54714 - "POST /api/v1/logs/frontend/batch HTTP/1.1" 200 OK
🔍 DEBUG: Database path being used: V:\stage-1-labeling-app\app-3-fix-release-system-422-error\database.db
🔍 DEBUG: Database exists: True
🔍 DEBUG: SQL query returned 2 projects
INFO:     127.0.0.1:56065 - "POST /api/v1/releases/create HTTP/1.1" 200 OK
INFO:     127.0.0.1:54714 - "OPTIONS /api/transformation/available-transformations?_t=1758390058969 HTTP/1.1" 200 OK
INFO:     127.0.0.1:63405 - "OPTIONS /api/image-transformations/pending?_t=1758390058969 HTTP/1.1" 200 OK
INFO:     127.0.0.1:62945 - "OPTIONS /api/transformation/available-transformations?_t=1758390058969 HTTP/1.1" 200 OK
INFO:     127.0.0.1:62155 - "OPTIONS /api/image-transformations/pending?_t=1758390058969 HTTP/1.1" 200 OK
INFO:     127.0.0.1:54714 - "GET /api/transformation/available-transformations?_t=1758390058969 HTTP/1.1"
 200 OK
INFO:     127.0.0.1:62945 - "GET /api/transformation/available-transformations?_t=1758390058969 HTTP/1.1"
 200 OK
INFO:     127.0.0.1:56065 - "GET /api/v1/projects/1/releases HTTP/1.1" 200 OK
INFO:     127.0.0.1:63405 - "GET /api/image-transformations/pending?_t=1758390058969 HTTP/1.1" 200 OK    
INFO:     127.0.0.1:62155 - "GET /api/image-transformations/pending?_t=1758390058969 HTTP/1.1" 200 OK    
INFO:     127.0.0.1:62155 - "GET /api/image-transformations/release-config/version_auto_2025_09_20_19_40 HTTP/1.1" 200 OK
INFO:     127.0.0.1:62155 - "POST /api/v1/logs/frontend/batch HTTP/1.1" 200 OK
INFO:     127.0.0.1:62155 - "POST /api/v1/logs/frontend/batch HTTP/1.1" 200 OK
INFO:     127.0.0.1:63711 - "OPTIONS /api/transformation/available-transformations?_t