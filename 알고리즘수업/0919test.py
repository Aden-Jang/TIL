# # 엔디안
# import sys
#
# print(sys.byteorder)
#
# # 비트
# def bit_print(i):       # 7번비트 -> 0번 비트 출력
#     s = ''
#     for j in range(7, -1, -1):
#         s += '1' if (i&(1<<j)) else '0'
#     print(s)
#
# bit_print(5)
# bit_print(-5)
# bit_print(-6)
# bit_print(-6>>1)

# 실수
import struct
a = 9.187500
bits, = struct.unpack('I', struct.pack('f', a))
print(f'{bits:032b}')