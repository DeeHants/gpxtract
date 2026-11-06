import dvtm_library_pb2 as _dvtm_library_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProductMeta(_message.Message):
    __slots__ = ("clip_meta", "stream_meta", "frame_meta")
    CLIP_META_FIELD_NUMBER: _ClassVar[int]
    STREAM_META_FIELD_NUMBER: _ClassVar[int]
    FRAME_META_FIELD_NUMBER: _ClassVar[int]
    clip_meta: ClipMeta
    stream_meta: StreamMeta
    frame_meta: FrameMeta
    def __init__(self, clip_meta: _Optional[_Union[ClipMeta, _Mapping]] = ..., stream_meta: _Optional[_Union[StreamMeta, _Mapping]] = ..., frame_meta: _Optional[_Union[FrameMeta, _Mapping]] = ...) -> None: ...

class ClipMeta(_message.Message):
    __slots__ = ("clip_meta_header", "clip_streams_meta", "distortion_coefficients", "sensor_readout_time", "sensor_read_direction", "digital_focal_length", "eis_status", "imu_sampling_rate", "sensor_fps", "ITD_value", "LRO_value", "sensor_res", "f_number", "style_filter_mode", "yltm_enable")
    CLIP_META_HEADER_FIELD_NUMBER: _ClassVar[int]
    CLIP_STREAMS_META_FIELD_NUMBER: _ClassVar[int]
    DISTORTION_COEFFICIENTS_FIELD_NUMBER: _ClassVar[int]
    SENSOR_READOUT_TIME_FIELD_NUMBER: _ClassVar[int]
    SENSOR_READ_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    DIGITAL_FOCAL_LENGTH_FIELD_NUMBER: _ClassVar[int]
    EIS_STATUS_FIELD_NUMBER: _ClassVar[int]
    IMU_SAMPLING_RATE_FIELD_NUMBER: _ClassVar[int]
    SENSOR_FPS_FIELD_NUMBER: _ClassVar[int]
    ITD_VALUE_FIELD_NUMBER: _ClassVar[int]
    LRO_VALUE_FIELD_NUMBER: _ClassVar[int]
    SENSOR_RES_FIELD_NUMBER: _ClassVar[int]
    F_NUMBER_FIELD_NUMBER: _ClassVar[int]
    STYLE_FILTER_MODE_FIELD_NUMBER: _ClassVar[int]
    YLTM_ENABLE_FIELD_NUMBER: _ClassVar[int]
    clip_meta_header: _dvtm_library_pb2.ClipMetaHeader
    clip_streams_meta: _dvtm_library_pb2.ClipStreamsMeta
    distortion_coefficients: _dvtm_library_pb2.LensDistortionCoefficients
    sensor_readout_time: _dvtm_library_pb2.SensorFrameReadOutTime
    sensor_read_direction: _dvtm_library_pb2.SensorReadDirection
    digital_focal_length: _dvtm_library_pb2.DigitalFocalLength
    eis_status: _dvtm_library_pb2.EisStatus
    imu_sampling_rate: _dvtm_library_pb2.IMUSamplingRate
    sensor_fps: _dvtm_library_pb2.SensorFrameRate
    ITD_value: _dvtm_library_pb2.ITDValue
    LRO_value: _dvtm_library_pb2.LROValue
    sensor_res: _dvtm_library_pb2.SensorRes
    f_number: _dvtm_library_pb2.FNumber
    style_filter_mode: _dvtm_library_pb2.StyleFilterMode
    yltm_enable: _dvtm_library_pb2.YltmEnable
    def __init__(self, clip_meta_header: _Optional[_Union[_dvtm_library_pb2.ClipMetaHeader, _Mapping]] = ..., clip_streams_meta: _Optional[_Union[_dvtm_library_pb2.ClipStreamsMeta, _Mapping]] = ..., distortion_coefficients: _Optional[_Union[_dvtm_library_pb2.LensDistortionCoefficients, _Mapping]] = ..., sensor_readout_time: _Optional[_Union[_dvtm_library_pb2.SensorFrameReadOutTime, _Mapping]] = ..., sensor_read_direction: _Optional[_Union[_dvtm_library_pb2.SensorReadDirection, _Mapping]] = ..., digital_focal_length: _Optional[_Union[_dvtm_library_pb2.DigitalFocalLength, _Mapping]] = ..., eis_status: _Optional[_Union[_dvtm_library_pb2.EisStatus, _Mapping]] = ..., imu_sampling_rate: _Optional[_Union[_dvtm_library_pb2.IMUSamplingRate, _Mapping]] = ..., sensor_fps: _Optional[_Union[_dvtm_library_pb2.SensorFrameRate, _Mapping]] = ..., ITD_value: _Optional[_Union[_dvtm_library_pb2.ITDValue, _Mapping]] = ..., LRO_value: _Optional[_Union[_dvtm_library_pb2.LROValue, _Mapping]] = ..., sensor_res: _Optional[_Union[_dvtm_library_pb2.SensorRes, _Mapping]] = ..., f_number: _Optional[_Union[_dvtm_library_pb2.FNumber, _Mapping]] = ..., style_filter_mode: _Optional[_Union[_dvtm_library_pb2.StyleFilterMode, _Mapping]] = ..., yltm_enable: _Optional[_Union[_dvtm_library_pb2.YltmEnable, _Mapping]] = ...) -> None: ...

