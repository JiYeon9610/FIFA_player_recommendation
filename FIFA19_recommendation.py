import operator
import pandas as pd
OF=pd.read_csv("OF_set.csv")
DF=pd.read_csv("DF_set.csv")
MF=pd.read_csv("MF_set.csv")
GK=pd.read_csv("GK_set.csv")

def sort_OF(pos):
    #Pace DribblingA Shooting Defending Passing Physicality
    #Pace > DribblingA > Physicality > Shooting > Passing > Defending
    pos_sort=sorted(pos.items(), key=operator.itemgetter(1))
    pos_OF=OF.sort_values(by=[pos_sort[0][0],pos_sort[1][0],pos_sort[2][0],
                              pos_sort[3][0],pos_sort[4][0],pos_sort[5][0]],
                          axis=0, ascending=False)
    OF_final=pos_OF[0:10]
    return OF_final

def sort_DF(pos):
    #Pace DribblingA Shooting Defending Passing Physicality
    #Physicality > Pace > Defending > DribblingA > Passing > Shooting
    pos_sort=sorted(pos.items(), key=operator.itemgetter(1))
    pos_DF=DF.sort_values(by=[pos_sort[0][0],pos_sort[1][0],pos_sort[2][0],
                              pos_sort[3][0],pos_sort[4][0],pos_sort[5][0]],
                          axis=0, ascending=False)
    DF_final=pos_DF[0:10]
    return DF_final

def sort_MF(pos):
    #Pace DribblingA Shooting Defending Passing Physicality
    #Pace > DribblingA > Physicality > Passing > Shooting > Defending
    pos_sort=sorted(pos.items(), key=operator.itemgetter(1))
    pos_MF=MF.sort_values(by=[pos_sort[0][0],pos_sort[1][0],pos_sort[2][0],
                              pos_sort[3][0],pos_sort[4][0],pos_sort[5][0]],
                          axis=0, ascending=False)
    MF_final=pos_MF[0:10]
    return MF_final

def sort_GK(pos):
    #GKDiving GKHandling GKKicking GKPositioning GKReflexes
    pos_sort=sorted(pos.items(), key=operator.itemgetter(1))
    pos_GK=GK.sort_values(by=[pos_sort[0][0], pos_sort[1][0], pos_sort[2][0],
                              pos_sort[3][0], pos_sort[4][0]],
                          axis=0, ascending=False)
    GK_final=pos_GK[0:10]
    return GK_final

