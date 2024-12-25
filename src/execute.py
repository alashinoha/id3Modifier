import os
import sys

from TagManager import TagManager
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
            if not tel.is_exists_settings_file():
                print(f"設定ファイルがありません: {tel.get_setting_file_path()}")
                print(f"先にprepare.shを実行してください")
            else:
                track_list = tel.load_list_from_settings()
                TagManager.bulk_update(track_list)
                print(f"タグ情報を更新しました: {dir_path}")
                print(f"処理した数: {len(track_list)}")
