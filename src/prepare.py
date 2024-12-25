import os
import sys

from TrackEntitiesLoader import TrackEntitiesLoader

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("引数が足りません")
    else:
        script_name = sys.argv[0]
        dir_path = os.path.abspath(sys.argv[1])
        if not os.path.exists(dir_path):
            print(f"存在しないパスです: {dir_path}")
        elif not os.path.isdir(dir_path):
            print(f"ディレクトリではないパスです: {dir_path}")
        else:
            tel = TrackEntitiesLoader(dir_path)
            tel.generate_settings()
            print(f"設定ファイルを作成しました: {tel.get_setting_file_path()}")
