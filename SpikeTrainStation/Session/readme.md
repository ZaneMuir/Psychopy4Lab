#module Session
目前主要用于提取运动速度与视觉速度，并储存于./s1/speed.csv, ./s2/speed.csv, ... 

输出格式为：
时间，视觉速度，运动速度

## 使用
修改testSetting.py中的参数(主要为fartlek\_seq)
于工作目录运行SessionInfo.py即可

## 各文档用途
* Cleaner.clean() --> int
	通过检查Corridor文档来判断当天所跑的session数目，检查并新建各个输出的目录，并返回session数
* getCorridorSpeed.getCorridorSpeed(file\_path,VR\_ttl=0,time\_limit=(0,300,1)) --> float
	通过输入时刻并读取testSetting.py中的参数计算并返回对应的视觉速度
* 
