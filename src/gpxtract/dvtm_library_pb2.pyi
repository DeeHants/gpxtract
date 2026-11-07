from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FCMLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEMI_AUTO_FCM: _ClassVar[FCMLevel]
    FULL_AUTO_FCM: _ClassVar[FCMLevel]

class AeMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AE_MODE_OFF: _ClassVar[AeMode]
    AE_MODE_ON: _ClassVar[AeMode]

class AiMotObjState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AI_MOT_OBJ_STATE_INVALID: _ClassVar[AiMotObjState]
    AI_MOT_OBJ_STATE_TRACKED: _ClassVar[AiMotObjState]
SEMI_AUTO_FCM: FCMLevel
FULL_AUTO_FCM: FCMLevel
AE_MODE_OFF: AeMode
AE_MODE_ON: AeMode
AI_MOT_OBJ_STATE_INVALID: AiMotObjState
AI_MOT_OBJ_STATE_TRACKED: AiMotObjState

class ClipMetaHeader(_message.Message):
    __slots__ = ("proto_file_name", "library_proto_version", "product_proto_version", "product_sn", "product_firmware_version", "meta_encryption_type", "meta_compression_type", "clip_timestamp", "product_name")
    class MetaEncryptionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        META_ENCRYPTION_TYPE_NONE: _ClassVar[ClipMetaHeader.MetaEncryptionType]
    META_ENCRYPTION_TYPE_NONE: ClipMetaHeader.MetaEncryptionType
    class MetaCompressionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        META_COMPRESSION_TYPE_NONE: _ClassVar[ClipMetaHeader.MetaCompressionType]
    META_COMPRESSION_TYPE_NONE: ClipMetaHeader.MetaCompressionType
    PROTO_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    LIBRARY_PROTO_VERSION_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_PROTO_VERSION_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_SN_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    META_ENCRYPTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    META_COMPRESSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLIP_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    proto_file_name: str
    library_proto_version: str
    product_proto_version: str
    product_sn: str
    product_firmware_version: str
    meta_encryption_type: ClipMetaHeader.MetaEncryptionType
    meta_compression_type: ClipMetaHeader.MetaCompressionType
    clip_timestamp: int
    product_name: str
    def __init__(self, proto_file_name: _Optional[str] = ..., library_proto_version: _Optional[str] = ..., product_proto_version: _Optional[str] = ..., product_sn: _Optional[str] = ..., product_firmware_version: _Optional[str] = ..., meta_encryption_type: _Optional[_Union[ClipMetaHeader.MetaEncryptionType, str]] = ..., meta_compression_type: _Optional[_Union[ClipMetaHeader.MetaCompressionType, str]] = ..., clip_timestamp: _Optional[int] = ..., product_name: _Optional[str] = ...) -> None: ...

class StreamMetaHeader(_message.Message):
    __slots__ = ("stream_id", "stream_type", "stream_name")
    class StreamType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STREAM_TYPE_VIDEO: _ClassVar[StreamMetaHeader.StreamType]
        STREAM_TYPE_AUDIO: _ClassVar[StreamMetaHeader.StreamType]
    STREAM_TYPE_VIDEO: StreamMetaHeader.StreamType
    STREAM_TYPE_AUDIO: StreamMetaHeader.StreamType
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_TYPE_FIELD_NUMBER: _ClassVar[int]
    STREAM_NAME_FIELD_NUMBER: _ClassVar[int]
    stream_id: int
    stream_type: StreamMetaHeader.StreamType
    stream_name: str
    def __init__(self, stream_id: _Optional[int] = ..., stream_type: _Optional[_Union[StreamMetaHeader.StreamType, str]] = ..., stream_name: _Optional[str] = ...) -> None: ...

class FrameMetaHeader(_message.Message):
    __slots__ = ("frame_seq_num", "frame_timestamp", "stream_id", "check_code_enable", "check_code_type", "check_code")
    class CheckCodeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CHECK_CODE_TYPE_NONE: _ClassVar[FrameMetaHeader.CheckCodeType]
        CHECK_CODE_TYPE_CRC32: _ClassVar[FrameMetaHeader.CheckCodeType]
    CHECK_CODE_TYPE_NONE: FrameMetaHeader.CheckCodeType
    CHECK_CODE_TYPE_CRC32: FrameMetaHeader.CheckCodeType
    FRAME_SEQ_NUM_FIELD_NUMBER: _ClassVar[int]
    FRAME_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    CHECK_CODE_ENABLE_FIELD_NUMBER: _ClassVar[int]
    CHECK_CODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHECK_CODE_FIELD_NUMBER: _ClassVar[int]
    frame_seq_num: int
    frame_timestamp: int
    stream_id: int
    check_code_enable: bool
    check_code_type: FrameMetaHeader.CheckCodeType
    check_code: int
    def __init__(self, frame_seq_num: _Optional[int] = ..., frame_timestamp: _Optional[int] = ..., stream_id: _Optional[int] = ..., check_code_enable: _Optional[bool] = ..., check_code_type: _Optional[_Union[FrameMetaHeader.CheckCodeType, str]] = ..., check_code: _Optional[int] = ...) -> None: ...

class MetaHeaderOfDevice(_message.Message):
    __slots__ = ("device_id", "device_type", "device_sub_type", "device_name", "device_frequency", "device_timestamp")
    class DeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEVICE_TYPE_UNDEFINED: _ClassVar[MetaHeaderOfDevice.DeviceType]
        DEVICE_TYPE_PHYSICAL: _ClassVar[MetaHeaderOfDevice.DeviceType]
        DEVICE_TYPE_VIRTUAL: _ClassVar[MetaHeaderOfDevice.DeviceType]
    DEVICE_TYPE_UNDEFINED: MetaHeaderOfDevice.DeviceType
    DEVICE_TYPE_PHYSICAL: MetaHeaderOfDevice.DeviceType
    DEVICE_TYPE_VIRTUAL: MetaHeaderOfDevice.DeviceType
    class DeviceSubType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEVICE_SUB_TYPE_UNDEFINED: _ClassVar[MetaHeaderOfDevice.DeviceSubType]
        DEVICE_SUB_TYPE_CAMERA_BODY: _ClassVar[MetaHeaderOfDevice.DeviceSubType]
        DEVICE_SUB_TYPE_DRONE: _ClassVar[MetaHeaderOfDevice.DeviceSubType]
        DEVICE_SUB_TYPE_GIMBAL: _ClassVar[MetaHeaderOfDevice.DeviceSubType]
        DEVICE_SUB_TYPE_GIMBAL_ZAXIS: _ClassVar[MetaHeaderOfDevice.DeviceSubType]
        DEVICE_SUB_TYPE_RECORDER: _ClassVar[MetaHeaderOfDevice.DeviceSubType]
        DEVICE_SUB_TYPE_LASER_RANGING: _ClassVar[MetaHeaderOfDevice.DeviceSubType]
    DEVICE_SUB_TYPE_UNDEFINED: MetaHeaderOfDevice.DeviceSubType
    DEVICE_SUB_TYPE_CAMERA_BODY: MetaHeaderOfDevice.DeviceSubType
    DEVICE_SUB_TYPE_DRONE: MetaHeaderOfDevice.DeviceSubType
    DEVICE_SUB_TYPE_GIMBAL: MetaHeaderOfDevice.DeviceSubType
    DEVICE_SUB_TYPE_GIMBAL_ZAXIS: MetaHeaderOfDevice.DeviceSubType
    DEVICE_SUB_TYPE_RECORDER: MetaHeaderOfDevice.DeviceSubType
    DEVICE_SUB_TYPE_LASER_RANGING: MetaHeaderOfDevice.DeviceSubType
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    device_id: int
    device_type: MetaHeaderOfDevice.DeviceType
    device_sub_type: MetaHeaderOfDevice.DeviceSubType
    device_name: str
    device_frequency: float
    device_timestamp: int
    def __init__(self, device_id: _Optional[int] = ..., device_type: _Optional[_Union[MetaHeaderOfDevice.DeviceType, str]] = ..., device_sub_type: _Optional[_Union[MetaHeaderOfDevice.DeviceSubType, str]] = ..., device_name: _Optional[str] = ..., device_frequency: _Optional[float] = ..., device_timestamp: _Optional[int] = ...) -> None: ...

class MetaHeaderOfSubDevice(_message.Message):
    __slots__ = ("sub_dev_id", "sub_device_type", "sub_device_sub_type", "sub_device_name", "sub_device_frequency", "sub_device_timestamp")
    class SubDeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUB_DEVICE_TYPE_UNDEFINED: _ClassVar[MetaHeaderOfSubDevice.SubDeviceType]
        SUB_DEVICE_TYPE_PHYSICAL: _ClassVar[MetaHeaderOfSubDevice.SubDeviceType]
        SUB_DEVICE_TYPE_VIRTUAL: _ClassVar[MetaHeaderOfSubDevice.SubDeviceType]
    SUB_DEVICE_TYPE_UNDEFINED: MetaHeaderOfSubDevice.SubDeviceType
    SUB_DEVICE_TYPE_PHYSICAL: MetaHeaderOfSubDevice.SubDeviceType
    SUB_DEVICE_TYPE_VIRTUAL: MetaHeaderOfSubDevice.SubDeviceType
    class SubDeviceSubType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUB_DEVICE_SUB_TYPE_UNDEFINED: _ClassVar[MetaHeaderOfSubDevice.SubDeviceSubType]
        SUB_DEVICE_SUB_TYPE_LENS: _ClassVar[MetaHeaderOfSubDevice.SubDeviceSubType]
    SUB_DEVICE_SUB_TYPE_UNDEFINED: MetaHeaderOfSubDevice.SubDeviceSubType
    SUB_DEVICE_SUB_TYPE_LENS: MetaHeaderOfSubDevice.SubDeviceSubType
    SUB_DEV_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SUB_DEVICE_SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    SUB_DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    SUB_DEVICE_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    SUB_DEVICE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    sub_dev_id: int
    sub_device_type: MetaHeaderOfSubDevice.SubDeviceType
    sub_device_sub_type: MetaHeaderOfSubDevice.SubDeviceSubType
    sub_device_name: str
    sub_device_frequency: float
    sub_device_timestamp: int
    def __init__(self, sub_dev_id: _Optional[int] = ..., sub_device_type: _Optional[_Union[MetaHeaderOfSubDevice.SubDeviceType, str]] = ..., sub_device_sub_type: _Optional[_Union[MetaHeaderOfSubDevice.SubDeviceSubType, str]] = ..., sub_device_name: _Optional[str] = ..., sub_device_frequency: _Optional[float] = ..., sub_device_timestamp: _Optional[int] = ...) -> None: ...

class VideoStreamMeta(_message.Message):
    __slots__ = ("resolution_width", "resolution_height", "framerate", "is_bit_depth_valid", "bit_depth", "bit_format", "video_stream_type", "video_codec_type")
    class BitFormatType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BIT_FORMAT_TYPE_UNKNOWN: _ClassVar[VideoStreamMeta.BitFormatType]
        BIT_FORMAT_TYPE_RAW: _ClassVar[VideoStreamMeta.BitFormatType]
        BIT_FORMAT_TYPE_RGB: _ClassVar[VideoStreamMeta.BitFormatType]
        BIT_FORMAT_TYPE_RGBA: _ClassVar[VideoStreamMeta.BitFormatType]
        BIT_FORMAT_TYPE_YUV420: _ClassVar[VideoStreamMeta.BitFormatType]
        BIT_FORMAT_TYPE_YUV422: _ClassVar[VideoStreamMeta.BitFormatType]
        BIT_FORMAT_TYPE_YUV444: _ClassVar[VideoStreamMeta.BitFormatType]
    BIT_FORMAT_TYPE_UNKNOWN: VideoStreamMeta.BitFormatType
    BIT_FORMAT_TYPE_RAW: VideoStreamMeta.BitFormatType
    BIT_FORMAT_TYPE_RGB: VideoStreamMeta.BitFormatType
    BIT_FORMAT_TYPE_RGBA: VideoStreamMeta.BitFormatType
    BIT_FORMAT_TYPE_YUV420: VideoStreamMeta.BitFormatType
    BIT_FORMAT_TYPE_YUV422: VideoStreamMeta.BitFormatType
    BIT_FORMAT_TYPE_YUV444: VideoStreamMeta.BitFormatType
    class VideoStreamType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VIDEO_STREAM_TYPE_NORMAL: _ClassVar[VideoStreamMeta.VideoStreamType]
        VIDEO_STREAM_TYPE_DELAY: _ClassVar[VideoStreamMeta.VideoStreamType]
        VIDEO_STREAM_TYPE_SLOW_MOTION: _ClassVar[VideoStreamMeta.VideoStreamType]
        VIDEO_STREAM_TYPE_QUICK_MOVIE: _ClassVar[VideoStreamMeta.VideoStreamType]
        VIDEO_STREAM_TYPE_TIMELAPSE: _ClassVar[VideoStreamMeta.VideoStreamType]
        VIDEO_STREAM_TYPE_MOTIONLAPSE: _ClassVar[VideoStreamMeta.VideoStreamType]
        VIDEO_STREAM_TYPE_HYPERLAPSE: _ClassVar[VideoStreamMeta.VideoStreamType]
        VIDEO_STREAM_TYPE_HDR: _ClassVar[VideoStreamMeta.VideoStreamType]
        VIDEO_STREAM_TYPE_LOOP_RECORD: _ClassVar[VideoStreamMeta.VideoStreamType]
        VIDEO_STREAM_TYPE_LOW_LIGHT: _ClassVar[VideoStreamMeta.VideoStreamType]
    VIDEO_STREAM_TYPE_NORMAL: VideoStreamMeta.VideoStreamType
    VIDEO_STREAM_TYPE_DELAY: VideoStreamMeta.VideoStreamType
    VIDEO_STREAM_TYPE_SLOW_MOTION: VideoStreamMeta.VideoStreamType
    VIDEO_STREAM_TYPE_QUICK_MOVIE: VideoStreamMeta.VideoStreamType
    VIDEO_STREAM_TYPE_TIMELAPSE: VideoStreamMeta.VideoStreamType
    VIDEO_STREAM_TYPE_MOTIONLAPSE: VideoStreamMeta.VideoStreamType
    VIDEO_STREAM_TYPE_HYPERLAPSE: VideoStreamMeta.VideoStreamType
    VIDEO_STREAM_TYPE_HDR: VideoStreamMeta.VideoStreamType
    VIDEO_STREAM_TYPE_LOOP_RECORD: VideoStreamMeta.VideoStreamType
    VIDEO_STREAM_TYPE_LOW_LIGHT: VideoStreamMeta.VideoStreamType
    class VideoCodecType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VIDEO_CODEC_TYPE_H264: _ClassVar[VideoStreamMeta.VideoCodecType]
        VIDEO_CODEC_TYPE_H265: _ClassVar[VideoStreamMeta.VideoCodecType]
        VIDEO_CODEC_TYPE_PRORES: _ClassVar[VideoStreamMeta.VideoCodecType]
        VIDEO_CODEC_TYPE_PRORESRAW: _ClassVar[VideoStreamMeta.VideoCodecType]
        VIDEO_CODEC_TYPE_JPEG: _ClassVar[VideoStreamMeta.VideoCodecType]
        VIDEO_CODEC_TYPE_JPEG2000: _ClassVar[VideoStreamMeta.VideoCodecType]
        VIDEO_CODEC_TYPE_JPEG_LOSSLESS: _ClassVar[VideoStreamMeta.VideoCodecType]
    VIDEO_CODEC_TYPE_H264: VideoStreamMeta.VideoCodecType
    VIDEO_CODEC_TYPE_H265: VideoStreamMeta.VideoCodecType
    VIDEO_CODEC_TYPE_PRORES: VideoStreamMeta.VideoCodecType
    VIDEO_CODEC_TYPE_PRORESRAW: VideoStreamMeta.VideoCodecType
    VIDEO_CODEC_TYPE_JPEG: VideoStreamMeta.VideoCodecType
    VIDEO_CODEC_TYPE_JPEG2000: VideoStreamMeta.VideoCodecType
    VIDEO_CODEC_TYPE_JPEG_LOSSLESS: VideoStreamMeta.VideoCodecType
    RESOLUTION_WIDTH_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    FRAMERATE_FIELD_NUMBER: _ClassVar[int]
    IS_BIT_DEPTH_VALID_FIELD_NUMBER: _ClassVar[int]
    BIT_DEPTH_FIELD_NUMBER: _ClassVar[int]
    BIT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_STREAM_TYPE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_CODEC_TYPE_FIELD_NUMBER: _ClassVar[int]
    resolution_width: int
    resolution_height: int
    framerate: float
    is_bit_depth_valid: bool
    bit_depth: int
    bit_format: VideoStreamMeta.BitFormatType
    video_stream_type: VideoStreamMeta.VideoStreamType
    video_codec_type: VideoStreamMeta.VideoCodecType
    def __init__(self, resolution_width: _Optional[int] = ..., resolution_height: _Optional[int] = ..., framerate: _Optional[float] = ..., is_bit_depth_valid: _Optional[bool] = ..., bit_depth: _Optional[int] = ..., bit_format: _Optional[_Union[VideoStreamMeta.BitFormatType, str]] = ..., video_stream_type: _Optional[_Union[VideoStreamMeta.VideoStreamType, str]] = ..., video_codec_type: _Optional[_Union[VideoStreamMeta.VideoCodecType, str]] = ...) -> None: ...

