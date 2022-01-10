# InSpace_PLC_Station 설정

## 1. TCPPORT-30M 초기 설정방법

### 1) Board IP 설정
TCPPORT-30M은 딥스위치로 간단히 IP를 설정가능. TCPPORT-30M의 IP는 192.168.2xx 으로 고정되어 있고 사용자는 IP주소의 네번째 자리를 200~215번까지 딥스위치로 설정. 4개의 딥스위치는 각각 8,4,2,1값(2진수)으로 구성. 만약 IP를 192.168.0.207로 만든 다면 8 OFF & 1,2,4 

![image](https://user-images.githubusercontent.com/38932208/148735067-9abbaa7b-d3ab-4776-83f7-b2e2381b14e8.png)

* GATE WAY: 192.168.0.1, SUBNET MASK: 255.255.255.0, PORT: 502 으로 고정이며 사용자가 변경 불가

### 2) 컴퓨터 IP 설정
인터넷 프로토콜 버젼 4(TCP/IPv4)속성을 아래 그림과 같이 수정. 여기서 IP주소는 192.168.0.2~199값 임의로 사용

![image](https://user-images.githubusercontent.com/38932208/148735886-023cb09a-637b-4a8e-ab8e-a41ff0e09b72.png)
###### 내용출처 http://comfilewiki.co.kr/ko/doku.php?id=tcpport:%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EB%A7%9D_%EA%B5%AC%EC%84%B1%EA%B3%BC_ip%EC%84%A4%EC%A0%95:index
  
## 2. Python Module
pymodbus, requests, json 모듈 각각 pip을 이용하여 설치
```
pip install pymodbus
pip install requests
pip install json
```

## 3. exe 파일 변환
pyinstaller를 이용하여 파일변환 가능. 역시 pip을 이용하여 설치
```
pip install pyinstaller
```
* 명령어
```
pyinstaller 파일이름.py
pyinstaller --onfile 파일이름.py
```

## 4. 사용하는 코드 설명
### Modbus
본 코드에서 PLC보드와 컴퓨터간의 연결에는 크게 연결, Input 데이터 읽기, Output 데이터 쓰기 사용. pwm은 사용하지 않기 때문에 register 사용 x
* 연결
```python
c = ModbusTcpClient(PLC_IP, port=502)
c.connect()
c.close()
```
* Input 데이터 읽기 (0~15까지. write불가)
```python
c.read_coils(0,8).bits[0] # (Input address, The number of coils to read)
```
* Output 데이터 쓰기 (16~23까지. read불가)
```python
c.write_coil(16,True) # (Output address, value)
```

### REST API
본 코드에서 주로 사용하는 기능은 get(값 받아오기), patch(값 갱신하기)
* Get
```python
requests.get(Web_IP+Station_id).json() # (address).json 형태
ServerResponse["command"] # [불러올 변수명]
```
* Patch
```python
requests.patch(Web_IP+Station_id, json = {'runningStatus':'CONTROL_STATUS_CLOSE'}) #(address, 바꿀부분)
```

## 5. Trouble Shooting
### 연결거부 문제
> server computer에서 연결을 거부하였거나 PLC 보드의 연결이 불확실한 경우. 대부분 후자의 경우로 이더넷 설정을 검토하면 해결. 전자의 경우 연결을 허용하여 주면 해결
### 윈도우 pip 설치
> https://blog.naver.com/larysa/222499026621 참고
### python 경로 설정
> https://blog.naver.com/hwangsh20/222507848257 
> * 추가로 python을 설치할 때 설정해 주어도 됨.
> ![image](https://user-images.githubusercontent.com/38932208/148741673-c72bbe71-a16a-42c1-a221-cbb7b606d951.png)
#### 진행에 따라 추가예정
