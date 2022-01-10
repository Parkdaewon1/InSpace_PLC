# InSpace_PLC_Server 연결방법

## 1. TCPPORT-30M 설정방법

출처 http://comfilewiki.co.kr/ko/doku.php?id=tcpport:%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EB%A7%9D_%EA%B5%AC%EC%84%B1%EA%B3%BC_ip%EC%84%A4%EC%A0%95:index

### IP 설정
  > TCPPORT-30M은 딥스위치로 간단히 IP를 설정가능. TCPPORT-30M의 IP는 192.168.2xx 으로 고정되어 있고 사용자는 IP주소의 네번째 자리를 200~215번까지 딥스위치로 설정. 4개의 딥스위치는 각각 8,4,2,1값(2진수)으로 구성. 만약 IP를 192.168.0.200로 만든 다면 전부 OFF

![image](https://user-images.githubusercontent.com/38932208/148735067-9abbaa7b-d3ab-4776-83f7-b2e2381b14e8.png)

  * GATE WAY: 192.168.0.1, SUBNET MASK: 255.255.255.0, PORT: 502 으로 고정이며 사용자가 변경 불가 >

### IP 설정
