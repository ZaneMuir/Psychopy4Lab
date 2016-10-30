# Spike Station

目前主要用于整理分析spike数据与运动和视觉速度之间关系。
## 主要处理：
1. 统计一定时间间隔内spike的数目以及对应的visual flow和motor speed。
2. 运用 random forest 的方法寻找spike与速度间的关系，并用PP值与theta角来评估(abs(PP)>0.16为阈值)



对程序代码的结构做了优化，将部分内容做了对象化。

## Requirement
### Python module
* python 2.7
* matplotlib
* numpy
* scipy
* sklearn

### File Directory Structure (example)
* 20160922-no.25-s1
	* PSTH Ch1.txt
	* PSTH Ch2.txt
	* ...
* No.25\_16.09.22\_PathData\_S1.csv
* No.25\_160922\_psychopy\_S1-4.csv
* No.25\_Corridor-16.09.22\_S1.csv
* Change\_pmm\_selfDesign\_Control\_playback.py

## 使用
1. 进入储存数据的目录
2. 运行 process.py 即可。
3. 结果可在 summary 文档中看到。
