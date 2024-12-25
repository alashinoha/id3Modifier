import os

import yaml

from TagSettingsEntity import TagSettingsEntity, TagSettingsTrackEntity
from TrackEntity import TrackEntity


class TrackEntitiesLoader:
    settings_file_name = "tag_settings.yaml"

    def __init__(self, path):
        self.path = path

    def is_exists_settings_file(self) -> bool:
        return os.path.exists(self._get_setting_file_path())

    def _get_setting_file_path(self):
        return os.path.abspath(os.path.join(self.path, self.settings_file_name))

    def load_list_from_settings(self) -> list[TrackEntity]:
        setting: TagSettingsEntity = self.load_settings()
        tracks: list[TrackEntity] = []
        for track in setting.tracks:
            tracks.append(
                TrackEntity(
                    abs_file_path=os.path.abspath(os.path.join(self.path, track.file_name)),
                    abs_img_path=None if setting.album_img != "" else os.path.abspath(os.path.join(self.path, setting.album_img)),
                    track_number=track.track_number,
                    track_total=setting.track_total,
                    title=track.title,
                    album=setting.album,
                    file_type=track.file_type,
                    artist=setting.artist,
                )
            )
        return tracks

    def load_settings(self) -> TagSettingsEntity:
        setting: TagSettingsEntity = TagSettingsEntity()
        with open(self._get_setting_file_path(), "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
            setting.album = data["album"]
            setting.artist = data["artist"]
            setting.disc_number = data["disc_number"]
            setting.disc_total = data["disc_total"]
            setting.track_total = data["track_total"]
            setting.album_img = data["album_img"]
            for d in data["tracks"]:
                track: TagSettingsTrackEntity = TagSettingsTrackEntity()
                track.title = d["title"]
                track.file_name = d["file_name"]
                track.file_type = d["file_type"]
                setting.tracks.append(track)
        return setting

    def generate_settings(self):
        setting: TagSettingsEntity = TagSettingsEntity()
        setting.album = os.path.basename(self.path.rstrip("/"))
        img_path: [str | None] = None
        file_list_music: list[str] = []
        for item in sorted([f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))],
                           key=lambda f: f.lower()):
            if img_path is None and TrackEntitiesLoader.is_picture_file(item):
                img_path = item
            elif TrackEntitiesLoader.is_music_file(item):
                file_list_music.append(item)
        # settingの情報の更新
        setting.track_total = len(file_list_music)
        setting.album_img = img_path
        for index, item in enumerate(file_list_music):
            track = TagSettingsTrackEntity()
            track.track_number = index + 1
            track.title = TrackEntitiesLoader.extract_title(item)
            track.file_name = item
            track.file_type = TrackEntitiesLoader.extract_ext(item)
            setting.tracks.append(track)
        # ファイルの書き込み
        with open(self._get_setting_file_path(), "w", encoding="utf-8") as file:
            yaml.dump(setting.dump(), file, allow_unicode=True, default_flow_style=False)

    @staticmethod
    def is_picture_file(file_name: str) -> bool:
        return (file_name.lower().endswith(".jpg") or
                file_name.lower().endswith(".jpeg") or
                file_name.lower().endswith(".png"))

    @staticmethod
    def is_music_file(file_name: str) -> bool:
        return (file_name.lower().endswith(".mp3") or
                file_name.lower().endswith(".wav") or
                file_name.lower().endswith(".flac") or
                file_name.lower().endswith(".m4a"))

    @staticmethod
    def extract_ext(file_name: str):
        _, ext_with_dot = os.path.splitext(file_name)
        ext = ext_with_dot.lstrip('.')
        return ext.lower()

    @staticmethod
    def extract_title(file_name):
        _, ext_with_dot = os.path.splitext(file_name)
        return _
