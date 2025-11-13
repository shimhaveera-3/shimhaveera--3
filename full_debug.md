
=== 🔍 TRANSFORMATIONS DEBUG :: cat.jpg ===
transformations variable: [{'type': 'resize', 'params': {'width': 300, 'height': 300}}]
transformations type: <class 'list'>
transformations bool: True
🎯 RESIZE-ONLY DETECTED for cat.jpg
🖼️ Original image dims: (800, 600)
🖼️ Resized image dims: (300, 300)

🔍 TRACKING FUNCTION INPUT:
   Transformations: [{'type': 'resize', 'params': {'width': 300, 'height': 300}}]
   Original dims: (800, 600)
   Final dims: (300, 300)
🎯 RESIZE CONFIG ALREADY EXISTS: {'enabled': True, 'width': 300, 'height': 300}

📍 ANNOTATION TRACKING ORDER: ['resize']
🔧 GEOMETRIC TRANSFORMS ORDER: ['resize']
🔍 TRANSFORMATION CONFIG DETAILS: {'resize': {'enabled': True, 'width': 300, 'height': 300}}

🎯 TRACKING FUNCTION OUTPUT:
   transformation_config: {'resize': {'enabled': True, 'width': 300, 'height': 300}}
   Has geometric transforms: True
   Geometric transforms: [{'type': 'resize', 'params': {'width': 300, 'height': 300}, 'index': 0}]       
🎯 RESIZE-ONLY: Using tracking system for annotations!
🎯 RELEASES.PY: Using NEW FUNCTIONS with internal transformation!
   📊 Tracking data: {'transformation_sequence': [{'index': 0, 'type': 'resize', 'params': {'width': 300, 'height': 300}, 'is_geometric': True, 'is_photometric': False}], 'transformation_config': {'resize': {'enabled': True, 'width': 300, 'height': 300}}, 'original_dims': (800, 600), 'final_dims': (300, 300), 'debug_transformation_order': {'annotation_config_order': ['resize'], 'geometric_transforms_order': ['resize'], 'orders_match': True, 'duplicate_resize_detected': False}, 'has_geometric_transforms': True, 'geometric_transforms': [{'type': 'resize', 'params': {'width': 300, 'height': 300}, 'index': 0}], 'photometric_transforms': [], 'total_transforms': 1, 'geometric_count': 1, 'photometric_count': 0}
🎯 NEW DETECTION FUNCTION CALLED!
   Annotations: 3
   Final dims: 300x300
   Has transform_config: True
   Original dims: (800, 600)
🔧 TRANSFORMING ANNOTATIONS: (800, 600) → 300x300
🔧 TRANSFORM CONFIG: {'resize': {'enabled': True, 'width': 300, 'height': 300}}
📦 ORIGINAL ANNOTATIONS (3):
   1. cat: x_min=0.0, y_min=31.761766419753087, x_max=0.4175644444444433, y_max=36.155105679012344       
   2. cat eye: x_min=1.2533333333333325, y_min=36.39922222222222, x_max=1.8399999999999992, y_max=37.34737037037037
   3. cat eye: x_min=2.4479999999999995, y_min=36.342333333333336, x_max=3.0239999999999996, y_max=37.29048148148148

🔄 UPDATE_ANNOTATIONS_FOR_TRANSFORMATIONS CALLED!
   📊 Input: 3 annotations
   📐 Dimensions: (800, 600) → (300, 300)
   🔧 Transform config: {'resize': {'enabled': True, 'width': 300, 'height': 300}}
   🎯 Has affine matrix: False
   🎯 RESIZE MODE: stretch_to
   📏 Target size: 300x300
   📏 Original size: 800.0x600.0
   📐 STRETCH_TO: final_canvas=300x300
   🎯 FINAL CANVAS DIMENSIONS: (300, 300)
   🔧 USING LEGACY/SEQUENTIAL TRANSFORMATION PATH
   📊 Processing 3 annotations individually
   🔄 Processing annotation 1/3: cat
      🎯 _TRANSFORM_SINGLE_ANNOTATION called
         📦 Annotation type: Annotation
         📦 Annotation full type: <class 'database.models.Annotation'>
         📦 Class: cat
         📦 Input bbox: x_min=0.0, y_min=31.761766419753087, x_max=0.4175644444444433, y_max=36.155105679012344
         📐 Dimensions: (800, 600) → (300, 300)
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
   x_min: 0.0, y_min: 31.761766419753087
   x_max: 0.4175644444444433, y_max: 36.155105679012344
   width: 0.4175644444444433, height: 4.393339259259257
