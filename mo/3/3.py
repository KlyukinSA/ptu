from PIL import Image, ImageDraw
import numpy as np
from sklearn.cluster import KMeans

i = [4, 8, 16, 32]
for num_clusters in i:
    img = Image.open(r'task3image.jpeg')
    matrix = np.asarray(img)
    draw = ImageDraw.Draw(img)
    width = img.size[0]
    height = img.size[1]
    arr = [elem for el in matrix for elem in el]
    print(len(arr))

    model = KMeans(n_clusters=num_clusters)
    model.fit(arr)
    centers = model.cluster_centers_
    
    for i in range(num_clusters):
        for j in range(3):
            centers[i, j] = int(centers[i, j])
    
    dataset = np.insert(arr, 3, model.predict(arr), 1)

    for y in range(height):
        for x in range(width):
            draw.point((x, y), (
                    int(centers[dataset[y * width + x, 3]][0]),
                    int(centers[dataset[y * width + x, 3]][1]),
                    int(centers[dataset[y * width + x, 3]][2])
                )
            )

    img.save('task3result.jpeg', "JPEG")
    print()
