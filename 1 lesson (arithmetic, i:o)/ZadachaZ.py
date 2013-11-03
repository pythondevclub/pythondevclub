N = int(input())
K = int(input())
M = int(input())

KD = (K // M) * (N // K)

N1 = (N % K) + (K % M) * (N // K)
KD1 = (K // M) * (N1 // K)

N2 = (N1 % K) + (K % M) * (N1 // K)
KD2 = (K // M) * (N2 // K)

N3 = (N2 % K) + (K % M) * (N2 // K)
KD3 = (K // M) * (N3 // K)

N4 = (N3 % K) + (K % M) * (N3 // K)
KD4 = (K // M) * (N4 // K)

N5 = (N4 % K) + (K % M) * (N4 // K)
KD5 = (K // M) * (N5 // K)

print(KD + KD1 + KD2 + KD3 + KD4 + KD5)
