# Copyright 2019 The Google Research Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pylint: skip-file
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: model_metrics.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='model_metrics.proto',
  package='nasbench',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x13model_metrics.proto\x12\x08nasbench\"s\n\x0cModelMetrics\x12\x31\n\x0f\x65valuation_data\x18\x01 \x03(\x0b\x32\x18.nasbench.EvaluationData\x12\x1c\n\x14trainable_parameters\x18\x02 \x01(\x05\x12\x12\n\ntotal_time\x18\x03 \x01(\x01\"\xa3\x01\n\x0e\x45valuationData\x12\x15\n\rcurrent_epoch\x18\x01 \x01(\x01\x12\x15\n\rtraining_time\x18\x02 \x01(\x01\x12\x16\n\x0etrain_accuracy\x18\x03 \x01(\x01\x12\x1b\n\x13validation_accuracy\x18\x04 \x01(\x01\x12\x15\n\rtest_accuracy\x18\x05 \x01(\x01\x12\x17\n\x0f\x63heckpoint_path\x18\x06 \x01(\t')
)




_MODELMETRICS = _descriptor.Descriptor(
  name='ModelMetrics',
  full_name='nasbench.ModelMetrics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='evaluation_data', full_name='nasbench.ModelMetrics.evaluation_data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trainable_parameters', full_name='nasbench.ModelMetrics.trainable_parameters', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_time', full_name='nasbench.ModelMetrics.total_time', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=148,
)


_EVALUATIONDATA = _descriptor.Descriptor(
  name='EvaluationData',
  full_name='nasbench.EvaluationData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='current_epoch', full_name='nasbench.EvaluationData.current_epoch', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='training_time', full_name='nasbench.EvaluationData.training_time', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='train_accuracy', full_name='nasbench.EvaluationData.train_accuracy', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validation_accuracy', full_name='nasbench.EvaluationData.validation_accuracy', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='test_accuracy', full_name='nasbench.EvaluationData.test_accuracy', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkpoint_path', full_name='nasbench.EvaluationData.checkpoint_path', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=151,
  serialized_end=314,
)

_MODELMETRICS.fields_by_name['evaluation_data'].message_type = _EVALUATIONDATA
DESCRIPTOR.message_types_by_name['ModelMetrics'] = _MODELMETRICS
DESCRIPTOR.message_types_by_name['EvaluationData'] = _EVALUATIONDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ModelMetrics = _reflection.GeneratedProtocolMessageType('ModelMetrics', (_message.Message,), dict(
  DESCRIPTOR = _MODELMETRICS,
  __module__ = 'model_metrics_pb2'
  # @@protoc_insertion_point(class_scope:nasbench.ModelMetrics)
  ))
_sym_db.RegisterMessage(ModelMetrics)

EvaluationData = _reflection.GeneratedProtocolMessageType('EvaluationData', (_message.Message,), dict(
  DESCRIPTOR = _EVALUATIONDATA,
  __module__ = 'model_metrics_pb2'
  # @@protoc_insertion_point(class_scope:nasbench.EvaluationData)
  ))
_sym_db.RegisterMessage(EvaluationData)


# @@protoc_insertion_point(module_scope)