📐 DIMENSIONS:
   original_dims: (800, 600)
   new_dims: (300, 300)
🔧 TRANSFORMATION CONFIG:
   1. resize: {'enabled': True, 'width': 300, 'height': 300}
================================================================================
🔢 INITIAL VALUES:
   x_min: 0.0, y_min: 31.761766419753087
   x_max: 0.4175644444444433, y_max: 36.155105679012344
   current_width: 800, current_height: 600

🔍 RESIZE TRANSFORMATION DEBUG
============================================================
📊 INPUT PARAMETERS:
   target_width: 300
   target_height: 300
   resize_mode: stretch_to
   current_width: 800
   current_height: 600
📍 ORIGINAL BBOX (before resize):
   x_min: 0.0, y_min: 31.761766419753087
   x_max: 0.4175644444444433, y_max: 36.155105679012344
   width: 0.4175644444444433, height: 4.393339259259257
🔢 FLOAT CONVERSIONS:
   source_w: 800.0, source_h: 600.0
   tw: 300.0, th: 300.0
🎯 STRETCH_TO MODE:
   sx = 300.0 / 800.0 = 0.375
   sy = 300.0 / 600.0 = 0.5
📍 BEFORE SCALING:
   x_min: 0.0, x_max: 0.4175644444444433
   y_min: 31.761766419753087, y_max: 36.155105679012344
📍 AFTER SCALING:
   x_min: 0.0, x_max: 0.15658666666666624
   y_min: 15.880883209876544, y_max: 18.077552839506172
🖼️ CANVAS SIZE: 300.0 x 300.0
✅ RESIZE COMPLETE - NEW CANVAS: 300.0 x 300.0
============================================================

🔧 FINAL CLIPPING AND VALIDATION:
   Before clipping: x_min=0.0, y_min=15.880883209876544, x_max=0.15658666666666624, y_max=18.077552839506172
   🔄 Processing annotation 2/3: cat eye
      🎯 _TRANSFORM_SINGLE_ANNOTATION called
         📦 Annotation type: Annotation
         📦 Annotation full type: <class 'database.models.Annotation'>
         📦 Class: cat eye
         📦 Input bbox: x_min=1.2533333333333325, y_min=36.39922222222222, x_max=1.8399999999999992, y_max=37.34737037037037
         📐 Dimensions: (800, 600) → (300, 300)
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
   x_min: 1.2533333333333325, y_min: 36.39922222222222
   x_max: 1.8399999999999992, y_max: 37.34737037037037
   width: 0.5866666666666667, height: 0.9481481481481495
📐 DIMENSIONS:
   original_dims: (800, 600)
   new_dims: (300, 300)
🔧 TRANSFORMATION CONFIG:
   1. resize: {'enabled': True, 'width': 300, 'height': 300}
================================================================================
🔢 INITIAL VALUES:
   x_min: 1.2533333333333325, y_min: 36.39922222222222
   x_max: 1.8399999999999992, y_max: 37.34737037037037
   current_width: 800, current_height: 600

🔍 RESIZE TRANSFORMATION DEBUG
============================================================
📊 INPUT PARAMETERS:
   target_width: 300
   target_height: 300
   resize_mode: stretch_to
   current_width: 800
   current_height: 600
📍 ORIGINAL BBOX (before resize):
   x_min: 1.2533333333333325, y_min: 36.39922222222222
   x_max: 1.8399999999999992, y_max: 37.34737037037037
   width: 0.5866666666666667, height: 0.9481481481481495
🔢 FLOAT CONVERSIONS:
   source_w: 800.0, source_h: 600.0
   tw: 300.0, th: 300.0
🎯 STRETCH_TO MODE:
   sx = 300.0 / 800.0 = 0.375
   sy = 300.0 / 600.0 = 0.5
📍 BEFORE SCALING:
   x_min: 1.2533333333333325, x_max: 1.8399999999999992
   y_min: 36.39922222222222, y_max: 37.34737037037037
📍 AFTER SCALING:
   x_min: 0.4699999999999997, x_max: 0.6899999999999997
   y_min: 18.19961111111111, y_max: 18.673685185185185
🖼️ CANVAS SIZE: 300.0 x 300.0
✅ RESIZE COMPLETE - NEW CANVAS: 300.0 x 300.0
============================================================

