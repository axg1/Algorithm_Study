def solution(n, lost, reserve):
    # 조건에서 여벌의 체육복이 있는 학생도 도난당했을 수 있다는 것은 lost 값과 reserve 값이 공통적으로 존재 할 수 있다는 것을 의미
    # 따라서 여벌의 체육복은 1개이므로 체육복을 다른 학생에게 빌려줄 수 없다
    set_reserve = set(reserve) - set(lost)  # 동일하게 존재하는 값 제거 ex{3,4,5}-{1,2,3}={4,5}
    set_lost = set(lost) - set(reserve)  # 동일하게 존재하는 값 제거 ex){1,2,3}-{3,4,5}={1,2}

    # reserve 학생의 왼쪽 학생부터 빌려주고, 만약 없으면 오른쪽 학생을 빌려줌
    for i in set_reserve:  # reserve에 있는 값을 하나씩 넣는다
        if i - 1 in set_lost:  # 만약 reserve-1의 값이 lost에 포함되어있다면
            set_lost.remove(i - 1)  # lost에서 그 값을 제거한다
        elif i + 1 in set_lost:  # 만약 reserve+1의 값이 lost에 포함되어있다면
            set_lost.remove(i + 1)  # lost에서 그 값을 제거한다
    return n - len(set_lost)  # 총 학생수 - 체육복 잃어버린 학생수