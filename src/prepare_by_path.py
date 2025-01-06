import os
import sys

from TrackEntitiesLoader import TrackEntitiesLoader

def prepare_by_path(work_dir_path: str):
    if not os.path.exists(work_dir_path):
        print(f"存在しないパスです: {work_dir_path}")
    elif not os.path.isdir(work_dir_path):
        print(f"ディレクトリではないパスです: {work_dir_path}")
    else:
        directories = [entry for entry in os.listdir(work_dir_path) if
                       os.path.isdir(os.path.join(work_dir_path, entry))]
        for dir_name in directories:
            dir_path = os.path.join(work_dir_path, dir_name)
            tel = TrackEntitiesLoader(dir_path)
            tel.generate_settings()
            print(f"設定ファイルを作成しました: {tel.get_setting_file_path()}")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("引数が足りません")
    else:
        script_name = sys.argv[0]
        work_dir_path = os.path.abspath(sys.argv[1])
        prepare_by_path(work_dir_path)