🔧 FINAL CLIPPING AND VALIDATION:
   Before clipping: x_min=0.4699999999999997, y_min=18.19961111111111, x_max=0.6899999999999997, y_max=18.673685185185185
   🔄 Processing annotation 3/3: cat eye
      🎯 _TRANSFORM_SINGLE_ANNOTATION called
         📦 Annotation type: Annotation
         📦 Annotation full type: <class 'database.models.Annotation'>
         📦 Class: cat eye
         📦 Input bbox: x_min=2.4479999999999995, y_min=36.342333333333336, x_max=3.0239999999999996, y_max=37.29048148148148
         📐 Dimensions: (800, 600) → (300, 300)
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
   x_min: 2.4479999999999995, y_min: 36.342333333333336
   x_max: 3.0239999999999996, y_max: 37.29048148148148
   width: 0.5760000000000001, height: 0.9481481481481424
📐 DIMENSIONS:
   original_dims: (800, 600)
   new_dims: (300, 300)
🔧 TRANSFORMATION CONFIG:
   1. resize: {'enabled': True, 'width': 300, 'height': 300}
================================================================================
🔢 INITIAL VALUES:
   x_min: 2.4479999999999995, y_min: 36.342333333333336
   x_max: 3.0239999999999996, y_max: 37.29048148148148
   current_width: 800, current_height: 600

🔍 RESIZE TRANSFORMATION DEBUG
============================================================
📊 INPUT PARAMETERS:
   target_width: 300
   target_height: 300
   resize_mode: stretch_to
   current_width: 800
   current_height: 600
📍 ORIGINAL BBOX (before resize):
   x_min: 2.4479999999999995, y_min: 36.342333333333336
   x_max: 3.0239999999999996, y_max: 37.29048148148148
   width: 0.5760000000000001, height: 0.9481481481481424
🔢 FLOAT CONVERSIONS:
   source_w: 800.0, source_h: 600.0
   tw: 300.0, th: 300.0
🎯 STRETCH_TO MODE:
   sx = 300.0 / 800.0 = 0.375
   sy = 300.0 / 600.0 = 0.5
📍 BEFORE SCALING:
   x_min: 2.4479999999999995, x_max: 3.0239999999999996
   y_min: 36.342333333333336, y_max: 37.29048148148148
📍 AFTER SCALING:
   x_min: 0.9179999999999998, x_max: 1.134
   y_min: 18.171166666666668, y_max: 18.64524074074074
🖼️ CANVAS SIZE: 300.0 x 300.0
✅ RESIZE COMPLETE - NEW CANVAS: 300.0 x 300.0
============================================================

🔧 FINAL CLIPPING AND VALIDATION:
   Before clipping: x_min=0.9179999999999998, y_min=18.171166666666668, x_max=1.134, y_max=18.64524074074074
   Original: 3 → Transformed: 3
📦 TRANSFORMED ANNOTATIONS (3):
   1. cat: x_min=0.0, y_min=31.761766419753087, x_max=0.4175644444444433, y_max=36.155105679012344       
   2. cat eye: x_min=1.2533333333333325, y_min=36.39922222222222, x_max=1.8399999999999992, y_max=37.34737037037037
   3. cat eye: x_min=2.4479999999999995, y_min=36.342333333333336, x_max=3.0239999999999996, y_max=37.29048148148148
✅ NEW DETECTION FUNCTION RESULT: 3 lines

=== 🔍 TRANSFORMATIONS DEBUG :: car.jpg ===
transformations variable: [{'type': 'resize', 'params': {'width': 300, 'height': 300}}]
transformations type: <class 'list'>
transformations bool: True
🎯 RESIZE-ONLY DETECTED for car.jpg
🖼️ Original image dims: (800, 600)
🖼️ Resized image dims: (300, 300)

🔍 TRACKING FUNCTION INPUT:
   Transformations: [{'type': 'resize', 'params': {'width': 300, 'height': 300}}]
   Original dims: (800, 600)
   Final dims: (300, 300)
🎯 RESIZE CONFIG ALREADY EXISTS: {'enabled': True, 'width': 300, 'height': 300}

📍 ANNOTATION TRACKING ORDER: ['resize']
🔧 GEOMETRIC TRANSFORMS ORDER: ['resize']
🔍 TRANSFORMATION CONFIG DETAILS: {'resize': {'enabled': True, 'width': 300, 'height': 300}}

