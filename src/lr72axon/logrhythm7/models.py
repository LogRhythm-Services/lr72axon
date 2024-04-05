import json

from lr72axon.utils.mapping import *


class SimpleStruct:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        result = {}
        for key, value in self.__dict__.items():
            if value is not None:
                if hasattr(value, 'to_dict'):
                    result[key] = value.to_dict()
                else:
                    result[key] = value
        return result

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)


class AlarmRule:
    def __init__(self, id, name, enabled=False):
        self.id = id
        self.name = name
        self.enabled = enabled

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        result = {}
        for key, value in self.__dict__.items():
            if value is not None:
                if hasattr(value, 'to_dict'):
                    result[key] = value.to_dict()
                else:
                    result[key] = value
        return result


class Value:
    def __init__(self, filterType, valueType, value, displayValue):
        self.filterType = filterType
        self.valueType = valueType
        self.value = value
        self.displayValue = displayValue

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        result = {}
        for key, value in self.__dict__.items():
            if value is not None:
                if hasattr(value, 'to_dict'):
                    result[key] = value.to_dict()
                else:
                    result[key] = value
        return result

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)


class FieldFilter:
    def __init__(self, filterItemType, fieldOperator, filterMode, filterType, values, name):
        self.filterItemType = filterItemType
        self.fieldOperator = fieldOperator
        self.filterMode = filterMode
        self.filterType = filterType
        self.values = [Value(**v) for v in values]
        self.name = name

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        result = {}
        for key, value in self.__dict__.items():
            if value is not None:
                if hasattr(value, 'to_dict'):
                    result[key] = value.to_dict()
                else:
                    result[key] = value
        return result

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)


class Criteria:
    def __init__(self, msgFilterType, isSavedFilter, fieldFilters):
        self.msgFilterType = msgFilterType
        self.isSavedFilter = isSavedFilter
        self.fieldFilters = [FieldFilter(**f) for f in fieldFilters]

    def create_extended_filter_string(self):
        filter_strings = []
        for filter_obj in self.fieldFilters:
            if filter_obj.filterItemType == 2:
                # Skip unsupported filterItemType (LISTS not available)
                continue

            value_parts = []
            for value in filter_obj.values:
                if " (REGEX " in value.displayValue:
                    actual_value = value.displayValue.split(" (REGEX ")[0]
                    value_part = f'{filter_obj.name} contains "{actual_value}"'
                else:
                    value_part = f"{filter_obj.name} = {value.displayValue}"
                value_parts.append(value_part)

            value_str = " or ".join(value_parts)
            if filter_obj.filterItemType == 1:
                value_str = f"({value_str})"
            filter_strings.append(value_str)

        operator = " and " if self.fieldFilters and self.fieldFilters[0].fieldOperator == 1 else " or "
        combined_filter_string = operator.join(filter_strings)

        return combined_filter_string

    def create_filter_for_axon_mapping(self, include_observer=False, include_unattributed=False):
        filter_strings = []
        lists_values = []
        all_operators = []

        for i, filter_obj in enumerate(self.fieldFilters):
            if filter_obj.filterItemType == 2:
                print(f"Unsupported filterItemType: {filter_obj.filterItemType}")
                continue

            mapped_keys, size = get_axon_field_for_key(filter_obj.name, include_observer=include_observer,
                                                       include_unattributed=include_unattributed)
            value_parts = []
            for mapped_key in mapped_keys:
                for value in filter_obj.values:
                    # Handle list values
                    if value.valueType == 11:
                        operator = "not in" if filter_obj.filterMode == 2 else "in"
                        value_part = f"{mapped_key} {operator} SUBLIST_{value.value['guid']}_{value.value['name']}"
                        lists_values.append(value_part)
                    elif "range" in filter_obj.name.lower():
                        start_value, end_value = value.displayValue.split(' to ')
                        value_part = f"{mapped_key} BETWEEN {start_value} AND {end_value}"
                    elif filter_obj.name in ["Classification",
                                             "MsgClass"] and value.displayValue in axon_classification_mapping:
                        mapped_value = axon_classification_mapping[value.displayValue]
                        value_part = f"{mapped_key} = {mapped_value}"
                    elif " (REGEX " in value.displayValue:
                        actual_value = value.displayValue.split(" (REGEX ")[0]
                        value_part = f'{mapped_key} contains "{actual_value}"'
                    else:
                        operator = "!=" if filter_obj.filterMode == 2 else "="
                        value_part = f"{mapped_key} {operator} {value.displayValue}"
                    value_parts.append(value_part)

            value_str = " or ".join(value_parts)
            if filter_obj.filterItemType == 2 or len(value_parts) > 2:
                value_str = f"({value_str})"

            filter_strings.append(value_str)
            all_operators.append(filter_obj.fieldOperator)

        operator_strings = ["and" if op == 1 else "or" for op in all_operators]
        combined_filter_string = " ".join(
            f"{filter_str} {op}" for filter_str, op in zip(filter_strings, operator_strings[:-1])
        )

        combined_filter_string += f" {filter_strings[-1]}"

        if self.msgFilterType == 2:
            combined_filter_string = f"({combined_filter_string})"

        return combined_filter_string, list(set(lists_values))

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        result = {}
        for key, value in self.__dict__.items():
            if value is not None:
                if hasattr(value, 'to_dict'):
                    result[key] = value.to_dict()
                else:
                    result[key] = value
        return result

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)


