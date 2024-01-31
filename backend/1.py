from ultralytics import YOLO

# 加载模型
model = YOLO('yolov8n.yaml')  # 从YAML构建新模型
model = YOLO('yolov8n.pt')    # 加载预训练模型（推荐用于训练）
model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # 从YAML构建并转移权重

# 训练模型
results = model.train(data='coco128.yaml', epochs=100, imgsz=640)



from ultralytics import YOLO

# 加载模型
model = YOLO('yolov8n.pt')  # 预训练的 YOLOv8n 模型

# 在图片列表上运行批量推理
results = model(['im1.jpg', 'im2.jpg'])  # 返回 Results 对象列表

# 处理结果列表
for result in results:
    boxes = result.boxes  # 边界框输出的 Boxes 对象
    masks = result.masks  # 分割掩码输出的 Masks 对象
    keypoints = result.keypoints  # 姿态输出的 Keypoints 对象
    probs = result.probs  # 分类输出的 Probs 对象





from ultralytics import YOLO

# 加载预训练的 YOLOv8n 模型
model = YOLO('yolov8n.pt')

# 定义视频文件路径
source = 'path/to/video.mp4'

# 对来源进行推理
results = model(source, stream=True)  # Results 对象的生成器



from ultralytics import YOLO

# 加载预训练的 YOLOv8n 模型
model = YOLO('yolov8n.pt')

# 定义包含图像和视频文件用于推理的目录路径
source = 'path/to/dir'

# 对来源进行推理
results = model(source, stream=True)  # Results 对象的生成器



from ultralytics import YOLO

# 加载一个模型
model = YOLO('yolov8n.yaml')  # 从YAML建立一个新模型
model = YOLO('yolov8n.pt')  # 加载预训练模型（推荐用于训练）
model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # 从YAML建立并转移权重

# 训练模型
results = model.train(data='coco128.yaml', epochs=100, imgsz=640)



from ultralytics import YOLO

# 加载模型
model = YOLO('yolov8n.pt')  # 加载预训练模型（推荐用于训练）

# 使用2个GPU训练模型
results = model.train(data='coco128.yaml', epochs=100, imgsz=640, device=[0, 1])



from ultralytics import YOLO

# 加载模型
model = YOLO('yolov8n.pt')  # 加载预训练模型（推荐用于训练）

# 使用2个GPU训练模型
results = model.train(data='coco128.yaml', epochs=100, imgsz=640, device='mps')