import os
import subprocess
from pathlib import Path

def main():
    # プロジェクトのルートディレクトリを取得
    base_dir = Path(__file__).resolve().parent.parent
    experiments_dir = base_dir / "experiments"

    # 実行するスクリプトのリスト
    scripts = [
        experiments_dir / "shift_operator" / "shift_operator.py",
        experiments_dir / "convolution_fft" / "convolution_fft.py",
    ]

    for script_path in scripts:
        print(f"[{script_path.name}] を実行中...")
        if script_path.exists():
            try:
                subprocess.run(["python", str(script_path)], check=True)
                print(f"[{script_path.name}] 実行完了！\n")
            except subprocess.CalledProcessError as e:
                print(f"[{script_path.name}] の実行中にエラーが発生しました: {e}\n")
        else:
            print(f"ファイルが見つかりません: {script_path}\n")

if __name__ == "__main__":
    main()
