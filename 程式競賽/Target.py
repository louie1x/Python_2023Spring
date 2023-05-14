n, x, y = map(int, input().split())
targets = list(map(int, input().split()))


# 計算擊倒特定標靶需要幾次射擊
if y in targets:
    shots = 0
    for i in range(n):
        # 如果這個標靶還沒被擊倒，就進行射擊
        if targets[i] != -1:
            shots += 1
            # 如果擊倒了目標標靶，就結束射擊
            if targets[i] == y:
                break
            # 擊倒最近的相同類型的標靶
            for j in range(i+1, n):
                if targets[j] == targets[i]:
                    targets[j] = -1
                    break

    print(shots)
