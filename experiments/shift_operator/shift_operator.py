"""
巡回シフト演算子の固有値を計算し、複素平面上にプロットするスクリプト。
"""

import numpy as np
import matplotlib.pyplot as plt

def create_cyclic_shift_operator(n):
    """
    n x n の巡回シフト演算子 S を生成する
    S e_k = e_{k+1} (ただし e_n = e_0)
    """
    S = np.zeros((n, n))
    for i in range(n):
        S[(i + 1) % n, i] = 1
    return S

def main():
    # 行列のサイズを設定
    n = 8
    S = create_cyclic_shift_operator(n)

    print(f"巡回シフト演算子 S ({n}x{n}):")
    print(S)

    # 行列 S の固有値（Eigenvalues）と固有ベクトル（Eigenvectors）を計算
    eigenvalues, eigenvectors = np.linalg.eig(S)

    # 巡回シフト演算子の固有値は1のべき根 (roots of unity) になる
    print("\n計算された固有値:")
    for i, ev in enumerate(eigenvalues):
        print(f"λ_{i} = {ev.real: .4f} {ev.imag:+.4f}j")

    # 固有値を複素平面にプロット
    plt.figure(figsize=(6, 6))

    # 単位円を描画
    theta = np.linspace(0, 2*np.pi, 200)
    plt.plot(np.cos(theta), np.sin(theta), color='gray', linestyle='--', label='Unit Circle')

    # 固有値を散布図としてプロット
    plt.scatter(eigenvalues.real, eigenvalues.imag, color='red', s=100, zorder=5, label='Eigenvalues')

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.axis('equal')
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.title(f"Eigenvalues of {n}x{n} Cyclic Shift Operator")
    plt.xlabel("Real Part")
    plt.ylabel("Imaginary Part")
    plt.legend()

    # 表示
    print("\n固有値のプロットを表示します。ウィンドウを閉じるとプログラムが終了します。")
    plt.show()

if __name__ == "__main__":
    main()
