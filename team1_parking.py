def print_list(list):
    for i in range(3):print(list[5-i])  # 3x6 주차지 출력
    print()
    for j in range(3, 6):print(list[5-j])   # 3x6 주차지 출력

parking = [[0 for _ in range(6)] for _ in range(6)] # 6x6 주차지 생성
parking_sucess = False # 주차지 사용 여부 초기 값

while True:
    obj = str(input("차량 종류 : "))    # 차량 종류 입력
    park_time = int(input("주차 시간(h) : ")) # 주차 시간 입력
    if obj == 'car' and park_time < 24: # 차량 종류가 car이고 주차 시간이 24시간 미만일 경우
        for i in range(6):
            for j in range(6):
                if parking[i][j] == 0: # 주차지에 차량이 없을 경우
                    parking[i][j] = 1   # 주차지에 차량 추가
                    parking_sucess = True # 주차 성공
                    break
                else:
                    pass
            if parking_sucess == True: # 주차 성공 시
                break
        print_list(parking) # 주차지 출력 함수 호출
        parking_sucess = False # 주차 성공 초기화
    elif obj == 'truck' and park_time < 24: # 차량 종류가 truck이고 주차 시간이 24시간 미만일 경우
        for i in range(6):
            for j in range(6):
                if parking[i][j] == 0 and parking[i+1][j] == 0: # 주차지에 차량이 없고 주차지 옆에 차량이 없을 경우
                    parking[i][j] = 1  # 주차지에 차량 추가
                    parking[i+1][j] = 1 # 주차지 옆에 차량 추가
                    parking_sucess = True # 주차 성공
                    break
                else:
                    pass
            if parking_sucess == True: # 주차 성공 시
                break
        print_list(parking) # 주차지 출력 함수 호출
        parking_sucess = False # 주차 성공 초기화
    elif obj == 'car' and park_time >= 24: # 차량 종류가 car이고 주차 시간이 24시간 이상일 경우
        for i in range(6):
            if i == 1 or i == 4: # 주차지의 행이 1, 4일 경우
                for j in range(6):
                    if parking[i][j] == 0: # 주차지에 차량이 없을 경우
                        parking[i][j] = 1   # 주차지에 차량 추가
                        parking_sucess = True # 주차 성공
                        break
                    else: 
                        pass  
                if parking_sucess == True: # 주차 성공 시
                    break
            else:
                pass
        print_list(parking) # 주차지 출력 함수 호출
        parking_sucess = False # 주차 성공 초기화
    elif obj == 'truck' and park_time >= 24: # 차량 종류가 truck이고 주차 시간이 24시간 이상일 경우
        for i in range(6):
            if i == 1 or i == 4: # 주차지의 행이 1, 4일 경우
                for j in range(6):
                    if parking[i][j] == 0 and parking[i+1][j] == 0: # 주차지에 차량이 없고 주차지 옆에 차량이 없을 경우
                        parking[i][j] = 1 # 주차지에 차량 추가
                        parking[i+1][j] = 1     # 주차지 옆에 차량 추가
                        parking_sucess = True   # 주차 성공
                        break
                    else:
                        pass
                if parking_sucess == True: # 주차 성공 시
                    break
            else:
                pass
        print_list(parking) # 주차지 출력 함수 호출
        parking_sucess = False # 주차 성공 초기화
    else:
        break