class StreamMeta(_message.Message):
    __slots__ = ("stream_meta_header", "video_stream_meta", "color_mode", "fov_type", "pano_dewarp_params", "extri_lens_mode", "shading_calib_mode_num")
    STREAM_META_HEADER_FIELD_NUMBER: _ClassVar[int]
    VIDEO_STREAM_META_FIELD_NUMBER: _ClassVar[int]
    COLOR_MODE_FIELD_NUMBER: _ClassVar[int]
    FOV_TYPE_FIELD_NUMBER: _ClassVar[int]
    PANO_DEWARP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    EXTRI_LENS_MODE_FIELD_NUMBER: _ClassVar[int]
    SHADING_CALIB_MODE_NUM_FIELD_NUMBER: _ClassVar[int]
    stream_meta_header: _dvtm_library_pb2.StreamMetaHeader
    video_stream_meta: _dvtm_library_pb2.VideoStreamMeta
    color_mode: _dvtm_library_pb2.ColorMode
    fov_type: _dvtm_library_pb2.FOVType
    pano_dewarp_params: _dvtm_library_pb2.PanoDewarpParams
    extri_lens_mode: _dvtm_library_pb2.ExtriLensMode
    shading_calib_mode_num: _dvtm_library_pb2.ShadingCalibModeNum
    def __init__(self, stream_meta_header: _Optional[_Union[_dvtm_library_pb2.StreamMetaHeader, _Mapping]] = ..., video_stream_meta: _Optional[_Union[_dvtm_library_pb2.VideoStreamMeta, _Mapping]] = ..., color_mode: _Optional[_Union[_dvtm_library_pb2.ColorMode, _Mapping]] = ..., fov_type: _Optional[_Union[_dvtm_library_pb2.FOVType, _Mapping]] = ..., pano_dewarp_params: _Optional[_Union[_dvtm_library_pb2.PanoDewarpParams, _Mapping]] = ..., extri_lens_mode: _Optional[_Union[_dvtm_library_pb2.ExtriLensMode, _Mapping]] = ..., shading_calib_mode_num: _Optional[_Union[_dvtm_library_pb2.ShadingCalibModeNum, _Mapping]] = ...) -> None: ...

