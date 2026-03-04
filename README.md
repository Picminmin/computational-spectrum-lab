# Computational Spectrum Lab

**Visualizing the spectral structure of computation**

![manim](https://img.shields.io/badge/made%20with-Manim-blue)
![python](https://img.shields.io/badge/python-3.x-green)
![fft](https://img.shields.io/badge/topic-FFT-orange)

---

## English

Computational Spectrum Lab is a research-oriented project that explores the deep mathematical connection between

- Fourier Transform
- Convolution
- Shift Operators
- Circulant Matrices
- Eigenvalue Decomposition

through **visualization and computational experiments**.

This project aims to make the following structure intuitive:

Shift Operator → Fourier Basis → Spectral Decomposition → Fast Convolution

The repository contains both

- Python experiments
- Manim mathematical animations

to explore the **spectral structure of computation**.

---

## 日本語

Computational Spectrum Lab は

- フーリエ変換
- 畳み込み
- シフト演算子
- 巡回行列
- 固有値分解

などの関係を **実験と可視化によって理解するための研究プロジェクト**です。

このプロジェクトでは次の構造を直感的に理解することを目的としています。


Python と Manim を用いて

- 計算実験
- 数学アニメーション

を作成しています。

---

# Example Visualization

Below is an example animation showing how convolution becomes diagonalized in the Fourier basis.

![Convolution Animation](outputs/gifs/convolution_diagonalization.gif)

---

# Mathematical Insight

The core mathematical idea explored in this repository is

\[
F^{-1} S F = \Lambda
\]

where

- \(S\) is the shift operator
- \(F\) is the Fourier matrix
- \(\Lambda\) is diagonal.

This means that the Fourier transform **diagonalizes the shift operator**.

As a result,

**convolution becomes multiplication in the Fourier domain**.

---

# Project Structure

```text
computational-spectrum-lab
│
├ experiments
│   ├ shift_operator
│   └ convolution_fft
│
├ animations
│   └ manim
│
├ outputs
│   ├ videos
│   └ gifs
│
├ scripts
│
├ docs
│
└ README.md

```
# Installation

```bash
Clone the repository
git clone https://github.com/yourname/computational-spectrum-lab.git
cd computational-spectrum-lab
```

install dependencies
```bash
pip install -r requirements.txt
```
To render animations with Manim, install system dependencies such as

ffmpeg

LaTeX

See the official Manim documentation:

https://docs.manim.community/

# Experiments

## Shift Operator

```bash
python experiments/shift_operator/shift_operator.py
```

## Convolution & FFT

```bash
python experiments/convolution_fft/convolution_fft.py
```

# Animations

## Convolution Diagonalization

```bash
manim -pql animations/manim/convolution_theorem.py ConvolutionDiagonalization
```

## Future Work
Planned extensions include

- Fourier matrix visualization
- convolution diagonalization animation
- spectral interpretation of filters
- GPU FFT experiments

## Topics

fft
fourier-transform
signal-processing
linear-algebra
manim
visualization

## License
MIT License

## Author
[Your Name]
[Your Affiliation]
[Your Contact Information]

## Acknowledgments

- Manim Community for the animation framework
- NumPy and SciPy for numerical computation
- Matplotlib for plotting

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

## License

This project is licensed under the terms of the MIT License.

## Author
GitHub
https://github.com/picminmin
