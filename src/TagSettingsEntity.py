

class TagSettingsTrackEntity:

    track_number: int = 1

    title: str = None
    file_name: str = None
    file_type: str = None

    def dump(self) -> dict:
        return {
            "track_number": self.track_number,
            "title": self.title,
            "file_name": self.file_name,
            "file_type": self.file_type,
        }

class TagSettingsEntity:

    album: str = ""
    artist: str = ""
    disc_number: int = 1
    disc_total: int = 1
    track_total: int = 1
    album_img: str = ""

    tracks: list[TagSettingsTrackEntity] = []

    def dump(self) -> dict:
        return {
            "album": self.album,
            "artist": self.artist,
            "disc_number": self.disc_number,
            "disc_total": self.disc_total,
            "track_total": self.track_total,
            "album_img": self.album_img,
            "tracks": list(map(lambda track: track.dump(), self.tracks)),
        }