class ImageProcessingQuality(_message.Message):
    __slots__ = ("image_processing_quality",)
    class ImageProcessingQualityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IMAGE_PROCESSING_QUALITY_TYPE_NORMAL: _ClassVar[ImageProcessingQuality.ImageProcessingQualityType]
        IMAGE_PROCESSING_QUALITY_TYPE_HIGH: _ClassVar[ImageProcessingQuality.ImageProcessingQualityType]
    IMAGE_PROCESSING_QUALITY_TYPE_NORMAL: ImageProcessingQuality.ImageProcessingQualityType
    IMAGE_PROCESSING_QUALITY_TYPE_HIGH: ImageProcessingQuality.ImageProcessingQualityType
    IMAGE_PROCESSING_QUALITY_FIELD_NUMBER: _ClassVar[int]
    image_processing_quality: ImageProcessingQuality.ImageProcessingQualityType
    def __init__(self, image_processing_quality: _Optional[_Union[ImageProcessingQuality.ImageProcessingQualityType, str]] = ...) -> None: ...

class ProresCodecQuality(_message.Message):
    __slots__ = ("prores_codec_quality",)
    class ProresCodecQualityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRORES_CODEC_QUALITY_TYPE_UNDEFINED: _ClassVar[ProresCodecQuality.ProresCodecQualityType]
        PRORES_CODEC_QUALITY_TYPE_PROXY: _ClassVar[ProresCodecQuality.ProresCodecQualityType]
        PRORES_CODEC_QUALITY_TYPE_LT: _ClassVar[ProresCodecQuality.ProresCodecQualityType]
        PRORES_CODEC_QUALITY_TYPE_SD: _ClassVar[ProresCodecQuality.ProresCodecQualityType]
        PRORES_CODEC_QUALITY_TYPE_HQ: _ClassVar[ProresCodecQuality.ProresCodecQualityType]
        PRORES_CODEC_QUALITY_TYPE_XQ: _ClassVar[ProresCodecQuality.ProresCodecQualityType]
    PRORES_CODEC_QUALITY_TYPE_UNDEFINED: ProresCodecQuality.ProresCodecQualityType
    PRORES_CODEC_QUALITY_TYPE_PROXY: ProresCodecQuality.ProresCodecQualityType
    PRORES_CODEC_QUALITY_TYPE_LT: ProresCodecQuality.ProresCodecQualityType
    PRORES_CODEC_QUALITY_TYPE_SD: ProresCodecQuality.ProresCodecQualityType
    PRORES_CODEC_QUALITY_TYPE_HQ: ProresCodecQuality.ProresCodecQualityType
    PRORES_CODEC_QUALITY_TYPE_XQ: ProresCodecQuality.ProresCodecQualityType
    PRORES_CODEC_QUALITY_FIELD_NUMBER: _ClassVar[int]
    prores_codec_quality: ProresCodecQuality.ProresCodecQualityType
    def __init__(self, prores_codec_quality: _Optional[_Union[ProresCodecQuality.ProresCodecQualityType, str]] = ...) -> None: ...

class ClipStreamsMeta(_message.Message):
    __slots__ = ("video_stream_num", "audio_stream_num")
    VIDEO_STREAM_NUM_FIELD_NUMBER: _ClassVar[int]
    AUDIO_STREAM_NUM_FIELD_NUMBER: _ClassVar[int]
    video_stream_num: int
    audio_stream_num: int
    def __init__(self, video_stream_num: _Optional[int] = ..., audio_stream_num: _Optional[int] = ...) -> None: ...

class DeviceSN(_message.Message):
    __slots__ = ("device_sn",)
    DEVICE_SN_FIELD_NUMBER: _ClassVar[int]
    device_sn: str
    def __init__(self, device_sn: _Optional[str] = ...) -> None: ...

class ENdSerialNumber(_message.Message):
    __slots__ = ("eND_sn",)
    END_SN_FIELD_NUMBER: _ClassVar[int]
    eND_sn: str
    def __init__(self, eND_sn: _Optional[str] = ...) -> None: ...

class DeviceVersion(_message.Message):
    __slots__ = ("device_hw_version", "device_sw_version")
    DEVICE_HW_VERSION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_SW_VERSION_FIELD_NUMBER: _ClassVar[int]
    device_hw_version: str
    device_sw_version: str
    def __init__(self, device_hw_version: _Optional[str] = ..., device_sw_version: _Optional[str] = ...) -> None: ...

class CinemaProductionInfo(_message.Message):
    __slots__ = ("production", "production_company", "director", "cinematographer", "cinema_operator", "location", "scene", "take")
    PRODUCTION_FIELD_NUMBER: _ClassVar[int]
    PRODUCTION_COMPANY_FIELD_NUMBER: _ClassVar[int]
    DIRECTOR_FIELD_NUMBER: _ClassVar[int]
    CINEMATOGRAPHER_FIELD_NUMBER: _ClassVar[int]
    CINEMA_OPERATOR_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    SCENE_FIELD_NUMBER: _ClassVar[int]
    TAKE_FIELD_NUMBER: _ClassVar[int]
    production: str
    production_company: str
    director: str
    cinematographer: str
    cinema_operator: str
    location: str
    scene: int
    take: int
    def __init__(self, production: _Optional[str] = ..., production_company: _Optional[str] = ..., director: _Optional[str] = ..., cinematographer: _Optional[str] = ..., cinema_operator: _Optional[str] = ..., location: _Optional[str] = ..., scene: _Optional[int] = ..., take: _Optional[int] = ...) -> None: ...

class CinemaClipNaming(_message.Message):
    __slots__ = ("camera_index", "reel_name", "camera_id", "clip_name", "spin_name")
    CAMERA_INDEX_FIELD_NUMBER: _ClassVar[int]
    REEL_NAME_FIELD_NUMBER: _ClassVar[int]
    CAMERA_ID_FIELD_NUMBER: _ClassVar[int]
    CLIP_NAME_FIELD_NUMBER: _ClassVar[int]
    SPIN_NAME_FIELD_NUMBER: _ClassVar[int]
    camera_index: str
    reel_name: str
    camera_id: str
    clip_name: str
    spin_name: str
    def __init__(self, camera_index: _Optional[str] = ..., reel_name: _Optional[str] = ..., camera_id: _Optional[str] = ..., clip_name: _Optional[str] = ..., spin_name: _Optional[str] = ...) -> None: ...

class ProjectFps(_message.Message):
    __slots__ = ("project_fps",)
    PROJECT_FPS_FIELD_NUMBER: _ClassVar[int]
    project_fps: float
    def __init__(self, project_fps: _Optional[float] = ...) -> None: ...

class ImageSizeType(_message.Message):
    __slots__ = ("image_size_type",)
    class ImageSizeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IMAGE_SIZE_TYPE_DEFAULT: _ClassVar[ImageSizeType.ImageSizeType]
        IMAGE_SIZE_TYPE_OPEN_GATE: _ClassVar[ImageSizeType.ImageSizeType]
        IMAGE_SIZE_TYPE_FULL_FRAME: _ClassVar[ImageSizeType.ImageSizeType]
        IMAGE_SIZE_TYPE_S35: _ClassVar[ImageSizeType.ImageSizeType]
        IMAGE_SIZE_TYPE_43: _ClassVar[ImageSizeType.ImageSizeType]
    IMAGE_SIZE_TYPE_DEFAULT: ImageSizeType.ImageSizeType
    IMAGE_SIZE_TYPE_OPEN_GATE: ImageSizeType.ImageSizeType
    IMAGE_SIZE_TYPE_FULL_FRAME: ImageSizeType.ImageSizeType
    IMAGE_SIZE_TYPE_S35: ImageSizeType.ImageSizeType
    IMAGE_SIZE_TYPE_43: ImageSizeType.ImageSizeType
    IMAGE_SIZE_TYPE_FIELD_NUMBER: _ClassVar[int]
    image_size_type: ImageSizeType.ImageSizeType
    def __init__(self, image_size_type: _Optional[_Union[ImageSizeType.ImageSizeType, str]] = ...) -> None: ...

class FOVType(_message.Message):
    __slots__ = ("fov_type",)
    class FOVType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FOV_TYPE_DEFAULT: _ClassVar[FOVType.FOVType]
        FOV_TYPE_NORMAL: _ClassVar[FOVType.FOVType]
        FOV_TYPE_NARROW: _ClassVar[FOVType.FOVType]
        FOV_TYPE_WIDE: _ClassVar[FOVType.FOVType]
        FOV_TYPE_SNARROW: _ClassVar[FOVType.FOVType]
        FOV_TYPE_NATURAL_WIDE: _ClassVar[FOVType.FOVType]
        FOV_TYPE_EXTREME_WIDE: _ClassVar[FOVType.FOVType]
        FOV_TYPE_FLAT: _ClassVar[FOVType.FOVType]
    FOV_TYPE_DEFAULT: FOVType.FOVType
    FOV_TYPE_NORMAL: FOVType.FOVType
    FOV_TYPE_NARROW: FOVType.FOVType
    FOV_TYPE_WIDE: FOVType.FOVType
    FOV_TYPE_SNARROW: FOVType.FOVType
    FOV_TYPE_NATURAL_WIDE: FOVType.FOVType
    FOV_TYPE_EXTREME_WIDE: FOVType.FOVType
    FOV_TYPE_FLAT: FOVType.FOVType
    FOV_TYPE_FIELD_NUMBER: _ClassVar[int]
    fov_type: FOVType.FOVType
    def __init__(self, fov_type: _Optional[_Union[FOVType.FOVType, str]] = ...) -> None: ...

class ImageArea(_message.Message):
    __slots__ = ("active_image_area", "full_image_area")
    ACTIVE_IMAGE_AREA_FIELD_NUMBER: _ClassVar[int]
    FULL_IMAGE_AREA_FIELD_NUMBER: _ClassVar[int]
    active_image_area: _containers.RepeatedScalarFieldContainer[int]
    full_image_area: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, active_image_area: _Optional[_Iterable[int]] = ..., full_image_area: _Optional[_Iterable[int]] = ...) -> None: ...

class CFAPattern(_message.Message):
    __slots__ = ("cfa_pattern",)
    class CFAPatternType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CFA_PATTERN_TYPE_RGGB: _ClassVar[CFAPattern.CFAPatternType]
        CFA_PATTERN_TYPE_GRBG: _ClassVar[CFAPattern.CFAPatternType]
        CFA_PATTERN_TYPE_BGGR: _ClassVar[CFAPattern.CFAPatternType]
        CFA_PATTERN_TYPE_GBRG: _ClassVar[CFAPattern.CFAPatternType]
    CFA_PATTERN_TYPE_RGGB: CFAPattern.CFAPatternType
    CFA_PATTERN_TYPE_GRBG: CFAPattern.CFAPatternType
    CFA_PATTERN_TYPE_BGGR: CFAPattern.CFAPatternType
    CFA_PATTERN_TYPE_GBRG: CFAPattern.CFAPatternType
    CFA_PATTERN_FIELD_NUMBER: _ClassVar[int]
    cfa_pattern: CFAPattern.CFAPatternType
    def __init__(self, cfa_pattern: _Optional[_Union[CFAPattern.CFAPatternType, str]] = ...) -> None: ...

class BayerGreenSplit(_message.Message):
    __slots__ = ("bayer_green_split",)
    BAYER_GREEN_SPLIT_FIELD_NUMBER: _ClassVar[int]
    bayer_green_split: float
    def __init__(self, bayer_green_split: _Optional[float] = ...) -> None: ...

class ColorSpace(_message.Message):
    __slots__ = ("color_space",)
    class ColorSpaceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COLOR_SPACE_TYPE_DEFAULT: _ClassVar[ColorSpace.ColorSpaceType]
        COLOR_SPACE_TYPE_DGAMUT: _ClassVar[ColorSpace.ColorSpaceType]
        COLOR_SPACE_TYPE_REC709: _ClassVar[ColorSpace.ColorSpaceType]
        COLOR_SPACE_TYPE_BT2020: _ClassVar[ColorSpace.ColorSpaceType]
        COLOR_SPACE_TYPE_BT2100: _ClassVar[ColorSpace.ColorSpaceType]
    COLOR_SPACE_TYPE_DEFAULT: ColorSpace.ColorSpaceType
    COLOR_SPACE_TYPE_DGAMUT: ColorSpace.ColorSpaceType
    COLOR_SPACE_TYPE_REC709: ColorSpace.ColorSpaceType
    COLOR_SPACE_TYPE_BT2020: ColorSpace.ColorSpaceType
    COLOR_SPACE_TYPE_BT2100: ColorSpace.ColorSpaceType
    COLOR_SPACE_FIELD_NUMBER: _ClassVar[int]
    color_space: ColorSpace.ColorSpaceType
    def __init__(self, color_space: _Optional[_Union[ColorSpace.ColorSpaceType, str]] = ...) -> None: ...

class ColorMatrixBox(_message.Message):
    __slots__ = ("color_matrix",)
    COLOR_MATRIX_FIELD_NUMBER: _ClassVar[int]
    color_matrix: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, color_matrix: _Optional[_Iterable[float]] = ...) -> None: ...

class ColorMatrix(_message.Message):
    __slots__ = ("color_matrix_box",)
    COLOR_MATRIX_BOX_FIELD_NUMBER: _ClassVar[int]
    color_matrix_box: _containers.RepeatedCompositeFieldContainer[ColorMatrixBox]
    def __init__(self, color_matrix_box: _Optional[_Iterable[_Union[ColorMatrixBox, _Mapping]]] = ...) -> None: ...

class CalibrationIlluminant(_message.Message):
    __slots__ = ("calibration_illuminant",)
    CALIBRATION_ILLUMINANT_FIELD_NUMBER: _ClassVar[int]
    calibration_illuminant: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, calibration_illuminant: _Optional[_Iterable[int]] = ...) -> None: ...

class NoiseReductionApplied(_message.Message):
    __slots__ = ("noise_reduction_applied",)
    NOISE_REDUCTION_APPLIED_FIELD_NUMBER: _ClassVar[int]
    noise_reduction_applied: float
    def __init__(self, noise_reduction_applied: _Optional[float] = ...) -> None: ...

class Saturation(_message.Message):
    __slots__ = ("saturation",)
    SATURATION_FIELD_NUMBER: _ClassVar[int]
    saturation: float
    def __init__(self, saturation: _Optional[float] = ...) -> None: ...

class Sharpness(_message.Message):
    __slots__ = ("sharpness",)
    SHARPNESS_FIELD_NUMBER: _ClassVar[int]
    sharpness: float
    def __init__(self, sharpness: _Optional[float] = ...) -> None: ...

class PixelAspectRatio(_message.Message):
    __slots__ = ("pixel_aspect_ratio",)
    PIXEL_ASPECT_RATIO_FIELD_NUMBER: _ClassVar[int]
    pixel_aspect_ratio: float
    def __init__(self, pixel_aspect_ratio: _Optional[float] = ...) -> None: ...

class LookUpTable3DFile(_message.Message):
    __slots__ = ("lut3d_file_name", "lut3d_file_data")
    LUT3D_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    LUT3D_FILE_DATA_FIELD_NUMBER: _ClassVar[int]
    lut3d_file_name: str
    lut3d_file_data: bytes
    def __init__(self, lut3d_file_name: _Optional[str] = ..., lut3d_file_data: _Optional[bytes] = ...) -> None: ...

class ColorProcessingVersion(_message.Message):
    __slots__ = ("color_processing_version",)
    COLOR_PROCESSING_VERSION_FIELD_NUMBER: _ClassVar[int]
    color_processing_version: str
    def __init__(self, color_processing_version: _Optional[str] = ...) -> None: ...

class OpBox(_message.Message):
    __slots__ = ("type", "data")
    class OpType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OP_TYPE_WARP_RECTILINEAR: _ClassVar[OpBox.OpType]
        OP_TYPE_WARP_FISHEYE: _ClassVar[OpBox.OpType]
        OP_TYPE_FIX_VIGNETTE_RADIAL: _ClassVar[OpBox.OpType]
        OP_TYPE_TRIM_BOUNDS: _ClassVar[OpBox.OpType]
        OP_TYPE_MAP_TABLE: _ClassVar[OpBox.OpType]
        OP_TYPE_MAP_POLYNOMIAL: _ClassVar[OpBox.OpType]
        OP_TYPE_GAIN_MAP: _ClassVar[OpBox.OpType]
        OP_TYPE_DELTA_PER_ROW: _ClassVar[OpBox.OpType]
        OP_TYPE_DELTA_PER_COLUMN: _ClassVar[OpBox.OpType]
        OP_TYPE_SCALE_PER_ROW: _ClassVar[OpBox.OpType]
        OP_TYPE_SCALE_PER_COLUMN: _ClassVar[OpBox.OpType]
    OP_TYPE_WARP_RECTILINEAR: OpBox.OpType
    OP_TYPE_WARP_FISHEYE: OpBox.OpType
    OP_TYPE_FIX_VIGNETTE_RADIAL: OpBox.OpType
    OP_TYPE_TRIM_BOUNDS: OpBox.OpType
    OP_TYPE_MAP_TABLE: OpBox.OpType
    OP_TYPE_MAP_POLYNOMIAL: OpBox.OpType
    OP_TYPE_GAIN_MAP: OpBox.OpType
    OP_TYPE_DELTA_PER_ROW: OpBox.OpType
    OP_TYPE_DELTA_PER_COLUMN: OpBox.OpType
    OP_TYPE_SCALE_PER_ROW: OpBox.OpType
    OP_TYPE_SCALE_PER_COLUMN: OpBox.OpType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    type: OpBox.OpType
    data: bytes
    def __init__(self, type: _Optional[_Union[OpBox.OpType, str]] = ..., data: _Optional[bytes] = ...) -> None: ...