🎯 TRACKING FUNCTION OUTPUT:
   transformation_config: {'resize': {'enabled': True, 'width': 300, 'height': 300}}
   Has geometric transforms: True
   Geometric transforms: [{'type': 'resize', 'params': {'width': 300, 'height': 300}, 'index': 0}]       
🎯 RESIZE-ONLY: Using tracking system for annotations!
🎯 RELEASES.PY: Using NEW FUNCTIONS with internal transformation!
   📊 Tracking data: {'transformation_sequence': [{'index': 0, 'type': 'resize', 'params': {'width': 300, 'height': 300}, 'is_geometric': True, 'is_photometric': False}], 'transformation_config': {'resize': {'enabled': True, 'width': 300, 'height': 300}}, 'original_dims': (800, 600), 'final_dims': (300, 300), 'debug_transformation_order': {'annotation_config_order': ['resize'], 'geometric_transforms_order': ['resize'], 'orders_match': True, 'duplicate_resize_detected': False}, 'has_geometric_transforms': True, 'geometric_transforms': [{'type': 'resize', 'params': {'width': 300, 'height': 300}, 'index': 0}], 'photometric_transforms': [], 'total_transforms': 1, 'geometric_count': 1, 'photometric_count': 0}
🎯 NEW DETECTION FUNCTION CALLED!
   Annotations: 2
   Final dims: 300x300
   Has transform_config: True
   Original dims: (800, 600)
🔧 TRANSFORMING ANNOTATIONS: (800, 600) → 300x300
🔧 TRANSFORM CONFIG: {'resize': {'enabled': True, 'width': 300, 'height': 300}}
📦 ORIGINAL ANNOTATIONS (2):
   1. dog: x_min=0.0, y_min=34.57877777777778, x_max=4.207999999999999, y_max=43.87062962962963
   2. dog eye: x_min=2.714666666666666, y_min=37.992111111111114, x_max=3.226666666666666, y_max=38.67477777777778

🔄 UPDATE_ANNOTATIONS_FOR_TRANSFORMATIONS CALLED!
   📊 Input: 2 annotations
   📐 Dimensions: (800, 600) → (300, 300)
   🔧 Transform config: {'resize': {'enabled': True, 'width': 300, 'height': 300}}
   🎯 Has affine matrix: False
   🎯 RESIZE MODE: stretch_to
   📏 Target size: 300x300
   📏 Original size: 800.0x600.0
   📐 STRETCH_TO: final_canvas=300x300
   🎯 FINAL CANVAS DIMENSIONS: (300, 300)
   🔧 USING LEGACY/SEQUENTIAL TRANSFORMATION PATH
   📊 Processing 2 annotations individually
   🔄 Processing annotation 1/2: dog
      🎯 _TRANSFORM_SINGLE_ANNOTATION called
         📦 Annotation type: Annotation
         📦 Annotation full type: <class 'database.models.Annotation'>
         📦 Class: dog
         📦 Input bbox: x_min=0.0, y_min=34.57877777777778, x_max=4.207999999999999, y_max=43.87062962962963
         📐 Dimensions: (800, 600) → (300, 300)
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
   x_min: 0.0, y_min: 34.57877777777778
   x_max: 4.207999999999999, y_max: 43.87062962962963
   width: 4.207999999999999, height: 9.291851851851852
📐 DIMENSIONS:
   original_dims: (800, 600)
   new_dims: (300, 300)
🔧 TRANSFORMATION CONFIG:
   1. resize: {'enabled': True, 'width': 300, 'height': 300}
================================================================================
🔢 INITIAL VALUES:
   x_min: 0.0, y_min: 34.57877777777778
   x_max: 4.207999999999999, y_max: 43.87062962962963
   current_width: 800, current_height: 600

🔍 RESIZE TRANSFORMATION DEBUG
============================================================
📊 INPUT PARAMETERS:
   target_width: 300
   target_height: 300
   resize_mode: stretch_to
   current_width: 800
   current_height: 600
📍 ORIGINAL BBOX (before resize):
   x_min: 0.0, y_min: 34.57877777777778
   x_max: 4.207999999999999, y_max: 43.87062962962963
   width: 4.207999999999999, height: 9.291851851851852
🔢 FLOAT CONVERSIONS:
   source_w: 800.0, source_h: 600.0
   tw: 300.0, th: 300.0
