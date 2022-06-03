##  <p align="center"> NCNN Models </p>

The collection of pre-trained AI models, and how they were converted, deployed. [中文](README-CN.md)

![](docs/images/logo.png)

### About

The ncnn framework enables cross-device deployment with the help of the vulkan api. We pre-train models via pytorch, tensorflow, paddle etc. and then convert them to ncnn models for final deployment on Windows, mac, linux, android, ios, WebAssembly and uni-app. However, model conversion is not a one-click process and needs to be handled manually. In order to extend the boundary applications of ncnn, we have created this repository to receive any cases of successful or failed conversions.

### How to contribute

[Contribute tutorial](contribute.md)

	✅ : good to work
    ❌ : bad to work
    ⭕ : good to work, but not good to contribute
    🤔 : not sure, but good to contribute
    🔥🔥💥
### Failure Notes

> We believe we will succeed in the end. 跪求各位大佬修正失败案例，个人失败太多快要自闭了😂。

| Model                                             | Year | Size  | From    | Type                 | Convert | IsWork | Heat |
| :------------------------------------------------ | :--- | :---- | :------ | :------------------- | :------ | :----- | :--- |
| [MAT](image_inpainting/mat)                       | 2022 |       | Pytorch | image_inpainting     | ❌       |        | 💥    |
| [RVM](image_matting/RVM)                          | 2021 | 13.6M | Pytorch | image_matting        | ❌       | ✅      | 💥    |
| [vitea](image_matting/vitea)                      | 2022 | 52.9M | Pytorch | image_matting        | ❌       |        |      |
| [AnimeGanV3](style_transfer/animeganv3)           | 2022 |       | Onnx    | style_transfer       | ❌       |        | 🔥    |
| [HybridNets](object_dection/hybridnets)           | 2022 |       | Pytorch | object_dection       | ❌       |        |      |
| [yolop](object_dection/yolop)                     | 2021 |       | Pytorch | object_dection       | ❌       | 🤔      | 💥    |
| [pfld](face_dection/pfld)                         | 2019 | 4.9M  | Pytorch | face_dection         | ❌       | ✅      |      |
| [Anime](face_dection/Anime_Face)                  | 2021 | 18.8M | Onnx    | face_dection         | ✅       | ⭕      |      |
| [CaiT](image_classification/cait)                 | 2021 | 34.3M | Pytorch | image_classification | ✅       | ❌      |      |
| [yolov5](object_dection/yolov5)                   | 2021 | 14.1M | Pytorch | object_dection       | ⭕       | ✅      | 💥    |
| [yolo-fastestv2](object_dection/yolo-fastestv2)   | 2021 | 0.4M  | Pytorch | object_dection       | ✅       | ✅      | 💥    |
| [yolox](object_dection/yolox)                     | 2021 | 1.7M  | Pytorch | object_dection       | ✅       | ✅      | 💥    |
| [nanodet](object_dection/nanodet)                 | 2020 | 2.3M  | Onnx    | object_dection       | ✅       | ✅      | 🔥    |
| [DenseNet](image_classification/denseNet)         | 2018 | 21.5M | Pytorch | image_classification | ✅       | ✅      |      |
| [resnet18](image_classification/resnet18)         | 2015 | 22.8M | Pytorch | image_classification | ✅       | ✅      |      |
| [mobilenet_v2](image_classification/mobilenet_v2) | 2019 | 6.8M  | Pytorch | image_classification | ✅       | ✅      | 🔥    |
| [mobilenet_v3](image_classification/mobilenet_v3) | 2019 | 10.7M | Pytorch | image_classification | ✅       | ✅      | 🔥    |
| [Res2Net](image_classification/res2net)           | 2021 | 88.2M | Pytorch | image_classification | ✅       | ✅      |      |
| [Res2Next50](image_classification/res2next50)     | 2021 | 48.1M | Pytorch | image_classification | ✅       | ✅      |      |
| [shufflenetv2](image_classification/shufflenetv2) | 2018 | 4.4M  | Onnx    | image_classification | ✅       | ✅      |      |
| [vgg16](image_classification/vgg16)               | 2015 | 263M  | Pytorch | image_classification | ✅       | ✅      |      |
| [efficientnet](image_classification/efficientnet) | 2021 | 10.3M | Pytorch | image_classification | ✅       | ✅      | 🔥    |
| [deeplabv3](image_matting/deeplabv3)              | 2017 | 21.5M | Pytorch | image_matting        | ✅       | ✅      |      |
| [deoldify](image_inpainting/deoldify)             | 2019 | 242M  | Onnx    | image_inpainting     | 🤔       | ✅      | 🔥    |
| [UltraFace](face_dection/ultraface)               | 2019 | 0.6M  | Pytorch | face_dection         | ✅       | ✅      | 🔥    |
| [Anime2Real](style_transfer/anime2real)           | 2022 | 22.2M | Pytorch | style_transfer       | ✅       | ✅      |      |
| [AnimeGanV2](style_transfer/animeganv2)           | 2020 | 4.2M  | Pytorch | style_transfer       | ✅       | ✅      | 💥    |
| [styletransfer](style_transfer/styletransfer)     | 2016 | 3.2M  | Onnx    | style_transfer       | ✅       | ✅      |      |




### Action recognition

> need to be contribute

### Frame Interpolation

### Super resolution

### Text recognition

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Baiyuetribe/ncnn-models&type=Date)](https://star-history.com/#Baiyuetribe/ncnn-models&Date)