class OpGroup(_message.Message):
    __slots__ = ("op_group1", "op_group2", "op_group3", "op_group4")
    OP_GROUP1_FIELD_NUMBER: _ClassVar[int]
    OP_GROUP2_FIELD_NUMBER: _ClassVar[int]
    OP_GROUP3_FIELD_NUMBER: _ClassVar[int]
    OP_GROUP4_FIELD_NUMBER: _ClassVar[int]
    op_group1: _containers.RepeatedCompositeFieldContainer[OpBox]
    op_group2: _containers.RepeatedCompositeFieldContainer[OpBox]
    op_group3: _containers.RepeatedCompositeFieldContainer[OpBox]
    op_group4: _containers.RepeatedCompositeFieldContainer[OpBox]
    def __init__(self, op_group1: _Optional[_Iterable[_Union[OpBox, _Mapping]]] = ..., op_group2: _Optional[_Iterable[_Union[OpBox, _Mapping]]] = ..., op_group3: _Optional[_Iterable[_Union[OpBox, _Mapping]]] = ..., op_group4: _Optional[_Iterable[_Union[OpBox, _Mapping]]] = ...) -> None: ...

class NoiseProfile(_message.Message):
    __slots__ = ("noise_profile",)
    NOISE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    noise_profile: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, noise_profile: _Optional[_Iterable[float]] = ...) -> None: ...

class ImageDataSize(_message.Message):
    __slots__ = ("image_data_size",)
    IMAGE_DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
    image_data_size: int
    def __init__(self, image_data_size: _Optional[int] = ...) -> None: ...

class ExposureIndex(_message.Message):
    __slots__ = ("exposure_index",)
    EXPOSURE_INDEX_FIELD_NUMBER: _ClassVar[int]
    exposure_index: float
    def __init__(self, exposure_index: _Optional[float] = ...) -> None: ...

class ISO(_message.Message):
    __slots__ = ("iso",)
    ISO_FIELD_NUMBER: _ClassVar[int]
    iso: float
    def __init__(self, iso: _Optional[float] = ...) -> None: ...

class ExposureTime(_message.Message):
    __slots__ = ("exposure_time",)
    EXPOSURE_TIME_FIELD_NUMBER: _ClassVar[int]
    exposure_time: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, exposure_time: _Optional[_Iterable[int]] = ...) -> None: ...

class FNumber(_message.Message):
    __slots__ = ("f_number",)
    F_NUMBER_FIELD_NUMBER: _ClassVar[int]
    f_number: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, f_number: _Optional[_Iterable[int]] = ...) -> None: ...

class ApertureValue(_message.Message):
    __slots__ = ("aperture_value",)
    APERTURE_VALUE_FIELD_NUMBER: _ClassVar[int]
    aperture_value: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, aperture_value: _Optional[_Iterable[int]] = ...) -> None: ...

class ShutterAngle(_message.Message):
    __slots__ = ("shutter_angle",)
    SHUTTER_ANGLE_FIELD_NUMBER: _ClassVar[int]
    shutter_angle: float
    def __init__(self, shutter_angle: _Optional[float] = ...) -> None: ...

class FocusDistance(_message.Message):
    __slots__ = ("focus_unit", "focus_distance")
    class FocusUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FOCUS_UNIT_1000_INCH: _ClassVar[FocusDistance.FocusUnit]
        FOCUS_UNIT_MILLIMETRE: _ClassVar[FocusDistance.FocusUnit]
    FOCUS_UNIT_1000_INCH: FocusDistance.FocusUnit
    FOCUS_UNIT_MILLIMETRE: FocusDistance.FocusUnit
    FOCUS_UNIT_FIELD_NUMBER: _ClassVar[int]
    FOCUS_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    focus_unit: FocusDistance.FocusUnit
    focus_distance: int
    def __init__(self, focus_unit: _Optional[_Union[FocusDistance.FocusUnit, str]] = ..., focus_distance: _Optional[int] = ...) -> None: ...

class FocalLength(_message.Message):
    __slots__ = ("focal_length",)
    FOCAL_LENGTH_FIELD_NUMBER: _ClassVar[int]
    focal_length: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, focal_length: _Optional[_Iterable[int]] = ...) -> None: ...

class SensorZoomRatio(_message.Message):
    __slots__ = ("sensor_zoom_ratio",)
    SENSOR_ZOOM_RATIO_FIELD_NUMBER: _ClassVar[int]
    sensor_zoom_ratio: float
    def __init__(self, sensor_zoom_ratio: _Optional[float] = ...) -> None: ...

class OpticalZoomRatio(_message.Message):
    __slots__ = ("optical_zoom_ratio",)
    OPTICAL_ZOOM_RATIO_FIELD_NUMBER: _ClassVar[int]
    optical_zoom_ratio: float
    def __init__(self, optical_zoom_ratio: _Optional[float] = ...) -> None: ...

class DigitalZoomRatio(_message.Message):
    __slots__ = ("digital_zoom_ratio",)
    DIGITAL_ZOOM_RATIO_FIELD_NUMBER: _ClassVar[int]
    digital_zoom_ratio: float
    def __init__(self, digital_zoom_ratio: _Optional[float] = ...) -> None: ...

class WhiteBalanceCCT(_message.Message):
    __slots__ = ("white_balance_cct",)
    WHITE_BALANCE_CCT_FIELD_NUMBER: _ClassVar[int]
    white_balance_cct: int
    def __init__(self, white_balance_cct: _Optional[int] = ...) -> None: ...

class WhiteBalanceTint(_message.Message):
    __slots__ = ("white_balance_tint",)
    WHITE_BALANCE_TINT_FIELD_NUMBER: _ClassVar[int]
    white_balance_tint: float
    def __init__(self, white_balance_tint: _Optional[float] = ...) -> None: ...

class AsShotNeutral(_message.Message):
    __slots__ = ("as_shot_neutral",)
    AS_SHOT_NEUTRAL_FIELD_NUMBER: _ClassVar[int]
    as_shot_neutral: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, as_shot_neutral: _Optional[_Iterable[float]] = ...) -> None: ...

class NDFilter(_message.Message):
    __slots__ = ("nd_filter_enable", "nd_density")
    ND_FILTER_ENABLE_FIELD_NUMBER: _ClassVar[int]
    ND_DENSITY_FIELD_NUMBER: _ClassVar[int]
    nd_filter_enable: bool
    nd_density: float
    def __init__(self, nd_filter_enable: _Optional[bool] = ..., nd_density: _Optional[float] = ...) -> None: ...

class BlackLevel(_message.Message):
    __slots__ = ("black_level",)
    BLACK_LEVEL_FIELD_NUMBER: _ClassVar[int]
    black_level: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, black_level: _Optional[_Iterable[float]] = ...) -> None: ...

class WhiteLevel(_message.Message):
    __slots__ = ("white_level",)
    WHITE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    white_level: float
    def __init__(self, white_level: _Optional[float] = ...) -> None: ...

class TimeCode(_message.Message):
    __slots__ = ("timecode_run_mode", "timecode", "sub_second_frame_count")
    class TimecodeRunMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TIMECODE_RUN_MODE_FREE: _ClassVar[TimeCode.TimecodeRunMode]
        TIMECODE_RUN_MODE_RECORD: _ClassVar[TimeCode.TimecodeRunMode]
    TIMECODE_RUN_MODE_FREE: TimeCode.TimecodeRunMode
    TIMECODE_RUN_MODE_RECORD: TimeCode.TimecodeRunMode
    TIMECODE_RUN_MODE_FIELD_NUMBER: _ClassVar[int]
    TIMECODE_FIELD_NUMBER: _ClassVar[int]
    SUB_SECOND_FRAME_COUNT_FIELD_NUMBER: _ClassVar[int]
    timecode_run_mode: TimeCode.TimecodeRunMode
    timecode: str
    sub_second_frame_count: int
    def __init__(self, timecode_run_mode: _Optional[_Union[TimeCode.TimecodeRunMode, str]] = ..., timecode: _Optional[str] = ..., sub_second_frame_count: _Optional[int] = ...) -> None: ...

class Orientation(_message.Message):
    __slots__ = ("orientation",)
    class OrientationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ORIENTATION_NO_REVERSE: _ClassVar[Orientation.OrientationType]
        ORIENTATION_H_REVERSE: _ClassVar[Orientation.OrientationType]
        ORIENTATION_V_REVERSE: _ClassVar[Orientation.OrientationType]
        ORIENTATION_HV_REVERSE: _ClassVar[Orientation.OrientationType]
        ORIENTATION_H_90: _ClassVar[Orientation.OrientationType]
        ORIENTATION_H_270: _ClassVar[Orientation.OrientationType]
    ORIENTATION_NO_REVERSE: Orientation.OrientationType
    ORIENTATION_H_REVERSE: Orientation.OrientationType
    ORIENTATION_V_REVERSE: Orientation.OrientationType
    ORIENTATION_HV_REVERSE: Orientation.OrientationType
    ORIENTATION_H_90: Orientation.OrientationType
    ORIENTATION_H_270: Orientation.OrientationType
    ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    orientation: Orientation.OrientationType
    def __init__(self, orientation: _Optional[_Union[Orientation.OrientationType, str]] = ...) -> None: ...

class ColorMode(_message.Message):
    __slots__ = ("color_mode",)
    class ColorModeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COLOR_MODE_DEFAULT: _ClassVar[ColorMode.ColorModeType]
        COLOR_MODE_D_CINELIKE: _ClassVar[ColorMode.ColorModeType]
        COLOR_MODE_D_LOG: _ClassVar[ColorMode.ColorModeType]
        COLOR_MODE_FILM_A: _ClassVar[ColorMode.ColorModeType]
        COLOR_MODE_FILM_B: _ClassVar[ColorMode.ColorModeType]
        COLOR_MODE_FILM_C: _ClassVar[ColorMode.ColorModeType]
        COLOR_MODE_FILM_D: _ClassVar[ColorMode.ColorModeType]
        COLOR_MODE_FILM_E: _ClassVar[ColorMode.ColorModeType]
        COLOR_MODE_FILM_F: _ClassVar[ColorMode.ColorModeType]
        COLOR_MODE_HLG: _ClassVar[ColorMode.ColorModeType]
        COLOR_MODE_ART: _ClassVar[ColorMode.ColorModeType]
        COLOR_MODE_BW: _ClassVar[ColorMode.ColorModeType]
        COLOR_MODE_VIVID: _ClassVar[ColorMode.ColorModeType]
        COLOR_MODE_BEACH: _ClassVar[ColorMode.ColorModeType]
        COLOR_MODE_DREAM: _ClassVar[ColorMode.ColorModeType]
        COLOR_MODE_SRGB: _ClassVar[ColorMode.ColorModeType]
        COLOR_MODE_ADOBERGB: _ClassVar[ColorMode.ColorModeType]
        COLOR_MODE_IR_CUT: _ClassVar[ColorMode.ColorModeType]
        COLOR_MODE_RACING: _ClassVar[ColorMode.ColorModeType]
        COLOR_MODE_DLOG_M: _ClassVar[ColorMode.ColorModeType]
        COLOR_MODE_LASER_FILL_LIGHT: _ClassVar[ColorMode.ColorModeType]
        COLOR_MODE_SPOT_LIGHT: _ClassVar[ColorMode.ColorModeType]
        COLOR_MODE_DLOG2: _ClassVar[ColorMode.ColorModeType]
    COLOR_MODE_DEFAULT: ColorMode.ColorModeType
    COLOR_MODE_D_CINELIKE: ColorMode.ColorModeType
    COLOR_MODE_D_LOG: ColorMode.ColorModeType
    COLOR_MODE_FILM_A: ColorMode.ColorModeType
    COLOR_MODE_FILM_B: ColorMode.ColorModeType
    COLOR_MODE_FILM_C: ColorMode.ColorModeType
    COLOR_MODE_FILM_D: ColorMode.ColorModeType
    COLOR_MODE_FILM_E: ColorMode.ColorModeType
    COLOR_MODE_FILM_F: ColorMode.ColorModeType
    COLOR_MODE_HLG: ColorMode.ColorModeType
    COLOR_MODE_ART: ColorMode.ColorModeType
    COLOR_MODE_BW: ColorMode.ColorModeType
    COLOR_MODE_VIVID: ColorMode.ColorModeType
    COLOR_MODE_BEACH: ColorMode.ColorModeType
    COLOR_MODE_DREAM: ColorMode.ColorModeType
    COLOR_MODE_SRGB: ColorMode.ColorModeType
    COLOR_MODE_ADOBERGB: ColorMode.ColorModeType
    COLOR_MODE_IR_CUT: ColorMode.ColorModeType
    COLOR_MODE_RACING: ColorMode.ColorModeType
    COLOR_MODE_DLOG_M: ColorMode.ColorModeType
    COLOR_MODE_LASER_FILL_LIGHT: ColorMode.ColorModeType
    COLOR_MODE_SPOT_LIGHT: ColorMode.ColorModeType
    COLOR_MODE_DLOG2: ColorMode.ColorModeType
    COLOR_MODE_FIELD_NUMBER: _ClassVar[int]
    color_mode: ColorMode.ColorModeType
    def __init__(self, color_mode: _Optional[_Union[ColorMode.ColorModeType, str]] = ...) -> None: ...

class ExposureIndexMode(_message.Message):
    __slots__ = ("exposure_index_mode",)
    class ExposureIndexModeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EI_MODE_OFF: _ClassVar[ExposureIndexMode.ExposureIndexModeType]
        EI_MODE_ON: _ClassVar[ExposureIndexMode.ExposureIndexModeType]
    EI_MODE_OFF: ExposureIndexMode.ExposureIndexModeType
    EI_MODE_ON: ExposureIndexMode.ExposureIndexModeType
    EXPOSURE_INDEX_MODE_FIELD_NUMBER: _ClassVar[int]
    exposure_index_mode: ExposureIndexMode.ExposureIndexModeType
    def __init__(self, exposure_index_mode: _Optional[_Union[ExposureIndexMode.ExposureIndexModeType, str]] = ...) -> None: ...

class GainMode(_message.Message):
    __slots__ = ("gain_mode",)
    class GainModeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GAIN_MODE_TYPE_AUTO: _ClassVar[GainMode.GainModeType]
        GAIN_MODE_TYPE_LOW_GAIN: _ClassVar[GainMode.GainModeType]
        GAIN_MODE_TYPE_HIGH_GAIN: _ClassVar[GainMode.GainModeType]
    GAIN_MODE_TYPE_AUTO: GainMode.GainModeType
    GAIN_MODE_TYPE_LOW_GAIN: GainMode.GainModeType
    GAIN_MODE_TYPE_HIGH_GAIN: GainMode.GainModeType
    GAIN_MODE_FIELD_NUMBER: _ClassVar[int]
    gain_mode: GainMode.GainModeType
    def __init__(self, gain_mode: _Optional[_Union[GainMode.GainModeType, str]] = ...) -> None: ...

class BaselineExposure(_message.Message):
    __slots__ = ("baseline_exposure",)
    BASELINE_EXPOSURE_FIELD_NUMBER: _ClassVar[int]
    baseline_exposure: float
    def __init__(self, baseline_exposure: _Optional[float] = ...) -> None: ...

class Quaternion(_message.Message):
    __slots__ = ("quaternion_w", "quaternion_x", "quaternion_y", "quaternion_z")
    QUATERNION_W_FIELD_NUMBER: _ClassVar[int]
    QUATERNION_X_FIELD_NUMBER: _ClassVar[int]
    QUATERNION_Y_FIELD_NUMBER: _ClassVar[int]
    QUATERNION_Z_FIELD_NUMBER: _ClassVar[int]
    quaternion_w: float
    quaternion_x: float
    quaternion_y: float
    quaternion_z: float
    def __init__(self, quaternion_w: _Optional[float] = ..., quaternion_x: _Optional[float] = ..., quaternion_y: _Optional[float] = ..., quaternion_z: _Optional[float] = ...) -> None: ...

class Velocity(_message.Message):
    __slots__ = ("velocity_x", "velocity_y", "velocity_z")
    VELOCITY_X_FIELD_NUMBER: _ClassVar[int]
    VELOCITY_Y_FIELD_NUMBER: _ClassVar[int]
    VELOCITY_Z_FIELD_NUMBER: _ClassVar[int]
    velocity_x: float
    velocity_y: float
    velocity_z: float
    def __init__(self, velocity_x: _Optional[float] = ..., velocity_y: _Optional[float] = ..., velocity_z: _Optional[float] = ...) -> None: ...

