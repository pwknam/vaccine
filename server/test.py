from deepface import DeepFace

# result = DeepFace.verify(img1_path = "live.jpeg", img2_path = "ocr_image.jpeg")
# dfs = DeepFace.find(img_path = "ocr_image.jpg", db_path = "C://storage")
objs = DeepFace.analyze(img_path = "./storage/ocr_image.jpeg", 
        actions = ['age', 'gender', 'race', 'emotion']
)

print(objs)