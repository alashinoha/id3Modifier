class TrackEntity:
    abs_file_path: str = None
    abs_img_path: str = None
    img_type: str = "jpeg"
    track_number: int = None
    track_total: int = None
    title: str = None
    album: str = None
    file_type: str = None
    artist: str = None

    def __init__(self,
                 abs_file_path: str,
                 abs_img_path: str = None,
                 img_type: str = "jpeg",
                 track_number: int = None,
                 track_total: int = None,
                 title: str = None,
                 album: str = None,
                 file_type: str = None,
                 artist: str = None,
                 ):
        self.img_type = img_type
        self.abs_file_path = abs_file_path
        self.abs_img_path = abs_img_path
        self.track_number = track_number
        self.track_total = track_total
        self.title = title
        self.album = album
        self.file_type = file_type
        self.artist = artist