print("FIFA19 선수 추천 프로그램")
while(True):
    n=input("\n선수를 추천받고 싶다면 1을,\n종료하려면 2를 입력하세요. ")
    if n=='1':
        print("\n골키퍼(GK) 제외 크게 세 포지션으로 나뉘어 있습니다. (각 포지션에 해당하는 것들)")
        print("공격수(OF) : CF, LF, LS, RF, RS, ST")
        print("수비수(DF) : CB, LB, LCB, LW, LWB, RB, RCB, RW, RWB")
        print("미드필더(MF) : CAM, CDM, CM, LAM, LCM, LDM, LM, RAM, RCM, RDM, RM")

        user_pos=True

        while (user_pos==True):
            user_pos=input("\n원하는 포지션을 입력해주세요. (OF, DF, MF, GK 중 택 1): ")
            if user_pos=='OF':
                print("\n6가지의 능력치가 있습니다.")
                print("Pace : Acceleration(가속력), Sprint speed(최고 속력)")
                print("Dribbling : Agility(민첩성), Balance(균형 감각), Reactions(반응 속도), Ball control(볼 조종력), Dribbling(드리블 실력), Composure(침착성)")
                print("Shooting : Positioning(위치 선정), Finishing(골 결정력), Shot power(슛 파워), Long shots(장거리 슛), Volleys(발리 슛), Penalties(페널티킥 정확도)")
                print("Defending : Interceptions(가로채기), Heading accuracy(헤딩 정확도), Marking(대인 방어), Standing tackle(서서 하는 태클), Sliding tackle(슬라이딩 태클)")
                print("Passing : Vision(선수의 시야), Crossing(크로스 정확도), Free kick accuracy(프리킥 정확도), Short passing(단거리 패스), Long passing(장거리 패스), Curve(커브 수치)")
                print("Physicality : Jumping(점프력), Stamina(체력), Strength(힘), Aggression(공격성)")

                print("\n포지션별 능력치 평균 차이")
                print("Pace : OF>MF>DF\nDribblingA : MF>OF>DF\nShooting : OF>>MF>>DF\nDefending : DF>>MF>>>OF \nPassing : MF>>OF>DF\nPhysicality : DF>OF>MF")

                print("\nOF 가이드 라인")
                print("OF 선수들 평균 능력치 수치 : Pace > DribblingA > Physicality > Shooting > Passing > Defending\n")

                print("<<능력치 별 중요도 입력하기>>\n※중요도가 같은 경우 OF 선수 평균 능력치 순대로 정렬되어 보여집니다.")
                pace=int(input("Pace 중요도를 입력하세요. (1~5) : "))
                drib=int(input("Dribbling 중요도를 입력하세요. (1~5) : "))
                shot=int(input("Shooting 중요도를 입력하세요. (1~5) : "))
                defn=int(input("Defending 중요도를 입력하세요. (1~5) : "))
                pas=int(input("Passing 중요도를 입력하세요. (1~5) : "))
                phy=int(input("Physicality 중요도를 입력하세요. (1~5) : "))
                #Pace > DribblingA > Physicality > Shooting > Passing > Defending
                OFimpt={'Pace':pace, 'DribblingA':drib, 'Physicality':phy,
                        'Shooting':shot, 'Passing':pas, 'Defending':defn}
                OF_final=sort_OF(OFimpt)

                print("\n추천 선수 목록입니다.")
                print(OF_final)
                
            elif user_pos=='DF':
                print("\n6가지의 능력치가 있습니다.")
                print("Pace : Acceleration(가속력), Sprint speed(최고 속력)")
                print("Dribbling : Agility(민첩성), Balance(균형 감각), Reactions(반응 속도), Ball control(볼 조종력), Dribbling(드리블 실력), Composure(침착성)")
                print("Shooting : Positioning(위치 선정), Finishing(골 결정력), Shot power(슛 파워), Long shots(장거리 슛), Volleys(발리 슛), Penalties(페널티킥 정확도)")
                print("Defending : Interceptions(가로채기), Heading accuracy(헤딩 정확도), Marking(대인 방어), Standing tackle(서서 하는 태클), Sliding tackle(슬라이딩 태클)")
                print("Passing : Vision(선수의 시야), Crossing(크로스 정확도), Free kick accuracy(프리킥 정확도), Short passing(단거리 패스), Long passing(장거리 패스), Curve(커브 수치)")
                print("Physicality : Jumping(점프력), Stamina(체력), Strength(힘), Aggression(공격성)")

                print("\n포지션별 능력치 평균 차이")
                print("Pace : OF>MF>DF\nDribblingA : MF>OF>DF\nShooting : OF>>MF>>DF\nDefending : DF>>MF>>>OF \nPassing : MF>>OF>DF\nPhysicality : DF>OF>MF")
                
                print("\nDF 가이드 라인")
                print("DF 선수들 평균 능력치 수치 : Physicality > Pace > Defending > DribblingA > Passing > Shooting\n")

                print("<<능력치 별 중요도 입력하기>>\n※중요도가 같은 경우 DF 선수 평균 능력치 순대로 정렬되어 보여집니다.")
                pace=int(input("Pace 중요도를 입력하세요. (1~5) : "))
                drib=int(input("Dribbling 중요도를 입력하세요. (1~5) : "))
                shot=int(input("Shooting 중요도를 입력하세요. (1~5) : "))
                defn=int(input("Defending 중요도를 입력하세요. (1~5) : "))
                pas=int(input("Passing 중요도를 입력하세요. (1~5) : "))
                phy=int(input("Physicality 중요도를 입력하세요. (1~5) : "))
                #Physicality > Pace > Defending > DribblingA > Passing > Shooting
                DFimpt={'Physicality':phy, 'Pace':pace, 'Defending':defn,
                        'DribblingA':drib, 'Passing':pas, 'Shooting':shot}
                DF_final=sort_DF(DFimpt)

                print("\n추천 선수 목록입니다.")
                print(DF_final)

            elif user_pos=='MF':
                print("\n6가지의 능력치가 있습니다.")
                print("Pace : Acceleration(가속력), Sprint speed(최고 속력)")
                print("Dribbling : Agility(민첩성), Balance(균형 감각), Reactions(반응 속도), Ball control(볼 조종력), Dribbling(드리블 실력), Composure(침착성)")
                print("Shooting : Positioning(위치 선정), Finishing(골 결정력), Shot power(슛 파워), Long shots(장거리 슛), Volleys(발리 슛), Penalties(페널티킥 정확도)")
                print("Defending : Interceptions(가로채기), Heading accuracy(헤딩 정확도), Marking(대인 방어), Standing tackle(서서 하는 태클), Sliding tackle(슬라이딩 태클)")
                print("Passing : Vision(선수의 시야), Crossing(크로스 정확도), Free kick accuracy(프리킥 정확도), Short passing(단거리 패스), Long passing(장거리 패스), Curve(커브 수치)")
                print("Physicality : Jumping(점프력), Stamina(체력), Strength(힘), Aggression(공격성)")

                print("\n포지션별 능력치 평균 차이")
                print("Pace : OF>MF>DF\nDribblingA : MF>OF>DF\nShooting : OF>>MF>>DF\nDefending : DF>>MF>>>OF \nPassing : MF>>OF>DF\nPhysicality : DF>OF>MF")
                
                print("\nMF 가이드 라인")
                print("MF 선수들 평균 능력치 수치 : Pace > DribblingA > Physicality > Passing > Shooting > Defending\n")

                print("<<능력치 별 중요도 입력하기>>\n※중요도가 같은 경우 MF 선수 평균 능력치 순대로 정렬되어 보여집니다.")
                #숫자 아닌 다른 거 입력했을 때 발생할 오류 try catch 추가해야 
                pace=int(input("Pace 중요도를 입력하세요. (1~5) : "))
                drib=int(input("Dribbling 중요도를 입력하세요. (1~5) : "))
                shot=int(input("Shooting 중요도를 입력하세요. (1~5) : "))
                defn=int(input("Defending 중요도를 입력하세요. (1~5) : "))
                pas=int(input("Passing 중요도를 입력하세요. (1~5) : "))
                phy=int(input("Physicality 중요도를 입력하세요. (1~5) : "))
                #Pace > DribblingA > Physicality > Passing > Shooting > Defending
                MFimpt={'Pace':pace, 'DribblingA':drib, 'Physicality':phy,
                        'Passing':pas, 'Shooting':shot, 'Defending':defn}
                MF_final=sort_MF(MFimpt)

                print("\n추천 선수 목록입니다.")
                print(MF_final)

            elif user_pos=='GK':
                #GKDiving GKHandling GKKicking GKPositioning GKReflexes
                print("\n5가지의 능력치가 있습니다.")
                print("GKDiving : 골을 막을 때 다이빙력")
                print("GKHandling : 공 핸들링 능력")
                print("GKKicking : 공을 차는 능력")
                print("GKPositioning : 위치 선정 능력")
                print("GKReflexes : 민첩성, 순발력")

                print("\nGK 가이드라인")
                print("골키퍼의 경우 능력치 대부분에서 전반적으로 상위권이 우세하여 모든 능력치가 중요합니다.")
                print("하지만 Kicking의 경우 상위권에서도 고르지 않은 분포를 보여, 상대적 중요도가 덜합니다.")
                print("\nGK 선수들 평균 능력치 수치 : GKReflexes > GKDiving > GKPositioning > GKHandling > GKKicking")

                print("\n<<능력치 별 중요도 입력하기>>\n※중요도가 같은 경우 GK 선수 평균 능력치 순대로 정렬되어 보여집니다.")
                dive=int(input("GKDiving 중요도를 입력하세요. (1~5) : "))
                hand=int(input("GKHandling 중요도를 입력하세요. (1~5) : "))
                kick=int(input("GKKicking 중요도를 입력하세요. (1~5) : "))
                posi=int(input("GKPositioning 중요도를 입력하세요. (1~5) : "))
                refl=int(input("GKReflexes 중요도를 입력하세요. (1~5) : "))
                #GKReflexes > GKDiving > GKPositioning > GKHandling > GKKicking
                GKimpt={'GKReflexes':refl, 'GKDiving':dive, 'GKPositioning':posi,
                        'GKHandling':hand, 'GKKicking':kick}
                GK_final=sort_GK(GKimpt)

                print("\n추천 선수 목록입니다.")
                print(GK_final)
                
            else:
                print("\n올바른 포지션을 입력해주세요. ")
        
    elif n=='2':
        break
    else:
        print("\n올바른 숫자를 입력해주세요. ")