class Position(_message.Message):
    __slots__ = ("position_x", "position_y", "position_z")
    POSITION_X_FIELD_NUMBER: _ClassVar[int]
    POSITION_Y_FIELD_NUMBER: _ClassVar[int]
    POSITION_Z_FIELD_NUMBER: _ClassVar[int]
    position_x: float
    position_y: float
    position_z: float
    def __init__(self, position_x: _Optional[float] = ..., position_y: _Optional[float] = ..., position_z: _Optional[float] = ...) -> None: ...

class AbsoluteAltitude(_message.Message):
    __slots__ = ("absolute_altitude_m",)
    ABSOLUTE_ALTITUDE_M_FIELD_NUMBER: _ClassVar[int]
    absolute_altitude_m: float
    def __init__(self, absolute_altitude_m: _Optional[float] = ...) -> None: ...

class RelativeAltitude(_message.Message):
    __slots__ = ("relative_altitude_mm", "is_relative_altitude_valid")
    RELATIVE_ALTITUDE_MM_FIELD_NUMBER: _ClassVar[int]
    IS_RELATIVE_ALTITUDE_VALID_FIELD_NUMBER: _ClassVar[int]
    relative_altitude_mm: float
    is_relative_altitude_valid: bool
    def __init__(self, relative_altitude_mm: _Optional[float] = ..., is_relative_altitude_valid: _Optional[bool] = ...) -> None: ...

class RelativeDistance(_message.Message):
    __slots__ = ("relative_distance",)
    RELATIVE_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    relative_distance: int
    def __init__(self, relative_distance: _Optional[int] = ...) -> None: ...

class GimbalInstallPosition(_message.Message):
    __slots__ = ("gimbal_install_position",)
    class GimbalInstallPositionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GIMBAL_INSTALL_POSITION_TYPE_NORMAL: _ClassVar[GimbalInstallPosition.GimbalInstallPositionType]
        GIMBAL_INSTALL_POSITION_TYPE_REVERSE: _ClassVar[GimbalInstallPosition.GimbalInstallPositionType]
    GIMBAL_INSTALL_POSITION_TYPE_NORMAL: GimbalInstallPosition.GimbalInstallPositionType
    GIMBAL_INSTALL_POSITION_TYPE_REVERSE: GimbalInstallPosition.GimbalInstallPositionType
    GIMBAL_INSTALL_POSITION_FIELD_NUMBER: _ClassVar[int]
    gimbal_install_position: GimbalInstallPosition.GimbalInstallPositionType
    def __init__(self, gimbal_install_position: _Optional[_Union[GimbalInstallPosition.GimbalInstallPositionType, str]] = ...) -> None: ...

class GimbalMode(_message.Message):
    __slots__ = ("gimbal_mode",)
    class GimbalModeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GIMBAL_MODE_OFF: _ClassVar[GimbalMode.GimbalModeType]
        GIMBAL_MODE_LOCK: _ClassVar[GimbalMode.GimbalModeType]
        GIMBAL_MODE_FOLLOW: _ClassVar[GimbalMode.GimbalModeType]
    GIMBAL_MODE_OFF: GimbalMode.GimbalModeType
    GIMBAL_MODE_LOCK: GimbalMode.GimbalModeType
    GIMBAL_MODE_FOLLOW: GimbalMode.GimbalModeType
    GIMBAL_MODE_FIELD_NUMBER: _ClassVar[int]
    gimbal_mode: GimbalMode.GimbalModeType
    def __init__(self, gimbal_mode: _Optional[_Union[GimbalMode.GimbalModeType, str]] = ...) -> None: ...

class GimbalModeFollowSubStatus(_message.Message):
    __slots__ = ("pan_follow", "tilt_follow", "roll_follow")
    PAN_FOLLOW_FIELD_NUMBER: _ClassVar[int]
    TILT_FOLLOW_FIELD_NUMBER: _ClassVar[int]
    ROLL_FOLLOW_FIELD_NUMBER: _ClassVar[int]
    pan_follow: bool
    tilt_follow: bool
    roll_follow: bool
    def __init__(self, pan_follow: _Optional[bool] = ..., tilt_follow: _Optional[bool] = ..., roll_follow: _Optional[bool] = ...) -> None: ...

class EulerAngle(_message.Message):
    __slots__ = ("pitch_decidegree", "roll_decidegree", "yaw_decidegree")
    PITCH_DECIDEGREE_FIELD_NUMBER: _ClassVar[int]
    ROLL_DECIDEGREE_FIELD_NUMBER: _ClassVar[int]
    YAW_DECIDEGREE_FIELD_NUMBER: _ClassVar[int]
    pitch_decidegree: int
    roll_decidegree: int
    yaw_decidegree: int
    def __init__(self, pitch_decidegree: _Optional[int] = ..., roll_decidegree: _Optional[int] = ..., yaw_decidegree: _Optional[int] = ...) -> None: ...

class PositionCoord(_message.Message):
    __slots__ = ("position_coord_unit", "latitude", "longitude")
    class PositionCoordUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNIT_RAD: _ClassVar[PositionCoord.PositionCoordUnit]
        UNIT_DEG: _ClassVar[PositionCoord.PositionCoordUnit]
    UNIT_RAD: PositionCoord.PositionCoordUnit
    UNIT_DEG: PositionCoord.PositionCoordUnit
    POSITION_COORD_UNIT_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    position_coord_unit: PositionCoord.PositionCoordUnit
    latitude: float
    longitude: float
    def __init__(self, position_coord_unit: _Optional[_Union[PositionCoord.PositionCoordUnit, str]] = ..., latitude: _Optional[float] = ..., longitude: _Optional[float] = ...) -> None: ...

class GpsTime(_message.Message):
    __slots__ = ("time",)
    TIME_FIELD_NUMBER: _ClassVar[int]
    time: str
    def __init__(self, time: _Optional[str] = ...) -> None: ...

class GpsBasic(_message.Message):
    __slots__ = ("gps_coordinates", "gps_altitude_mm", "gps_status", "gps_altitude_type", "has_gps_time", "gps_time")
    class GpsStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GPS_NORMAL: _ClassVar[GpsBasic.GpsStatus]
        GPS_INVALID: _ClassVar[GpsBasic.GpsStatus]
        GPS_RTK: _ClassVar[GpsBasic.GpsStatus]
    GPS_NORMAL: GpsBasic.GpsStatus
    GPS_INVALID: GpsBasic.GpsStatus
    GPS_RTK: GpsBasic.GpsStatus
    class GpsAltType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRESSURE_ALTITUDE: _ClassVar[GpsBasic.GpsAltType]
        GPS_FUSION_ALTITUDE: _ClassVar[GpsBasic.GpsAltType]
        RTK_ALTITUDE: _ClassVar[GpsBasic.GpsAltType]
    PRESSURE_ALTITUDE: GpsBasic.GpsAltType
    GPS_FUSION_ALTITUDE: GpsBasic.GpsAltType
    RTK_ALTITUDE: GpsBasic.GpsAltType
    GPS_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    GPS_ALTITUDE_MM_FIELD_NUMBER: _ClassVar[int]
    GPS_STATUS_FIELD_NUMBER: _ClassVar[int]
    GPS_ALTITUDE_TYPE_FIELD_NUMBER: _ClassVar[int]
    HAS_GPS_TIME_FIELD_NUMBER: _ClassVar[int]
    GPS_TIME_FIELD_NUMBER: _ClassVar[int]
    gps_coordinates: PositionCoord
    gps_altitude_mm: int
    gps_status: GpsBasic.GpsStatus
    gps_altitude_type: GpsBasic.GpsAltType
    has_gps_time: bool
    gps_time: GpsTime
    def __init__(self, gps_coordinates: _Optional[_Union[PositionCoord, _Mapping]] = ..., gps_altitude_mm: _Optional[int] = ..., gps_status: _Optional[_Union[GpsBasic.GpsStatus, str]] = ..., gps_altitude_type: _Optional[_Union[GpsBasic.GpsAltType, str]] = ..., has_gps_time: _Optional[bool] = ..., gps_time: _Optional[_Union[GpsTime, _Mapping]] = ...) -> None: ...

class Accelerometer(_message.Message):
    __slots__ = ("accelerometer_x", "accelerometer_y", "accelerometer_z")
    ACCELEROMETER_X_FIELD_NUMBER: _ClassVar[int]
    ACCELEROMETER_Y_FIELD_NUMBER: _ClassVar[int]
    ACCELEROMETER_Z_FIELD_NUMBER: _ClassVar[int]
    accelerometer_x: float
    accelerometer_y: float
    accelerometer_z: float
    def __init__(self, accelerometer_x: _Optional[float] = ..., accelerometer_y: _Optional[float] = ..., accelerometer_z: _Optional[float] = ...) -> None: ...

class Gyroscope(_message.Message):
    __slots__ = ("msg_timestamp", "gyroscope_x", "gyroscope_y", "gyroscope_z")
    MSG_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    GYROSCOPE_X_FIELD_NUMBER: _ClassVar[int]
    GYROSCOPE_Y_FIELD_NUMBER: _ClassVar[int]
    GYROSCOPE_Z_FIELD_NUMBER: _ClassVar[int]
    msg_timestamp: int
    gyroscope_x: float
    gyroscope_y: float
    gyroscope_z: float
    def __init__(self, msg_timestamp: _Optional[int] = ..., gyroscope_x: _Optional[float] = ..., gyroscope_y: _Optional[float] = ..., gyroscope_z: _Optional[float] = ...) -> None: ...

class LaserStatus(_message.Message):
    __slots__ = ("laser_status",)
    class LaserStatusType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LASER_NORMAL: _ClassVar[LaserStatus.LaserStatusType]
        LASER_TOO_CLOSE: _ClassVar[LaserStatus.LaserStatusType]
        LASER_TOO_FAR: _ClassVar[LaserStatus.LaserStatusType]
        LASER_CLOSED: _ClassVar[LaserStatus.LaserStatusType]
        LASER_OUT_OF_RANGE: _ClassVar[LaserStatus.LaserStatusType]
    LASER_NORMAL: LaserStatus.LaserStatusType
    LASER_TOO_CLOSE: LaserStatus.LaserStatusType
    LASER_TOO_FAR: LaserStatus.LaserStatusType
    LASER_CLOSED: LaserStatus.LaserStatusType
    LASER_OUT_OF_RANGE: LaserStatus.LaserStatusType
    LASER_STATUS_FIELD_NUMBER: _ClassVar[int]
    laser_status: LaserStatus.LaserStatusType
    def __init__(self, laser_status: _Optional[_Union[LaserStatus.LaserStatusType, str]] = ...) -> None: ...

class LaserRawData(_message.Message):
    __slots__ = ("distance", "intensity")
    DISTANCE_FIELD_NUMBER: _ClassVar[int]
    INTENSITY_FIELD_NUMBER: _ClassVar[int]
    distance: _containers.RepeatedScalarFieldContainer[int]
    intensity: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, distance: _Optional[_Iterable[int]] = ..., intensity: _Optional[_Iterable[int]] = ...) -> None: ...

class RangingStatus(_message.Message):
    __slots__ = ("ranging_status",)
    class RangingStatusType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RANGING_OFF: _ClassVar[RangingStatus.RangingStatusType]
        RANGING_ON: _ClassVar[RangingStatus.RangingStatusType]
    RANGING_OFF: RangingStatus.RangingStatusType
    RANGING_ON: RangingStatus.RangingStatusType
    RANGING_STATUS_FIELD_NUMBER: _ClassVar[int]
    ranging_status: RangingStatus.RangingStatusType
    def __init__(self, ranging_status: _Optional[_Union[RangingStatus.RangingStatusType, str]] = ...) -> None: ...

class ScreenOffset(_message.Message):
    __slots__ = ("screen_offset_x", "screen_offset_y")
    SCREEN_OFFSET_X_FIELD_NUMBER: _ClassVar[int]
    SCREEN_OFFSET_Y_FIELD_NUMBER: _ClassVar[int]
    screen_offset_x: int
    screen_offset_y: int
    def __init__(self, screen_offset_x: _Optional[int] = ..., screen_offset_y: _Optional[int] = ...) -> None: ...

class InfraredSceneMode(_message.Message):
    __slots__ = ("infrared_scene_mode", "infrared_dde_percent", "infrared_contrast_percent", "infrared_brightness_percent")
    class InfraredSceneModeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SCENE_MODE_MANUAL: _ClassVar[InfraredSceneMode.InfraredSceneModeType]
        SCENE_MODE_COMMON: _ClassVar[InfraredSceneMode.InfraredSceneModeType]
        SCENE_MODE_INSPECTION: _ClassVar[InfraredSceneMode.InfraredSceneModeType]
    SCENE_MODE_MANUAL: InfraredSceneMode.InfraredSceneModeType
    SCENE_MODE_COMMON: InfraredSceneMode.InfraredSceneModeType
    SCENE_MODE_INSPECTION: InfraredSceneMode.InfraredSceneModeType
    INFRARED_SCENE_MODE_FIELD_NUMBER: _ClassVar[int]
    INFRARED_DDE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    INFRARED_CONTRAST_PERCENT_FIELD_NUMBER: _ClassVar[int]
    INFRARED_BRIGHTNESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    infrared_scene_mode: InfraredSceneMode.InfraredSceneModeType
    infrared_dde_percent: int
    infrared_contrast_percent: int
    infrared_brightness_percent: int
    def __init__(self, infrared_scene_mode: _Optional[_Union[InfraredSceneMode.InfraredSceneModeType, str]] = ..., infrared_dde_percent: _Optional[int] = ..., infrared_contrast_percent: _Optional[int] = ..., infrared_brightness_percent: _Optional[int] = ...) -> None: ...

class InfraredPseudoColor(_message.Message):
    __slots__ = ("infrared_pseudo_color",)
    class InfraredPseudoColorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INFRARED_PSEUDO_COLOR_WHITEHOT: _ClassVar[InfraredPseudoColor.InfraredPseudoColorType]
        INFRARED_PSEUDO_COLOR_LAVA: _ClassVar[InfraredPseudoColor.InfraredPseudoColorType]
        INFRARED_PSEUDO_COLOR_IRON_RED: _ClassVar[InfraredPseudoColor.InfraredPseudoColorType]
        INFRARED_PSEUDO_COLOR_HOTIRON: _ClassVar[InfraredPseudoColor.InfraredPseudoColorType]
        INFRARED_PSEUDO_COLOR_MEDICINE: _ClassVar[InfraredPseudoColor.InfraredPseudoColorType]
        INFRARED_PSEUDO_COLOR_NORTHPOLE: _ClassVar[InfraredPseudoColor.InfraredPseudoColorType]
        INFRARED_PSEUDO_COLOR_RAINBOW1: _ClassVar[InfraredPseudoColor.InfraredPseudoColorType]
        INFRARED_PSEUDO_COLOR_RAINBOW2: _ClassVar[InfraredPseudoColor.InfraredPseudoColorType]
        INFRARED_PSEUDO_COLOR_TRACERED: _ClassVar[InfraredPseudoColor.InfraredPseudoColorType]
        INFRARED_PSEUDO_COLOR_BLACKHOT: _ClassVar[InfraredPseudoColor.InfraredPseudoColorType]
    INFRARED_PSEUDO_COLOR_WHITEHOT: InfraredPseudoColor.InfraredPseudoColorType
    INFRARED_PSEUDO_COLOR_LAVA: InfraredPseudoColor.InfraredPseudoColorType
    INFRARED_PSEUDO_COLOR_IRON_RED: InfraredPseudoColor.InfraredPseudoColorType
    INFRARED_PSEUDO_COLOR_HOTIRON: InfraredPseudoColor.InfraredPseudoColorType
    INFRARED_PSEUDO_COLOR_MEDICINE: InfraredPseudoColor.InfraredPseudoColorType
    INFRARED_PSEUDO_COLOR_NORTHPOLE: InfraredPseudoColor.InfraredPseudoColorType
    INFRARED_PSEUDO_COLOR_RAINBOW1: InfraredPseudoColor.InfraredPseudoColorType
    INFRARED_PSEUDO_COLOR_RAINBOW2: InfraredPseudoColor.InfraredPseudoColorType
    INFRARED_PSEUDO_COLOR_TRACERED: InfraredPseudoColor.InfraredPseudoColorType
    INFRARED_PSEUDO_COLOR_BLACKHOT: InfraredPseudoColor.InfraredPseudoColorType
    INFRARED_PSEUDO_COLOR_FIELD_NUMBER: _ClassVar[int]
    infrared_pseudo_color: InfraredPseudoColor.InfraredPseudoColorType
    def __init__(self, infrared_pseudo_color: _Optional[_Union[InfraredPseudoColor.InfraredPseudoColorType, str]] = ...) -> None: ...

