"""autogenerated by genmsg_py from imu.msg. Do not edit."""
import roslib.message
import struct


class imu(roslib.message.Message):
  _md5sum = "4ed31225b8988ef9b0cd0b234eb0aa9b"
  _type = "glados_sensors/imu"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float32 bearing
float32 gx
float32 gy

"""
  __slots__ = ['bearing','gx','gy']
  _slot_types = ['float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       bearing,gx,gy
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(imu, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.bearing is None:
        self.bearing = 0.
      if self.gx is None:
        self.gx = 0.
      if self.gy is None:
        self.gy = 0.
    else:
      self.bearing = 0.
      self.gx = 0.
      self.gy = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    @param buff: buffer
    @type  buff: StringIO
    """
    try:
      _x = self
      buff.write(_struct_3f.pack(_x.bearing, _x.gx, _x.gy))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    @param str: byte array of serialized message
    @type  str: str
    """
    try:
      end = 0
      _x = self
      start = end
      end += 12
      (_x.bearing, _x.gx, _x.gy,) = _struct_3f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    @param buff: buffer
    @type  buff: StringIO
    @param numpy: numpy python module
    @type  numpy module
    """
    try:
      _x = self
      buff.write(_struct_3f.pack(_x.bearing, _x.gx, _x.gy))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    @param str: byte array of serialized message
    @type  str: str
    @param numpy: numpy python module
    @type  numpy: module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 12
      (_x.bearing, _x.gx, _x.gy,) = _struct_3f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
_struct_3f = struct.Struct("<3f")