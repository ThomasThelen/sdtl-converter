from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://example.org/sdtl"


@dataclass
class AppendFlagVariable:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class ArgumentName:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class CanChangeData:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[bool] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class CaseNumberVariable:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class CharacterPosition:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Command:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class CommandCount:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class CommentText:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class ConsumesDataframe:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class CountById:
    """
    :ivar value:
    """
    class Meta:
        name = "CountByID"
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class CountByIdlabel:
    """
    :ivar value:
    """
    class Meta:
        name = "CountByIDLabel"
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class DataType:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class DisplayFormatName:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class DisplayFormatSchema:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class FileName:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class First:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class FirstVariable:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Force:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Function:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Id:
    """
    :ivar value:
    """
    class Meta:
        name = "ID"
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class IndexVariableLabel:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class IndexVariableName:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class IsCompressed:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[bool] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class IsSdtlName:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[bool] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class KeepNullCases:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[bool] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Label:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Last:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class LastVariable:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class LineCount:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class LineNumber:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class LineNumberEnd:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class LineNumberStart:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class MergeFlagVariable:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class MergeType:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Message:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class MessageText:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class ModelCreatedTime:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class ModelVersion:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Name:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class NewRow:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[bool] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class NumericType:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class OriginalSourceText:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class OutputDatasetName:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Overlap:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Parser:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class ParserVersion:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class ProcessedSourceText:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class ProducesDataframe:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class PropertyName:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class RangeEnd:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class RangeStart:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class ScriptMD5:
    """
    :ivar value:
    """
    class Meta:
        name = "ScriptMD5"
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class ScriptSHA1:
    """
    :ivar value:
    """
    class Meta:
        name = "ScriptSHA1"
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Severity:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Software:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class SortDirection:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Source:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class SourceFileLastUpdate:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class SourceFileName:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class SourceFileSize:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class SourceLanguage:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class SourceStartIndex:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class SourceStopIndex:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Stub:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class SubType:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class SubTypeSchema:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Target:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TargetVariableLabel:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TargetVariableName:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class To:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TypeOfObject:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Value:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class VariableName:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class ExpressionBase:
    """TODO.

    :ivar name: The name of the argument, when the expression is passed to a function.
    """
    name: Optional[Name] = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )


@dataclass
class IteratorSymbolExpression:
    """The name of an iterator symbol used as an index in describing the actions of
    a loop.

    :ivar name: A name used for the index variable that takes different values inside a loop.
    """
    name: Optional[Name] = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Element",
            namespace="http://example.org/sdtl",
            required=True
        )
    )


@dataclass
class Messages:
    """
    :ivar severity: Information, Warning, Error
    :ivar line_number: The line number of the source that the messages is related to, if relevant.
    :ivar character_position: The character position of the source that the message is related to, if relevant.
    :ivar message_text: The content of the message.
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    severity: Optional[Severity] = field(
        default=None,
        metadata=dict(
            name="Severity",
            type="Element"
        )
    )
    line_number: Optional[LineNumber] = field(
        default=None,
        metadata=dict(
            name="LineNumber",
            type="Element"
        )
    )
    character_position: Optional[CharacterPosition] = field(
        default=None,
        metadata=dict(
            name="CharacterPosition",
            type="Element"
        )
    )
    message_text: Optional[MessageText] = field(
        default=None,
        metadata=dict(
            name="MessageText",
            type="Element"
        )
    )


@dataclass
class RecodeVariable:
    """Describes a variable that will have its values recoded.

    :ivar source: The name of the variable which will have its values recoded
    :ivar target: The name of the new variable into which the recoded values are inserted. This may be the same as the source variable if values are recoded in place.
    """
    source: Optional[Source] = field(
        default=None,
        metadata=dict(
            name="Source",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    target: Optional[Target] = field(
        default=None,
        metadata=dict(
            name="Target",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )


@dataclass
class ReferenceType:
    """Used for referencing an identified item, by lookup of the URN and/or an IRDI
    identification sequence.

    :ivar id: ID of the object being referenced.
    :ivar type_of_object: Strongly typed name of the item which is being referenced.
    """
    id: Optional[Id] = field(
        default=None,
        metadata=dict(
            name="ID",
            type="Element",
            namespace="http://example.org/sdtl",
            required=True
        )
    )
    type_of_object: Optional[TypeOfObject] = field(
        default=None,
        metadata=dict(
            name="TypeOfObject",
            type="Element",
            namespace="http://example.org/sdtl",
            required=True
        )
    )


@dataclass
class SourceInformation:
    """
    :ivar line_number_start: The line number of the beginning of the transform code
    :ivar line_number_end: The line number of the end of the transform code
    :ivar source_start_index: The character index of the beginning of the transform code
    :ivar source_stop_index: The character index of the end of the transform code
    :ivar original_source_text: The original source code of the data transform code
    :ivar processed_source_text: The source code of the data transform code after processing macros or loops
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    line_number_start: Optional[LineNumberStart] = field(
        default=None,
        metadata=dict(
            name="LineNumberStart",
            type="Element"
        )
    )
    line_number_end: Optional[LineNumberEnd] = field(
        default=None,
        metadata=dict(
            name="LineNumberEnd",
            type="Element"
        )
    )
    source_start_index: Optional[SourceStartIndex] = field(
        default=None,
        metadata=dict(
            name="SourceStartIndex",
            type="Element"
        )
    )
    source_stop_index: Optional[SourceStopIndex] = field(
        default=None,
        metadata=dict(
            name="SourceStopIndex",
            type="Element"
        )
    )
    original_source_text: Optional[OriginalSourceText] = field(
        default=None,
        metadata=dict(
            name="OriginalSourceText",
            type="Element"
        )
    )
    processed_source_text: Optional[ProcessedSourceText] = field(
        default=None,
        metadata=dict(
            name="ProcessedSourceText",
            type="Element"
        )
    )


