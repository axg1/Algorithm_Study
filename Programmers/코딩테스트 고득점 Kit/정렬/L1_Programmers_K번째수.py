def solution(array, commands):
    listmake = [] #빈 리스트를 만든다
    for i in commands:
        new_array = array[i[0]-1:i[1]]
        new_array.sort()
        listmake.append(new_array[i[2]-1])
    return listmake