class InfraredIsotherm(_message.Message):
    __slots__ = ("infrared_isotherm_mode", "infrared_isotherm_high_threshold", "infrared_isotherm_low_threshold")
    class InfraredIsothermModeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INFRARED_ISOTHERM_MODE_OFF: _ClassVar[InfraredIsotherm.InfraredIsothermModeType]
        INFRARED_ISOTHERM_MODE_ON: _ClassVar[InfraredIsotherm.InfraredIsothermModeType]
    INFRARED_ISOTHERM_MODE_OFF: InfraredIsotherm.InfraredIsothermModeType
    INFRARED_ISOTHERM_MODE_ON: InfraredIsotherm.InfraredIsothermModeType
    INFRARED_ISOTHERM_MODE_FIELD_NUMBER: _ClassVar[int]
    INFRARED_ISOTHERM_HIGH_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    INFRARED_ISOTHERM_LOW_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    infrared_isotherm_mode: InfraredIsotherm.InfraredIsothermModeType
    infrared_isotherm_high_threshold: int
    infrared_isotherm_low_threshold: int
    def __init__(self, infrared_isotherm_mode: _Optional[_Union[InfraredIsotherm.InfraredIsothermModeType, str]] = ..., infrared_isotherm_high_threshold: _Optional[int] = ..., infrared_isotherm_low_threshold: _Optional[int] = ...) -> None: ...

class InfraredGainMode(_message.Message):
    __slots__ = ("infrared_gain_mode",)
    class InfraredGainModeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INFRARED_GAIN_MODE_HIGH: _ClassVar[InfraredGainMode.InfraredGainModeType]
        INFRARED_GAIN_MODE_LOW: _ClassVar[InfraredGainMode.InfraredGainModeType]
    INFRARED_GAIN_MODE_HIGH: InfraredGainMode.InfraredGainModeType
    INFRARED_GAIN_MODE_LOW: InfraredGainMode.InfraredGainModeType
    INFRARED_GAIN_MODE_FIELD_NUMBER: _ClassVar[int]
    infrared_gain_mode: InfraredGainMode.InfraredGainModeType
    def __init__(self, infrared_gain_mode: _Optional[_Union[InfraredGainMode.InfraredGainModeType, str]] = ...) -> None: ...

class ExposureValue(_message.Message):
    __slots__ = ("exposure_value",)
    EXPOSURE_VALUE_FIELD_NUMBER: _ClassVar[int]
    exposure_value: float
    def __init__(self, exposure_value: _Optional[float] = ...) -> None: ...

class ColorTempAtmosphere(_message.Message):
    __slots__ = ("color_temp_atmosphere",)
    COLOR_TEMP_ATMOSPHERE_FIELD_NUMBER: _ClassVar[int]
    color_temp_atmosphere: int
    def __init__(self, color_temp_atmosphere: _Optional[int] = ...) -> None: ...

class SensorTemperature(_message.Message):
    __slots__ = ("sensor_temperature",)
    SENSOR_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    sensor_temperature: float
    def __init__(self, sensor_temperature: _Optional[float] = ...) -> None: ...

class SensorActiveSize(_message.Message):
    __slots__ = ("sensor_active_physical_width_um", "sensor_active_physical_height_um")
    SENSOR_ACTIVE_PHYSICAL_WIDTH_UM_FIELD_NUMBER: _ClassVar[int]
    SENSOR_ACTIVE_PHYSICAL_HEIGHT_UM_FIELD_NUMBER: _ClassVar[int]
    sensor_active_physical_width_um: int
    sensor_active_physical_height_um: int
    def __init__(self, sensor_active_physical_width_um: _Optional[int] = ..., sensor_active_physical_height_um: _Optional[int] = ...) -> None: ...

class ImuRawData(_message.Message):
    __slots__ = ("gyro_x", "gyro_y", "gyro_z", "acc_x", "acc_y", "acc_z")
    GYRO_X_FIELD_NUMBER: _ClassVar[int]
    GYRO_Y_FIELD_NUMBER: _ClassVar[int]
    GYRO_Z_FIELD_NUMBER: _ClassVar[int]
    ACC_X_FIELD_NUMBER: _ClassVar[int]
    ACC_Y_FIELD_NUMBER: _ClassVar[int]
    ACC_Z_FIELD_NUMBER: _ClassVar[int]
    gyro_x: float
    gyro_y: float
    gyro_z: float
    acc_x: float
    acc_y: float
    acc_z: float
    def __init__(self, gyro_x: _Optional[float] = ..., gyro_y: _Optional[float] = ..., gyro_z: _Optional[float] = ..., acc_x: _Optional[float] = ..., acc_y: _Optional[float] = ..., acc_z: _Optional[float] = ...) -> None: ...

class DeviceRawAttitude(_message.Message):
    __slots__ = ("timestamp", "imu_raw_data")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    IMU_RAW_DATA_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    imu_raw_data: _containers.RepeatedCompositeFieldContainer[ImuRawData]
    def __init__(self, timestamp: _Optional[int] = ..., imu_raw_data: _Optional[_Iterable[_Union[ImuRawData, _Mapping]]] = ...) -> None: ...

class DeviceAttitude(_message.Message):
    __slots__ = ("timestamp", "vsync", "attitude", "offset")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    VSYNC_FIELD_NUMBER: _ClassVar[int]
    ATTITUDE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    vsync: int
    attitude: _containers.RepeatedCompositeFieldContainer[Quaternion]
    offset: float
    def __init__(self, timestamp: _Optional[int] = ..., vsync: _Optional[int] = ..., attitude: _Optional[_Iterable[_Union[Quaternion, _Mapping]]] = ..., offset: _Optional[float] = ...) -> None: ...

class DeviceMultiAttitude(_message.Message):
    __slots__ = ("current_frame", "prev_frame", "next_frame")
    CURRENT_FRAME_FIELD_NUMBER: _ClassVar[int]
    PREV_FRAME_FIELD_NUMBER: _ClassVar[int]
    NEXT_FRAME_FIELD_NUMBER: _ClassVar[int]
    current_frame: DeviceAttitude
    prev_frame: DeviceAttitude
    next_frame: DeviceAttitude
    def __init__(self, current_frame: _Optional[_Union[DeviceAttitude, _Mapping]] = ..., prev_frame: _Optional[_Union[DeviceAttitude, _Mapping]] = ..., next_frame: _Optional[_Union[DeviceAttitude, _Mapping]] = ...) -> None: ...

class SensorShiftParam(_message.Message):
    __slots__ = ("sensor_shift_arr", "sensor_shift_arr_with_roll", "sensor_shift_arr_without_roll", "sensor_shift_arr_only_yaw", "sensor_shift_ctrl_type")
    SENSOR_SHIFT_ARR_FIELD_NUMBER: _ClassVar[int]
    SENSOR_SHIFT_ARR_WITH_ROLL_FIELD_NUMBER: _ClassVar[int]
    SENSOR_SHIFT_ARR_WITHOUT_ROLL_FIELD_NUMBER: _ClassVar[int]
    SENSOR_SHIFT_ARR_ONLY_YAW_FIELD_NUMBER: _ClassVar[int]
    SENSOR_SHIFT_CTRL_TYPE_FIELD_NUMBER: _ClassVar[int]
    sensor_shift_arr: _containers.RepeatedScalarFieldContainer[int]
    sensor_shift_arr_with_roll: _containers.RepeatedScalarFieldContainer[int]
    sensor_shift_arr_without_roll: _containers.RepeatedScalarFieldContainer[int]
    sensor_shift_arr_only_yaw: _containers.RepeatedScalarFieldContainer[int]
    sensor_shift_ctrl_type: int
    def __init__(self, sensor_shift_arr: _Optional[_Iterable[int]] = ..., sensor_shift_arr_with_roll: _Optional[_Iterable[int]] = ..., sensor_shift_arr_without_roll: _Optional[_Iterable[int]] = ..., sensor_shift_arr_only_yaw: _Optional[_Iterable[int]] = ..., sensor_shift_ctrl_type: _Optional[int] = ...) -> None: ...

class FaiDegree(_message.Message):
    __slots__ = ("fai_g_deg",)
    FAI_G_DEG_FIELD_NUMBER: _ClassVar[int]
    fai_g_deg: int
    def __init__(self, fai_g_deg: _Optional[int] = ...) -> None: ...

class FancyMode(_message.Message):
    __slots__ = ("timestamp", "fancy_mode_type", "fancy_mode_act_cnt")
    class FancyModeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FANCY_MODE_NULL: _ClassVar[FancyMode.FancyModeType]
        FANCY_MODE_TURN_AROUND_RIGHT: _ClassVar[FancyMode.FancyModeType]
        FANCY_MODE_TURN_AROUND_LEFT: _ClassVar[FancyMode.FancyModeType]
        FANCY_MODE_TURN_OVER_RIGHT: _ClassVar[FancyMode.FancyModeType]
        FANCY_MODE_TURN_OVER_LEFT: _ClassVar[FancyMode.FancyModeType]
        FANCY_MODE_TURN_OVER_BACK: _ClassVar[FancyMode.FancyModeType]
        FANCY_MODE_TURN_OVER_FRONT: _ClassVar[FancyMode.FancyModeType]
    FANCY_MODE_NULL: FancyMode.FancyModeType
    FANCY_MODE_TURN_AROUND_RIGHT: FancyMode.FancyModeType
    FANCY_MODE_TURN_AROUND_LEFT: FancyMode.FancyModeType
    FANCY_MODE_TURN_OVER_RIGHT: FancyMode.FancyModeType
    FANCY_MODE_TURN_OVER_LEFT: FancyMode.FancyModeType
    FANCY_MODE_TURN_OVER_BACK: FancyMode.FancyModeType
    FANCY_MODE_TURN_OVER_FRONT: FancyMode.FancyModeType
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    FANCY_MODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FANCY_MODE_ACT_CNT_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    fancy_mode_type: FancyMode.FancyModeType
    fancy_mode_act_cnt: int
    def __init__(self, timestamp: _Optional[int] = ..., fancy_mode_type: _Optional[_Union[FancyMode.FancyModeType, str]] = ..., fancy_mode_act_cnt: _Optional[int] = ...) -> None: ...

class LiveViewHfov(_message.Message):
    __slots__ = ("lv_hfov", "lv_hfov_camera", "lv_view_site", "lv_frame_ratio")
    LV_HFOV_FIELD_NUMBER: _ClassVar[int]
    LV_HFOV_CAMERA_FIELD_NUMBER: _ClassVar[int]
    LV_VIEW_SITE_FIELD_NUMBER: _ClassVar[int]
    LV_FRAME_RATIO_FIELD_NUMBER: _ClassVar[int]
    lv_hfov: float
    lv_hfov_camera: float
    lv_view_site: float
    lv_frame_ratio: float
    def __init__(self, lv_hfov: _Optional[float] = ..., lv_hfov_camera: _Optional[float] = ..., lv_view_site: _Optional[float] = ..., lv_frame_ratio: _Optional[float] = ...) -> None: ...

class GimbalAngleDeviation(_message.Message):
    __slots__ = ("x_deviation", "y_deviation", "z_deviation")
    X_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    Y_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    Z_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    x_deviation: float
    y_deviation: float
    z_deviation: float
    def __init__(self, x_deviation: _Optional[float] = ..., y_deviation: _Optional[float] = ..., z_deviation: _Optional[float] = ...) -> None: ...

class TrackingInfo(_message.Message):
    __slots__ = ("tracking_mode", "sub_tracking_mode", "id", "obj_class", "center_x", "center_y", "width", "height")
    TRACKING_MODE_FIELD_NUMBER: _ClassVar[int]
    SUB_TRACKING_MODE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    OBJ_CLASS_FIELD_NUMBER: _ClassVar[int]
    CENTER_X_FIELD_NUMBER: _ClassVar[int]
    CENTER_Y_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    tracking_mode: int
    sub_tracking_mode: int
    id: int
    obj_class: int
    center_x: float
    center_y: float
    width: float
    height: float
    def __init__(self, tracking_mode: _Optional[int] = ..., sub_tracking_mode: _Optional[int] = ..., id: _Optional[int] = ..., obj_class: _Optional[int] = ..., center_x: _Optional[float] = ..., center_y: _Optional[float] = ..., width: _Optional[float] = ..., height: _Optional[float] = ...) -> None: ...

class UavToTargetPos(_message.Message):
    __slots__ = ("time_stamp_us", "drone_coord_navi", "q_drone2navi", "phi_g", "target_type", "q_target2navi", "is_target_coord_valid", "target_coord_navi")
    class TargetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TARGET_TYPE_UNKNOWN: _ClassVar[UavToTargetPos.TargetType]
        TARGET_TYPE_PERSON: _ClassVar[UavToTargetPos.TargetType]
        TARGET_TYPE_CAR: _ClassVar[UavToTargetPos.TargetType]
        TARGET_TYPE_VAN: _ClassVar[UavToTargetPos.TargetType]
        TARGET_TYPE_BIKE: _ClassVar[UavToTargetPos.TargetType]
        TARGET_TYPE_ANIMAL: _ClassVar[UavToTargetPos.TargetType]
        TARGET_TYPE_BOAT: _ClassVar[UavToTargetPos.TargetType]
        TARGET_TYPE_HUMAN_FACE: _ClassVar[UavToTargetPos.TargetType]
        TARGET_TYPE_HEAD_SHOULDER: _ClassVar[UavToTargetPos.TargetType]
        TARGET_TYPE_HUMAN_BODY: _ClassVar[UavToTargetPos.TargetType]
        TARGET_TYPE_HUMAN_HEAD: _ClassVar[UavToTargetPos.TargetType]
        TARGET_TYPE_ANIMAL_BODY: _ClassVar[UavToTargetPos.TargetType]
        TARGET_TYPE_ANIMAL_FACE: _ClassVar[UavToTargetPos.TargetType]
        TARGET_TYPE_BEACON: _ClassVar[UavToTargetPos.TargetType]
        TARGET_TYPE_BEACON_DISPLAY: _ClassVar[UavToTargetPos.TargetType]
    TARGET_TYPE_UNKNOWN: UavToTargetPos.TargetType
    TARGET_TYPE_PERSON: UavToTargetPos.TargetType
    TARGET_TYPE_CAR: UavToTargetPos.TargetType
    TARGET_TYPE_VAN: UavToTargetPos.TargetType
    TARGET_TYPE_BIKE: UavToTargetPos.TargetType
    TARGET_TYPE_ANIMAL: UavToTargetPos.TargetType
    TARGET_TYPE_BOAT: UavToTargetPos.TargetType
    TARGET_TYPE_HUMAN_FACE: UavToTargetPos.TargetType
    TARGET_TYPE_HEAD_SHOULDER: UavToTargetPos.TargetType
    TARGET_TYPE_HUMAN_BODY: UavToTargetPos.TargetType
    TARGET_TYPE_HUMAN_HEAD: UavToTargetPos.TargetType
    TARGET_TYPE_ANIMAL_BODY: UavToTargetPos.TargetType
    TARGET_TYPE_ANIMAL_FACE: UavToTargetPos.TargetType
    TARGET_TYPE_BEACON: UavToTargetPos.TargetType
    TARGET_TYPE_BEACON_DISPLAY: UavToTargetPos.TargetType
    TIME_STAMP_US_FIELD_NUMBER: _ClassVar[int]
    DRONE_COORD_NAVI_FIELD_NUMBER: _ClassVar[int]
    Q_DRONE2NAVI_FIELD_NUMBER: _ClassVar[int]
    PHI_G_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    Q_TARGET2NAVI_FIELD_NUMBER: _ClassVar[int]
    IS_TARGET_COORD_VALID_FIELD_NUMBER: _ClassVar[int]
    TARGET_COORD_NAVI_FIELD_NUMBER: _ClassVar[int]
    time_stamp_us: int
    drone_coord_navi: _containers.RepeatedScalarFieldContainer[float]
    q_drone2navi: Quaternion
    phi_g: float
    target_type: UavToTargetPos.TargetType
    q_target2navi: Quaternion
    is_target_coord_valid: bool
    target_coord_navi: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, time_stamp_us: _Optional[int] = ..., drone_coord_navi: _Optional[_Iterable[float]] = ..., q_drone2navi: _Optional[_Union[Quaternion, _Mapping]] = ..., phi_g: _Optional[float] = ..., target_type: _Optional[_Union[UavToTargetPos.TargetType, str]] = ..., q_target2navi: _Optional[_Union[Quaternion, _Mapping]] = ..., is_target_coord_valid: _Optional[bool] = ..., target_coord_navi: _Optional[_Iterable[float]] = ...) -> None: ...

class SensorFrameReadOutTime(_message.Message):
    __slots__ = ("readout_time",)
    READOUT_TIME_FIELD_NUMBER: _ClassVar[int]
    readout_time: int
    def __init__(self, readout_time: _Optional[int] = ...) -> None: ...

class LROValue(_message.Message):
    __slots__ = ("LRO_value",)
    LRO_VALUE_FIELD_NUMBER: _ClassVar[int]
    LRO_value: int
    def __init__(self, LRO_value: _Optional[int] = ...) -> None: ...

class SensorRes(_message.Message):
    __slots__ = ("sensor_width", "sensor_height")
    SENSOR_WIDTH_FIELD_NUMBER: _ClassVar[int]
    SENSOR_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    sensor_width: int
    sensor_height: int
    def __init__(self, sensor_width: _Optional[int] = ..., sensor_height: _Optional[int] = ...) -> None: ...