class DayTimeCriteria:
    def __init__(self, dateFilters, timeZoneName, timeZoneOffset):
        self.dateFilters = dateFilters
        self.timeZoneName = timeZoneName
        self.timeZoneOffset = timeZoneOffset

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        result = {}
        for key, value in self.__dict__.items():
            if value is not None:
                if hasattr(value, 'to_dict'):
                    result[key] = value.to_dict()
                else:
                    result[key] = value
        return result

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)


class StorageFormat(SimpleStruct):
    pass


class CompareOp(SimpleStruct):
    pass


class LiteralOpType(SimpleStruct):
    pass


class ExpressionType(SimpleStruct):
    pass


class DataField(SimpleStruct):
    pass


class BlockType(SimpleStruct):
    pass


class FieldRelationship:
    def __init__(self, fieldOperator, currentBlockField, priorBlockField):
        self.fieldOperator = SimpleStruct(**fieldOperator)
        self.currentBlockField = SimpleStruct(**currentBlockField)
        self.priorBlockField = SimpleStruct(**priorBlockField)

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        result = {}
        for key, value in self.__dict__.items():
            if value is not None:
                if hasattr(value, 'to_dict'):
                    result[key] = value.to_dict()
                else:
                    result[key] = value
        return result

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)


class BlockRelationship:
    def __init__(self, fieldRelationships, duration, offset, linkCriteria):
        self.fieldRelationships = [FieldRelationship(**fr) for fr in fieldRelationships] if fieldRelationships else []
        self.duration = duration
        self.offset = offset
        self.linkCriteria = linkCriteria

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        result = {}
        for key, value in self.__dict__.items():
            if value is not None:
                if hasattr(value, 'to_dict'):
                    result[key] = value.to_dict()
                else:
                    result[key] = value
        return result

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)


class BlockValue:
    def __init__(self, field, count):
        self.field = SimpleStruct(**field)
        self.count = count

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        result = {}
        for key, value in self.__dict__.items():
            if value is not None:
                if hasattr(value, 'to_dict'):
                    result[key] = value.to_dict()
                else:
                    result[key] = value
        return result

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)


class ThresholdField:
    def __init__(self, field, value):
        self.field = SimpleStruct(**field)
        self.value = value

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        result = {}
        for key, value in self.__dict__.items():
            if value is not None:
                if hasattr(value, 'to_dict'):
                    result[key] = value.to_dict()
                else:
                    result[key] = value
        return result

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)