🎯 STRETCH_TO MODE:
   sx = 300.0 / 800.0 = 0.375
   sy = 300.0 / 600.0 = 0.5
📍 BEFORE SCALING:
   x_min: 0.0, x_max: 4.207999999999999
   y_min: 34.57877777777778, y_max: 43.87062962962963
📍 AFTER SCALING:
   x_min: 0.0, x_max: 1.5779999999999998
   y_min: 17.28938888888889, y_max: 21.935314814814816
🖼️ CANVAS SIZE: 300.0 x 300.0
✅ RESIZE COMPLETE - NEW CANVAS: 300.0 x 300.0
============================================================

🔧 FINAL CLIPPING AND VALIDATION:
   Before clipping: x_min=0.0, y_min=17.28938888888889, x_max=1.5779999999999998, y_max=21.935314814814816
   🔄 Processing annotation 2/2: dog eye
      🎯 _TRANSFORM_SINGLE_ANNOTATION called
         📦 Annotation type: Annotation
         📦 Annotation full type: <class 'database.models.Annotation'>
         📦 Class: dog eye
         📦 Input bbox: x_min=2.714666666666666, y_min=37.992111111111114, x_max=3.226666666666666, y_max=38.67477777777778
         📐 Dimensions: (800, 600) → (300, 300)
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
   x_min: 2.714666666666666, y_min: 37.992111111111114
   x_max: 3.226666666666666, y_max: 38.67477777777778
   width: 0.512, height: 0.6826666666666625
📐 DIMENSIONS:
   original_dims: (800, 600)
   new_dims: (300, 300)
🔧 TRANSFORMATION CONFIG:
   1. resize: {'enabled': True, 'width': 300, 'height': 300}
================================================================================
🔢 INITIAL VALUES:
   x_min: 2.714666666666666, y_min: 37.992111111111114
   x_max: 3.226666666666666, y_max: 38.67477777777778
   current_width: 800, current_height: 600

🔍 RESIZE TRANSFORMATION DEBUG
============================================================
📊 INPUT PARAMETERS:
   target_width: 300
   target_height: 300
   resize_mode: stretch_to
   current_width: 800
   current_height: 600
📍 ORIGINAL BBOX (before resize):
   x_min: 2.714666666666666, y_min: 37.992111111111114
   x_max: 3.226666666666666, y_max: 38.67477777777778
   width: 0.512, height: 0.6826666666666625
🔢 FLOAT CONVERSIONS:
   source_w: 800.0, source_h: 600.0
   tw: 300.0, th: 300.0
🎯 STRETCH_TO MODE:
   sx = 300.0 / 800.0 = 0.375
   sy = 300.0 / 600.0 = 0.5
📍 BEFORE SCALING:
   x_min: 2.714666666666666, x_max: 3.226666666666666
   y_min: 37.992111111111114, y_max: 38.67477777777778
📍 AFTER SCALING:
   x_min: 1.0179999999999998, x_max: 1.2099999999999997
   y_min: 18.996055555555557, y_max: 19.33738888888889
🖼️ CANVAS SIZE: 300.0 x 300.0
✅ RESIZE COMPLETE - NEW CANVAS: 300.0 x 300.0
============================================================

🔧 FINAL CLIPPING AND VALIDATION:
   Before clipping: x_min=1.0179999999999998, y_min=18.996055555555557, x_max=1.2099999999999997, y_max=19.33738888888889
   Original: 2 → Transformed: 2
📦 TRANSFORMED ANNOTATIONS (2):
   1. dog: x_min=0.0, y_min=34.57877777777778, x_max=4.207999999999999, y_max=43.87062962962963
   2. dog eye: x_min=2.714666666666666, y_min=37.992111111111114, x_max=3.226666666666666, y_max=38.67477777777778
✅ NEW DETECTION FUNCTION RESULT: 2 lines

=== 🔍 TRANSFORMATIONS DEBUG :: dog.jpg ===
transformations variable: [{'type': 'resize', 'params': {'width': 300, 'height': 300}}]
transformations type: <class 'list'>
transformations bool: True
🎯 RESIZE-ONLY DETECTED for dog.jpg
🖼️ Original image dims: (800, 600)
🖼️ Resized image dims: (300, 300)

🔍 TRACKING FUNCTION INPUT:
   Transformations: [{'type': 'resize', 'params': {'width': 300, 'height': 300}}]
   Original dims: (800, 600)
   Final dims: (300, 300)
