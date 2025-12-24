N = int(input())  # 生徒の数Nを読み込む
T = list(map(int, input().split()))  # 各生徒のゴールまでの時間を読み込む
# ここにプログラムを追記

for i,v in enumerate(T):
 if v==min(T):
  print(i+1)