class FrameMeta(_message.Message):
    __slots__ = ("frame_meta_header", "camera_frame_meta", "imu_frame_meta", "gimbal_frame_meta", "ebike_frame_meta")
    FRAME_META_HEADER_FIELD_NUMBER: _ClassVar[int]
    CAMERA_FRAME_META_FIELD_NUMBER: _ClassVar[int]
    IMU_FRAME_META_FIELD_NUMBER: _ClassVar[int]
    GIMBAL_FRAME_META_FIELD_NUMBER: _ClassVar[int]
    EBIKE_FRAME_META_FIELD_NUMBER: _ClassVar[int]
    frame_meta_header: _dvtm_library_pb2.FrameMetaHeader
    camera_frame_meta: FrameMetaOfCamera
    imu_frame_meta: FrameMetaOfIMU
    gimbal_frame_meta: FrameMetaOfGimbal
    ebike_frame_meta: FrameMetaOfEbike
    def __init__(self, frame_meta_header: _Optional[_Union[_dvtm_library_pb2.FrameMetaHeader, _Mapping]] = ..., camera_frame_meta: _Optional[_Union[FrameMetaOfCamera, _Mapping]] = ..., imu_frame_meta: _Optional[_Union[FrameMetaOfIMU, _Mapping]] = ..., gimbal_frame_meta: _Optional[_Union[FrameMetaOfGimbal, _Mapping]] = ..., ebike_frame_meta: _Optional[_Union[FrameMetaOfEbike, _Mapping]] = ...) -> None: ...

class FrameMetaOfCamera(_message.Message):
    __slots__ = ("camera_dev_header", "exposure_index", "iso", "exposure_time", "digital_zoom_ratio", "white_balance_cct", "orientation", "current_underwater_confidence", "camera_attitude", "camera_acc", "sharpness", "denoising", "track_ret", "aec_ae", "sensor_temperature", "equivalent_focal_length")
    CAMERA_DEV_HEADER_FIELD_NUMBER: _ClassVar[int]
    EXPOSURE_INDEX_FIELD_NUMBER: _ClassVar[int]
    ISO_FIELD_NUMBER: _ClassVar[int]
    EXPOSURE_TIME_FIELD_NUMBER: _ClassVar[int]
    DIGITAL_ZOOM_RATIO_FIELD_NUMBER: _ClassVar[int]
    WHITE_BALANCE_CCT_FIELD_NUMBER: _ClassVar[int]
    ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    CURRENT_UNDERWATER_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    CAMERA_ATTITUDE_FIELD_NUMBER: _ClassVar[int]
    CAMERA_ACC_FIELD_NUMBER: _ClassVar[int]
    SHARPNESS_FIELD_NUMBER: _ClassVar[int]
    DENOISING_FIELD_NUMBER: _ClassVar[int]
    TRACK_RET_FIELD_NUMBER: _ClassVar[int]
    AEC_AE_FIELD_NUMBER: _ClassVar[int]
    SENSOR_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    EQUIVALENT_FOCAL_LENGTH_FIELD_NUMBER: _ClassVar[int]
    camera_dev_header: _dvtm_library_pb2.MetaHeaderOfDevice
    exposure_index: _dvtm_library_pb2.ExposureIndex
    iso: _dvtm_library_pb2.ISO
    exposure_time: _dvtm_library_pb2.ExposureTime
    digital_zoom_ratio: _dvtm_library_pb2.DigitalZoomRatio
    white_balance_cct: _dvtm_library_pb2.WhiteBalanceCCT
    orientation: _dvtm_library_pb2.Orientation
    current_underwater_confidence: _dvtm_library_pb2.CurrentUnderwaterConfidence
    camera_attitude: _dvtm_library_pb2.Quaternion
    camera_acc: _dvtm_library_pb2.Accelerometer
    sharpness: _dvtm_library_pb2.Sharpness
    denoising: _dvtm_library_pb2.NoiseReductionApplied
    track_ret: _dvtm_library_pb2.TrackResultBox
    aec_ae: _dvtm_library_pb2.AecAe
    sensor_temperature: _dvtm_library_pb2.SensorTemperature
    equivalent_focal_length: _dvtm_library_pb2.EquivalentFocalLength
    def __init__(self, camera_dev_header: _Optional[_Union[_dvtm_library_pb2.MetaHeaderOfDevice, _Mapping]] = ..., exposure_index: _Optional[_Union[_dvtm_library_pb2.ExposureIndex, _Mapping]] = ..., iso: _Optional[_Union[_dvtm_library_pb2.ISO, _Mapping]] = ..., exposure_time: _Optional[_Union[_dvtm_library_pb2.ExposureTime, _Mapping]] = ..., digital_zoom_ratio: _Optional[_Union[_dvtm_library_pb2.DigitalZoomRatio, _Mapping]] = ..., white_balance_cct: _Optional[_Union[_dvtm_library_pb2.WhiteBalanceCCT, _Mapping]] = ..., orientation: _Optional[_Union[_dvtm_library_pb2.Orientation, _Mapping]] = ..., current_underwater_confidence: _Optional[_Union[_dvtm_library_pb2.CurrentUnderwaterConfidence, _Mapping]] = ..., camera_attitude: _Optional[_Union[_dvtm_library_pb2.Quaternion, _Mapping]] = ..., camera_acc: _Optional[_Union[_dvtm_library_pb2.Accelerometer, _Mapping]] = ..., sharpness: _Optional[_Union[_dvtm_library_pb2.Sharpness, _Mapping]] = ..., denoising: _Optional[_Union[_dvtm_library_pb2.NoiseReductionApplied, _Mapping]] = ..., track_ret: _Optional[_Union[_dvtm_library_pb2.TrackResultBox, _Mapping]] = ..., aec_ae: _Optional[_Union[_dvtm_library_pb2.AecAe, _Mapping]] = ..., sensor_temperature: _Optional[_Union[_dvtm_library_pb2.SensorTemperature, _Mapping]] = ..., equivalent_focal_length: _Optional[_Union[_dvtm_library_pb2.EquivalentFocalLength, _Mapping]] = ...) -> None: ...