class FlatRes(_message.Message):
    __slots__ = ("flat_width", "flat_height")
    FLAT_WIDTH_FIELD_NUMBER: _ClassVar[int]
    FLAT_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    flat_width: int
    flat_height: int
    def __init__(self, flat_width: _Optional[int] = ..., flat_height: _Optional[int] = ...) -> None: ...

class ImuVsyncPos(_message.Message):
    __slots__ = ("vsync_pos",)
    VSYNC_POS_FIELD_NUMBER: _ClassVar[int]
    vsync_pos: int
    def __init__(self, vsync_pos: _Optional[int] = ...) -> None: ...

class ITDValue(_message.Message):
    __slots__ = ("ITD_value",)
    ITD_VALUE_FIELD_NUMBER: _ClassVar[int]
    ITD_value: int
    def __init__(self, ITD_value: _Optional[int] = ...) -> None: ...

class SensorReadDirection(_message.Message):
    __slots__ = ("direction",)
    class SenorReadDirectionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TOP_LEFT: _ClassVar[SensorReadDirection.SenorReadDirectionType]
        TOP_RIGHT: _ClassVar[SensorReadDirection.SenorReadDirectionType]
        BOTTOM_RIGHT: _ClassVar[SensorReadDirection.SenorReadDirectionType]
        BOTTOM_LEFT: _ClassVar[SensorReadDirection.SenorReadDirectionType]
        LEFT_TOP: _ClassVar[SensorReadDirection.SenorReadDirectionType]
        RIGHT_TOP: _ClassVar[SensorReadDirection.SenorReadDirectionType]
        RIGHT_BOTTOM: _ClassVar[SensorReadDirection.SenorReadDirectionType]
        LEFT_BOTTOM: _ClassVar[SensorReadDirection.SenorReadDirectionType]
    TOP_LEFT: SensorReadDirection.SenorReadDirectionType
    TOP_RIGHT: SensorReadDirection.SenorReadDirectionType
    BOTTOM_RIGHT: SensorReadDirection.SenorReadDirectionType
    BOTTOM_LEFT: SensorReadDirection.SenorReadDirectionType
    LEFT_TOP: SensorReadDirection.SenorReadDirectionType
    RIGHT_TOP: SensorReadDirection.SenorReadDirectionType
    RIGHT_BOTTOM: SensorReadDirection.SenorReadDirectionType
    LEFT_BOTTOM: SensorReadDirection.SenorReadDirectionType
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    direction: SensorReadDirection.SenorReadDirectionType
    def __init__(self, direction: _Optional[_Union[SensorReadDirection.SenorReadDirectionType, str]] = ...) -> None: ...

class SensorFrameRate(_message.Message):
    __slots__ = ("sensor_frame_rate",)
    SENSOR_FRAME_RATE_FIELD_NUMBER: _ClassVar[int]
    sensor_frame_rate: float
    def __init__(self, sensor_frame_rate: _Optional[float] = ...) -> None: ...

class IMUSamplingRate(_message.Message):
    __slots__ = ("imu_sampling_rate",)
    IMU_SAMPLING_RATE_FIELD_NUMBER: _ClassVar[int]
    imu_sampling_rate: int
    def __init__(self, imu_sampling_rate: _Optional[int] = ...) -> None: ...

class DigitalFocalLength(_message.Message):
    __slots__ = ("focal_length",)
    FOCAL_LENGTH_FIELD_NUMBER: _ClassVar[int]
    focal_length: float
    def __init__(self, focal_length: _Optional[float] = ...) -> None: ...

class LensDistortionCoefficients(_message.Message):
    __slots__ = ("coeffients",)
    COEFFIENTS_FIELD_NUMBER: _ClassVar[int]
    coeffients: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, coeffients: _Optional[_Iterable[float]] = ...) -> None: ...

class EisStatus(_message.Message):
    __slots__ = ("status",)
    class EisStatusType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EIS_OFF: _ClassVar[EisStatus.EisStatusType]
        EIS_ROCK_STEADY: _ClassVar[EisStatus.EisStatusType]
        EIS_HORIZON_STEADY: _ClassVar[EisStatus.EisStatusType]
        EIS_HYPER: _ClassVar[EisStatus.EisStatusType]
        EIS_TRADEOFF: _ClassVar[EisStatus.EisStatusType]
        EIS_HORIZON_BALANCING: _ClassVar[EisStatus.EisStatusType]
        EIS_DEEPSPACE: _ClassVar[EisStatus.EisStatusType]
        EIS_OFF_WITH_CROP: _ClassVar[EisStatus.EisStatusType]
        EIS_HORIZON_CORRECTION: _ClassVar[EisStatus.EisStatusType]
        EIS_RS_AUTO: _ClassVar[EisStatus.EisStatusType]
    EIS_OFF: EisStatus.EisStatusType
    EIS_ROCK_STEADY: EisStatus.EisStatusType
    EIS_HORIZON_STEADY: EisStatus.EisStatusType
    EIS_HYPER: EisStatus.EisStatusType
    EIS_TRADEOFF: EisStatus.EisStatusType
    EIS_HORIZON_BALANCING: EisStatus.EisStatusType
    EIS_DEEPSPACE: EisStatus.EisStatusType
    EIS_OFF_WITH_CROP: EisStatus.EisStatusType
    EIS_HORIZON_CORRECTION: EisStatus.EisStatusType
    EIS_RS_AUTO: EisStatus.EisStatusType
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: EisStatus.EisStatusType
    def __init__(self, status: _Optional[_Union[EisStatus.EisStatusType, str]] = ...) -> None: ...

class CurrentUnderwaterConfidence(_message.Message):
    __slots__ = ("current_underwater_confidence",)
    CURRENT_UNDERWATER_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    current_underwater_confidence: int
    def __init__(self, current_underwater_confidence: _Optional[int] = ...) -> None: ...

class WayPointStatus(_message.Message):
    __slots__ = ("status",)
    class WayPointStatusType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        WAYPOINT_OFF: _ClassVar[WayPointStatus.WayPointStatusType]
        WAYPOINT_ON: _ClassVar[WayPointStatus.WayPointStatusType]
    WAYPOINT_OFF: WayPointStatus.WayPointStatusType
    WAYPOINT_ON: WayPointStatus.WayPointStatusType
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: WayPointStatus.WayPointStatusType
    def __init__(self, status: _Optional[_Union[WayPointStatus.WayPointStatusType, str]] = ...) -> None: ...

class FCMData(_message.Message):
    __slots__ = ("timestamp", "center_x", "center_y", "min_x", "min_y", "max_x", "max_y", "relative_direction", "dest_direction", "movement", "relative_horizontal_distance_m", "relative_height_m", "target_speed_mps", "move_exec_state", "exit_reason", "score")
    class Drone_Movement(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_MOVE: _ClassVar[FCMData.Drone_Movement]
        CLOCKWISE: _ClassVar[FCMData.Drone_Movement]
        COUNTER_CLOCKWISE: _ClassVar[FCMData.Drone_Movement]
        AUTO_CHOICE: _ClassVar[FCMData.Drone_Movement]
    UNKNOWN_MOVE: FCMData.Drone_Movement
    CLOCKWISE: FCMData.Drone_Movement
    COUNTER_CLOCKWISE: FCMData.Drone_Movement
    AUTO_CHOICE: FCMData.Drone_Movement
    class BodyRelativeDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BEHIND: _ClassVar[FCMData.BodyRelativeDirection]
        BEHIND_RIGHT: _ClassVar[FCMData.BodyRelativeDirection]
        RIGHT: _ClassVar[FCMData.BodyRelativeDirection]
        LEAD_RIGHT: _ClassVar[FCMData.BodyRelativeDirection]
        LEAD: _ClassVar[FCMData.BodyRelativeDirection]
        LEAD_LEFT: _ClassVar[FCMData.BodyRelativeDirection]
        LEFT: _ClassVar[FCMData.BodyRelativeDirection]
        BEHIND_LEFT: _ClassVar[FCMData.BodyRelativeDirection]
        BEHIND_OUTER: _ClassVar[FCMData.BodyRelativeDirection]
        BEHIND_RIGHT_OUTER: _ClassVar[FCMData.BodyRelativeDirection]
        RIGHT_OUTER: _ClassVar[FCMData.BodyRelativeDirection]
        LEAD_RIGHT_OUTER: _ClassVar[FCMData.BodyRelativeDirection]
        LEAD_OUTER: _ClassVar[FCMData.BodyRelativeDirection]
        LEAD_LEFT_OUTER: _ClassVar[FCMData.BodyRelativeDirection]
        LEFT_OUTER: _ClassVar[FCMData.BodyRelativeDirection]
        BEHIND_LEFT_OUTER: _ClassVar[FCMData.BodyRelativeDirection]
    BEHIND: FCMData.BodyRelativeDirection
    BEHIND_RIGHT: FCMData.BodyRelativeDirection
    RIGHT: FCMData.BodyRelativeDirection
    LEAD_RIGHT: FCMData.BodyRelativeDirection
    LEAD: FCMData.BodyRelativeDirection
    LEAD_LEFT: FCMData.BodyRelativeDirection
    LEFT: FCMData.BodyRelativeDirection
    BEHIND_LEFT: FCMData.BodyRelativeDirection
    BEHIND_OUTER: FCMData.BodyRelativeDirection
    BEHIND_RIGHT_OUTER: FCMData.BodyRelativeDirection
    RIGHT_OUTER: FCMData.BodyRelativeDirection
    LEAD_RIGHT_OUTER: FCMData.BodyRelativeDirection
    LEAD_OUTER: FCMData.BodyRelativeDirection
    LEAD_LEFT_OUTER: FCMData.BodyRelativeDirection
    LEFT_OUTER: FCMData.BodyRelativeDirection
    BEHIND_LEFT_OUTER: FCMData.BodyRelativeDirection
    class Movement_Exec_State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MOVE_NO_CMD: _ClassVar[FCMData.Movement_Exec_State]
        MOVE_RECEIVED_START_CMD: _ClassVar[FCMData.Movement_Exec_State]
        MOVE_EXECUTING: _ClassVar[FCMData.Movement_Exec_State]
        MOVE_FINISHED: _ClassVar[FCMData.Movement_Exec_State]
    MOVE_NO_CMD: FCMData.Movement_Exec_State
    MOVE_RECEIVED_START_CMD: FCMData.Movement_Exec_State
    MOVE_EXECUTING: FCMData.Movement_Exec_State
    MOVE_FINISHED: FCMData.Movement_Exec_State
    class Exit_Reason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DJI_FCM_OK: _ClassVar[FCMData.Exit_Reason]
        DJI_FCM_OBSTACLE_STUCK: _ClassVar[FCMData.Exit_Reason]
        DJI_FCM_ABORTED: _ClassVar[FCMData.Exit_Reason]
    DJI_FCM_OK: FCMData.Exit_Reason
    DJI_FCM_OBSTACLE_STUCK: FCMData.Exit_Reason
    DJI_FCM_ABORTED: FCMData.Exit_Reason
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CENTER_X_FIELD_NUMBER: _ClassVar[int]
    CENTER_Y_FIELD_NUMBER: _ClassVar[int]
    MIN_X_FIELD_NUMBER: _ClassVar[int]
    MIN_Y_FIELD_NUMBER: _ClassVar[int]
    MAX_X_FIELD_NUMBER: _ClassVar[int]
    MAX_Y_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    DEST_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    MOVEMENT_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_HORIZONTAL_DISTANCE_M_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_HEIGHT_M_FIELD_NUMBER: _ClassVar[int]
    TARGET_SPEED_MPS_FIELD_NUMBER: _ClassVar[int]
    MOVE_EXEC_STATE_FIELD_NUMBER: _ClassVar[int]
    EXIT_REASON_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    center_x: float
    center_y: float
    min_x: float
    min_y: float
    max_x: float
    max_y: float
    relative_direction: FCMData.BodyRelativeDirection
    dest_direction: FCMData.BodyRelativeDirection
    movement: FCMData.Drone_Movement
    relative_horizontal_distance_m: float
    relative_height_m: float
    target_speed_mps: float
    move_exec_state: FCMData.Movement_Exec_State
    exit_reason: FCMData.Exit_Reason
    score: float
    def __init__(self, timestamp: _Optional[int] = ..., center_x: _Optional[float] = ..., center_y: _Optional[float] = ..., min_x: _Optional[float] = ..., min_y: _Optional[float] = ..., max_x: _Optional[float] = ..., max_y: _Optional[float] = ..., relative_direction: _Optional[_Union[FCMData.BodyRelativeDirection, str]] = ..., dest_direction: _Optional[_Union[FCMData.BodyRelativeDirection, str]] = ..., movement: _Optional[_Union[FCMData.Drone_Movement, str]] = ..., relative_horizontal_distance_m: _Optional[float] = ..., relative_height_m: _Optional[float] = ..., target_speed_mps: _Optional[float] = ..., move_exec_state: _Optional[_Union[FCMData.Movement_Exec_State, str]] = ..., exit_reason: _Optional[_Union[FCMData.Exit_Reason, str]] = ..., score: _Optional[float] = ...) -> None: ...

class RC_Mode(_message.Message):
    __slots__ = ("rc_mode",)
    class Rc_Mode_Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DJI_COMMAND_MODE_MANUAL: _ClassVar[RC_Mode.Rc_Mode_Enum]
        DJI_COMMAND_MODE_ATTI_NORMAL: _ClassVar[RC_Mode.Rc_Mode_Enum]
        DJI_COMMAND_MODE_GPS_NORMAL: _ClassVar[RC_Mode.Rc_Mode_Enum]
        DJI_COMMAND_MODE_GPS_SPORT: _ClassVar[RC_Mode.Rc_Mode_Enum]
        DJI_COMMAND_MODE_TRIPOD: _ClassVar[RC_Mode.Rc_Mode_Enum]
        DJI_COMMAND_MODE_FPV: _ClassVar[RC_Mode.Rc_Mode_Enum]
    DJI_COMMAND_MODE_MANUAL: RC_Mode.Rc_Mode_Enum
    DJI_COMMAND_MODE_ATTI_NORMAL: RC_Mode.Rc_Mode_Enum
    DJI_COMMAND_MODE_GPS_NORMAL: RC_Mode.Rc_Mode_Enum
    DJI_COMMAND_MODE_GPS_SPORT: RC_Mode.Rc_Mode_Enum
    DJI_COMMAND_MODE_TRIPOD: RC_Mode.Rc_Mode_Enum
    DJI_COMMAND_MODE_FPV: RC_Mode.Rc_Mode_Enum
    RC_MODE_FIELD_NUMBER: _ClassVar[int]
    rc_mode: RC_Mode.Rc_Mode_Enum
    def __init__(self, rc_mode: _Optional[_Union[RC_Mode.Rc_Mode_Enum, str]] = ...) -> None: ...

class Battery_Info(_message.Message):
    __slots__ = ("battery_percent",)
    BATTERY_PERCENT_FIELD_NUMBER: _ClassVar[int]
    battery_percent: int
    def __init__(self, battery_percent: _Optional[int] = ...) -> None: ...

class Barrier_Distance(_message.Message):
    __slots__ = ("below_tof_state", "below_dist_cm")
    class Tof_State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TOF_STATE_NO_REFLECTION: _ClassVar[Barrier_Distance.Tof_State]
        TOF_STATE_REFLECTED: _ClassVar[Barrier_Distance.Tof_State]
    TOF_STATE_NO_REFLECTION: Barrier_Distance.Tof_State
    TOF_STATE_REFLECTED: Barrier_Distance.Tof_State
    BELOW_TOF_STATE_FIELD_NUMBER: _ClassVar[int]
    BELOW_DIST_CM_FIELD_NUMBER: _ClassVar[int]
    below_tof_state: Barrier_Distance.Tof_State
    below_dist_cm: int
    def __init__(self, below_tof_state: _Optional[_Union[Barrier_Distance.Tof_State, str]] = ..., below_dist_cm: _Optional[int] = ...) -> None: ...

class RealFocalLength(_message.Message):
    __slots__ = ("real_focal_length",)
    REAL_FOCAL_LENGTH_FIELD_NUMBER: _ClassVar[int]
    real_focal_length: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, real_focal_length: _Optional[_Iterable[int]] = ...) -> None: ...

class Barometer(_message.Message):
    __slots__ = ("is_in_water", "altitude_dm", "atmospheric_hpa")
    IS_IN_WATER_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_DM_FIELD_NUMBER: _ClassVar[int]
    ATMOSPHERIC_HPA_FIELD_NUMBER: _ClassVar[int]
    is_in_water: bool
    altitude_dm: int
    atmospheric_hpa: int
    def __init__(self, is_in_water: _Optional[bool] = ..., altitude_dm: _Optional[int] = ..., atmospheric_hpa: _Optional[int] = ...) -> None: ...

