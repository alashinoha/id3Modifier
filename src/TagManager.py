import taglib

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
