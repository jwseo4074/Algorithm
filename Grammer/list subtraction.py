# 리스트에 리스트 합치는건 리스트 + 리스트로 해결.
# 리스트 - 리스트 ?

Nlist = [i for i in range(0,N)]

for oneVal in combiList:
    startTeam = list(oneVal)
    linkTeam = [x for x in Nlist if x not in startTeam]
    totalList.append([startTeam, linkTeam])

# linkTeam은 1~6까지의 수 중에서 startTeam 에 있는 숫자들을 빼고 나머지 값들

[x for x in Nlist if x not in startTeam] 

# 이 부분이 핵심, Nlist 에 있는 걸 하나씩 돌건데 startTeam 에 없는 애만 배열에 추가해줄거야