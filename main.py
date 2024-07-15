import time

def genHam(num):
    hamarr = [0, 0, 0, 0, 0, 0, 0]
    hamarr[2] = num[0]; hamarr[4] = num[1];
    hamarr[5] = num[2]; hamarr[6] = num[3]; 
    print(hamarr)
    # 0, 1, 3 index
    for i in range(3):
        temp_parity = 0
        if i == 0: temp_parity = f"{hamarr[2]}" + f"{hamarr[4]}" + f"{hamarr[6]}"
        elif i == 1: temp_parity = f"{hamarr[2]}" + f"{hamarr[5]}" + f"{hamarr[6]}"
        else: temp_parity = f"{hamarr[4]}" + f"{hamarr[5]}" + f"{hamarr[6]}"
        
        one_count = temp_parity.count('1')
        hamarr[3 if i == 2 else i] = one_count % 2
    print(hamarr)
    
def debugHam(ham):
   hamarr = list(map(str, ham))
   c1 = hamarr[0]; c2 = hamarr[1]; c4 = hamarr[3]
   err_loc = int(f"{c1}{c2}{c4}", 2)
   hamarr[err_loc - 1] = str(int(hamarr[err_loc - 1]) ^ 1) # XOR 노드가 아닌 다른 노드 쓰는 방안 찾아보기 (or Inverse)
   print(list(map(str, ham)))
   print(hamarr)
   if list(map(str, ham)) == hamarr:
       print("오류가 없습니다")
   else:
       print(f"{err_loc}번째 비트에 오류가 있습니다.")
       print(f"정정된 해밍 코드 :: ", end="")
       for i in range(len(hamarr)): print(hamarr[i], end="")   
       print()

# def debugHam(ham):
#     hamarr = list(map(int, ham))  # 입력을 정수 리스트로 변환
#     c1 = hamarr[0]
#     c2 = hamarr[1]
#     c4 = hamarr[3]
    
#     # 오류 위치 계산 (1 기반)
#     err_loc = int(f"{c1}{c2}{c4}", 2)
    
#     if err_loc == 0:
#         print("오류가 없습니다.")
#     else:
#         # 오류 수정
#         hamarr[err_loc - 1] = hamarr[err_loc - 1] ^ 1  # XOR 연산으로 비트 교정
        
#         # 교정 후 결과 출력
#         print(f"{err_loc}번째 비트에 오류가 있습니다.")
#         print("정정된 해밍 코드 :: ", end="")
#         for bit in hamarr:
#             print(bit, end="")
#         print()
    
def main():
    print("Python 해밍 코드")
    print("1. Hamming Code 생성하기")
    print("2. Hamming Code 에러 찾기")
    opt = int(input(">> "))
    if opt == 1:
        inp = int(input("Data Bit을 입력해주세요. (0 ~ 9까지의 자연수)\n>> "))
        genHam(f"{inp:04b}")
    elif opt == 2:
        inp = input("제공받은 해밍 코드를 입력해주세요.\n>> ")
        debugHam(inp)
    else:
        print("올바른지 않은 입력입니다.")
        print("초기 화면으로 돌아갑니다.")
        time.sleep(1)
        main()

main()