🎯 RESIZE CONFIG ALREADY EXISTS: {'enabled': True, 'width': 300, 'height': 300}

📍 ANNOTATION TRACKING ORDER: ['resize']
🔧 GEOMETRIC TRANSFORMS ORDER: ['resize']
🔍 TRANSFORMATION CONFIG DETAILS: {'resize': {'enabled': True, 'width': 300, 'height': 300}}

🎯 TRACKING FUNCTION OUTPUT:
   transformation_config: {'resize': {'enabled': True, 'width': 300, 'height': 300}}
   Has geometric transforms: True
   Geometric transforms: [{'type': 'resize', 'params': {'width': 300, 'height': 300}, 'index': 0}]       
🎯 RESIZE-ONLY: Using tracking system for annotations!
🎯 RELEASES.PY: Using NEW FUNCTIONS with internal transformation!
   📊 Tracking data: {'transformation_sequence': [{'index': 0, 'type': 'resize', 'params': {'width': 300, 'height': 300}, 'is_geometric': True, 'is_photometric': False}], 'transformation_config': {'resize': {'enabled': True, 'width': 300, 'height': 300}}, 'original_dims': (800, 600), 'final_dims': (300, 300), 'debug_transformation_order': {'annotation_config_order': ['resize'], 'geometric_transforms_order': ['resize'], 'orders_match': True, 'duplicate_resize_detected': False}, 'has_geometric_transforms': True, 'geometric_transforms': [{'type': 'resize', 'params': {'width': 300, 'height': 300}, 'index': 0}], 'photometric_transforms': [], 'total_transforms': 1, 'geometric_count': 1, 'photometric_count': 0}
🎯 NEW DETECTION FUNCTION CALLED!
   Annotations: 1
   Final dims: 300x300
   Has transform_config: True
   Original dims: (800, 600)
🔧 TRANSFORMING ANNOTATIONS: (800, 600) → 300x300
🔧 TRANSFORM CONFIG: {'resize': {'enabled': True, 'width': 300, 'height': 300}}
📦 ORIGINAL ANNOTATIONS (1):
   1. dog: x_min=0.0, y_min=31.737493827160495, x_max=0.16270222222222125, y_max=36.26837777777778       

🔄 UPDATE_ANNOTATIONS_FOR_TRANSFORMATIONS CALLED!
   📊 Input: 1 annotations
   📐 Dimensions: (800, 600) → (300, 300)
   🔧 Transform config: {'resize': {'enabled': True, 'width': 300, 'height': 300}}
   🎯 Has affine matrix: False
   🎯 RESIZE MODE: stretch_to
   📏 Target size: 300x300
   📏 Original size: 800.0x600.0
   📐 STRETCH_TO: final_canvas=300x300
   🎯 FINAL CANVAS DIMENSIONS: (300, 300)
   🔧 USING LEGACY/SEQUENTIAL TRANSFORMATION PATH
   📊 Processing 1 annotations individually
   🔄 Processing annotation 1/1: dog
      🎯 _TRANSFORM_SINGLE_ANNOTATION called
         📦 Annotation type: Annotation
         📦 Annotation full type: <class 'database.models.Annotation'>
         📦 Class: dog
         📦 Input bbox: x_min=0.0, y_min=31.737493827160495, x_max=0.16270222222222125, y_max=36.26837777777778
         📐 Dimensions: (800, 600) → (300, 300)
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
   x_min: 0.0, y_min: 31.737493827160495
   x_max: 0.16270222222222125, y_max: 36.26837777777778
   width: 0.16270222222222125, height: 4.530883950617284
📐 DIMENSIONS:
   original_dims: (800, 600)
   new_dims: (300, 300)
🔧 TRANSFORMATION CONFIG:
   1. resize: {'enabled': True, 'width': 300, 'height': 300}
================================================================================
🔢 INITIAL VALUES:
   x_min: 0.0, y_min: 31.737493827160495
   x_max: 0.16270222222222125, y_max: 36.26837777777778
   current_width: 800, current_height: 600

🔍 RESIZE TRANSFORMATION DEBUG
============================================================
📊 INPUT PARAMETERS:
   target_width: 300
   target_height: 300
   resize_mode: stretch_to
   current_width: 800
   current_height: 600
