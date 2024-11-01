diff var30/emitter.py var20/emitter.py
9d8
< ATTRACTOR_POSITION = [5, 2, 7]
11d9
< center = (0, 0, 0)
23,24c21,26
<         x, y, z = self.position
<         coef = 0.03
---
>         z = np.random.uniform(0, self.cone_height)
>         heigth = (self.cone_height - z)
>         tan = self.cone_radius / self.cone_height
>         x = heigth * (tan) * np.random.uniform(-1, 1)
>         y = heigth * (tan) * np.random.uniform(-1, 1)
>         coef = 0.01
31d32
<         # velocity += np.array(ATTRACTOR_POSITION) * 0.001
44,51c45
< 
<         glPushMatrix()
<         glPointSize(10)
<         glBegin(GL_POINTS)
<         glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, PLATE_COLOR)
<         glVertex3f(*self.position)
<         glEnd()
<         glPopMatrix()
---
>         glutSolidCone(self.cone_radius, self.cone_height, sides, sides)
diff var30/particle.py var20/particle.py
24c24
<         self.color = PARTICLE_COLOR.copy()
---
>         self.color = [0.5, 0.8, 0.8, 1.0]
35,45c35,39
<         x_norm = x_dist / abs(x_dist)
<         y_norm = y_dist / abs(y_dist)
<         z_norm = z_dist / abs(z_dist)
<         move_vector = np.array([0, 0, 0])
<         if (self.color[3] > 0.1):
<             self.color[3] = self.getDistance(self.velocity, [0,0,0]) * 50
< 
<         # lifetime acceleration
<         self.velocity -= self.velocity / 200# [0.999]*3# [0.00002]*3
<         
<         # логика аттрактора
---
>         x_vec = x_dist / abs(x_dist)
>         y_vec = y_dist / abs(y_dist)
>         z_vex = z_dist / abs(z_dist)
>         move_vector = [0, 0, 0]
>         # считаем расстояние до аттрактора
46a41,49
>         if (self.color[0] < 1):
>             self.color[0] += 1 / (self.life_time)
>         else:
>             if (self.color[1] > 0.5):
>                 self.color[1] -= 1 / (self.life_time)
>             else:
>                 if (self.color[2] > 0.4):
>                     self.color[2] -= 1 / (self.life_time)
>         # логика аттрактора
48,53c51,67
<             self.color[0]=1
<             self.color[1]=0
<             v = np.array([x_norm, y_norm, z_norm])
<             v *= -0.0001
<             self.velocity += v
<             move_vector = self.velocity
---
>             # увеличиваем скорость приближения к аттрактору
>             self.velocity[0] += (x_dist) / 500
>             self.velocity[1] += (y_dist) / 500
>             self.velocity[2] += (z_dist) / 500
>             # определяем положение относительно ускорения
>             if (abs(x_dist) < abs(self.velocity[0])):
>                 move_vector[0] = x_dist
>             else:
>                 move_vector[0] = self.velocity[0]
>             if (abs(y_dist) < abs(self.velocity[1])):
>                 move_vector[1] = y_dist
>             else:
>                 move_vector[1] = self.velocity[1]
>             if (abs(z_dist) < abs(self.velocity[2])):
>                 move_vector[2] = z_dist
>             else:
>                 move_vector[2] = self.velocity[2]
55,56d68
<             self.color[0]=0
<             self.color[1]=1