class CommonEvent:
    def __init__(self, id, name, classification, riskRating):
        self.id = id
        self.name = name
        self.classification = classification
        self.riskRating = riskRating

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        result = {}
        for key, value in self.__dict__.items():
            if value is not None:
                if hasattr(value, 'to_dict'):
                    result[key] = value.to_dict()
                else:
                    result[key] = value
        return result

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)


class Schedule:
    def __init__(self, intervals, frequency, timeZone, useDaylightSavingsTime):
        self.intervals = intervals
        self.frequency = frequency
        self.timeZone = timeZone
        self.useDaylightSavingsTime = useDaylightSavingsTime

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        result = {}
        for key, value in self.__dict__.items():
            if value is not None:
                if hasattr(value, 'to_dict'):
                    result[key] = value.to_dict()
                else:
                    result[key] = value
        return result

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)


class Argument:
    def __init__(self, datasourceIndex=None, aieFieldName=None, aieSubField=None, index=None, compareOp=None,
                 literalOpType=None, value=None):
        self.datasourceIndex = datasourceIndex
        self.aieFieldName = aieFieldName
        self.aieSubField = aieSubField
        self.index = index
        self.compareOp = compareOp
        self.literalOpType = literalOpType
        self.value = value

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        result = {}
        for key, value in self.__dict__.items():
            if value is not None:
                if hasattr(value, 'to_dict'):
                    result[key] = value.to_dict()
                else:
                    result[key] = value
        return result

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)


class Expression:
    def __init__(self, expressions, expressionText, expressionType):
        self.expressions = [LinkCriteriaExpression(**expr) for expr in expressions]
        self.expressionText = expressionText
        self.expressionType = ExpressionType(**expressionType)

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        result = {}
        for key, value in self.__dict__.items():
            if value is not None:
                if hasattr(value, 'to_dict'):
                    result[key] = value.to_dict()
                else:
                    result[key] = value
        return result

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)


class LinkedDateBlock:
    def __init__(self, id, blockType, primaryCriteria, filterIn, filterOut, dayTimeCriteria, logSourceIds,
                 logSourceListIds, groupByFields, datasource, blockRelationship, dataFields, storageMoniker,
                 storageFormat, allowShareData, schedule=None, linkCriteria=None, collectionStart=None,
                 collectionEnd=None):
        self.collectionStart = collectionStart
        self.collectionEnd = collectionEnd
        self.id = id
        self.blockType = BlockType(blockType['id'], blockType['name'])
        self.primaryCriteria = [Criteria(**crit) for crit in primaryCriteria]
        self.filterIn = [Criteria(**fi) for fi in filterIn] if filterIn else []
        self.filterOut = [Criteria(**fi) for fi in filterOut] if filterOut else []
        self.dayTimeCriteria = DayTimeCriteria(**dayTimeCriteria) if dayTimeCriteria else None
        self.logSourceIds = logSourceIds
        self.logSourceListIds = logSourceListIds
        self.groupByFields = [SimpleStruct(**g) for g in groupByFields]
        self.datasource = datasource
        self.blockRelationship = BlockRelationship(**blockRelationship) if blockRelationship else None
        self.dataFields = [DataField(**df) for df in dataFields] if dataFields else []
        self.storageMoniker = storageMoniker
        self.storageFormat = StorageFormat(**storageFormat) if storageFormat else None
        self.allowShareData = allowShareData
        self.schedule = Schedule(**schedule) if schedule else None
        self.linkCriteria = LinkCriteria(**linkCriteria) if linkCriteria else None

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        result = {}
        for key, value in self.__dict__.items():
            if value is not None:
                if hasattr(value, 'to_dict'):
                    result[key] = value.to_dict()
                else:
                    result[key] = value
        return result

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)