@dataclass
class ValueLabel:
    """Assigns a label to the value of a categorical variable.

    :ivar value: The value to which a label is assigned
    :ivar label: The label to be assigned to the value
    """
    value: Optional[Value] = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    label: Optional[Label] = field(
        default=None,
        metadata=dict(
            name="Label",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )


@dataclass
class Analysis:
    """Describes an analysis command. An analysis command does not result in any
    data transformation.

    :ivar command: The type of transform command
    :ivar source_information: Information about the source of the transform command.
    :ivar can_change_data: Indicates that the transform is capable of changing the values in the data.
    :ivar produces_dataframe: Signify the dataframe which this transform produces.
    :ivar consumes_dataframe: Signify the dataframe which this transform acts upon.
    :ivar message: A message listing commands that are not supported in SDTL.
    """
    command: Optional[Command] = field(
        default=None,
        metadata=dict(
            name="Command",
            type="Element",
            namespace="http://example.org/sdtl",
            required=True
        )
    )
    source_information: Optional[SourceInformation] = field(
        default=None,
        metadata=dict(
            name="SourceInformation",
            type="Element",
            namespace="http://example.org/sdtl",
            required=True
        )
    )
    can_change_data: Optional[CanChangeData] = field(
        default=None,
        metadata=dict(
            name="CanChangeData",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    produces_dataframe: List[ProducesDataframe] = field(
        default_factory=list,
        metadata=dict(
            name="ProducesDataframe",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    consumes_dataframe: List[ConsumesDataframe] = field(
        default_factory=list,
        metadata=dict(
            name="ConsumesDataframe",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    message: Optional[Message] = field(
        default=None,
        metadata=dict(
            name="Message",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )


@dataclass
class ArgumentValue(ExpressionBase):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class BooleanConstantExpression(ExpressionBase):
    """BooleanConstantExpression takes values of TRUE and FALSE.

    :ivar value: Values of TRUE and FALSE are used in logical expressions.
    """
    value: Optional[Value] = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Element",
            namespace="http://example.org/sdtl",
            required=True
        )
    )


@dataclass
class ComputedVariableName(ExpressionBase):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class Condition(ExpressionBase):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class EndCondition(ExpressionBase):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class Expression(ExpressionBase):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class FromValue(ExpressionBase):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class IndexValues(ExpressionBase):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class Invalid:
    """Describes an invalid command. A command is invalid if it uses incorrect
    syntax, or is otherwise not allowed by the executing system.

    :ivar command: The type of transform command
    :ivar source_information: Information about the source of the transform command.
    :ivar can_change_data: Indicates that the transform is capable of changing the values in the data.
    :ivar produces_dataframe: Signify the dataframe which this transform produces.
    :ivar consumes_dataframe: Signify the dataframe which this transform acts upon.
    :ivar message: A message describing the issue with the invalid command.
    """
    command: Optional[Command] = field(
        default=None,
        metadata=dict(
            name="Command",
            type="Element",
            namespace="http://example.org/sdtl",
            required=True
        )
    )
    source_information: Optional[SourceInformation] = field(
        default=None,
        metadata=dict(
            name="SourceInformation",
            type="Element",
            namespace="http://example.org/sdtl",
            required=True
        )
    )
    can_change_data: Optional[CanChangeData] = field(
        default=None,
        metadata=dict(
            name="CanChangeData",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    produces_dataframe: List[ProducesDataframe] = field(
        default_factory=list,
        metadata=dict(
            name="ProducesDataframe",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    consumes_dataframe: List[ConsumesDataframe] = field(
        default_factory=list,
        metadata=dict(
            name="ConsumesDataframe",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    message: Optional[Message] = field(
        default=None,
        metadata=dict(
            name="Message",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )


@dataclass
class IteratorSymbolName(IteratorSymbolExpression):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class IteratorValues(ExpressionBase):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class Labels(ValueLabel):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class MissingValueConstantExpression(ExpressionBase):
    """A missing value constant.  Some languages allow multiple missing value
    constants.

    :ivar value: The missing value as it appears in the system (e.g., .a, .b, .c)
    """
    value: Optional[Value] = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )


@dataclass
class NumberRangeEnd(ExpressionBase):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class NumberRangeIncrement(ExpressionBase):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class NumberRangeStart(ExpressionBase):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class NumericConstantExpression(ExpressionBase):
    """A numeric constant.

    :ivar value: TODO
    :ivar numeric_type: TODO
    """
    value: Optional[Value] = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    numeric_type: Optional[NumericType] = field(
        default=None,
        metadata=dict(
            name="NumericType",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )


@dataclass
class NumericMaximumValueExpression(ExpressionBase):
    """Represents the largest numeric value supported by a system."""


@dataclass
class NumericMinimumValueExpression(ExpressionBase):
    """Represents the smallest numeric value supported by a system."""


@dataclass
class RecodedVariables(RecodeVariable):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class StringConstantExpression(ExpressionBase):
    """A text string.

    :ivar value: TODO
    """
    value: Optional[Value] = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Element",
            namespace="http://example.org/sdtl",
            required=True
        )
    )


@dataclass
class StringRangeExpression(ExpressionBase):
    """Defines a range of string values.

    :ivar range_start: Starting value for range
    :ivar range_end: Ending value for range
    """
    range_start: Optional[RangeStart] = field(
        default=None,
        metadata=dict(
            name="RangeStart",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    range_end: Optional[RangeEnd] = field(
        default=None,
        metadata=dict(
            name="RangeEnd",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )


@dataclass
class TopLevelReference(ReferenceType):
    """Denote which items in the Fragment Instance are the main items of
    interest."""
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class TransformBase:
    """TransformBase defines general properties available on all transform
    commands.

    :ivar command: The type of transform command
    :ivar source_information: Information about the source of the transform command.
    :ivar can_change_data: Indicates that the transform is capable of changing the values in the data.
    :ivar produces_dataframe: Signify the dataframe which this transform produces.
    :ivar consumes_dataframe: Signify the dataframe which this transform acts upon.
    :ivar message: Adds a message that can be displayed with the command.
    """
    command: Optional[Command] = field(
        default=None,
        metadata=dict(
            name="Command",
            type="Element",
            namespace="http://example.org/sdtl",
            required=True
        )
    )
    source_information: Optional[SourceInformation] = field(
        default=None,
        metadata=dict(
            name="SourceInformation",
            type="Element",
            namespace="http://example.org/sdtl",
            required=True
        )
    )
    can_change_data: Optional[CanChangeData] = field(
        default=None,
        metadata=dict(
            name="CanChangeData",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    produces_dataframe: List[ProducesDataframe] = field(
        default_factory=list,
        metadata=dict(
            name="ProducesDataframe",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    consumes_dataframe: List[ConsumesDataframe] = field(
        default_factory=list,
        metadata=dict(
            name="ConsumesDataframe",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    message: List[Message] = field(
        default_factory=list,
        metadata=dict(
            name="Message",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class UnhandledValuesExpression(ExpressionBase):
    """Represents any values not previously handled (for example, in a set of
    recode rules)."""


@dataclass
class Unsupported:
    """Describes an unsupported command. An unsupported command is valid syntax,
    but not supported by the parsing application.

    :ivar command: The type of transform command
    :ivar source_information: Information about the source of the transform command.
    :ivar can_change_data: Indicates that the transform is capable of changing the values in the data.
    :ivar produces_dataframe: Signify the dataframe which this transform produces.
    :ivar consumes_dataframe: Signify the dataframe which this transform acts upon.
    :ivar message: A message describing the issue with the invalid command.
    """
    command: Optional[Command] = field(
        default=None,
        metadata=dict(
            name="Command",
            type="Element",
            namespace="http://example.org/sdtl",
            required=True
        )
    )
    source_information: Optional[SourceInformation] = field(
        default=None,
        metadata=dict(
            name="SourceInformation",
            type="Element",
            namespace="http://example.org/sdtl",
            required=True
        )
    )
    can_change_data: Optional[CanChangeData] = field(
        default=None,
        metadata=dict(
            name="CanChangeData",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    produces_dataframe: List[ProducesDataframe] = field(
        default_factory=list,
        metadata=dict(
            name="ProducesDataframe",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    consumes_dataframe: List[ConsumesDataframe] = field(
        default_factory=list,
        metadata=dict(
            name="ConsumesDataframe",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    message: Optional[Message] = field(
        default=None,
        metadata=dict(
            name="Message",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )


@dataclass
class Values(ExpressionBase):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class VariableReferenceBase(ExpressionBase):
    """TODO."""


@dataclass
class AllNumericVariablesExpression(VariableReferenceBase):
    """An expression that represents all numeric variables in the dataset, similar
    to `_all` in SPSS or Stata."""


@dataclass
class AllTextVariablesExpression(VariableReferenceBase):
    """An expression that represents all text variables in the dataset, similar to
    `_all` in SPSS or Stata."""


@dataclass
class AllVariablesExpression(VariableReferenceBase):
    """An expression that represents all variables in the dataset, similar to
    `_all` in SPSS or Stata."""


@dataclass
class Commands(TransformBase):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class Comment(TransformBase):
    """Describes a source code comment.

    :ivar comment_text: The text of the source code comment.
    """
    comment_text: Optional[CommentText] = field(
        default=None,
        metadata=dict(
            name="CommentText",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )


@dataclass
class CompositeVariableNameExpression(VariableReferenceBase):
    """A composite variable name is used to describe a variable name that is
    computed.

    :ivar computed_variable_name: An expression that evaluates to the constructed variable name.
    """
    computed_variable_name: Optional[ComputedVariableName] = field(
        default=None,
        metadata=dict(
            name="ComputedVariableName",
            type="Element",
            namespace="http://example.org/sdtl",
            required=True
        )
    )


@dataclass
class DropVariables(VariableReferenceBase):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class ElseCommands(TransformBase):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class Execute(TransformBase):
    """This command causes the system to execute preceding commands before
    continuing to process the command script."""


@dataclass
class FunctionArgument:
    """Describes the arguments in a function as specified in the SDTL Function
    Library.

    :ivar argument_name: The name of the parameter.
    :ivar argument_value: The value of the parameter.
    """
    argument_name: Optional[ArgumentName] = field(
        default=None,
        metadata=dict(
            name="ArgumentName",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    argument_value: Optional[ArgumentValue] = field(
        default=None,
        metadata=dict(
            name="ArgumentValue",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )


@dataclass
class GroupByVariables(VariableReferenceBase):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class GroupedExpression(ExpressionBase):
    """A group of expressions to be evaluated before expressions outside of the
    group.  Used to control the order of operations in a formula.

    :ivar expression: TODO
    """
    expression: Optional[Expression] = field(
        default=None,
        metadata=dict(
            name="Expression",
            type="Element",
            namespace="http://example.org/sdtl",
            required=True
        )
    )


@dataclass
class Idvariables(VariableReferenceBase):
    class Meta:
        name = "IDVariables"
        namespace = "http://example.org/sdtl"


@dataclass
class IteratorCommands(TransformBase):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class IteratorDescription:
    """Describes an iteration process consisting of an IteratorSymbolExpression and
    a list of values it takes.

    :ivar iterator_symbol_name: The name used in  IteratorCommands  for the index variable that changes value in the loop.
    :ivar iterator_values: Describes the values that are substituted for the index variable that changes value in the loop.
    """
    iterator_symbol_name: Optional[IteratorSymbolName] = field(
        default=None,
        metadata=dict(
            name="IteratorSymbolName",
            type="Element",
            namespace="http://example.org/sdtl",
            required=True
        )
    )
    iterator_values: List[IteratorValues] = field(
        default_factory=list,
        metadata=dict(
            name="IteratorValues",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class KeepVariables(VariableReferenceBase):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class Load(TransformBase):
    """Load data from a file.

    :ivar file_name: The name of the file to be loaded.
    :ivar software: The name of the file format, or the software package that works with the file.
    :ivar is_compressed: Indicates whether the file format is compressed.
    """
    file_name: Optional[FileName] = field(
        default=None,
        metadata=dict(
            name="FileName",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    software: Optional[Software] = field(
        default=None,
        metadata=dict(
            name="Software",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    is_compressed: Optional[IsCompressed] = field(
        default=None,
        metadata=dict(
            name="IsCompressed",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )


@dataclass
class MergeByVariables(VariableReferenceBase):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class NumberRangeExpression(ExpressionBase):
    """Defines a range of numeric values.

    :ivar number_range_start: Starting value for range
    :ivar number_range_end: Ending value for range
    :ivar number_range_increment: Increment for stepping through range
    """
    number_range_start: Optional[NumberRangeStart] = field(
        default=None,
        metadata=dict(
            name="NumberRangeStart",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    number_range_end: Optional[NumberRangeEnd] = field(
        default=None,
        metadata=dict(
            name="NumberRangeEnd",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    number_range_increment: Optional[NumberRangeIncrement] = field(
        default=None,
        metadata=dict(
            name="NumberRangeIncrement",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )


@dataclass
class RecodeRule:
    """Describes how values will be recoded.

    :ivar from_value: The values to be recoded.
    :ivar to: The new value
    :ivar label: A value label for the new recoded value, if appropriate
    """
    from_value: List[FromValue] = field(
        default_factory=list,
        metadata=dict(
            name="FromValue",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    to: Optional[To] = field(
        default=None,
        metadata=dict(
            name="To",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    label: Optional[Label] = field(
        default=None,
        metadata=dict(
            name="Label",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )


@dataclass
class Save(TransformBase):
    """Writes a dataset to a file.

    :ivar file_name: The name of the file to be saved.
    :ivar software: The name of the file format, or the software package that works with the file.
    :ivar is_compressed: Indicates whether the file format is compressed.
    """
    file_name: Optional[FileName] = field(
        default=None,
        metadata=dict(
            name="FileName",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    software: Optional[Software] = field(
        default=None,
        metadata=dict(
            name="Software",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    is_compressed: Optional[IsCompressed] = field(
        default=None,
        metadata=dict(
            name="IsCompressed",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )


@dataclass
class Select(TransformBase):
    """Rows that match the selection condition are retained in the dataset.  Other
    rows are deleted.

    :ivar condition: The logical expresion that must be true for a case to remain in the working dataset.
    """
    condition: Optional[Condition] = field(
        default=None,
        metadata=dict(
            name="Condition",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )


@dataclass
class SetDatasetProperty(TransformBase):
    """Changes a property of a dataframe.

    :ivar property_name: The name of the property to be set (for example, 'Title' or 'Subtitle').
    :ivar value: The value of the property.
    """
    property_name: Optional[PropertyName] = field(
        default=None,
        metadata=dict(
            name="PropertyName",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    value: Optional[Value] = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )


@dataclass
class SourceVariables(VariableReferenceBase):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class ThenCommands(TransformBase):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class ValueListExpression(ExpressionBase):
    """Wraps a list of other expressions.

    :ivar values: The list of expressions.
    """
    values: List[Values] = field(
        default_factory=list,
        metadata=dict(
            name="Values",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Variable(VariableReferenceBase):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class VariableRangeExpression(VariableReferenceBase):
    """A list of variables in adjacent columns defined by the variable names of
    first and last columns.

    :ivar first: TODO
    :ivar last: TODO
    """
    first: Optional[First] = field(
        default=None,
        metadata=dict(
            name="First",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    last: Optional[Last] = field(
        default=None,
        metadata=dict(
            name="Last",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )


@dataclass
class VariableSymbolExpression(VariableReferenceBase):
    """A reference to a variable.

    :ivar variable_name: TODO
    """
    variable_name: Optional[VariableName] = field(
        default=None,
        metadata=dict(
            name="VariableName",
            type="Element",
            namespace="http://example.org/sdtl",
            required=True
        )
    )


@dataclass
class Variables(VariableReferenceBase):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class Arguments(FunctionArgument):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class Compute(TransformBase):
    """Assigns the value of an expression to a variable.

    :ivar variable: The variable that is computed.
    :ivar expression: The expression used to compute the value of the variable(s)
    """
    variable: Optional[Variable] = field(
        default=None,
        metadata=dict(
            name="Variable",
            type="Element",
            namespace="http://example.org/sdtl",
            required=True
        )
    )
    expression: Optional[Expression] = field(
        default=None,
        metadata=dict(
            name="Expression",
            type="Element",
            namespace="http://example.org/sdtl",
            required=True
        )
    )


@dataclass
class DeleteVariables(TransformBase):
    """Deletes variables from the data.

    :ivar variables: The variables to be deleted.
    """
    variables: List[Variables] = field(
        default_factory=list,
        metadata=dict(
            name="Variables",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class DoIf(TransformBase):
    """A set of commands that are performed when a logical expression is true.  May
    also include ElseCommands to be performed if the logical expression is false.
    The commands in DoIf are performed once, and it expects a logical condition
    that applies to the entire dataframe.  Use IfRows for commands that are
    performed on each row depending upon values on those rows.

    :ivar condition: A logical expression
    :ivar then_commands: Commands to be performed if the condition is true.
    :ivar else_commands: Commands to be performed if the condition is false.
    """
    condition: Optional[Condition] = field(
        default=None,
        metadata=dict(
            name="Condition",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    then_commands: List[ThenCommands] = field(
        default_factory=list,
        metadata=dict(
            name="ThenCommands",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    else_commands: List[ElseCommands] = field(
        default_factory=list,
        metadata=dict(
            name="ElseCommands",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class IfRows(TransformBase):
    """A set of commands that are performed on each row in the dataframe when a
    logical expression is true for that row.  May also include ElseCommands to be
    performed if the logical expression is false.  Use DoIf for a logical condition
    that applies to the entire dataframe and commands that are performed once.

    :ivar condition: A logical expression that is evaluated separately for every row in the dataframe.
    :ivar then_commands: Commands to be performed if the condition is true.
    :ivar else_commands: Commands to be performed if the condition is false.
    """
    condition: Optional[Condition] = field(
        default=None,
        metadata=dict(
            name="Condition",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    then_commands: List[ThenCommands] = field(
        default_factory=list,
        metadata=dict(
            name="ThenCommands",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    else_commands: List[ElseCommands] = field(
        default_factory=list,
        metadata=dict(
            name="ElseCommands",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Iterators(IteratorDescription):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class LoopWhile(TransformBase):
    """LoopWhile iterates over a set of commands under the control of one or more
    logical expressions.  Since the logical conditions typically depend upon values
    in the data, commands executed in a LoopWhile cannot be anticipated and
    expanded in SDTL.

    :ivar condition: Describes a condition required for the next iteration to begin.
    :ivar end_condition: Describes a condition that ends  interation.
    :ivar iterator_commands: Commands within the loop expressed in SDTL with IteratorSymbolExpressions.
    """
    condition: Optional[Condition] = field(
        default=None,
        metadata=dict(
            name="Condition",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    end_condition: Optional[EndCondition] = field(
        default=None,
        metadata=dict(
            name="EndCondition",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    iterator_commands: List[IteratorCommands] = field(
        default_factory=list,
        metadata=dict(
            name="IteratorCommands",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class NewVariable(VariableSymbolExpression):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class OldVariable(VariableSymbolExpression):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class Program:
    """
    :ivar id: ID of the object being referenced.
    :ivar source_file_name: The name of the file containing the source code.
    :ivar source_language: The language of the source code.
    :ivar script_md5: The MD5 hash of the contents of the file.
    :ivar script_sha1: The SHA-1 hash of the contents of the file.
    :ivar source_file_last_update: The date and time the file was last updated.
    :ivar source_file_size: The size of the file in bytes.
    :ivar line_count: The number of lines in the source file.
    :ivar command_count: The number of commands detected in the source file.
    :ivar messages: Messages related to the parsing of the source file.
    :ivar parser: The name of the parser used to generate the SDTL.
    :ivar parser_version: The version of the parser used to generate the SDTL.
    :ivar model_version: The version of the SDTL model.
    :ivar model_created_time: The date and time the SDTL was generated.
    :ivar commands: The list of commands that make up the program.
    """
    class Meta:
        namespace = "http://example.org/sdtl"

    id: Optional[Id] = field(
        default=None,
        metadata=dict(
            name="ID",
            type="Element",
            required=True
        )
    )
    source_file_name: Optional[SourceFileName] = field(
        default=None,
        metadata=dict(
            name="SourceFileName",
            type="Element"
        )
    )
    source_language: Optional[SourceLanguage] = field(
        default=None,
        metadata=dict(
            name="SourceLanguage",
            type="Element"
        )
    )
    script_md5: Optional[ScriptMD5] = field(
        default=None,
        metadata=dict(
            name="ScriptMD5",
            type="Element"
        )
    )
    script_sha1: Optional[ScriptSHA1] = field(
        default=None,
        metadata=dict(
            name="ScriptSHA1",
            type="Element"
        )
    )
    source_file_last_update: Optional[SourceFileLastUpdate] = field(
        default=None,
        metadata=dict(
            name="SourceFileLastUpdate",
            type="Element"
        )
    )
    source_file_size: Optional[SourceFileSize] = field(
        default=None,
        metadata=dict(
            name="SourceFileSize",
            type="Element"
        )
    )
    line_count: Optional[LineCount] = field(
        default=None,
        metadata=dict(
            name="LineCount",
            type="Element"
        )
    )
    command_count: Optional[CommandCount] = field(
        default=None,
        metadata=dict(
            name="CommandCount",
            type="Element"
        )
    )
    messages: List[Messages] = field(
        default_factory=list,
        metadata=dict(
            name="Messages",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    parser: Optional[Parser] = field(
        default=None,
        metadata=dict(
            name="Parser",
            type="Element"
        )
    )
    parser_version: Optional[ParserVersion] = field(
        default=None,
        metadata=dict(
            name="ParserVersion",
            type="Element"
        )
    )
    model_version: Optional[ModelVersion] = field(
        default=None,
        metadata=dict(
            name="ModelVersion",
            type="Element"
        )
    )
    model_created_time: Optional[ModelCreatedTime] = field(
        default=None,
        metadata=dict(
            name="ModelCreatedTime",
            type="Element"
        )
    )
    commands: List[Commands] = field(
        default_factory=list,
        metadata=dict(
            name="Commands",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class RecodedVariableRange(VariableRangeExpression):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class ReshapeItemDescription:
    """Descripbes a new variable created by reshaping a dataset from wide to long.

    :ivar target_variable_name: Name of new variable created by this command.
    :ivar target_variable_label: Label for new variable created by this command.
    :ivar source_variables: Source variables in the original dataset used to create this variable.
    :ivar stub: The stub is a string used in the names of variables in the wide dataset.
    :ivar index_values: A list of values that produce new rows (long) or columns (wide) for this variable.
    :ivar index_variable_name: Name of the variable that will contain the value of the index for this row.
    :ivar index_variable_label: Label for the variable in IndexVariableName.
    """
    target_variable_name: Optional[TargetVariableName] = field(
        default=None,
        metadata=dict(
            name="TargetVariableName",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    target_variable_label: Optional[TargetVariableLabel] = field(
        default=None,
        metadata=dict(
            name="TargetVariableLabel",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    source_variables: Optional[SourceVariables] = field(
        default=None,
        metadata=dict(
            name="SourceVariables",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    stub: Optional[Stub] = field(
        default=None,
        metadata=dict(
            name="Stub",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    index_values: Optional[IndexValues] = field(
        default=None,
        metadata=dict(
            name="IndexValues",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    index_variable_name: Optional[IndexVariableName] = field(
        default=None,
        metadata=dict(
            name="IndexVariableName",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    index_variable_label: Optional[IndexVariableLabel] = field(
        default=None,
        metadata=dict(
            name="IndexVariableLabel",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )


@dataclass
class Rules(RecodeRule):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class SetDataType(TransformBase):
    """
    Sets the data type of a variable.   
    Examples:   

    ```
    "dataType": "Text",
    "subTypeSchema": "Stata 15.1",
    "subType": "str1"
    ```

    ```
    "dataType": "Numeric",
    "subTypeSchema": "https://www.ddialliance.org/Specification/DDI-CV/DataType_1.0.html" ,
    "subType": "Int"
    ```
    :ivar variables: The variables that will have their format set
    :ivar data_type: General type of a variable,  e.g.  "Text" or "Numeric".
    :ivar sub_type_schema: A vendor or standards body with a controlled vocabulary.  The value can be a URL.
    :ivar sub_type: The name used in the associated schema.
    """
    variables: List[Variables] = field(
        default_factory=list,
        metadata=dict(
            name="Variables",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    data_type: Optional[DataType] = field(
        default=None,
        metadata=dict(
            name="DataType",
            type="Element",
            namespace="http://example.org/sdtl",
            required=True
        )
    )
    sub_type_schema: Optional[SubTypeSchema] = field(
        default=None,
        metadata=dict(
            name="SubTypeSchema",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    sub_type: Optional[SubType] = field(
        default=None,
        metadata=dict(
            name="SubType",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )


@dataclass
class SetDisplayFormat(TransformBase):
    """
    Sets the display or output format for a variable.    
    Examples:   
    ```
    "displayFormatSchema": "SAS"
    "displayFormatName": "DOLLAR6.2"
    ```

    ```
    "displayFormatSchema": "Stata 15.1"
    "displayFormatName": "%tcDDmonCCYY_HH:MM:SS"
    ```
    :ivar variables: The variables that will have their format set
    :ivar display_format_schema: A vendor or standards body with a controlled vocabulary.  The value can be a URL.
    :ivar display_format_name: The name used in the associated schema.
    """
    variables: List[Variables] = field(
        default_factory=list,
        metadata=dict(
            name="Variables",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    display_format_schema: Optional[DisplayFormatSchema] = field(
        default=None,
        metadata=dict(
            name="DisplayFormatSchema",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    display_format_name: Optional[DisplayFormatName] = field(
        default=None,
        metadata=dict(
            name="DisplayFormatName",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )


@dataclass
class SetMissingValues(TransformBase):
    """Defines values that are treated as missing values for a list of variables.

    :ivar variables: The list of variables to which the missing values are assigned
    :ivar values: The values to be considered as missing values
    """
    variables: List[Variables] = field(
        default_factory=list,
        metadata=dict(
            name="Variables",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    values: List[Values] = field(
        default_factory=list,
        metadata=dict(
            name="Values",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class SetValueLabels(TransformBase):
    """Describes the assignment of labels to categorical values.

    :ivar variables: The variables to which a label will be assigned
    :ivar labels: The label to be assigned to the variable
    """
    variables: List[Variables] = field(
        default_factory=list,
        metadata=dict(
            name="Variables",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    labels: List[Labels] = field(
        default_factory=list,
        metadata=dict(
            name="Labels",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class SetVariableLabel(TransformBase):
    """Describes the assignment of a label to a variable.

    :ivar variable: The name of the variable to which a label will be assigned
    :ivar label: The label to be assigned to the variable
    """
    variable: Optional[Variable] = field(
        default=None,
        metadata=dict(
            name="Variable",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    label: Optional[Label] = field(
        default=None,
        metadata=dict(
            name="Label",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )


@dataclass
class SortCriterion:
    """Describes a criterion by which cases are sorted, including the variable name
    and whether to sort ascending or descending.

    :ivar variable: The variable used to sort.
    :ivar sort_direction: The direction in which to sort.
    """
    variable: Optional[Variable] = field(
        default=None,
        metadata=dict(
            name="Variable",
            type="Element",
            namespace="http://example.org/sdtl",
            required=True
        )
    )
    sort_direction: Optional[SortDirection] = field(
        default=None,
        metadata=dict(
            name="SortDirection",
            type="Element",
            namespace="http://example.org/sdtl",
            required=True
        )
    )


@dataclass
class VariableListExpression(VariableReferenceBase):
    """A list of variables which may include variable names
    (VariableSymbolExpression) and variable ranges (VariableRangeExpression).

    :ivar variables: TODO
    """
    variables: List[Variables] = field(
        default_factory=list,
        metadata=dict(
            name="Variables",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class WeightVariable(VariableSymbolExpression):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class AggregateVariables(Compute):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class FunctionCallExpression(ExpressionBase):
    """An expression evaluated by reference to the Function Library.

    :ivar function: The name of the function being called.
    :ivar is_sdtl_name: When true, the Function property contains the name of a function from the SDTL function library. When false, the Function property contains the name of a system-specific or user-defined function.
    :ivar arguments: A list of parameters to the function.
    """
    function: Optional[Function] = field(
        default=None,
        metadata=dict(
            name="Function",
            type="Element",
            namespace="http://example.org/sdtl",
            required=True
        )
    )
    is_sdtl_name: Optional[IsSdtlName] = field(
        default=None,
        metadata=dict(
            name="IsSdtlName",
            type="Element",
            namespace="http://example.org/sdtl",
            required=True
        )
    )
    arguments: List[Arguments] = field(
        default_factory=list,
        metadata=dict(
            name="Arguments",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class ItemContainerType:
    """Used for serializing a set of items.

    :ivar top_level_reference:
    :ivar program:
    """
    top_level_reference: List[TopLevelReference] = field(
        default_factory=list,
        metadata=dict(
            name="TopLevelReference",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    program: List[Program] = field(
        default_factory=list,
        metadata=dict(
            name="Program",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class LoopOverList(TransformBase):
    """A loop creates multiple versions of a set of commands by iterating over a
    list of variables, numbers, or strings.

    :ivar iterators: Describes one or more iteration processes in this loop.
    :ivar commands: Commands generated by the loop expanded by replacing tokens with their values.
    """
    iterators: List[Iterators] = field(
        default_factory=list,
        metadata=dict(
            name="Iterators",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    commands: List[Commands] = field(
        default_factory=list,
        metadata=dict(
            name="Commands",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class MakeItems(ReshapeItemDescription):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class Recode(TransformBase):
    """Describes recoding values in one or more variables according to a specified
    mapping.

    The Recode command can either describe a recoding of one or more individual variables,
    or a range of variables. When one or more individual variables are described, a new
    variable name can be specified. In this case, the original variable is left alone, and
    a new variable is created with the recoded values.
    :ivar recoded_variables: The variables that will have their values recoded. The resulting values may be either stored in the same variable, or a newly created destination variable
    :ivar recoded_variable_range: A range of variables to which the recode rules are applied. The resulting values are stored in the same variable.
    :ivar rules: A mapping describing which values will be recoded to which new values
    """
    recoded_variables: List[RecodedVariables] = field(
        default_factory=list,
        metadata=dict(
            name="RecodedVariables",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    recoded_variable_range: Optional[RecodedVariableRange] = field(
        default=None,
        metadata=dict(
            name="RecodedVariableRange",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    rules: List[Rules] = field(
        default_factory=list,
        metadata=dict(
            name="Rules",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class RenamePair:
    """Variable names before and after a variable is renamed.

    :ivar old_variable: The old name of the variable.
    :ivar new_variable: The new name of the variable.
    """
    old_variable: Optional[OldVariable] = field(
        default=None,
        metadata=dict(
            name="OldVariable",
            type="Element",
            namespace="http://example.org/sdtl",
            required=True
        )
    )
    new_variable: Optional[NewVariable] = field(
        default=None,
        metadata=dict(
            name="NewVariable",
            type="Element",
            namespace="http://example.org/sdtl",
            required=True
        )
    )


@dataclass
class SortCriteria(SortCriterion):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class Aggregate(TransformBase):
    """An aggregation summarizes data using aggregation functions applied to data
    that may be grouped by one or more variables. The resulting summary data is
    added to each row of the existing dataset.

    :ivar group_by_variables: Variables used as keys to identify groups.
    :ivar aggregate_variables: The expressions that compute the aggregations. An aggregation function should be used.
    :ivar weight_variable: The variable used as a weight in the operation.
    """
    group_by_variables: List[GroupByVariables] = field(
        default_factory=list,
        metadata=dict(
            name="GroupByVariables",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    aggregate_variables: List[AggregateVariables] = field(
        default_factory=list,
        metadata=dict(
            name="AggregateVariables",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    weight_variable: Optional[WeightVariable] = field(
        default=None,
        metadata=dict(
            name="WeightVariable",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )


@dataclass
class Collapse(TransformBase):
    """A collapse command summarizes data using aggregation functions applied to
    data that may be grouped by one or more variables. The resulting summary data
    is represented in a new dataset.

    :ivar output_dataset_name: The name of a new, aggregated dataset to be created.
    :ivar group_by_variables: Variables used as keys to identify groups.
    :ivar aggregate_variables: The expressions that compute the aggregations. An aggregation function should be used.
    :ivar weight_variable: The variable used as a weight in the operation.
    """
    output_dataset_name: Optional[OutputDatasetName] = field(
        default=None,
        metadata=dict(
            name="OutputDatasetName",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    group_by_variables: List[GroupByVariables] = field(
        default_factory=list,
        metadata=dict(
            name="GroupByVariables",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    aggregate_variables: List[AggregateVariables] = field(
        default_factory=list,
        metadata=dict(
            name="AggregateVariables",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    weight_variable: Optional[WeightVariable] = field(
        default=None,
        metadata=dict(
            name="WeightVariable",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )


@dataclass
class ItemContainer(ItemContainerType):
    """A Item Container is used to transfer items plus any associated notes and
    other material.

    TopLevelReference provides a record of the main item of the Item
    Container.
    """
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class RenameVariables(RenamePair):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class Renames(RenamePair):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class ReshapeLong(TransformBase):
    """Creates a new dataset with multiple rows per case by assigning a set of
    variables in the original dataset to a single variable in the new dataset.

    :ivar make_items: New variables created by this command.
    :ivar case_number_variable: New variable identifying the case number in the wide data that created this row.
    :ivar idvariables: One or more variables identifying unique rows in the wide data.
    :ivar drop_variables: Variables to be dropped from the new dataset.
    :ivar keep_variables: Variables to be kept in the new dataset.
    :ivar keep_null_cases: When set to TRUE, rows in which all constructed variables are missing are not deleted.
    :ivar count_by_id: New variable with the number of cases in the long dataset that were created from the source row in the wide dataset.
    :ivar count_by_idlabel: Label for the CountByID variable.
    """
    make_items: List[MakeItems] = field(
        default_factory=list,
        metadata=dict(
            name="MakeItems",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    case_number_variable: Optional[CaseNumberVariable] = field(
        default=None,
        metadata=dict(
            name="CaseNumberVariable",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    idvariables: Optional[Idvariables] = field(
        default=None,
        metadata=dict(
            name="IDVariables",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    drop_variables: Optional[DropVariables] = field(
        default=None,
        metadata=dict(
            name="DropVariables",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    keep_variables: Optional[KeepVariables] = field(
        default=None,
        metadata=dict(
            name="KeepVariables",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    keep_null_cases: Optional[KeepNullCases] = field(
        default=None,
        metadata=dict(
            name="KeepNullCases",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    count_by_id: Optional[CountById] = field(
        default=None,
        metadata=dict(
            name="CountByID",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    count_by_idlabel: Optional[CountByIdlabel] = field(
        default=None,
        metadata=dict(
            name="CountByIDLabel",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )


@dataclass
class ReshapeWide(TransformBase):
    """ReshapeWide is not supported in the current version of SDTL, because it
    depends on values in the data.  However, it may be useful when values of the
    index variable are available in the metadata file or the data can be processed.

    :ivar make_items: New variables created by this command.
    :ivar idvariables: One or more variables identifying unique rows in the wide data.
    :ivar drop_variables: Variables to be dropped from the new dataset.
    :ivar keep_variables: Variables to be kept in the new dataset.
    """
    make_items: List[MakeItems] = field(
        default_factory=list,
        metadata=dict(
            name="MakeItems",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    idvariables: Optional[Idvariables] = field(
        default=None,
        metadata=dict(
            name="IDVariables",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    drop_variables: Optional[DropVariables] = field(
        default=None,
        metadata=dict(
            name="DropVariables",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    keep_variables: Optional[KeepVariables] = field(
        default=None,
        metadata=dict(
            name="KeepVariables",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )


@dataclass
class SortCases(TransformBase):
    """Sorts rows in the dataframe in a specified order.

    :ivar sort_criteria: Describes how cases are sorted.
    """
    sort_criteria: List[SortCriteria] = field(
        default_factory=list,
        metadata=dict(
            name="SortCriteria",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class AppendFileDescription:
    """Describes files used in an AppendDatasets command.

    :ivar file_name: Name of the file being merged.  May be "Active file".
    :ivar rename_variables: Variables to be renamed
    :ivar keep_variables: List of variables to keep
    :ivar drop_variables: List of variables to drop
    :ivar force: Forces variable attributes to be changed to the attributes in the "master"  dataframe, when appended dataframes have the same variable names but different attributes.  For example, "string" may be forced to "numeric"
    """
    file_name: Optional[FileName] = field(
        default=None,
        metadata=dict(
            name="FileName",
            type="Element",
            namespace="http://example.org/sdtl",
            required=True
        )
    )
    rename_variables: List[RenameVariables] = field(
        default_factory=list,
        metadata=dict(
            name="RenameVariables",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    keep_variables: List[KeepVariables] = field(
        default_factory=list,
        metadata=dict(
            name="KeepVariables",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    drop_variables: List[DropVariables] = field(
        default_factory=list,
        metadata=dict(
            name="DropVariables",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    force: Optional[Force] = field(
        default=None,
        metadata=dict(
            name="Force",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )


@dataclass
class MergeFileDescription:
    """Describes files used in a MergeData command.

    :ivar file_name: Name of the file being merged.  May be "Active file".
    :ivar merge_type: Describes the type of merge performed.
    :ivar merge_flag_variable: Creates a new variable indicating whether the row came from this file or a different input file.
    :ivar rename_variables: Variables to be renamed
    :ivar overlap: Outcome when the same variables exist in more than one file. "Master" means the value is taken from this file.  "Merge" means the value is taken from the other file.  "Update" means that value is taken from the other file when the value in this file is missing.
    :ivar new_row: Generate new row when not matched to other files
    :ivar keep_variables: List of variables to keep
    :ivar drop_variables: List of variables to drop
    """
    file_name: Optional[FileName] = field(
        default=None,
        metadata=dict(
            name="FileName",
            type="Element",
            namespace="http://example.org/sdtl",
            required=True
        )
    )
    merge_type: Optional[MergeType] = field(
        default=None,
        metadata=dict(
            name="MergeType",
            type="Element",
            namespace="http://example.org/sdtl",
            required=True
        )
    )
    merge_flag_variable: Optional[MergeFlagVariable] = field(
        default=None,
        metadata=dict(
            name="MergeFlagVariable",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    rename_variables: List[RenameVariables] = field(
        default_factory=list,
        metadata=dict(
            name="RenameVariables",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    overlap: Optional[Overlap] = field(
        default=None,
        metadata=dict(
            name="Overlap",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    new_row: Optional[NewRow] = field(
        default=None,
        metadata=dict(
            name="NewRow",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    keep_variables: List[KeepVariables] = field(
        default_factory=list,
        metadata=dict(
            name="KeepVariables",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    drop_variables: List[DropVariables] = field(
        default_factory=list,
        metadata=dict(
            name="DropVariables",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Rename(TransformBase):
    """Rename changes the name of a variable.

    :ivar renames: A list of variable rename objects, which includes the old name and the new name.
    """
    renames: List[Renames] = field(
        default_factory=list,
        metadata=dict(
            name="Renames",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class AppendFiles(AppendFileDescription):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class MergeFiles(MergeFileDescription):
    class Meta:
        namespace = "http://example.org/sdtl"


@dataclass
class AppendDatasets(TransformBase):
    """Combines datasets by concatenation for datasets with the same or overlapping
    variables.

    :ivar append_files: Description of files to be appended
    :ivar append_flag_variable: Creates a new variable identifying the source dataframe for a row with the variable name given in the value of the property
    """
    append_files: List[AppendFiles] = field(
        default_factory=list,
        metadata=dict(
            name="AppendFiles",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    append_flag_variable: Optional[AppendFlagVariable] = field(
        default=None,
        metadata=dict(
            name="AppendFlagVariable",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )


@dataclass
class MergeDatasets(TransformBase):
    """Merges datasets holding overlapping cases but different variables.  The
    merge may be controlled by keys or grouping variables.

    :ivar merge_files: Description of files to be merged.
    :ivar merge_by_variables: A variable or list of variables that acts as the unique case identifier across datasets.  If MatchByVariables is absent, MergeType must be "sequential" on all files.
    :ivar first_variable: The name of a variable set to 1 for the first row of each group of cases with the same value for the MatchByVariables variables and set to  0 for all other rows.
    :ivar last_variable: The name of a variable set to 1 for the last row of each group of cases with the same value for the MatchByVariables variables and set to  0 for all other rows.
    :ivar keep_variables: List of variables to keep
    :ivar drop_variables: List of variables to drop
    """
    merge_files: List[MergeFiles] = field(
        default_factory=list,
        metadata=dict(
            name="MergeFiles",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=2,
            max_occurs=9223372036854775807
        )
    )
    merge_by_variables: Optional[MergeByVariables] = field(
        default=None,
        metadata=dict(
            name="MergeByVariables",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    first_variable: Optional[FirstVariable] = field(
        default=None,
        metadata=dict(
            name="FirstVariable",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    last_variable: Optional[LastVariable] = field(
        default=None,
        metadata=dict(
            name="LastVariable",
            type="Element",
            namespace="http://example.org/sdtl"
        )
    )
    keep_variables: List[KeepVariables] = field(
        default_factory=list,
        metadata=dict(
            name="KeepVariables",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    drop_variables: List[DropVariables] = field(
        default_factory=list,
        metadata=dict(
            name="DropVariables",
            type="Element",
            namespace="http://example.org/sdtl",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


all_classes = (
    'dataFrame',
    'Aggregate',
    'AggregateVariables',
    'AllNumericVariablesExpression',
    'AllTextVariablesExpression',
    'AllVariablesExpression',
    'Analysis',
    'AppendDatasets',
    'AppendFileDescription',
    'AppendFiles',
    'AppendFlagVariable',
    'ArgumentName',
    'ArgumentValue',
    'Arguments',
    'BooleanConstantExpression',
    'CanChangeData',
    'CaseNumberVariable',
    'CharacterPosition',
    'Collapse',
    'Command',
    'CommandCount',
    'Commands',
    'Comment',
    'CommentText',
    'CompositeVariableNameExpression',
    'Compute',
    'ComputedVariableName',
    'Condition',
    'ConsumesDataframe',
    'CountById',
    'CountByIdlabel',
    'DataType',
    'DeleteVariables',
    'DisplayFormatName',
    'DisplayFormatSchema',
    'DoIf',
    'DropVariables',
    'ElseCommands',
    'EndCondition',
    'Execute',
    'Expression',
    'ExpressionBase',
    'FileName',
    'First',
    'FirstVariable',
    'Force',
    'FromValue',
    'Function',
    'FunctionArgument',
    'FunctionCallExpression',
    'GroupByVariables',
    'GroupedExpression',
    'Id',
    'Idvariables',
    'IfRows',
    'IndexValues',
    'IndexVariableLabel',
    'IndexVariableName',
    'Invalid',
    'IsCompressed',
    'IsSdtlName',
    'ItemContainer',
    'ItemContainerType',
    'IteratorCommands',
    'IteratorDescription',
    'IteratorSymbolExpression',
    'IteratorSymbolName',
    'IteratorValues',
    'Iterators',
    'KeepNullCases',
    'KeepVariables',
    'Label',
    'Labels',
    'Last',
    'LastVariable',
    'LineCount',
    'LineNumber',
    'LineNumberEnd',
    'LineNumberStart',
    'Load',
    'LoopOverList',
    'LoopWhile',
    'MakeItems',
    'MergeByVariables',
    'MergeDatasets',
    'MergeFileDescription',
    'MergeFiles',
    'MergeFlagVariable',
    'MergeType',
    'Message',
    'MessageText',
    'Messages',
    'MissingValueConstantExpression',
    'ModelCreatedTime',
    'ModelVersion',
    'Name',
    'NewRow',
    'NewVariable',
    'NumberRangeEnd',
    'NumberRangeExpression',
    'NumberRangeIncrement',
    'NumberRangeStart',
    'NumericConstantExpression',
    'NumericMaximumValueExpression',
    'NumericMinimumValueExpression',
    'NumericType',
    'OldVariable',
    'OriginalSourceText',
    'OutputDatasetName',
    'Overlap',
    'Parser',
    'ParserVersion',
    'ProcessedSourceText',
    'ProducesDataframe',
    'Program',
    'PropertyName',
    'RangeEnd',
    'RangeStart',
    'Recode',
    'RecodeRule',
    'RecodeVariable',
    'RecodedVariableRange',
    'RecodedVariables',
    'ReferenceType',
    'Rename',
    'RenamePair',
    'RenameVariables',
    'Renames',
    'ReshapeItemDescription',
    'ReshapeLong',
    'ReshapeWide',
    'Rules',
    'Save',
    'ScriptMD5',
    'ScriptSHA1',
    'Select',
    'SetDataType',
    'SetDatasetProperty',
    'SetDisplayFormat',
    'SetMissingValues',
    'SetValueLabels',
    'SetVariableLabel',
    'Severity',
    'Software',
    'SortCases',
    'SortCriteria',
    'SortCriterion',
    'SortDirection',
    'Source',
    'SourceFileLastUpdate',
    'SourceFileName',
    'SourceFileSize',
    'SourceInformation',
    'SourceLanguage',
    'SourceStartIndex',
    'SourceStopIndex',
    'SourceVariables',
    'StringConstantExpression',
    'StringRangeExpression',
    'Stub',
    'SubType',
    'SubTypeSchema',
    'Target',
    'TargetVariableLabel',
    'TargetVariableName',
    'ThenCommands',
    'To',
    'TopLevelReference,'
    'TransformBase',
    'TypeOfObject',
    'UnhandledValuesExpression',
    'Unsupported',
    'Value',
    'ValueLabel',
    'ValueListExpression',
    'Values',
    'Variable',
    'VariableListExpression',
    'VariableName',
    'VariableRangeExpression',
    'VariableReferenceBase',
    'VariableSymbolExpression',
    'Variables',
    'WeightVariable',
    'VariableInventory',
    'FunctionArgument')