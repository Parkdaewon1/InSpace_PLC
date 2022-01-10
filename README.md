# InSpace_PLC_Server 설정 및 코드정리

## 1. TCPPORT-30M 초기 설정방법

###### 출처 http://comfilewiki.co.kr/ko/doku.php?id=tcpport:%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EB%A7%9D_%EA%B5%AC%EC%84%B1%EA%B3%BC_ip%EC%84%A4%EC%A0%95:index

### 1) Board IP 설정
  TCPPORT-30M은 딥스위치로 간단히 IP를 설정가능. TCPPORT-30M의 IP는 192.168.2xx 으로 고정되어 있고 사용자는 IP주소의 네번째 자리를 200~215번까지 딥스위치로 설정. 4개의 딥스위치는 각각 8,4,2,1값(2진수)으로 구성. 만약 IP를 192.168.0.200로 만든 다면 전부 OFF
![image](https://user-images.githubusercontent.com/38932208/148735067-9abbaa7b-d3ab-4776-83f7-b2e2381b14e8.png)
  * GATE WAY: 192.168.0.1, SUBNET MASK: 255.255.255.0, PORT: 502 으로 고정이며 사용자가 변경 불가

### 2) 컴퓨터 IP 설정
  인터넷 프로토콜 버젼 4(TCP/IPv4)속성을 아래 그림과 같이 수정. 여기서 IP주소는 192.168.0.2~199값 임의로 사용
![image](https://user-images.githubusercontent.com/38932208/148735886-023cb09a-637b-4a8e-ab8e-a41ff0e09b72.png)
  
## 2. Python Module
```python
from pymodbus.client.sync import ModbusTcpClient
import requests
import json
```
  pymodbus, requests, json 모듈 각각 pip을 이용하여 설치
```
pip install pymodbus
pip install requests
pip install json
```

## 3. exe 파일 변환
```
pip install pyinstaller
```
  pyinstaller를 이용하여 파일변환 가능.
```
pyinstaller 파일이름.py
pyinstaller --onfile 파일이름.py # 하나의 파일로 변환해줌()
```