class ExpressionArgument:
    def __init__(self, datasourceIndex=None, aieFieldName=None, aieSubField=None, index=None, compareOp=None,
                 literalOpType=None, value=None):
        self.datasourceIndex = datasourceIndex
        self.aieFieldName = aieFieldName
        self.aieSubField = aieSubField
        self.index = index
        self.compareOp = CompareOp(**compareOp) if compareOp else None
        self.literalOpType = LiteralOpType(**literalOpType) if literalOpType else None
        self.value = value

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        result = {}
        for key, value in self.__dict__.items():
            if value is not None:
                if hasattr(value, 'to_dict'):
                    result[key] = value.to_dict()
                else:
                    result[key] = value
        return result

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)


class LinkCriteriaExpression:
    def __init__(self, arguments, expressionType):
        self.arguments = [ExpressionArgument(**arg) for arg in arguments]
        self.expressionType = ExpressionType(**expressionType)

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        result = {}
        for key, value in self.__dict__.items():
            if value is not None:
                if hasattr(value, 'to_dict'):
                    result[key] = value.to_dict()
                else:
                    result[key] = value
        return result

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)


class LinkCriteria:
    def __init__(self, expressions, expressionText, expressionType):
        self.expressions = [LinkCriteriaExpression(**expr) for expr in expressions]
        self.expressionText = expressionText
        self.expressionType = ExpressionType(**expressionType)

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        result = {}
        for key, value in self.__dict__.items():
            if value is not None:
                if hasattr(value, 'to_dict'):
                    result[key] = value.to_dict()
                else:
                    result[key] = value
        return result

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)


class Block:
    def __init__(self, id, blockType, primaryCriteria, filterIn, filterOut, dayTimeCriteria, logSourceIds,
                 logSourceListIds, groupByFields, datasource, blockRelationship, dataFields, storageMoniker,
                 storageFormat, allowShareData, schedule=None, expression=None,
                 thresholdFields=None, booleanOperator=None, durationSeconds=None, values=None, LinkedDateBlocks=None,
                 linkedDataBlocks=None):
        self.id = id
        self.blockType = BlockType(**blockType)
        self.primaryCriteria = [Criteria(**p) for p in primaryCriteria]
        self.filterIn = [Criteria(**f) for f in filterIn] if filterIn else []
        self.filterOut = [Criteria(**f) for f in filterOut] if filterOut else []
        self.dayTimeCriteria = DayTimeCriteria(**dayTimeCriteria)
        self.logSourceIds = logSourceIds
        self.logSourceListIds = logSourceListIds
        self.groupByFields = [SimpleStruct(**g) for g in groupByFields]
        self.datasource = datasource
        self.blockRelationship = BlockRelationship(**blockRelationship)
        self.dataFields = dataFields
        self.storageMoniker = storageMoniker
        self.storageFormat = StorageFormat(**storageFormat)
        self.allowShareData = allowShareData
        self.schedule = Schedule(**schedule) if schedule else None
        self.expression = Expression(**expression) if expression else None
        self.thresholdFields = [ThresholdField(**t) for t in thresholdFields] if thresholdFields else []
        self.booleanOperator = SimpleStruct(**booleanOperator) if booleanOperator else None
        self.durationSeconds = durationSeconds
        self.values = [BlockValue(**v) for v in values] if values else []
        self.LinkedDateBlocks = [LinkedDateBlock(**ldb) for ldb in LinkedDateBlocks] if LinkedDateBlocks else []
        self.linkedDataBlocks = [LinkedDateBlock(**ldb) for ldb in linkedDataBlocks] if linkedDataBlocks else []

    def get_list_group_by_fields(self):
        return [group.name for group in self.groupByFields]

    def get_list_group_by_fields_for_axon(self):
        mapped_group_names = [axon_group_by_mapping[group.name] for group in self.groupByFields if
                              axon_group_by_mapping.get(group.name) != 'SKIP_FIELD']
        return mapped_group_names

    def get_list_unique_fields_for_axon(self):
        mapped_group_names = [axon_group_by_mapping[value.field.name] for value in self.values if
                              axon_group_by_mapping.get(value.field.name) != 'SKIP_FIELD']
        return mapped_group_names

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        result = {}
        for key, value in self.__dict__.items():
            if value is not None:
                if hasattr(value, 'to_dict'):
                    result[key] = value.to_dict()
                else:
                    result[key] = value
        return result

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)