class FrameMetaOfIMU(_message.Message):
    __slots__ = ("IMU_dev_header", "IMU_attitude_after_fusion", "IMU_vsync_pos")
    IMU_DEV_HEADER_FIELD_NUMBER: _ClassVar[int]
    IMU_ATTITUDE_AFTER_FUSION_FIELD_NUMBER: _ClassVar[int]
    IMU_VSYNC_POS_FIELD_NUMBER: _ClassVar[int]
    IMU_dev_header: _dvtm_library_pb2.MetaHeaderOfDevice
    IMU_attitude_after_fusion: _dvtm_library_pb2.DeviceMultiAttitude
    IMU_vsync_pos: _dvtm_library_pb2.ImuVsyncPos
    def __init__(self, IMU_dev_header: _Optional[_Union[_dvtm_library_pb2.MetaHeaderOfDevice, _Mapping]] = ..., IMU_attitude_after_fusion: _Optional[_Union[_dvtm_library_pb2.DeviceMultiAttitude, _Mapping]] = ..., IMU_vsync_pos: _Optional[_Union[_dvtm_library_pb2.ImuVsyncPos, _Mapping]] = ...) -> None: ...

class FrameMetaOfGimbal(_message.Message):
    __slots__ = ("gimbal_dev_header", "gps_basic", "velocity")
    GIMBAL_DEV_HEADER_FIELD_NUMBER: _ClassVar[int]
    GPS_BASIC_FIELD_NUMBER: _ClassVar[int]
    VELOCITY_FIELD_NUMBER: _ClassVar[int]
    gimbal_dev_header: _dvtm_library_pb2.MetaHeaderOfDevice
    gps_basic: _dvtm_library_pb2.GpsBasic
    velocity: _dvtm_library_pb2.Velocity
    def __init__(self, gimbal_dev_header: _Optional[_Union[_dvtm_library_pb2.MetaHeaderOfDevice, _Mapping]] = ..., gps_basic: _Optional[_Union[_dvtm_library_pb2.GpsBasic, _Mapping]] = ..., velocity: _Optional[_Union[_dvtm_library_pb2.Velocity, _Mapping]] = ...) -> None: ...