📍 ORIGINAL BBOX (before resize):
   x_min: 0.0, y_min: 31.737493827160495
   x_max: 0.16270222222222125, y_max: 36.26837777777778
   width: 0.16270222222222125, height: 4.530883950617284
🔢 FLOAT CONVERSIONS:
   source_w: 800.0, source_h: 600.0
   tw: 300.0, th: 300.0
🎯 STRETCH_TO MODE:
   sx = 300.0 / 800.0 = 0.375
   sy = 300.0 / 600.0 = 0.5
📍 BEFORE SCALING:
   x_min: 0.0, x_max: 0.16270222222222125
   y_min: 31.737493827160495, y_max: 36.26837777777778
📍 AFTER SCALING:
   x_min: 0.0, x_max: 0.06101333333333297
   y_min: 15.868746913580248, y_max: 18.13418888888889
🖼️ CANVAS SIZE: 300.0 x 300.0
✅ RESIZE COMPLETE - NEW CANVAS: 300.0 x 300.0
============================================================

🔧 FINAL CLIPPING AND VALIDATION:
   Before clipping: x_min=0.0, y_min=15.868746913580248, x_max=0.06101333333333297, y_max=18.13418888888889
   Original: 1 → Transformed: 1
📦 TRANSFORMED ANNOTATIONS (1):
   1. dog: x_min=0.0, y_min=31.737493827160495, x_max=0.16270222222222125, y_max=36.26837777777778       
✅ NEW DETECTION FUNCTION RESULT: 1 lines

=== 📋 WRITING ANNOTATIONS.JSON ===
Total images with annotations: 3
   images\train\cat.jpg: 3 annotations
      First annotation: {'class_id': 0, 'bbox': [0.000696, 0.113195, 0.001392, 0.014644]}
   images\val\car.jpg: 2 annotations
      First annotation: {'class_id': 2, 'bbox': [0.007013, 0.130749, 0.014027, 0.030973]}
   images\test\dog.jpg: 1 annotations
      First annotation: {'class_id': 2, 'bbox': [0.000271, 0.113343, 0.000542, 0.015103]}
INFO:     127.0.0.1:50160 - "POST /api/v1/releases/create HTTP/1.1" 200 OK
INFO:     127.0.0.1:61230 - "OPTIONS /api/transformation/available-transformations?_t=1758402380515 HTTP/1.1" 200 OK
INFO:     127.0.0.1:61230 - "OPTIONS /api/image-transformations/pending?_t=1758402380515 HTTP/1.1" 200 OK
INFO:     127.0.0.1:61230 - "OPTIONS /api/transformation/available-transformations?_t=1758402380515 HTTP/1.1" 200 OK
INFO:     127.0.0.1:61230 - "OPTIONS /api/image-transformations/pending?_t=1758402380515 HTTP/1.1" 200 OK
INFO:     127.0.0.1:58470 - "POST /api/v1/logs/frontend/batch HTTP/1.1" 200 OK
INFO:     127.0.0.1:64783 - "POST /api/v1/logs/frontend/batch HTTP/1.1" 200 OK
INFO:     127.0.0.1:50160 - "GET /api/v1/projects/1/releases HTTP/1.1" 200 OK
INFO:     127.0.0.1:61230 - "GET /api/transformation/available-transformations?_t=1758402380515 HTTP/1.1"
 200 OK
INFO:     127.0.0.1:58470 - "POST /api/v1/logs/frontend/batch HTTP/1.1" 200 OK
INFO:     127.0.0.1:64783 - "POST /api/v1/logs/frontend/batch HTTP/1.1" 200 OK
INFO:     127.0.0.1:61230 - "GET /api/transformation/available-transformations?_t=1758402380515 HTTP/1.1"
 200 OK
INFO:     127.0.0.1:50160 - "GET /api/image-transformations/pending?_t=1758402380515 HTTP/1.1" 200 OK    
INFO:     127.0.0.1:61230 - "POST /api/v1/logs/frontend/batch HTTP/1.1" 200 OK
INFO:     127.0.0.1:58470 - "GET /api/image-transformations/pending?_t=1758402380515 HTTP/1.1" 200 OK
🔍 DEBUG: Database path being used: V:\stage-1-labeling-app\app-3-fix-release-system-422-error\database.db
🔍 DEBUG: Database exists: True
🔍 DEBUG: SQL query returned 2 projects
INFO:     127.0.0.1:58470 - "GET /api/image-transformations/release-config/version_auto