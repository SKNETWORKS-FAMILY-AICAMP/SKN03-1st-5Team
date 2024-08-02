# SKN03-1st-5Team
## 🚗 전국 자동차 등록 현황 및 기업 FAQ 조회 시스템

전국의 자동차 등록 현황을 조회하고, 기업 FAQ를 제공하는 시스템입니다.

## 📑 목차

- [📋 프로젝트 소개](#프로젝트-소개)
- [👥 팀원 소개](#팀원-소개)
- [⭐ 가이드](#사용-방법)
- [ ⚙️ 데이터 수집](#데이터1)
- [🚀 데이터 정리](#데이터2)
- [📜 실패요인](#실패요인)
- [📧 문의](#문의)

## 📋 프로젝트 소개

이 프로젝트는 전국 자동차 등록 현황 데이터를 시각화하고, 기업 관련 FAQ를 조회할 수 있는 웹 애플리케이션입니다.

## 👥 팀원 소개

- **팀장:** 박지용 (프로젝트 관리) - [GitHub](https://github.com/J-push)
- **팀원 1:** 박규택 (crawlikng)
- **팀원 2:** 방효식 (crawling)
- **팀원 3:** 송명신 (streamling)
- **팀원 4:** 이준석 (crawling)
- **팀원 5:** 허지원 (crawling)

## ⭐ 가이드

- 홈 화면에서는 '전국 자동차 등록 현황 데이터' 페이지와 '기업 FAQ' 페이지로 연결되는 링크가 제공된다.<br> '전국 자동차 등록 현황 데이터'페이지에서는 지역별 자동차 보유 현황을 자가용과 공업용으로 나뉜 탭을 통해 별도로 확인할 수 있으며, 추가로 '종합 현황' 탭을 통해 자가용, 공업용, 그리고 전체 보유 현황을 한꺼번에 확인할 수 있다. 
![main](/images/main.png)
![car](/images/car1.png)
![car](/images/car2.png)
![car](/images/car3.png)

## ⚙️ 데이터 수집
- **전국 자동차 현황**
  - [국토교통 통계누리_자동차 등록 현황](https://stat.molit.go.kr/portal/cate/statView.do?hRsId=58&hFormId=5498&hSelectId=5409&hPoint=&hAppr=1&hDivEng=&oFileName=&rFileName=&midpath=&sFormId=5498&sStart=202401&sEnd=202401&sStyleNum=2&settingRadio=xlsx "국토통계")
   ![alt text](/images/image.png)
  - text 형태로 제공된 자료 다운
    - csv로 다운 받으면, ','를 seperator로 사용하는데, 자료에 숫자가 1000 단위를 넘어 가면 ','로 자리수를 보여 주어, seperator로 작동 되는 문제가 있었음.

  - [전국 공영 주차장 자료](https://www.bigdata-culture.kr/bigdata/user/data_market/detail.do?id=6365bfc0-2531-41b6-bd6e-2e42de49dd6b "문화빅데이터플랫폼")
  - CRV로 형태로 제공된 자료 다운 
  - **주차장 이름, 시군구, 주차 공간** 데이터만 데이터베이스에 올리고 전국 자동차 등록 현황의 시군구 별 자동차 개수와 비교하여 공영 주차장의 증축 필요성을 알아보려려함
  - *데이터를 넣는 과정에서 시군구별 주차장 개수를 추출하는데 어려움을 느낌*
        
- **기업 FAQ**
  - [기아 자동차 FAQ 홈페이지](https://www.kia.com/kr/customer-service/center/faq "기아자동차 FAQ")
  - 기아 자동차 FAQ 홈페이지로 selenium을 이용해 웹크롤링을 진행함

  - [현대 자동차 FAQ 홈페이지](https://www.hyundai.com/kr/ko/e/customer/center/faq "현대자동차 FAQ")
  - 현대 자동차 FAQ 홈페이지로 웹크롤링을 진행하려 했으나 실패


## 🚀 데이터 정리 및 업로드
 - ERD
    ![erd](/images/erd.png)
- **전국 자동차 현황**
    - **승용 : 1, 승합 : 2, 화물 : 3 , 특수 : 4, 관용1, 자가용1, 영업용1, 계1** 등으로 작성하여 중복을 피하여 컬럼 정리
     ![alt text](/images/image-1.png)
    - MySQL
     ![alt text](/images/image-2.png)
- **기업 FAQ**
  - 웹크롤링을 통해 질문과 답변을 추출하였고 데이터 프레임형식으로 질문, 답변, 벤더(기아)로 테이블을 생성
  - MySQL
   ![alt text](/images/image_kia.png)
 


## 📜 실패요인

![alt text](/images/image-8.png)
![alt text](/images/image-9.png)
- 현대 자료를 crawling하는 인원의 컴퓨터에서 도출과 오류가 섞여서 발생 하며 코드가 지속적으로 실행이 안되는 문제가 발생



## 📧 문의

문의 사항이 있으시면 아래 연락처 참고바람:

- 박지용: a85429462@gmail.com
- GitHub: [J-push](https://github.com/J-push)
