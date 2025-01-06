import os
import sys

from TagManager import TagManager
from TrackEntitiesLoader import TrackEntitiesLoader


def execute_by_path(work_dir_path: str):
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
            if not tel.is_exists_settings_file():
                print(f"設定ファイルがありません: {tel.get_setting_file_path()}")
                print(f"先にprepare.shを実行してください")
            else:
                track_list = tel.load_list_from_settings()
                TagManager.bulk_update(track_list)
                print(f"タグ情報を更新しました: {dir_path}")
                print(f"処理した数: {len(track_list)}")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("引数が足りません")
    else:
        script_name = sys.argv[0]
        work_dir_path = os.path.abspath(sys.argv[1])
        execute_by_path(work_dir_path)
