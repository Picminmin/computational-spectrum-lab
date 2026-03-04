"""
1次元信号の畳み込みについて、直接計算（重畳積分）とFFTによる計算を比較するスクリプト。
計算速度の測定と結果の確認を行います。
"""

import numpy as np
import matplotlib.pyplot as plt
import time
from scipy import signal

def main():
    # サンプル数（データサイズ）を設定
    N = 10000

    print(f"信号の長さ (N) = {N}")

    # サンプル信号1 (合成波) の生成
    t = np.linspace(0, 10, N)
    f1, f2 = 2.0, 10.0
    x = np.sin(2 * np.pi * f1 * t) + 0.5 * np.cos(2 * np.pi * f2 * t)

    # サンプル信号2 (インパルス応答、フィルタのようなもの) を生成
    h = np.exp(-t * 2.0)

    # ==========================
    # 1. 直接的な畳み込み (O(N^2))
    # ==========================
    print("直接計算による畳み込みを実行中...")
    start_time = time.time()
    # mode='full' は出力長が 2N - 1 となる
    conv_direct = np.convolve(x, h, mode='full')
    time_direct = time.time() - start_time
    print(f" -> 実行時間: {time_direct:.6f} 秒")

    # ==========================
    # 2. FFTを用いた畳み込み (O(N log N))
    # ==========================
    print("FFTを用いた畳み込みを実行中...")
    start_time = time.time()
    # 内部的にFFT(x) * FFT(h) を計算し、IFFTで元に戻す
    conv_fft = signal.fftconvolve(x, h, mode='full')
    time_fft = time.time() - start_time
    print(f" -> 実行時間: {time_fft:.6f} 秒")

    # ==========================
    # 結果の比較
    # ==========================
    # 最大誤差の計算
    max_error = np.max(np.abs(conv_direct - conv_fft))
    print(f"\n直接計算とFFT計算の最大誤差: {max_error:.2e}")

    if time_fft > 0:
        print(f"FFT計算は直接計算に比べて約 {time_direct / time_fft:.2f} 倍高速でした。")

    # ==========================
    # プロット
    # ==========================
    fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=False)

    # 信号のプロット（冒頭部分のみ）
    plot_len = min(N, 1000)

    axs[0].plot(t[:plot_len], x[:plot_len], label="Signal x(t)", color="blue")
    axs[0].set_title("Input Signal x(t)")
    axs[0].grid(True, linestyle=":", alpha=0.7)

    axs[1].plot(t[:plot_len], h[:plot_len], label="Filter response h(t)", color="orange")
    axs[1].set_title("Impulse Response h(t)")
    axs[1].grid(True, linestyle=":", alpha=0.7)

    # 畳み込み結果のプロット
    conv_plot_len = min(len(conv_direct), 2000)
    axs[2].plot(conv_direct[:conv_plot_len], label="Direct Convolution", color="green", alpha=0.7)
    axs[2].plot(conv_fft[:conv_plot_len], label="FFT Convolution", color="red", linestyle="--", alpha=0.7)
    axs[2].set_title("Convolution Result Comparison")
    axs[2].legend()
    axs[2].grid(True, linestyle=":", alpha=0.7)

    plt.tight_layout()
    print("\n畳み込みのプロットを表示します。ウィンドウを閉じるとプログラムが終了します。")
    plt.show()

if __name__ == "__main__":
    main()