class CameraControllerScene(_message.Message):
    __slots__ = ("camera_controller_scene",)
    class CameraControllerScene(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAMERA_CONTROLLER_SCENE_STANDARD: _ClassVar[CameraControllerScene.CameraControllerScene]
        CAMERA_CONTROLLER_SCENE_GOGGLE: _ClassVar[CameraControllerScene.CameraControllerScene]
        CAMERA_CONTROLLER_SCENE_HANDHELD: _ClassVar[CameraControllerScene.CameraControllerScene]
    CAMERA_CONTROLLER_SCENE_STANDARD: CameraControllerScene.CameraControllerScene
    CAMERA_CONTROLLER_SCENE_GOGGLE: CameraControllerScene.CameraControllerScene
    CAMERA_CONTROLLER_SCENE_HANDHELD: CameraControllerScene.CameraControllerScene
    CAMERA_CONTROLLER_SCENE_FIELD_NUMBER: _ClassVar[int]
    camera_controller_scene: CameraControllerScene.CameraControllerScene
    def __init__(self, camera_controller_scene: _Optional[_Union[CameraControllerScene.CameraControllerScene, str]] = ...) -> None: ...

class EquivalentFocalLength(_message.Message):
    __slots__ = ("equivalent_focal_length",)
    EQUIVALENT_FOCAL_LENGTH_FIELD_NUMBER: _ClassVar[int]
    equivalent_focal_length: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, equivalent_focal_length: _Optional[_Iterable[int]] = ...) -> None: ...

class Effective35mmEqFocalLen(_message.Message):
    __slots__ = ("equivalent_focal_length",)
    EQUIVALENT_FOCAL_LENGTH_FIELD_NUMBER: _ClassVar[int]
    equivalent_focal_length: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, equivalent_focal_length: _Optional[_Iterable[int]] = ...) -> None: ...

class GimbalSelfCailParams(_message.Message):
    __slots__ = ("flag", "gimbal_yaw_h1", "gimbal_yaw_h2")
    FLAG_FIELD_NUMBER: _ClassVar[int]
    GIMBAL_YAW_H1_FIELD_NUMBER: _ClassVar[int]
    GIMBAL_YAW_H2_FIELD_NUMBER: _ClassVar[int]
    flag: int
    gimbal_yaw_h1: int
    gimbal_yaw_h2: int
    def __init__(self, flag: _Optional[int] = ..., gimbal_yaw_h1: _Optional[int] = ..., gimbal_yaw_h2: _Optional[int] = ...) -> None: ...

class DewarpParams(_message.Message):
    __slots__ = ("fx", "fy", "cx", "cy", "k1", "k2", "k3", "k4", "xi", "width", "height", "yaw", "pitch", "roll", "k5", "k6", "k7", "k8", "k9", "p", "q", "occlusion_pt_x", "occlusion_pt_y", "lens_model", "temperature", "cam_imu_extri_q", "tangent_coeff", "cam_extri_q", "cam_imu_cali_enable", "temp_compen_enable", "temp_compen_k", "gimbal_yaw_h1", "gimbal_yaw_h2", "gimbal_self_cail_param", "temp_compen_k_order")
    FX_FIELD_NUMBER: _ClassVar[int]
    FY_FIELD_NUMBER: _ClassVar[int]
    CX_FIELD_NUMBER: _ClassVar[int]
    CY_FIELD_NUMBER: _ClassVar[int]
    K1_FIELD_NUMBER: _ClassVar[int]
    K2_FIELD_NUMBER: _ClassVar[int]
    K3_FIELD_NUMBER: _ClassVar[int]
    K4_FIELD_NUMBER: _ClassVar[int]
    XI_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    YAW_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    ROLL_FIELD_NUMBER: _ClassVar[int]
    K5_FIELD_NUMBER: _ClassVar[int]
    K6_FIELD_NUMBER: _ClassVar[int]
    K7_FIELD_NUMBER: _ClassVar[int]
    K8_FIELD_NUMBER: _ClassVar[int]
    K9_FIELD_NUMBER: _ClassVar[int]
    P_FIELD_NUMBER: _ClassVar[int]
    Q_FIELD_NUMBER: _ClassVar[int]
    OCCLUSION_PT_X_FIELD_NUMBER: _ClassVar[int]
    OCCLUSION_PT_Y_FIELD_NUMBER: _ClassVar[int]
    LENS_MODEL_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    CAM_IMU_EXTRI_Q_FIELD_NUMBER: _ClassVar[int]
    TANGENT_COEFF_FIELD_NUMBER: _ClassVar[int]
    CAM_EXTRI_Q_FIELD_NUMBER: _ClassVar[int]
    CAM_IMU_CALI_ENABLE_FIELD_NUMBER: _ClassVar[int]
    TEMP_COMPEN_ENABLE_FIELD_NUMBER: _ClassVar[int]
    TEMP_COMPEN_K_FIELD_NUMBER: _ClassVar[int]
    GIMBAL_YAW_H1_FIELD_NUMBER: _ClassVar[int]
    GIMBAL_YAW_H2_FIELD_NUMBER: _ClassVar[int]
    GIMBAL_SELF_CAIL_PARAM_FIELD_NUMBER: _ClassVar[int]
    TEMP_COMPEN_K_ORDER_FIELD_NUMBER: _ClassVar[int]
    fx: float
    fy: float
    cx: float
    cy: float
    k1: float
    k2: float
    k3: float
    k4: float
    xi: float
    width: float
    height: float
    yaw: float
    pitch: float
    roll: float
    k5: float
    k6: float
    k7: float
    k8: float
    k9: float
    p: _containers.RepeatedScalarFieldContainer[float]
    q: _containers.RepeatedScalarFieldContainer[float]
    occlusion_pt_x: _containers.RepeatedScalarFieldContainer[float]
    occlusion_pt_y: _containers.RepeatedScalarFieldContainer[float]
    lens_model: float
    temperature: float
    cam_imu_extri_q: Quaternion
    tangent_coeff: _containers.RepeatedScalarFieldContainer[float]
    cam_extri_q: Quaternion
    cam_imu_cali_enable: bool
    temp_compen_enable: bool
    temp_compen_k: float
    gimbal_yaw_h1: float
    gimbal_yaw_h2: float
    gimbal_self_cail_param: GimbalSelfCailParams
    temp_compen_k_order: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, fx: _Optional[float] = ..., fy: _Optional[float] = ..., cx: _Optional[float] = ..., cy: _Optional[float] = ..., k1: _Optional[float] = ..., k2: _Optional[float] = ..., k3: _Optional[float] = ..., k4: _Optional[float] = ..., xi: _Optional[float] = ..., width: _Optional[float] = ..., height: _Optional[float] = ..., yaw: _Optional[float] = ..., pitch: _Optional[float] = ..., roll: _Optional[float] = ..., k5: _Optional[float] = ..., k6: _Optional[float] = ..., k7: _Optional[float] = ..., k8: _Optional[float] = ..., k9: _Optional[float] = ..., p: _Optional[_Iterable[float]] = ..., q: _Optional[_Iterable[float]] = ..., occlusion_pt_x: _Optional[_Iterable[float]] = ..., occlusion_pt_y: _Optional[_Iterable[float]] = ..., lens_model: _Optional[float] = ..., temperature: _Optional[float] = ..., cam_imu_extri_q: _Optional[_Union[Quaternion, _Mapping]] = ..., tangent_coeff: _Optional[_Iterable[float]] = ..., cam_extri_q: _Optional[_Union[Quaternion, _Mapping]] = ..., cam_imu_cali_enable: _Optional[bool] = ..., temp_compen_enable: _Optional[bool] = ..., temp_compen_k: _Optional[float] = ..., gimbal_yaw_h1: _Optional[float] = ..., gimbal_yaw_h2: _Optional[float] = ..., gimbal_self_cail_param: _Optional[_Union[GimbalSelfCailParams, _Mapping]] = ..., temp_compen_k_order: _Optional[_Iterable[float]] = ...) -> None: ...

class PanoDewarpParams(_message.Message):
    __slots__ = ("native_refine_slave", "native_refine_master", "native_refine_far_slave", "native_refine_far_master", "lens_guards_slave", "lens_guards_master", "water_proof_above_water_slave", "water_proof_above_water_master", "water_proof_under_water_slave", "water_proof_under_water_master", "native_slave", "native_master", "native_refine_far_07_slave", "native_refine_far_07_master", "native_refine_far_09_slave", "native_refine_far_09_master", "native_refine_far_11_slave", "native_refine_far_11_master", "native_refine_far_12_5_slave", "native_refine_far_12_5_master", "native_refine_far_14_slave", "native_refine_far_14_master", "native_refine_far_16_slave", "native_refine_far_16_master")
    NATIVE_REFINE_SLAVE_FIELD_NUMBER: _ClassVar[int]
    NATIVE_REFINE_MASTER_FIELD_NUMBER: _ClassVar[int]
    NATIVE_REFINE_FAR_SLAVE_FIELD_NUMBER: _ClassVar[int]
    NATIVE_REFINE_FAR_MASTER_FIELD_NUMBER: _ClassVar[int]
    LENS_GUARDS_SLAVE_FIELD_NUMBER: _ClassVar[int]
    LENS_GUARDS_MASTER_FIELD_NUMBER: _ClassVar[int]
    WATER_PROOF_ABOVE_WATER_SLAVE_FIELD_NUMBER: _ClassVar[int]
    WATER_PROOF_ABOVE_WATER_MASTER_FIELD_NUMBER: _ClassVar[int]
    WATER_PROOF_UNDER_WATER_SLAVE_FIELD_NUMBER: _ClassVar[int]
    WATER_PROOF_UNDER_WATER_MASTER_FIELD_NUMBER: _ClassVar[int]
    NATIVE_SLAVE_FIELD_NUMBER: _ClassVar[int]
    NATIVE_MASTER_FIELD_NUMBER: _ClassVar[int]
    NATIVE_REFINE_FAR_07_SLAVE_FIELD_NUMBER: _ClassVar[int]
    NATIVE_REFINE_FAR_07_MASTER_FIELD_NUMBER: _ClassVar[int]
    NATIVE_REFINE_FAR_09_SLAVE_FIELD_NUMBER: _ClassVar[int]
    NATIVE_REFINE_FAR_09_MASTER_FIELD_NUMBER: _ClassVar[int]
    NATIVE_REFINE_FAR_11_SLAVE_FIELD_NUMBER: _ClassVar[int]
    NATIVE_REFINE_FAR_11_MASTER_FIELD_NUMBER: _ClassVar[int]
    NATIVE_REFINE_FAR_12_5_SLAVE_FIELD_NUMBER: _ClassVar[int]
    NATIVE_REFINE_FAR_12_5_MASTER_FIELD_NUMBER: _ClassVar[int]
    NATIVE_REFINE_FAR_14_SLAVE_FIELD_NUMBER: _ClassVar[int]
    NATIVE_REFINE_FAR_14_MASTER_FIELD_NUMBER: _ClassVar[int]
    NATIVE_REFINE_FAR_16_SLAVE_FIELD_NUMBER: _ClassVar[int]
    NATIVE_REFINE_FAR_16_MASTER_FIELD_NUMBER: _ClassVar[int]
    native_refine_slave: DewarpParams
    native_refine_master: DewarpParams
    native_refine_far_slave: DewarpParams
    native_refine_far_master: DewarpParams
    lens_guards_slave: DewarpParams
    lens_guards_master: DewarpParams
    water_proof_above_water_slave: DewarpParams
    water_proof_above_water_master: DewarpParams
    water_proof_under_water_slave: DewarpParams
    water_proof_under_water_master: DewarpParams
    native_slave: DewarpParams
    native_master: DewarpParams
    native_refine_far_07_slave: DewarpParams
    native_refine_far_07_master: DewarpParams
    native_refine_far_09_slave: DewarpParams
    native_refine_far_09_master: DewarpParams
    native_refine_far_11_slave: DewarpParams
    native_refine_far_11_master: DewarpParams
    native_refine_far_12_5_slave: DewarpParams
    native_refine_far_12_5_master: DewarpParams
    native_refine_far_14_slave: DewarpParams
    native_refine_far_14_master: DewarpParams
    native_refine_far_16_slave: DewarpParams
    native_refine_far_16_master: DewarpParams
    def __init__(self, native_refine_slave: _Optional[_Union[DewarpParams, _Mapping]] = ..., native_refine_master: _Optional[_Union[DewarpParams, _Mapping]] = ..., native_refine_far_slave: _Optional[_Union[DewarpParams, _Mapping]] = ..., native_refine_far_master: _Optional[_Union[DewarpParams, _Mapping]] = ..., lens_guards_slave: _Optional[_Union[DewarpParams, _Mapping]] = ..., lens_guards_master: _Optional[_Union[DewarpParams, _Mapping]] = ..., water_proof_above_water_slave: _Optional[_Union[DewarpParams, _Mapping]] = ..., water_proof_above_water_master: _Optional[_Union[DewarpParams, _Mapping]] = ..., water_proof_under_water_slave: _Optional[_Union[DewarpParams, _Mapping]] = ..., water_proof_under_water_master: _Optional[_Union[DewarpParams, _Mapping]] = ..., native_slave: _Optional[_Union[DewarpParams, _Mapping]] = ..., native_master: _Optional[_Union[DewarpParams, _Mapping]] = ..., native_refine_far_07_slave: _Optional[_Union[DewarpParams, _Mapping]] = ..., native_refine_far_07_master: _Optional[_Union[DewarpParams, _Mapping]] = ..., native_refine_far_09_slave: _Optional[_Union[DewarpParams, _Mapping]] = ..., native_refine_far_09_master: _Optional[_Union[DewarpParams, _Mapping]] = ..., native_refine_far_11_slave: _Optional[_Union[DewarpParams, _Mapping]] = ..., native_refine_far_11_master: _Optional[_Union[DewarpParams, _Mapping]] = ..., native_refine_far_12_5_slave: _Optional[_Union[DewarpParams, _Mapping]] = ..., native_refine_far_12_5_master: _Optional[_Union[DewarpParams, _Mapping]] = ..., native_refine_far_14_slave: _Optional[_Union[DewarpParams, _Mapping]] = ..., native_refine_far_14_master: _Optional[_Union[DewarpParams, _Mapping]] = ..., native_refine_far_16_slave: _Optional[_Union[DewarpParams, _Mapping]] = ..., native_refine_far_16_master: _Optional[_Union[DewarpParams, _Mapping]] = ...) -> None: ...

class AecAe(_message.Message):
    __slots__ = ("lv", "lux_idx", "short_linear_gain", "middle_linear_gain", "long_linear_gain", "adrc_gain", "dark_boost_gain", "ae_mode", "yltm_enable_flag")
    LV_FIELD_NUMBER: _ClassVar[int]
    LUX_IDX_FIELD_NUMBER: _ClassVar[int]
    SHORT_LINEAR_GAIN_FIELD_NUMBER: _ClassVar[int]
    MIDDLE_LINEAR_GAIN_FIELD_NUMBER: _ClassVar[int]
    LONG_LINEAR_GAIN_FIELD_NUMBER: _ClassVar[int]
    ADRC_GAIN_FIELD_NUMBER: _ClassVar[int]
    DARK_BOOST_GAIN_FIELD_NUMBER: _ClassVar[int]
    AE_MODE_FIELD_NUMBER: _ClassVar[int]
    YLTM_ENABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    lv: float
    lux_idx: float
    short_linear_gain: float
    middle_linear_gain: float
    long_linear_gain: float
    adrc_gain: float
    dark_boost_gain: float
    ae_mode: AeMode
    yltm_enable_flag: int
    def __init__(self, lv: _Optional[float] = ..., lux_idx: _Optional[float] = ..., short_linear_gain: _Optional[float] = ..., middle_linear_gain: _Optional[float] = ..., long_linear_gain: _Optional[float] = ..., adrc_gain: _Optional[float] = ..., dark_boost_gain: _Optional[float] = ..., ae_mode: _Optional[_Union[AeMode, str]] = ..., yltm_enable_flag: _Optional[int] = ...) -> None: ...

class AtomicGainInfo(_message.Message):
    __slots__ = ("sensor_again", "sensor_dgain", "isp_dgain", "cg_ratio", "sensor_again_s", "isp_dgain_s")
    SENSOR_AGAIN_FIELD_NUMBER: _ClassVar[int]
    SENSOR_DGAIN_FIELD_NUMBER: _ClassVar[int]
    ISP_DGAIN_FIELD_NUMBER: _ClassVar[int]
    CG_RATIO_FIELD_NUMBER: _ClassVar[int]
    SENSOR_AGAIN_S_FIELD_NUMBER: _ClassVar[int]
    ISP_DGAIN_S_FIELD_NUMBER: _ClassVar[int]
    sensor_again: int
    sensor_dgain: int
    isp_dgain: int
    cg_ratio: int
    sensor_again_s: int
    isp_dgain_s: int
    def __init__(self, sensor_again: _Optional[int] = ..., sensor_dgain: _Optional[int] = ..., isp_dgain: _Optional[int] = ..., cg_ratio: _Optional[int] = ..., sensor_again_s: _Optional[int] = ..., isp_dgain_s: _Optional[int] = ...) -> None: ...

