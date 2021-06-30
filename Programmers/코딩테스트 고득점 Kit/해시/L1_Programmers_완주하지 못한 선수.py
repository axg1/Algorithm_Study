def solution(participant, completion):

    participant.sort()  # 정렬한다
    completion.sort()  # 정렬한다

    for p, c in zip(participant, completion):  # zip은 배열을 같은 인덱스끼리 짝지어준다
        if p != c:  # 만약 p와 c가 다르다면
            return p  # 다른 요소를 return한다

    return participant[-1]  # 다른 요소가 없다면 participant의 마지막 요소를 return한다!! participant의 길이는 completion의 길이보다 1크기 때문!!