class TagSettingsTrackEntity:

    def __init__(self):
        self.track_number: int = 1
        self.title: str = None
        self.file_name: str = None
        self.file_type: str = None

    def dump(self) -> dict:
        return {
            "track_number": self.track_number,
            "title": self.title,
            "file_name": self.file_name,
            "file_type": self.file_type,
        }


class TagSettingsEntity:

    def __init__(self):
        self.album: str = ""
        self.artist: str = ""
        self.disc_number: int = 1
        self.disc_total: int = 1
        self.track_total: int = 1
        self.album_img: str = ""
        self.album_img_type: str = "jpeg"
        self.tracks: list[TagSettingsTrackEntity] = []

    def dump(self) -> dict:
        return {
            "album": self.album,
            "artist": self.artist,
            "disc_number": self.disc_number,
            "disc_total": self.disc_total,
            "track_total": self.track_total,
            "album_img": self.album_img,
            "album_img_type": self.album_img_type,
            "tracks": list(map(lambda track: track.dump(), self.tracks)),
        }
