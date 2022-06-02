import os

# 1. download -- anime-face_hrnetv2.onnx \ anime-face_yolov3.onnx \anime-face_faster-rcnn.onnx
# download_url = https://storage.googleapis.com/ailia-models/anime-face-detector/anime-face_hrnetv2.onnx
os.system("")

# 2. onnx --> onnxsim
os.system("python -m onnxsim anime-face_hrnetv2.onnx sim.onnx --input-shape 1,3,256,256")

# 3. onnx --> ncnn
os.system("onnx2ncnn sim.onnx ncnn.param ncnn.bin")

# 4. ncnn --> optmize ---> ncnn
os.system("ncnnoptimize ncnn.param ncnn.bin opt.param opt.bin 1")  # 数字0 代表fp32 ；1代表fp16