class FrameMetaOfEbike(_message.Message):
    __slots__ = ("ebike_dev_header", "ebike_gps", "ebike_acc", "tilt_angle", "motor_power", "pedaling_power", "cadence", "motor_torque", "pedaling_torque", "slope", "mileage", "speed", "heart_rate", "pressure", "calories")
    EBIKE_DEV_HEADER_FIELD_NUMBER: _ClassVar[int]
    EBIKE_GPS_FIELD_NUMBER: _ClassVar[int]
    EBIKE_ACC_FIELD_NUMBER: _ClassVar[int]
    TILT_ANGLE_FIELD_NUMBER: _ClassVar[int]
    MOTOR_POWER_FIELD_NUMBER: _ClassVar[int]
    PEDALING_POWER_FIELD_NUMBER: _ClassVar[int]
    CADENCE_FIELD_NUMBER: _ClassVar[int]
    MOTOR_TORQUE_FIELD_NUMBER: _ClassVar[int]
    PEDALING_TORQUE_FIELD_NUMBER: _ClassVar[int]
    SLOPE_FIELD_NUMBER: _ClassVar[int]
    MILEAGE_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    HEART_RATE_FIELD_NUMBER: _ClassVar[int]
    PRESSURE_FIELD_NUMBER: _ClassVar[int]
    CALORIES_FIELD_NUMBER: _ClassVar[int]
    ebike_dev_header: _dvtm_library_pb2.MetaHeaderOfDevice
    ebike_gps: _dvtm_library_pb2.EbikeGps
    ebike_acc: _dvtm_library_pb2.EbikeAcc
    tilt_angle: _dvtm_library_pb2.EbikeTiltAngle
    motor_power: _dvtm_library_pb2.EbikeMotorPower
    pedaling_power: _dvtm_library_pb2.EbikePedalingPower
    cadence: _dvtm_library_pb2.EbikeCadence
    motor_torque: _dvtm_library_pb2.EbikeMotorTorque
    pedaling_torque: _dvtm_library_pb2.EbikePedalingTorque
    slope: _dvtm_library_pb2.EbikeSlope
    mileage: _dvtm_library_pb2.EbikeMileage
    speed: _dvtm_library_pb2.EbikeSpeed
    heart_rate: _dvtm_library_pb2.HeartRate
    pressure: _dvtm_library_pb2.EbikePressure
    calories: _dvtm_library_pb2.EbikeCalories
    def __init__(self, ebike_dev_header: _Optional[_Union[_dvtm_library_pb2.MetaHeaderOfDevice, _Mapping]] = ..., ebike_gps: _Optional[_Union[_dvtm_library_pb2.EbikeGps, _Mapping]] = ..., ebike_acc: _Optional[_Union[_dvtm_library_pb2.EbikeAcc, _Mapping]] = ..., tilt_angle: _Optional[_Union[_dvtm_library_pb2.EbikeTiltAngle, _Mapping]] = ..., motor_power: _Optional[_Union[_dvtm_library_pb2.EbikeMotorPower, _Mapping]] = ..., pedaling_power: _Optional[_Union[_dvtm_library_pb2.EbikePedalingPower, _Mapping]] = ..., cadence: _Optional[_Union[_dvtm_library_pb2.EbikeCadence, _Mapping]] = ..., motor_torque: _Optional[_Union[_dvtm_library_pb2.EbikeMotorTorque, _Mapping]] = ..., pedaling_torque: _Optional[_Union[_dvtm_library_pb2.EbikePedalingTorque, _Mapping]] = ..., slope: _Optional[_Union[_dvtm_library_pb2.EbikeSlope, _Mapping]] = ..., mileage: _Optional[_Union[_dvtm_library_pb2.EbikeMileage, _Mapping]] = ..., speed: _Optional[_Union[_dvtm_library_pb2.EbikeSpeed, _Mapping]] = ..., heart_rate: _Optional[_Union[_dvtm_library_pb2.HeartRate, _Mapping]] = ..., pressure: _Optional[_Union[_dvtm_library_pb2.EbikePressure, _Mapping]] = ..., calories: _Optional[_Union[_dvtm_library_pb2.EbikeCalories, _Mapping]] = ...) -> None: ...
