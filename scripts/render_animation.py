import os
import subprocess
from pathlib import Path

def main():
    base_dir = Path(__file__).resolve().parent.parent
    manim_script = base_dir / "animations" / "manim" / "convolution_theorem.py"
    output_dir = base_dir / "outputs" / "videos"

    # Manimのコマンドを構築
    # -p: Render後にプレビュー(再生)
    # -ql: 低画質(早送り・テスト用)。本番は -qh (高画質) を推奨
    # --media_dir: 出力先
    cmd = [
        "manim",
        str(manim_script),
        "ConvolutionDiagonalization",
        "-pqh",
        "--media_dir", str(output_dir)
    ]

    print(f"Manim アニメーションをレンダリングします...\n実行コマンド: {' '.join(cmd)}\n")
    try:
        subprocess.run(cmd, check=True)
        print("\nレンダリングが完了しました！")
    except FileNotFoundError:
        print("\n[エラー] manim コマンドが見つかりませんでした。")
        print("以下のコマンドでインストールするか、仮想環境を有効化してください。")
        print("  pip install manim")
        print("また、FFmpeg などのシステム依存ツールが必要な場合があります。")
    except subprocess.CalledProcessError as e:
        print(f"\n[エラー] Manim の実行中にエラーが発生しました: {e}")

if __name__ == "__main__":
    main()