class AIERule:
    def __init__(self, id, name, ruleGroup, description, details, alarmRule, commonEvent, supression,
                 supressionEff, permissions, runtimePriority, environmentalDependencyFactory,
                 falsePositiveProbability, accessType, eventForwardingEnabled, blocks):
        self.id = id
        self.name = name
        self.ruleGroup = ruleGroup
        self.description = description
        self.details = details
        self.alarmRule = AlarmRule(**alarmRule)
        self.commonEvent = CommonEvent(**commonEvent)
        self.supression = supression
        self.supressionEff = supressionEff
        self.permissions = SimpleStruct(**permissions)
        self.runtimePriority = SimpleStruct(**runtimePriority)
        self.environmentalDependencyFactory = SimpleStruct(**environmentalDependencyFactory)
        self.falsePositiveProbability = SimpleStruct(**falsePositiveProbability)
        self.accessType = SimpleStruct(**accessType)
        self.eventForwardingEnabled = eventForwardingEnabled
        self.blocks = [Block(**b) for b in blocks]

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        result = {}
        for key, value in self.__dict__.items():
            if value is not None:
                if hasattr(value, 'to_dict'):
                    result[key] = value.to_dict()
                else:
                    result[key] = value
        return result

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)


AIEBlockTypes = {
    'LogObserved': 1,
    'ThresholdObserved': 4,
    'UniqueValuesObserved': 7,
    # **** 22032024: Unsupported block types ****
    'LogNotObservedCompound': 2,
    'LogNotObservedScheduled': 3,
    'ThresholdNotObservedCompound': 5,
    'ThresholdNotObservedScheduled': 6,
    'UniqueValuesNotObservedCompound': 8,
    'UniqueValuesNotObservedScheduled': 9,
    'Whitelist': 10,
    'Blacklist': 11,
    'Statistical': 12,
    'Trend': 13,
    'AggregateScheduled': 21,
    'Linked_Profile': 200,
    'Linked_Trend': 201,
    'Linked_Baseline': 202,
    'Linked_File': 203,
}

AIEFilterItemType = {
    0: 'Filter',
    1: 'Group',
    2: 'PolyList'
}

AIEFieldOperator = {
    0: 'None',
    1: 'And',
    2: 'Or',
    3: 'AndPrevious',
    4: 'OrPrevious'
}

AIEFilterMode = {
    1: 'FilterIn',
    2: 'FilterOut'
}

AIEMsgFilterType = {
    'flatLegacy': 1,
    'Grouped': 2
}

lr7_list_item_data_type = ['List', 'Int32', 'String', 'PortRange', 'IP', 'IPRange']
lr7_list_item_type = ['List', 'KnownService', 'Classification', 'CommonEvent', 'KnownHost', 'IP',
                      'IPRange', 'Location', 'MsgSource', 'MsgSourceType', 'MPERule', 'Network',
                      'StringValue', 'Port', 'PortRange', 'Protocol', 'HostName', 'ADGroup', 'Entity',
                      'RootEntity', 'DomainOrigin', 'Hash', 'Policy', 'VendorInfo', 'Result', 'ObjectType',
                      'CVE', 'UserAgent', 'ParentProcessId', 'ParentProcessName', 'ParentProcessPath',
                      'SerialNumber', 'Reason', 'Status', 'ThreatId', 'ThreatName', 'SessionType',
                      'Action', 'ResponseCode', 'Identity']
lr_list_types = ['Application', 'Classification', 'CommonEvent', 'Host', 'Location', 'MsgSource',
                 'MsgSourceType', 'MPERule', 'Network', 'User', 'GeneralValue', 'Entity', 'RootEntity',
                 'IP', 'IPRange', 'Identity']
