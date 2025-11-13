
=== 🔍 TRANSFORMATIONS DEBUG :: cat.jpg ===
transformations variable: [{'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}, {'type': 'rotate', 'params': {'angle': 24.6}}]
transformations type: <class 'list'>
transformations bool: True
🎯 COMPLEX TRANSFORMATIONS for cat.jpg
🖼️ Original image dims: (800, 600)
🎯 ORIGINAL IMAGE: Applying ONLY resize (baseline behavior)
🖼️ Resized to: (400, 300) using mode: fit_within

🔍 TRACKING FUNCTION INPUT:
   Transformations: [{'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}]
   Original dims: (800, 600)
   Final dims: (400, 300)
🎯 RESIZE CONFIG ALREADY EXISTS: {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}

📍 ANNOTATION TRACKING ORDER: ['resize']
🔧 GEOMETRIC TRANSFORMS ORDER: ['resize']
🔍 TRANSFORMATION CONFIG DETAILS: {'resize': {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}

🎯 TRACKING FUNCTION OUTPUT:
   transformation_config: {'resize': {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}
   Has geometric transforms: True
   Geometric transforms: [{'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}, 'index': 0}]
🎯 ORIGINAL IMAGE BASELINE: Applied resize-only, augmented images will get full combinations!
🎯 RELEASES.PY: Using NEW FUNCTIONS with internal transformation!
   📊 Tracking data: {'transformation_sequence': [{'index': 0, 'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}, 'is_geometric': True, 'is_photometric': False}], 'transformation_config': {'resize': {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}, 'original_dims': (800, 600), 'final_dims': (400, 300), 'debug_transformation_order': {'annotation_config_order': ['resize'], 'geometric_transforms_order': ['resize'], 'orders_match': True, 'duplicate_resize_detected': False}, 'has_geometric_transforms': True, 'geometric_transforms': [{'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}, 'index': 0}], 'photometric_transforms': [], 'total_transforms': 1, 'geometric_count': 1, 'photometric_count': 0}
🎯 NEW DETECTION FUNCTION CALLED!
   Annotations: 3
   Final dims: 400x300
   Has transform_config: True
   Original dims: (800, 600)
🔧 TRANSFORMING ANNOTATIONS: (800, 600) → 400x300
🔧 TRANSFORM CONFIG: {'resize': {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}
📦 ORIGINAL ANNOTATIONS (3):
   1. cat: x_min=107.5, y_min=40.5, x_max=760.5, y_max=583.5
   2. cat eye: x_min=317.5, y_min=204.5, x_max=372.5, y_max=254.5
   3. cat eye: x_min=429.5, y_min=201.5, x_max=483.5, y_max=251.5

🔄 UPDATE_ANNOTATIONS_FOR_TRANSFORMATIONS CALLED!
   📊 Input: 3 annotations
   📐 Dimensions: (800, 600) → (400, 300)
   🔧 Transform config: {'resize': {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}
   🎯 Has affine matrix: False
   🎯 RESIZE MODE: fit_within
   📏 Target size: 400x399
   📏 Original size: 800.0x600.0
   📐 FIT_WITHIN: scale=0.5000, final_canvas=400x300
   🎯 FINAL CANVAS DIMENSIONS: (400, 300)
   🔧 USING LEGACY/SEQUENTIAL TRANSFORMATION PATH
   📊 Processing 3 annotations individually
   🔄 Processing annotation 1/3: cat
      🎯 _TRANSFORM_SINGLE_ANNOTATION called
         📦 Annotation type: Annotation
         📦 Annotation full type: <class 'database.models.Annotation'>
         📦 Class: cat
         📦 Input bbox: x_min=107.5, y_min=40.5, x_max=760.5, y_max=583.5
         📐 Dimensions: (800, 600) → (400, 300)
         🔍 isinstance(annotation, BoundingBox): False
         🔍 BoundingBox type: <class 'core.annotation_transformer.BoundingBox'>
         🔧 Detected database annotation - label_mode: yolo_detection
         🔧 Using bounding box coordinates for detection task...
         🔧 About to call _transform_bbox with temp bbox...

🚀 STARTING BBOX TRANSFORMATION
================================================================================
📦 INPUT BBOX:
   class_name: cat
   class_id: 12
   x_min: 107.5, y_min: 40.5
   x_max: 760.5, y_max: 583.5
   width: 653.0, height: 543.0
📐 DIMENSIONS:
   original_dims: (800, 600)
   new_dims: (400, 300)
🔧 TRANSFORMATION CONFIG:
   1. resize: {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}
================================================================================
🔢 INITIAL VALUES:
   x_min: 107.5, y_min: 40.5
   x_max: 760.5, y_max: 583.5
   current_width: 800, current_height: 600

🔍 RESIZE TRANSFORMATION DEBUG
============================================================
📊 INPUT PARAMETERS:
   target_width: 400
   target_height: 399
   resize_mode: fit_within
   current_width: 800
   current_height: 600
📍 ORIGINAL BBOX (before resize):
   x_min: 107.5, y_min: 40.5
   x_max: 760.5, y_max: 583.5
   width: 653.0, height: 543.0
🔢 FLOAT CONVERSIONS:
   source_w: 800.0, source_h: 600.0
   tw: 400.0, th: 399.0
🎯 FIT_WITHIN MODE:
   s = min(400.0/800.0, 399.0/600.0) = min(0.5, 0.665) = 0.5
📍 BEFORE SCALING:
   x_min: 107.5, x_max: 760.5
   y_min: 40.5, y_max: 583.5
📍 AFTER SCALING:
   x_min: 53.75, x_max: 380.25
   y_min: 20.25, y_max: 291.75
🖼️ CANVAS SIZE: 400.0 x 300.0
✅ RESIZE COMPLETE - NEW CANVAS: 400.0 x 300.0
============================================================

🔧 FINAL CLIPPING AND VALIDATION:
   Before clipping: x_min=53.75, y_min=20.25, x_max=380.25, y_max=291.75
   Canvas bounds: width=400.0, height=300.0
   After clipping: x_min=53.75, y_min=20.25, x_max=380.25, y_max=291.75

✅ TRANSFORMATION COMPLETE!
📦 FINAL BBOX:
   class_name: cat
   class_id: 12
   x_min: 53.75, y_min: 20.25
   x_max: 380.25, y_max: 291.75
   width: 326.5
   height: 271.5
================================================================================
         🔧 _transform_bbox returned: BoundingBox(x_min=53.75, y_min=20.25, x_max=380.25, y_max=291.75, class_name='cat', class_id=12, confidence=1.0)
         📦 Updated annotation: x_min=53.75, y_min=20.25, x_max=380.25, y_max=291.75
   🔄 Processing annotation 2/3: cat eye
      🎯 _TRANSFORM_SINGLE_ANNOTATION called
         📦 Annotation type: Annotation
         📦 Annotation full type: <class 'database.models.Annotation'>
         📦 Class: cat eye
         📦 Input bbox: x_min=317.5, y_min=204.5, x_max=372.5, y_max=254.5
         📐 Dimensions: (800, 600) → (400, 300)
         🔍 isinstance(annotation, BoundingBox): False
         🔍 BoundingBox type: <class 'core.annotation_transformer.BoundingBox'>
         🔧 Detected database annotation - label_mode: yolo_detection
         🔧 Using bounding box coordinates for detection task...
         🔧 About to call _transform_bbox with temp bbox...

🚀 STARTING BBOX TRANSFORMATION
================================================================================
📦 INPUT BBOX:
   class_name: cat eye
   class_id: 16
   x_min: 317.5, y_min: 204.5
   x_max: 372.5, y_max: 254.5
   width: 55.0, height: 50.0
📐 DIMENSIONS:
   original_dims: (800, 600)
   new_dims: (400, 300)
🔧 TRANSFORMATION CONFIG:
   1. resize: {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}
================================================================================
🔢 INITIAL VALUES:
   x_min: 317.5, y_min: 204.5
   x_max: 372.5, y_max: 254.5
   current_width: 800, current_height: 600

🔍 RESIZE TRANSFORMATION DEBUG
============================================================
📊 INPUT PARAMETERS:
   target_width: 400
   target_height: 399
   resize_mode: fit_within
   current_width: 800
   current_height: 600
📍 ORIGINAL BBOX (before resize):
   x_min: 317.5, y_min: 204.5
   x_max: 372.5, y_max: 254.5
   width: 55.0, height: 50.0
🔢 FLOAT CONVERSIONS:
   source_w: 800.0, source_h: 600.0
   tw: 400.0, th: 399.0
🎯 FIT_WITHIN MODE:
   s = min(400.0/800.0, 399.0/600.0) = min(0.5, 0.665) = 0.5
📍 BEFORE SCALING:
   x_min: 317.5, x_max: 372.5
   y_min: 204.5, y_max: 254.5
📍 AFTER SCALING:
   x_min: 158.75, x_max: 186.25
   y_min: 102.25, y_max: 127.25
🖼️ CANVAS SIZE: 400.0 x 300.0
✅ RESIZE COMPLETE - NEW CANVAS: 400.0 x 300.0
============================================================

🔧 FINAL CLIPPING AND VALIDATION:
   Before clipping: x_min=158.75, y_min=102.25, x_max=186.25, y_max=127.25
   Canvas bounds: width=400.0, height=300.0
   After clipping: x_min=158.75, y_min=102.25, x_max=186.25, y_max=127.25

✅ TRANSFORMATION COMPLETE!
📦 FINAL BBOX:
   class_name: cat eye
   class_id: 16
   x_min: 158.75, y_min: 102.25
   x_max: 186.25, y_max: 127.25
   width: 27.5
   height: 25.0
================================================================================
         🔧 _transform_bbox returned: BoundingBox(x_min=158.75, y_min=102.25, x_max=186.25, y_max=127.25, class_name='cat eye', class_id=16, confidence=1.0)
         📦 Updated annotation: x_min=158.75, y_min=102.25, x_max=186.25, y_max=127.25
   🔄 Processing annotation 3/3: cat eye
      🎯 _TRANSFORM_SINGLE_ANNOTATION called
         📦 Annotation type: Annotation
         📦 Annotation full type: <class 'database.models.Annotation'>
         📦 Class: cat eye
         📦 Input bbox: x_min=429.5, y_min=201.5, x_max=483.5, y_max=251.5
         📐 Dimensions: (800, 600) → (400, 300)
         🔍 isinstance(annotation, BoundingBox): False
         🔍 BoundingBox type: <class 'core.annotation_transformer.BoundingBox'>
         🔧 Detected database annotation - label_mode: yolo_detection
         🔧 Using bounding box coordinates for detection task...
         🔧 About to call _transform_bbox with temp bbox...

🚀 STARTING BBOX TRANSFORMATION
================================================================================
📦 INPUT BBOX:
   class_name: cat eye
   class_id: 16
   x_min: 429.5, y_min: 201.5
   x_max: 483.5, y_max: 251.5
   width: 54.0, height: 50.0
📐 DIMENSIONS:
   original_dims: (800, 600)
   new_dims: (400, 300)
🔧 TRANSFORMATION CONFIG:
   1. resize: {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}
================================================================================
🔢 INITIAL VALUES:
   x_min: 429.5, y_min: 201.5
   x_max: 483.5, y_max: 251.5
   current_width: 800, current_height: 600

🔍 RESIZE TRANSFORMATION DEBUG
============================================================
📊 INPUT PARAMETERS:
   target_width: 400
   target_height: 399
   resize_mode: fit_within
   current_width: 800
   current_height: 600
📍 ORIGINAL BBOX (before resize):
   x_min: 429.5, y_min: 201.5
   x_max: 483.5, y_max: 251.5
   width: 54.0, height: 50.0
🔢 FLOAT CONVERSIONS:
   source_w: 800.0, source_h: 600.0
   tw: 400.0, th: 399.0
🎯 FIT_WITHIN MODE:
   s = min(400.0/800.0, 399.0/600.0) = min(0.5, 0.665) = 0.5
📍 BEFORE SCALING:
   x_min: 429.5, x_max: 483.5
   y_min: 201.5, y_max: 251.5
📍 AFTER SCALING:
   x_min: 214.75, x_max: 241.75
   y_min: 100.75, y_max: 125.75
🖼️ CANVAS SIZE: 400.0 x 300.0
✅ RESIZE COMPLETE - NEW CANVAS: 400.0 x 300.0
============================================================

🔧 FINAL CLIPPING AND VALIDATION:
   Before clipping: x_min=214.75, y_min=100.75, x_max=241.75, y_max=125.75
   Canvas bounds: width=400.0, height=300.0
   After clipping: x_min=214.75, y_min=100.75, x_max=241.75, y_max=125.75

✅ TRANSFORMATION COMPLETE!
📦 FINAL BBOX:
   class_name: cat eye
   class_id: 16
   x_min: 214.75, y_min: 100.75
   x_max: 241.75, y_max: 125.75
   width: 27.0
   height: 25.0
================================================================================
         🔧 _transform_bbox returned: BoundingBox(x_min=214.75, y_min=100.75, x_max=241.75, y_max=125.75, class_name='cat eye', class_id=16, confidence=1.0)
         📦 Updated annotation: x_min=214.75, y_min=100.75, x_max=241.75, y_max=125.75
   Original: 3 → Transformed: 3
📦 TRANSFORMED ANNOTATIONS (3):
   1. cat: x_min=53.75, y_min=20.25, x_max=380.25, y_max=291.75
   2. cat eye: x_min=158.75, y_min=102.25, x_max=186.25, y_max=127.25
   3. cat eye: x_min=214.75, y_min=100.75, x_max=241.75, y_max=125.75
✅ NEW DETECTION FUNCTION RESULT: 3 lines

🖼️ IMAGE GENERATION ORDER: ['rotate', 'resize']

🔍 TRACKING FUNCTION INPUT:
   Transformations: [{'type': 'rotate', 'params': {'angle': 24.6}}, {'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}]
   Original dims: (800, 600)
   Final dims: (400, 359)
🎯 RESIZE CONFIG ALREADY EXISTS: {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}

📍 ANNOTATION TRACKING ORDER: ['rotate', 'resize']
🔧 GEOMETRIC TRANSFORMS ORDER: ['rotate', 'resize']
🔍 TRANSFORMATION CONFIG DETAILS: {'rotate': {'enabled': True, 'angle': 24.6}, 'resize': {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}

🎯 TRACKING FUNCTION OUTPUT:
   transformation_config: {'rotate': {'enabled': True, 'angle': 24.6}, 'resize': {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}
   Has geometric transforms: True
   Geometric transforms: [{'type': 'rotate', 'params': {'angle': 24.6}, 'index': 0}, {'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}, 'index': 1}]
🎯 RELEASES.PY: Using ADVANCED transformation system for annotations!
   📊 Tracking data: {'transformation_sequence': [{'index': 0, 'type': 'rotate', 'params': {'angle': 24.6}, 'is_geometric': True, 'is_photometric': False}, {'index': 1, 'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}, 'is_geometric': True, 'is_photometric': False}], 'transformation_config': {'rotate': {'enabled': True, 'angle': 24.6}, 'resize': {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}, 'original_dims': (800, 600), 'final_dims': (400, 359), 'debug_transformation_order': {'annotation_config_order': ['rotate', 'resize'], 'geometric_transforms_order': ['rotate', 'resize'], 'orders_match': True, 'duplicate_resize_detected': False}, 'has_geometric_transforms': True, 'geometric_transforms': [{'type': 'rotate', 'params': {'angle': 24.6}, 'index': 0}, {'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}, 'index': 1}], 'photometric_transforms': [], 'total_transforms': 2, 'geometric_count': 2, 'photometric_count': 0}
🔍 DEBUG: About to transform 3 annotations
   First annotation type: <class 'database.models.Annotation'>
   First annotation attrs: ['class_id', 'class_name', 'confidence', 'created_at', 'id', 'image', 'image_id', 'is_auto_generated', 'is_verified', 'metadata', 'model_id', 'registry', 'segmentation', 'updated_at', 'x_max', 'x_min', 'y_max', 'y_min']
   First annotation coords: (53.75, 20.25, 380.25, 291.75)

🖼️ IMAGE GENERATION ORDER: ['rotate', 'resize']

🔍 TRACKING FUNCTION INPUT:
   Transformations: [{'type': 'rotate', 'params': {'angle': -24.6}}, {'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}]
   Original dims: (800, 600)
   Final dims: (400, 359)
🎯 RESIZE CONFIG ALREADY EXISTS: {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}

📍 ANNOTATION TRACKING ORDER: ['rotate', 'resize']
🔧 GEOMETRIC TRANSFORMS ORDER: ['rotate', 'resize']
🔍 TRANSFORMATION CONFIG DETAILS: {'rotate': {'enabled': True, 'angle': -24.6}, 'resize': {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}

🎯 TRACKING FUNCTION OUTPUT:
   transformation_config: {'rotate': {'enabled': True, 'angle': -24.6}, 'resize': {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}
   Has geometric transforms: True
   Geometric transforms: [{'type': 'rotate', 'params': {'angle': -24.6}, 'index': 0}, {'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}, 'index': 1}]
🎯 RELEASES.PY: Using ADVANCED transformation system for annotations!
   📊 Tracking data: {'transformation_sequence': [{'index': 0, 'type': 'rotate', 'params': {'angle': -24.6}, 'is_geometric': True, 'is_photometric': False}, {'index': 1, 'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}, 'is_geometric': True, 'is_photometric': False}], 'transformation_config': {'rotate': {'enabled': True, 'angle': -24.6}, 'resize': {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}, 'original_dims': (800, 600), 'final_dims': (400, 359), 'debug_transformation_order': {'annotation_config_order': ['rotate', 'resize'], 'geometric_transforms_order': ['rotate', 'resize'], 'orders_match': True, 'duplicate_resize_detected': False}, 'has_geometric_transforms': True, 'geometric_transforms': [{'type': 'rotate', 'params': {'angle': -24.6}, 'index': 0}, {'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}, 'index': 1}], 'photometric_transforms': [], 'total_transforms': 2, 'geometric_count': 2, 'photometric_count': 0}
🔍 DEBUG: About to transform 3 annotations
   First annotation type: <class 'database.models.Annotation'>
   First annotation attrs: ['class_id', 'class_name', 'confidence', 'created_at', 'id', 'image', 'image_id', 'is_auto_generated', 'is_verified', 'metadata', 'model_id', 'registry', 'segmentation', 'updated_at', 'x_max', 'x_min', 'y_max', 'y_min']
   First annotation coords: (53.75, 20.25, 380.25, 291.75)

=== 🔍 TRANSFORMATIONS DEBUG :: car.jpg ===
transformations variable: [{'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}, {'type': 'rotate', 'params': {'angle': 24.6}}]
transformations type: <class 'list'>
transformations bool: True
🎯 COMPLEX TRANSFORMATIONS for car.jpg
🖼️ Original image dims: (800, 600)
🎯 ORIGINAL IMAGE: Applying ONLY resize (baseline behavior)
🖼️ Resized to: (400, 300) using mode: fit_within

🔍 TRACKING FUNCTION INPUT:
   Transformations: [{'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}]
   Original dims: (800, 600)
   Final dims: (400, 300)
🎯 RESIZE CONFIG ALREADY EXISTS: {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}

📍 ANNOTATION TRACKING ORDER: ['resize']
🔧 GEOMETRIC TRANSFORMS ORDER: ['resize']
🔍 TRANSFORMATION CONFIG DETAILS: {'resize': {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}

🎯 TRACKING FUNCTION OUTPUT:
   transformation_config: {'resize': {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}
   Has geometric transforms: True
   Geometric transforms: [{'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}, 'index': 0}]
🎯 ORIGINAL IMAGE BASELINE: Applied resize-only, augmented images will get full combinations!
🎯 RELEASES.PY: Using NEW FUNCTIONS with internal transformation!
   📊 Tracking data: {'transformation_sequence': [{'index': 0, 'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}, 'is_geometric': True, 'is_photometric': False}], 'transformation_config': {'resize': {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}, 'original_dims': (800, 600), 'final_dims': (400, 300), 'debug_transformation_order': {'annotation_config_order': ['resize'], 'geometric_transforms_order': ['resize'], 'orders_match': True, 'duplicate_resize_detected': False}, 'has_geometric_transforms': True, 'geometric_transforms': [{'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}, 'index': 0}], 'photometric_transforms': [], 'total_transforms': 1, 'geometric_count': 1, 'photometric_count': 0}
🎯 NEW DETECTION FUNCTION CALLED!
   Annotations: 2
   Final dims: 400x300
   Has transform_config: True
   Original dims: (800, 600)
🔧 TRANSFORMING ANNOTATIONS: (800, 600) → 400x300
🔧 TRANSFORM CONFIG: {'resize': {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}
📦 ORIGINAL ANNOTATIONS (2):
   1. dog: x_min=132.5, y_min=108.5, x_max=594.5, y_max=598.5
   2. dog eye: x_min=454.5, y_min=288.5, x_max=502.5, y_max=324.5

🔄 UPDATE_ANNOTATIONS_FOR_TRANSFORMATIONS CALLED!
   📊 Input: 2 annotations
   📐 Dimensions: (800, 600) → (400, 300)
   🔧 Transform config: {'resize': {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}
   🎯 Has affine matrix: False
   🎯 RESIZE MODE: fit_within
   📏 Target size: 400x399
   📏 Original size: 800.0x600.0
   📐 FIT_WITHIN: scale=0.5000, final_canvas=400x300
   🎯 FINAL CANVAS DIMENSIONS: (400, 300)
   🔧 USING LEGACY/SEQUENTIAL TRANSFORMATION PATH
   📊 Processing 2 annotations individually
   🔄 Processing annotation 1/2: dog
      🎯 _TRANSFORM_SINGLE_ANNOTATION called
         📦 Annotation type: Annotation
         📦 Annotation full type: <class 'database.models.Annotation'>
         📦 Class: dog
         📦 Input bbox: x_min=132.5, y_min=108.5, x_max=594.5, y_max=598.5
         📐 Dimensions: (800, 600) → (400, 300)
         🔍 isinstance(annotation, BoundingBox): False
         🔍 BoundingBox type: <class 'core.annotation_transformer.BoundingBox'>
         🔧 Detected database annotation - label_mode: yolo_detection
         🔧 Using bounding box coordinates for detection task...
         🔧 About to call _transform_bbox with temp bbox...

🚀 STARTING BBOX TRANSFORMATION
================================================================================
📦 INPUT BBOX:
   class_name: dog
   class_id: 1
   x_min: 132.5, y_min: 108.5
   x_max: 594.5, y_max: 598.5
   width: 462.0, height: 490.0
📐 DIMENSIONS:
   original_dims: (800, 600)
   new_dims: (400, 300)
🔧 TRANSFORMATION CONFIG:
   1. resize: {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}
================================================================================
🔢 INITIAL VALUES:
   x_min: 132.5, y_min: 108.5
   x_max: 594.5, y_max: 598.5
   current_width: 800, current_height: 600

🔍 RESIZE TRANSFORMATION DEBUG
============================================================
📊 INPUT PARAMETERS:
   target_width: 400
   target_height: 399
   resize_mode: fit_within
   current_width: 800
   current_height: 600
📍 ORIGINAL BBOX (before resize):
   x_min: 132.5, y_min: 108.5
   x_max: 594.5, y_max: 598.5
   width: 462.0, height: 490.0
🔢 FLOAT CONVERSIONS:
   source_w: 800.0, source_h: 600.0
   tw: 400.0, th: 399.0
🎯 FIT_WITHIN MODE:
   s = min(400.0/800.0, 399.0/600.0) = min(0.5, 0.665) = 0.5
📍 BEFORE SCALING:
   x_min: 132.5, x_max: 594.5
   y_min: 108.5, y_max: 598.5
📍 AFTER SCALING:
   x_min: 66.25, x_max: 297.25
   y_min: 54.25, y_max: 299.25
🖼️ CANVAS SIZE: 400.0 x 300.0
✅ RESIZE COMPLETE - NEW CANVAS: 400.0 x 300.0
============================================================

🔧 FINAL CLIPPING AND VALIDATION:
   Before clipping: x_min=66.25, y_min=54.25, x_max=297.25, y_max=299.25
   Canvas bounds: width=400.0, height=300.0
   After clipping: x_min=66.25, y_min=54.25, x_max=297.25, y_max=299.25

✅ TRANSFORMATION COMPLETE!
📦 FINAL BBOX:
   class_name: dog
   class_id: 1
   x_min: 66.25, y_min: 54.25
   x_max: 297.25, y_max: 299.25
   width: 231.0
   height: 245.0
================================================================================
         🔧 _transform_bbox returned: BoundingBox(x_min=66.25, y_min=54.25, x_max=297.25, y_max=299.25, class_name='dog', class_id=1, confidence=1.0)
         📦 Updated annotation: x_min=66.25, y_min=54.25, x_max=297.25, y_max=299.25
   🔄 Processing annotation 2/2: dog eye
      🎯 _TRANSFORM_SINGLE_ANNOTATION called
         📦 Annotation type: Annotation
         📦 Annotation full type: <class 'database.models.Annotation'>
         📦 Class: dog eye
         📦 Input bbox: x_min=454.5, y_min=288.5, x_max=502.5, y_max=324.5
         📐 Dimensions: (800, 600) → (400, 300)
         🔍 isinstance(annotation, BoundingBox): False
         🔍 BoundingBox type: <class 'core.annotation_transformer.BoundingBox'>
         🔧 Detected database annotation - label_mode: yolo_detection
         🔧 Using bounding box coordinates for detection task...
         🔧 About to call _transform_bbox with temp bbox...

🚀 STARTING BBOX TRANSFORMATION
================================================================================
📦 INPUT BBOX:
   class_name: dog eye
   class_id: 15
   x_min: 454.5, y_min: 288.5
   x_max: 502.5, y_max: 324.5
   width: 48.0, height: 36.0
📐 DIMENSIONS:
   original_dims: (800, 600)
   new_dims: (400, 300)
🔧 TRANSFORMATION CONFIG:
   1. resize: {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}
================================================================================
🔢 INITIAL VALUES:
   x_min: 454.5, y_min: 288.5
   x_max: 502.5, y_max: 324.5
   current_width: 800, current_height: 600

🔍 RESIZE TRANSFORMATION DEBUG
============================================================
📊 INPUT PARAMETERS:
   target_width: 400
   target_height: 399
   resize_mode: fit_within
   current_width: 800
   current_height: 600
📍 ORIGINAL BBOX (before resize):
   x_min: 454.5, y_min: 288.5
   x_max: 502.5, y_max: 324.5
   width: 48.0, height: 36.0
🔢 FLOAT CONVERSIONS:
   source_w: 800.0, source_h: 600.0
   tw: 400.0, th: 399.0
🎯 FIT_WITHIN MODE:
   s = min(400.0/800.0, 399.0/600.0) = min(0.5, 0.665) = 0.5
📍 BEFORE SCALING:
   x_min: 454.5, x_max: 502.5
   y_min: 288.5, y_max: 324.5
📍 AFTER SCALING:
   x_min: 227.25, x_max: 251.25
   y_min: 144.25, y_max: 162.25
🖼️ CANVAS SIZE: 400.0 x 300.0
✅ RESIZE COMPLETE - NEW CANVAS: 400.0 x 300.0
============================================================

🔧 FINAL CLIPPING AND VALIDATION:
   Before clipping: x_min=227.25, y_min=144.25, x_max=251.25, y_max=162.25
   Canvas bounds: width=400.0, height=300.0
   After clipping: x_min=227.25, y_min=144.25, x_max=251.25, y_max=162.25

✅ TRANSFORMATION COMPLETE!
📦 FINAL BBOX:
   class_name: dog eye
   class_id: 15
   x_min: 227.25, y_min: 144.25
   x_max: 251.25, y_max: 162.25
   width: 24.0
   height: 18.0
================================================================================
         🔧 _transform_bbox returned: BoundingBox(x_min=227.25, y_min=144.25, x_max=251.25, y_max=162.25, class_name='dog eye', class_id=15, confidence=1.0)
         📦 Updated annotation: x_min=227.25, y_min=144.25, x_max=251.25, y_max=162.25
   Original: 2 → Transformed: 2
📦 TRANSFORMED ANNOTATIONS (2):
   1. dog: x_min=66.25, y_min=54.25, x_max=297.25, y_max=299.25
   2. dog eye: x_min=227.25, y_min=144.25, x_max=251.25, y_max=162.25
✅ NEW DETECTION FUNCTION RESULT: 2 lines

🖼️ IMAGE GENERATION ORDER: ['rotate', 'resize']

🔍 TRACKING FUNCTION INPUT:
   Transformations: [{'type': 'rotate', 'params': {'angle': 24.6}}, {'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}]
   Original dims: (800, 600)
   Final dims: (400, 359)
🎯 RESIZE CONFIG ALREADY EXISTS: {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}

📍 ANNOTATION TRACKING ORDER: ['rotate', 'resize']
🔧 GEOMETRIC TRANSFORMS ORDER: ['rotate', 'resize']
🔍 TRANSFORMATION CONFIG DETAILS: {'rotate': {'enabled': True, 'angle': 24.6}, 'resize': {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}

🎯 TRACKING FUNCTION OUTPUT:
   transformation_config: {'rotate': {'enabled': True, 'angle': 24.6}, 'resize': {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}
   Has geometric transforms: True
   Geometric transforms: [{'type': 'rotate', 'params': {'angle': 24.6}, 'index': 0}, {'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}, 'index': 1}]
🎯 RELEASES.PY: Using ADVANCED transformation system for annotations!
   📊 Tracking data: {'transformation_sequence': [{'index': 0, 'type': 'rotate', 'params': {'angle': 24.6}, 'is_geometric': True, 'is_photometric': False}, {'index': 1, 'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}, 'is_geometric': True, 'is_photometric': False}], 'transformation_config': {'rotate': {'enabled': True, 'angle': 24.6}, 'resize': {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}, 'original_dims': (800, 600), 'final_dims': (400, 359), 'debug_transformation_order': {'annotation_config_order': ['rotate', 'resize'], 'geometric_transforms_order': ['rotate', 'resize'], 'orders_match': True, 'duplicate_resize_detected': False}, 'has_geometric_transforms': True, 'geometric_transforms': [{'type': 'rotate', 'params': {'angle': 24.6}, 'index': 0}, {'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}, 'index': 1}], 'photometric_transforms': [], 'total_transforms': 2, 'geometric_count': 2, 'photometric_count': 0}
🔍 DEBUG: About to transform 2 annotations
   First annotation type: <class 'database.models.Annotation'>
   First annotation attrs: ['class_id', 'class_name', 'confidence', 'created_at', 'id', 'image', 'image_id', 'is_auto_generated', 'is_verified', 'metadata', 'model_id', 'registry', 'segmentation', 'updated_at', 'x_max', 'x_min', 'y_max', 'y_min']
   First annotation coords: (66.25, 54.25, 297.25, 299.25)

🖼️ IMAGE GENERATION ORDER: ['rotate', 'resize']

🔍 TRACKING FUNCTION INPUT:
   Transformations: [{'type': 'rotate', 'params': {'angle': -24.6}}, {'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}]
   Original dims: (800, 600)
   Final dims: (400, 359)
🎯 RESIZE CONFIG ALREADY EXISTS: {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}

📍 ANNOTATION TRACKING ORDER: ['rotate', 'resize']
🔧 GEOMETRIC TRANSFORMS ORDER: ['rotate', 'resize']
🔍 TRANSFORMATION CONFIG DETAILS: {'rotate': {'enabled': True, 'angle': -24.6}, 'resize': {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}

🎯 TRACKING FUNCTION OUTPUT:
   transformation_config: {'rotate': {'enabled': True, 'angle': -24.6}, 'resize': {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}
   Has geometric transforms: True
   Geometric transforms: [{'type': 'rotate', 'params': {'angle': -24.6}, 'index': 0}, {'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}, 'index': 1}]
🎯 RELEASES.PY: Using ADVANCED transformation system for annotations!
   📊 Tracking data: {'transformation_sequence': [{'index': 0, 'type': 'rotate', 'params': {'angle': -24.6}, 'is_geometric': True, 'is_photometric': False}, {'index': 1, 'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}, 'is_geometric': True, 'is_photometric': False}], 'transformation_config': {'rotate': {'enabled': True, 'angle': -24.6}, 'resize': {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}, 'original_dims': (800, 600), 'final_dims': (400, 359), 'debug_transformation_order': {'annotation_config_order': ['rotate', 'resize'], 'geometric_transforms_order': ['rotate', 'resize'], 'orders_match': True, 'duplicate_resize_detected': False}, 'has_geometric_transforms': True, 'geometric_transforms': [{'type': 'rotate', 'params': {'angle': -24.6}, 'index': 0}, {'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}, 'index': 1}], 'photometric_transforms': [], 'total_transforms': 2, 'geometric_count': 2, 'photometric_count': 0}
🔍 DEBUG: About to transform 2 annotations
   First annotation type: <class 'database.models.Annotation'>
   First annotation attrs: ['class_id', 'class_name', 'confidence', 'created_at', 'id', 'image', 'image_id', 'is_auto_generated', 'is_verified', 'metadata', 'model_id', 'registry', 'segmentation', 'updated_at', 'x_max', 'x_min', 'y_max', 'y_min']
   First annotation coords: (66.25, 54.25, 297.25, 299.25)

=== 🔍 TRANSFORMATIONS DEBUG :: dog.jpg ===
transformations variable: [{'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}, {'type': 'rotate', 'params': {'angle': 24.6}}]
transformations type: <class 'list'>
transformations bool: True
🎯 COMPLEX TRANSFORMATIONS for dog.jpg
🖼️ Original image dims: (800, 600)
🎯 ORIGINAL IMAGE: Applying ONLY resize (baseline behavior)
🖼️ Resized to: (400, 300) using mode: fit_within

🔍 TRACKING FUNCTION INPUT:
   Transformations: [{'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}]
   Original dims: (800, 600)
   Final dims: (400, 300)
🎯 RESIZE CONFIG ALREADY EXISTS: {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}

📍 ANNOTATION TRACKING ORDER: ['resize']
🔧 GEOMETRIC TRANSFORMS ORDER: ['resize']
🔍 TRANSFORMATION CONFIG DETAILS: {'resize': {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}

🎯 TRACKING FUNCTION OUTPUT:
   transformation_config: {'resize': {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}
   Has geometric transforms: True
   Geometric transforms: [{'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}, 'index': 0}]
🎯 ORIGINAL IMAGE BASELINE: Applied resize-only, augmented images will get full combinations!
🎯 RELEASES.PY: Using NEW FUNCTIONS with internal transformation!
   📊 Tracking data: {'transformation_sequence': [{'index': 0, 'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}, 'is_geometric': True, 'is_photometric': False}], 'transformation_config': {'resize': {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}, 'original_dims': (800, 600), 'final_dims': (400, 300), 'debug_transformation_order': {'annotation_config_order': ['resize'], 'geometric_transforms_order': ['resize'], 'orders_match': True, 'duplicate_resize_detected': False}, 'has_geometric_transforms': True, 'geometric_transforms': [{'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}, 'index': 0}], 'photometric_transforms': [], 'total_transforms': 1, 'geometric_count': 1, 'photometric_count': 0}
🎯 NEW DETECTION FUNCTION CALLED!
   Annotations: 1
   Final dims: 400x300
   Has transform_config: True
   Original dims: (800, 600)
🔧 TRANSFORMING ANNOTATIONS: (800, 600) → 400x300
🔧 TRANSFORM CONFIG: {'resize': {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}
📦 ORIGINAL ANNOTATIONS (1):
   1. dog: x_min=179.5, y_min=37.5, x_max=704.5, y_max=597.5

🔄 UPDATE_ANNOTATIONS_FOR_TRANSFORMATIONS CALLED!
   📊 Input: 1 annotations
   📐 Dimensions: (800, 600) → (400, 300)
   🔧 Transform config: {'resize': {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}
   🎯 Has affine matrix: False
   🎯 RESIZE MODE: fit_within
   📏 Target size: 400x399
   📏 Original size: 800.0x600.0
   📐 FIT_WITHIN: scale=0.5000, final_canvas=400x300
   🎯 FINAL CANVAS DIMENSIONS: (400, 300)
   🔧 USING LEGACY/SEQUENTIAL TRANSFORMATION PATH
   📊 Processing 1 annotations individually
   🔄 Processing annotation 1/1: dog
      🎯 _TRANSFORM_SINGLE_ANNOTATION called
         📦 Annotation type: Annotation
         📦 Annotation full type: <class 'database.models.Annotation'>
         📦 Class: dog
         📦 Input bbox: x_min=179.5, y_min=37.5, x_max=704.5, y_max=597.5
         📐 Dimensions: (800, 600) → (400, 300)
         🔍 isinstance(annotation, BoundingBox): False
         🔍 BoundingBox type: <class 'core.annotation_transformer.BoundingBox'>
         🔧 Detected database annotation - label_mode: yolo_detection
         🔧 Using bounding box coordinates for detection task...
         🔧 About to call _transform_bbox with temp bbox...

🚀 STARTING BBOX TRANSFORMATION
================================================================================
📦 INPUT BBOX:
   class_name: dog
   class_id: 1
   x_min: 179.5, y_min: 37.5
   x_max: 704.5, y_max: 597.5
   width: 525.0, height: 560.0
📐 DIMENSIONS:
   original_dims: (800, 600)
   new_dims: (400, 300)
🔧 TRANSFORMATION CONFIG:
   1. resize: {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}
================================================================================
🔢 INITIAL VALUES:
   x_min: 179.5, y_min: 37.5
   x_max: 704.5, y_max: 597.5
   current_width: 800, current_height: 600

🔍 RESIZE TRANSFORMATION DEBUG
============================================================
📊 INPUT PARAMETERS:
   target_width: 400
   target_height: 399
   resize_mode: fit_within
   current_width: 800
   current_height: 600
📍 ORIGINAL BBOX (before resize):
   x_min: 179.5, y_min: 37.5
   x_max: 704.5, y_max: 597.5
   width: 525.0, height: 560.0
🔢 FLOAT CONVERSIONS:
   source_w: 800.0, source_h: 600.0
   tw: 400.0, th: 399.0
🎯 FIT_WITHIN MODE:
   s = min(400.0/800.0, 399.0/600.0) = min(0.5, 0.665) = 0.5
📍 BEFORE SCALING:
   x_min: 179.5, x_max: 704.5
   y_min: 37.5, y_max: 597.5
📍 AFTER SCALING:
   x_min: 89.75, x_max: 352.25
   y_min: 18.75, y_max: 298.75
🖼️ CANVAS SIZE: 400.0 x 300.0
✅ RESIZE COMPLETE - NEW CANVAS: 400.0 x 300.0
============================================================

🔧 FINAL CLIPPING AND VALIDATION:
   Before clipping: x_min=89.75, y_min=18.75, x_max=352.25, y_max=298.75
   Canvas bounds: width=400.0, height=300.0
   After clipping: x_min=89.75, y_min=18.75, x_max=352.25, y_max=298.75

✅ TRANSFORMATION COMPLETE!
📦 FINAL BBOX:
   class_name: dog
   class_id: 1
   x_min: 89.75, y_min: 18.75
   x_max: 352.25, y_max: 298.75
   width: 262.5
   height: 280.0
================================================================================
         🔧 _transform_bbox returned: BoundingBox(x_min=89.75, y_min=18.75, x_max=352.25, y_max=298.75, class_name='dog', class_id=1, confidence=1.0)
         📦 Updated annotation: x_min=89.75, y_min=18.75, x_max=352.25, y_max=298.75
   Original: 1 → Transformed: 1
📦 TRANSFORMED ANNOTATIONS (1):
   1. dog: x_min=89.75, y_min=18.75, x_max=352.25, y_max=298.75
✅ NEW DETECTION FUNCTION RESULT: 1 lines

🖼️ IMAGE GENERATION ORDER: ['rotate', 'resize']

🔍 TRACKING FUNCTION INPUT:
   Transformations: [{'type': 'rotate', 'params': {'angle': 24.6}}, {'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}]
   Original dims: (800, 600)
   Final dims: (400, 359)
🎯 RESIZE CONFIG ALREADY EXISTS: {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}

📍 ANNOTATION TRACKING ORDER: ['rotate', 'resize']
🔧 GEOMETRIC TRANSFORMS ORDER: ['rotate', 'resize']
🔍 TRANSFORMATION CONFIG DETAILS: {'rotate': {'enabled': True, 'angle': 24.6}, 'resize': {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}

🎯 TRACKING FUNCTION OUTPUT:
   transformation_config: {'rotate': {'enabled': True, 'angle': 24.6}, 'resize': {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}
   Has geometric transforms: True
   Geometric transforms: [{'type': 'rotate', 'params': {'angle': 24.6}, 'index': 0}, {'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}, 'index': 1}]
🎯 RELEASES.PY: Using ADVANCED transformation system for annotations!
   📊 Tracking data: {'transformation_sequence': [{'index': 0, 'type': 'rotate', 'params': {'angle': 24.6}, 'is_geometric': True, 'is_photometric': False}, {'index': 1, 'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}, 'is_geometric': True, 'is_photometric': False}], 'transformation_config': {'rotate': {'enabled': True, 'angle': 24.6}, 'resize': {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}, 'original_dims': (800, 600), 'final_dims': (400, 359), 'debug_transformation_order': {'annotation_config_order': ['rotate', 'resize'], 'geometric_transforms_order': ['rotate', 'resize'], 'orders_match': True, 'duplicate_resize_detected': False}, 'has_geometric_transforms': True, 'geometric_transforms': [{'type': 'rotate', 'params': {'angle': 24.6}, 'index': 0}, {'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}, 'index': 1}], 'photometric_transforms': [], 'total_transforms': 2, 'geometric_count': 2, 'photometric_count': 0}
🔍 DEBUG: About to transform 1 annotations
   First annotation type: <class 'database.models.Annotation'>
   First annotation attrs: ['class_id', 'class_name', 'confidence', 'created_at', 'id', 'image', 'image_id', 'is_auto_generated', 'is_verified', 'metadata', 'model_id', 'registry', 'segmentation', 'updated_at', 'x_max', 'x_min', 'y_max', 'y_min']
   First annotation coords: (89.75, 18.75, 352.25, 298.75)

🖼️ IMAGE GENERATION ORDER: ['rotate', 'resize']

🔍 TRACKING FUNCTION INPUT:
   Transformations: [{'type': 'rotate', 'params': {'angle': -24.6}}, {'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}]
   Original dims: (800, 600)
   Final dims: (400, 359)
🎯 RESIZE CONFIG ALREADY EXISTS: {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}

📍 ANNOTATION TRACKING ORDER: ['rotate', 'resize']
🔧 GEOMETRIC TRANSFORMS ORDER: ['rotate', 'resize']
🔍 TRANSFORMATION CONFIG DETAILS: {'rotate': {'enabled': True, 'angle': -24.6}, 'resize': {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}

🎯 TRACKING FUNCTION OUTPUT:
   transformation_config: {'rotate': {'enabled': True, 'angle': -24.6}, 'resize': {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}
   Has geometric transforms: True
   Geometric transforms: [{'type': 'rotate', 'params': {'angle': -24.6}, 'index': 0}, {'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}, 'index': 1}]
🎯 RELEASES.PY: Using ADVANCED transformation system for annotations!
   📊 Tracking data: {'transformation_sequence': [{'index': 0, 'type': 'rotate', 'params': {'angle': -24.6}, 'is_geometric': True, 'is_photometric': False}, {'index': 1, 'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}, 'is_geometric': True, 'is_photometric': False}], 'transformation_config': {'rotate': {'enabled': True, 'angle': -24.6}, 'resize': {'enabled': True, 'width': 400, 'height': 399, 'resize_mode': 'fit_within'}}, 'original_dims': (800, 600), 'final_dims': (400, 359), 'debug_transformation_order': {'annotation_config_order': ['rotate', 'resize'], 'geometric_transforms_order': ['rotate', 'resize'], 'orders_match': True, 'duplicate_resize_detected': False}, 'has_geometric_transforms': True, 'geometric_transforms': [{'type': 'rotate', 'params': {'angle': -24.6}, 'index': 0}, {'type': 'resize', 'params': {'width': 400, 'height': 399, 'resize_mode': 'fit_within'}, 'index': 1}], 'photometric_transforms': [], 'total_transforms': 2, 'geometric_count': 2, 'photometric_count': 0}
🔍 DEBUG: About to transform 1 annotations
   First annotation type: <class 'database.models.Annotation'>
   First annotation attrs: ['class_id', 'class_name', 'confidence', 'created_at', 'id', 'image', 'image_id', 'is_auto_generated', 'is_verified', 'metadata', 'model_id', 'registry', 'segmentation', 'updated_at', 'x_max', 'x_min', 'y_max', 'y_min']
   First annotation coords: (89.75, 18.75, 352.25, 298.75)

=== 📋 WRITING ANNOTATIONS.JSON ===
Total images with annotations: 9
   images\train\cat.jpg: 3 annotations
      First annotation: {'class_id': 0, 'bbox': [0.5425, 0.52, 0.81625, 0.905]}
   images\train\cat_rotate-24.jpg: 0 annotations
   images\train\cat_rotate24.jpg: 0 annotations
   images\val\car.jpg: 2 annotations
      First annotation: {'class_id': 2, 'bbox': [0.454375, 0.589167, 0.5775, 0.816667]}
   images\val\car_rotate-24.jpg: 0 annotations
   images\val\car_rotate24.jpg: 0 annotations
   images\test\dog.jpg: 1 annotations
      First annotation: {'class_id': 2, 'bbox': [0.5525, 0.529167, 0.65625, 0.933333]}
   images\test\dog_rotate-24.jpg: 0 annotations
   images\test\dog_rotate24.jpg: 0 annotations
