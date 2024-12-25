import os.path

import taglib
from mutagen.mp3 import MP3
from mutagen.wave import WAVE
from mutagen.id3 import ID3, APIC, error

from TrackEntity import TrackEntity


class TagManager:

    @staticmethod
    def bulk_update(track_entities: list[TrackEntity]):
        for entity in track_entities:
            TagManager.update(entity)

    @staticmethod
    def update(track_entity: TrackEntity):
        song = taglib.File(track_entity.abs_file_path)
        song.tags["ALBUM"] = TagManager.__convert_str_to_tag(track_entity.album)
        song.tags["TITLE"] = TagManager.__convert_str_to_tag(track_entity.title)
        if track_entity.file_type == "flac":
            # flacだけトラックナンバーの形式が違う
            song.tags["TRACKNUMBER"] = TagManager.__convert_str_to_tag(track_entity.track_number)
            song.tags["TRACKTOTAL"] = TagManager.__convert_str_to_tag(track_entity.track_total)
        else:
            song.tags["TRACKNUMBER"] = TagManager.__extract_track_number(track_entity)
        song.save()
        TagManager.update_track_image(track_entity)

    @staticmethod
    def read(track_entity: TrackEntity):
        return taglib.File(track_entity.abs_file_path).tags

    @staticmethod
    def __convert_str_to_tag(value: [str | None]) -> list[str]:
        if value is None:
            return [""]
        else:
            return [value]

    @classmethod
    def __extract_track_number(cls, track_entity: TrackEntity) -> list[str]:
        if track_entity.track_number is None:
            return [""]
        else:
            return [f"{track_entity.track_number}/{track_entity.track_total}"]

    @classmethod
    def update_track_image(cls, track_entity):
        if (track_entity.abs_img_path is None
                or track_entity.abs_img_path == ""
                or not os.path.exists(track_entity.abs_img_path)
                or not os.path.isfile(track_entity.abs_img_path)):
            return
        if track_entity.file_type == "mp3":
            cls.update_track_image_mp3(track_entity)
        if track_entity.file_type == "wav":
            cls.update_track_image_wav(track_entity)

    @classmethod
    def update_track_image_mp3(cls, track_entity: TrackEntity):
        try:
            # MP3ファイルを開く
            audio = MP3(track_entity.abs_file_path, ID3=ID3)
            # ID3タグがない場合は作成
            if audio.tags is None:
                audio.add_tags()
            # アルバムアートを追加
            with open(track_entity.abs_img_path, "rb") as img:
                audio.tags.add(
                    APIC(
                        encoding=3,  # UTF-8
                        mime=f"image/{track_entity.img_type}",  # MIMEタイプ
                        type=3,  # 表示用のカバーアート
                        desc="Cover",
                        data=img.read()  # 画像データを読み込む
                    )
                )
            # UTF-8エンコーディングを明示的に設定
            audio.tags.update_to_v23()  # ID3v2.3に変換することで互換性を確保
            # ファイルを保存
            audio.save()
        except error as e:
            print(f"Error: {e}")

    @classmethod
    def update_track_image_wav(cls, track_entity: TrackEntity):
        try:
            # WAVファイルを開く
            audio = WAVE(track_entity.abs_file_path)
            # ID3タグを追加
            if audio.tags is None:
                audio.add_tags()
            # アルバムアートを追加
            with open(track_entity.abs_img_path, "rb") as img:
                audio.tags.add(
                    APIC(
                        encoding=3,  # UTF-8
                        mime=f"image/{track_entity.img_type}",  # MIMEタイプ
                        type=3,  # 表示用のカバーアート
                        desc="Cover",
                        data=img.read()  # 画像データ
                    )
                )
            # ファイルを保存
            audio.save()
        except Exception as e:
            print(f"Error: {e}")
