for x in range(9):                    # ① 9行分ループ（0〜8）
    for y in range(9):                # ① 同じく9列分ループ（0〜8）
        print('%2d' % ((x + 1) * (y + 1)), end=' ')  # ③ 掛け算結果を表示（2桁揃え）
    print('')                         # ② 改行
