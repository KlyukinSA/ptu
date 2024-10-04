diff --git a/py3d/examples/example-6-5-shadows.py b/py3d/examples/example-6-5-shadows.py
index db9424e..ede7b4e 100644
--- a/py3d/examples/example-6-5-shadows.py
+++ b/py3d/examples/example-6-5-shadows.py
@@ -3,6 +3,8 @@ import math
 import pathlib
 import sys
 
+from py3d.geometry.cone import ConeGeometry
+
 # Get the package directory
 package_dir = str(pathlib.Path(__file__).resolve().parents[2])
 # Add the package directory into sys.path if necessary
@@ -23,6 +25,7 @@ from py3d.geometry.rectangle import RectangleGeometry
 from py3d.geometry.sphere import SphereGeometry
 from py3d.extras.movement_rig import MovementRig
 from py3d.extras.directional_light import DirectionalLightHelper
+from py3d.geometry.parametric import ParametricGeometry
 
 
 class Example(Base):
@@ -46,8 +49,6 @@ class Example(Base):
         # the global matrix of its child.
         self.directional_light.set_position([2, 4, 0])
         self.scene.add(self.directional_light)
-        direct_helper = DirectionalLightHelper(self.directional_light)
-        self.directional_light.add(direct_helper)
 
         sphere_geometry = SphereGeometry()
         phong_material = PhongMaterial(
@@ -56,14 +57,26 @@ class Example(Base):
             use_shadow=True
         )
 
-        sphere1 = Mesh(sphere_geometry, phong_material)
-        sphere1.set_position([-2, 1, 0])
+        c = 0.8
+        a = 0.5
+        sz = 2*3.14
+        cnt = 20
+        torus_geometry = ParametricGeometry(0, sz, cnt, 0, sz, cnt,
+            lambda u, v: [(c + a*math.cos(v)) * math.cos(u), (c + a * math.cos(v)) * math.sin(u), a * math.sin(v)])
+
+        sphere1 = Mesh(torus_geometry, phong_material)
+        sphere1.set_position([-2, 2, 0])
         self.scene.add(sphere1)
 
         sphere2 = Mesh(sphere_geometry, phong_material)
         sphere2.set_position([1, 2.2, -0.5])
         self.scene.add(sphere2)
 
+        cone_geometry = ConeGeometry(1, 2)
+        cone = Mesh(cone_geometry, phong_material)
+        cone.set_position([3, 2.2, -0.5])
+        self.scene.add(cone)
+
         self.renderer.enable_shadows(self.directional_light)
 
         """
