# FIFA_player_recommendation
2019.05 ~ 2019.06

-> 세부적인 프로젝트 내용은 'FIFA19 Progect_presentation.pdf' 참고


# FIFA 선수 추천 시스템


## 데이터 출처
FIFA19 게임 선수 데이터(Kaggle 수집)

## 프로젝트 분석 목적
- 동기: 게임 사업의 지속적인 수익을 내기 위해서는 새로운 유저들의 유입이 필수적이다. 새로운 유저들의 유입이 어려운 원인 중 하나로 진입장벽이 있음.
- 목적: 새로운 유저들을 위해 포지션별 선수들의 대략적인 능력치 인사이트를 제공해주자. 개인별로 선호하는 능력치를 고려해 적절한 선수를 추천해주는 프로그램을 작성해보자.

## 결과물
- 데이터 전처리를 통해 세부적으로 나뉘어져 있는 변수들의 범주를 알기 쉽게 압축하여 분류(선수의 세부적인 능력치들을 알기 쉽게 상위 카테고리로 합침)
- -> (포지션 변수(범주 27개) → 4가지 분류, 능력치 변수(범주 30개) → 6가지 분류)
- 다양한 시각화를 통해 능력치별, 포지션별로 발견할 수 있는 인사이트를 핵심적으로 요약
- 개인의 선수 능력치 선호도를 반영하여 선수를 추천해주는 프로그램 알고리즘 작성

**
**개인별 선수 추천 프로그램 작성
- 포지션 선택지를 입력하면 포지션별 일반적인 능력치 가이드라인 제시
- 사용자의 선호 능력치를 고려해 가중치 점수를 매겨 적절한 선수 추천