class GacGainInfo(_message.Message):
    __slots__ = ("gac_enable", "isp_dgain", "gamma_dgain", "ccm_dgain", "drc_gtm_dgain", "drc_in_dgain", "drc_gamma_dgain", "gamma_knee_dgain", "dsp_dgain")
    GAC_ENABLE_FIELD_NUMBER: _ClassVar[int]
    ISP_DGAIN_FIELD_NUMBER: _ClassVar[int]
    GAMMA_DGAIN_FIELD_NUMBER: _ClassVar[int]
    CCM_DGAIN_FIELD_NUMBER: _ClassVar[int]
    DRC_GTM_DGAIN_FIELD_NUMBER: _ClassVar[int]
    DRC_IN_DGAIN_FIELD_NUMBER: _ClassVar[int]
    DRC_GAMMA_DGAIN_FIELD_NUMBER: _ClassVar[int]
    GAMMA_KNEE_DGAIN_FIELD_NUMBER: _ClassVar[int]
    DSP_DGAIN_FIELD_NUMBER: _ClassVar[int]
    gac_enable: bool
    isp_dgain: float
    gamma_dgain: float
    ccm_dgain: float
    drc_gtm_dgain: float
    drc_in_dgain: float
    drc_gamma_dgain: float
    gamma_knee_dgain: float
    dsp_dgain: float
    def __init__(self, gac_enable: _Optional[bool] = ..., isp_dgain: _Optional[float] = ..., gamma_dgain: _Optional[float] = ..., ccm_dgain: _Optional[float] = ..., drc_gtm_dgain: _Optional[float] = ..., drc_in_dgain: _Optional[float] = ..., drc_gamma_dgain: _Optional[float] = ..., gamma_knee_dgain: _Optional[float] = ..., dsp_dgain: _Optional[float] = ...) -> None: ...

class AecEagle(_message.Message):
    __slots__ = ("lv", "atomic_gain_info", "gac_gain_info")
    LV_FIELD_NUMBER: _ClassVar[int]
    ATOMIC_GAIN_INFO_FIELD_NUMBER: _ClassVar[int]
    GAC_GAIN_INFO_FIELD_NUMBER: _ClassVar[int]
    lv: int
    atomic_gain_info: AtomicGainInfo
    gac_gain_info: GacGainInfo
    def __init__(self, lv: _Optional[int] = ..., atomic_gain_info: _Optional[_Union[AtomicGainInfo, _Mapping]] = ..., gac_gain_info: _Optional[_Union[GacGainInfo, _Mapping]] = ...) -> None: ...

class ExpoBalanceMode(_message.Message):
    __slots__ = ("mode",)
    MODE_FIELD_NUMBER: _ClassVar[int]
    mode: int
    def __init__(self, mode: _Optional[int] = ...) -> None: ...

class Coordinate(_message.Message):
    __slots__ = ("fx", "fy")
    FX_FIELD_NUMBER: _ClassVar[int]
    FY_FIELD_NUMBER: _ClassVar[int]
    fx: float
    fy: float
    def __init__(self, fx: _Optional[float] = ..., fy: _Optional[float] = ...) -> None: ...

class TrackResultBox(_message.Message):
    __slots__ = ("vertex_top_left", "vertex_top_right", "vertex_bottom_left", "vertex_bottom_right")
    VERTEX_TOP_LEFT_FIELD_NUMBER: _ClassVar[int]
    VERTEX_TOP_RIGHT_FIELD_NUMBER: _ClassVar[int]
    VERTEX_BOTTOM_LEFT_FIELD_NUMBER: _ClassVar[int]
    VERTEX_BOTTOM_RIGHT_FIELD_NUMBER: _ClassVar[int]
    vertex_top_left: Coordinate
    vertex_top_right: Coordinate
    vertex_bottom_left: Coordinate
    vertex_bottom_right: Coordinate
    def __init__(self, vertex_top_left: _Optional[_Union[Coordinate, _Mapping]] = ..., vertex_top_right: _Optional[_Union[Coordinate, _Mapping]] = ..., vertex_bottom_left: _Optional[_Union[Coordinate, _Mapping]] = ..., vertex_bottom_right: _Optional[_Union[Coordinate, _Mapping]] = ...) -> None: ...

class Coordinate3D(_message.Message):
    __slots__ = ("x", "y", "z")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ...) -> None: ...

class TrackResultBox3D(_message.Message):
    __slots__ = ("vertex_top_left", "vertex_top_right", "vertex_bottom_left", "vertex_bottom_right")
    VERTEX_TOP_LEFT_FIELD_NUMBER: _ClassVar[int]
    VERTEX_TOP_RIGHT_FIELD_NUMBER: _ClassVar[int]
    VERTEX_BOTTOM_LEFT_FIELD_NUMBER: _ClassVar[int]
    VERTEX_BOTTOM_RIGHT_FIELD_NUMBER: _ClassVar[int]
    vertex_top_left: Coordinate3D
    vertex_top_right: Coordinate3D
    vertex_bottom_left: Coordinate3D
    vertex_bottom_right: Coordinate3D
    def __init__(self, vertex_top_left: _Optional[_Union[Coordinate3D, _Mapping]] = ..., vertex_top_right: _Optional[_Union[Coordinate3D, _Mapping]] = ..., vertex_bottom_left: _Optional[_Union[Coordinate3D, _Mapping]] = ..., vertex_bottom_right: _Optional[_Union[Coordinate3D, _Mapping]] = ...) -> None: ...

class TrackRoiBox(_message.Message):
    __slots__ = ("roi_id", "roi_box")
    ROI_ID_FIELD_NUMBER: _ClassVar[int]
    ROI_BOX_FIELD_NUMBER: _ClassVar[int]
    roi_id: int
    roi_box: TrackResultBox3D
    def __init__(self, roi_id: _Optional[int] = ..., roi_box: _Optional[_Union[TrackResultBox3D, _Mapping]] = ...) -> None: ...

class TrackRoiBoxListSurround(_message.Message):
    __slots__ = ("is_check_valid", "roi_frame_id", "real_frame_id", "main_roi_id", "roi_box_face_list", "roi_box_body_list")
    IS_CHECK_VALID_FIELD_NUMBER: _ClassVar[int]
    ROI_FRAME_ID_FIELD_NUMBER: _ClassVar[int]
    REAL_FRAME_ID_FIELD_NUMBER: _ClassVar[int]
    MAIN_ROI_ID_FIELD_NUMBER: _ClassVar[int]
    ROI_BOX_FACE_LIST_FIELD_NUMBER: _ClassVar[int]
    ROI_BOX_BODY_LIST_FIELD_NUMBER: _ClassVar[int]
    is_check_valid: bool
    roi_frame_id: int
    real_frame_id: int
    main_roi_id: int
    roi_box_face_list: _containers.RepeatedCompositeFieldContainer[TrackRoiBox]
    roi_box_body_list: _containers.RepeatedCompositeFieldContainer[TrackRoiBox]
    def __init__(self, is_check_valid: _Optional[bool] = ..., roi_frame_id: _Optional[int] = ..., real_frame_id: _Optional[int] = ..., main_roi_id: _Optional[int] = ..., roi_box_face_list: _Optional[_Iterable[_Union[TrackRoiBox, _Mapping]]] = ..., roi_box_body_list: _Optional[_Iterable[_Union[TrackRoiBox, _Mapping]]] = ...) -> None: ...

class AIMOTDataVersion(_message.Message):
    __slots__ = ("ai_mot_version",)
    AI_MOT_VERSION_FIELD_NUMBER: _ClassVar[int]
    ai_mot_version: int
    def __init__(self, ai_mot_version: _Optional[int] = ...) -> None: ...

class ObjGroup2DBoxWithDistance(_message.Message):
    __slots__ = ("obj_id", "obj_type", "obj_state", "cx", "cy", "w", "h", "distance")
    OBJ_ID_FIELD_NUMBER: _ClassVar[int]
    OBJ_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJ_STATE_FIELD_NUMBER: _ClassVar[int]
    CX_FIELD_NUMBER: _ClassVar[int]
    CY_FIELD_NUMBER: _ClassVar[int]
    W_FIELD_NUMBER: _ClassVar[int]
    H_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_FIELD_NUMBER: _ClassVar[int]
    obj_id: int
    obj_type: str
    obj_state: AiMotObjState
    cx: int
    cy: int
    w: int
    h: int
    distance: int
    def __init__(self, obj_id: _Optional[int] = ..., obj_type: _Optional[str] = ..., obj_state: _Optional[_Union[AiMotObjState, str]] = ..., cx: _Optional[int] = ..., cy: _Optional[int] = ..., w: _Optional[int] = ..., h: _Optional[int] = ..., distance: _Optional[int] = ...) -> None: ...

class AIMOTData(_message.Message):
    __slots__ = ("third_party_model", "model_name", "ai_mot_timestamp_ms", "ai_mot_total_detected_obj_count", "ai_mot_obj_count", "ai_mot_obj_data")
    THIRD_PARTY_MODEL_FIELD_NUMBER: _ClassVar[int]
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    AI_MOT_TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
    AI_MOT_TOTAL_DETECTED_OBJ_COUNT_FIELD_NUMBER: _ClassVar[int]
    AI_MOT_OBJ_COUNT_FIELD_NUMBER: _ClassVar[int]
    AI_MOT_OBJ_DATA_FIELD_NUMBER: _ClassVar[int]
    third_party_model: int
    model_name: str
    ai_mot_timestamp_ms: int
    ai_mot_total_detected_obj_count: int
    ai_mot_obj_count: int
    ai_mot_obj_data: _containers.RepeatedCompositeFieldContainer[ObjGroup2DBoxWithDistance]
    def __init__(self, third_party_model: _Optional[int] = ..., model_name: _Optional[str] = ..., ai_mot_timestamp_ms: _Optional[int] = ..., ai_mot_total_detected_obj_count: _Optional[int] = ..., ai_mot_obj_count: _Optional[int] = ..., ai_mot_obj_data: _Optional[_Iterable[_Union[ObjGroup2DBoxWithDistance, _Mapping]]] = ...) -> None: ...

class EbikeGps(_message.Message):
    __slots__ = ("gps_basic",)
    GPS_BASIC_FIELD_NUMBER: _ClassVar[int]
    gps_basic: GpsBasic
    def __init__(self, gps_basic: _Optional[_Union[GpsBasic, _Mapping]] = ...) -> None: ...

class EbikeAcc(_message.Message):
    __slots__ = ("ebike_acc",)
    EBIKE_ACC_FIELD_NUMBER: _ClassVar[int]
    ebike_acc: Accelerometer
    def __init__(self, ebike_acc: _Optional[_Union[Accelerometer, _Mapping]] = ...) -> None: ...

class EbikeTiltAngle(_message.Message):
    __slots__ = ("tilt_angle",)
    TILT_ANGLE_FIELD_NUMBER: _ClassVar[int]
    tilt_angle: float
    def __init__(self, tilt_angle: _Optional[float] = ...) -> None: ...

class EbikeMotorPower(_message.Message):
    __slots__ = ("power",)
    POWER_FIELD_NUMBER: _ClassVar[int]
    power: int
    def __init__(self, power: _Optional[int] = ...) -> None: ...

class EbikePedalingPower(_message.Message):
    __slots__ = ("power",)
    POWER_FIELD_NUMBER: _ClassVar[int]
    power: int
    def __init__(self, power: _Optional[int] = ...) -> None: ...

class EbikeCadence(_message.Message):
    __slots__ = ("cadence",)
    CADENCE_FIELD_NUMBER: _ClassVar[int]
    cadence: int
    def __init__(self, cadence: _Optional[int] = ...) -> None: ...

class EbikeMotorTorque(_message.Message):
    __slots__ = ("torque",)
    TORQUE_FIELD_NUMBER: _ClassVar[int]
    torque: int
    def __init__(self, torque: _Optional[int] = ...) -> None: ...

class EbikePedalingTorque(_message.Message):
    __slots__ = ("torque",)
    TORQUE_FIELD_NUMBER: _ClassVar[int]
    torque: int
    def __init__(self, torque: _Optional[int] = ...) -> None: ...

class EbikeSpeed(_message.Message):
    __slots__ = ("speed",)
    SPEED_FIELD_NUMBER: _ClassVar[int]
    speed: float
    def __init__(self, speed: _Optional[float] = ...) -> None: ...

class EbikeMileage(_message.Message):
    __slots__ = ("mileage",)
    MILEAGE_FIELD_NUMBER: _ClassVar[int]
    mileage: float
    def __init__(self, mileage: _Optional[float] = ...) -> None: ...

class EbikeSlope(_message.Message):
    __slots__ = ("slope",)
    SLOPE_FIELD_NUMBER: _ClassVar[int]
    slope: float
    def __init__(self, slope: _Optional[float] = ...) -> None: ...

class HeartRate(_message.Message):
    __slots__ = ("heartrate",)
    HEARTRATE_FIELD_NUMBER: _ClassVar[int]
    heartrate: int
    def __init__(self, heartrate: _Optional[int] = ...) -> None: ...

class EbikePressure(_message.Message):
    __slots__ = ("pressure",)
    PRESSURE_FIELD_NUMBER: _ClassVar[int]
    pressure: int
    def __init__(self, pressure: _Optional[int] = ...) -> None: ...

class EbikeCalories(_message.Message):
    __slots__ = ("calories",)
    CALORIES_FIELD_NUMBER: _ClassVar[int]
    calories: int
    def __init__(self, calories: _Optional[int] = ...) -> None: ...

class YltmEnable(_message.Message):
    __slots__ = ("enable",)
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    enable: int
    def __init__(self, enable: _Optional[int] = ...) -> None: ...

class ExtriLensMode(_message.Message):
    __slots__ = ("mode",)
    class ExtriLensModeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXTRI_LENS_MODE_NATIVE_REFINE: _ClassVar[ExtriLensMode.ExtriLensModeType]
        EXTRI_LENS_MODE_LENS_GUARDS: _ClassVar[ExtriLensMode.ExtriLensModeType]
        EXTRI_LENS_MODE_WATER_PROOF_UNDER_WATER: _ClassVar[ExtriLensMode.ExtriLensModeType]
    EXTRI_LENS_MODE_NATIVE_REFINE: ExtriLensMode.ExtriLensModeType
    EXTRI_LENS_MODE_LENS_GUARDS: ExtriLensMode.ExtriLensModeType
    EXTRI_LENS_MODE_WATER_PROOF_UNDER_WATER: ExtriLensMode.ExtriLensModeType
    MODE_FIELD_NUMBER: _ClassVar[int]
    mode: ExtriLensMode.ExtriLensModeType
    def __init__(self, mode: _Optional[_Union[ExtriLensMode.ExtriLensModeType, str]] = ...) -> None: ...

class ShadingCalibModeNum(_message.Message):
    __slots__ = ("num",)
    NUM_FIELD_NUMBER: _ClassVar[int]
    num: int
    def __init__(self, num: _Optional[int] = ...) -> None: ...

class AnyAspectRatioExport(_message.Message):
    __slots__ = ("support", "has_black_corner")
    SUPPORT_FIELD_NUMBER: _ClassVar[int]
    HAS_BLACK_CORNER_FIELD_NUMBER: _ClassVar[int]
    support: int
    has_black_corner: int
    def __init__(self, support: _Optional[int] = ..., has_black_corner: _Optional[int] = ...) -> None: ...

class StyleFilterMode(_message.Message):
    __slots__ = ("mode",)
    MODE_FIELD_NUMBER: _ClassVar[int]
    mode: int
    def __init__(self, mode: _Optional[int] = ...) -> None: ...

class BeautyParams(_message.Message):
    __slots__ = ("enable", "face_temperature", "face_whiten", "face_smooth")
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    FACE_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    FACE_WHITEN_FIELD_NUMBER: _ClassVar[int]
    FACE_SMOOTH_FIELD_NUMBER: _ClassVar[int]
    enable: int
    face_temperature: int
    face_whiten: int
    face_smooth: int
    def __init__(self, enable: _Optional[int] = ..., face_temperature: _Optional[int] = ..., face_whiten: _Optional[int] = ..., face_smooth: _Optional[int] = ...) -> None: ...

class VideoType(_message.Message):
    __slots__ = ("type",)
    class VideoTypes(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VIDEO_TYPE_NONE: _ClassVar[VideoType.VideoTypes]
        VIDEO_TYPE_BOKERH: _ClassVar[VideoType.VideoTypes]
        VIDEO_TYPE_BOKERH_ORIGINAL: _ClassVar[VideoType.VideoTypes]
    VIDEO_TYPE_NONE: VideoType.VideoTypes
    VIDEO_TYPE_BOKERH: VideoType.VideoTypes
    VIDEO_TYPE_BOKERH_ORIGINAL: VideoType.VideoTypes
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: VideoType.VideoTypes
    def __init__(self, type: _Optional[_Union[VideoType.VideoTypes, str]] = ...) -> None: ...

class FlightPoseNavi(_message.Message):
    __slots__ = ("imu_flag", "position", "velocity", "quaternion")
    IMU_FLAG_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    VELOCITY_FIELD_NUMBER: _ClassVar[int]
    QUATERNION_FIELD_NUMBER: _ClassVar[int]
    imu_flag: int
    position: Position
    velocity: Velocity
    quaternion: Quaternion
    def __init__(self, imu_flag: _Optional[int] = ..., position: _Optional[_Union[Position, _Mapping]] = ..., velocity: _Optional[_Union[Velocity, _Mapping]] = ..., quaternion: _Optional[_Union[Quaternion, _Mapping]] = ...) -> None: ...
