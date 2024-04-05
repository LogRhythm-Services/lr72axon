import json
import uuid
from enum import Enum


class AxonRule:
    def __init__(self, title, description, version=3, observationPipeline=None):
        self.title = title
        self.version = version
        self.description = description
        self.observationPipeline = observationPipeline if isinstance(observationPipeline, ObservationPipeline) else ObservationPipeline(**observationPipeline) if observationPipeline else None

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        """Convert the object to a dictionary, filtering out None values and handling nested objects and lists."""
        result = {}
        for key, value in self.__dict__.items():
            if value is None:
                continue
            if hasattr(value, 'to_dict'):
                result[key] = value.to_dict()
            elif isinstance(value, list):
                result[key] = [item.to_dict() if hasattr(item, 'to_dict') else item for item in value]
            else:
                result[key] = value
        return result

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)

    def __repr__(self):
        return json.dumps(self.to_dict(), indent=4)


class ObservationPipeline:
    def __init__(self, pattern, commonEvents, metadataFields=None, suppressionConfig=None):
        self.pattern = pattern if isinstance(pattern, Pattern) else Pattern(**pattern)
        self.commonEvents = commonEvents
        self.metadataFields = metadataFields
        self.suppressionConfig = SuppressionConfig(**suppressionConfig) if suppressionConfig else None

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        """Convert the object to a dictionary, filtering out None values and handling nested objects and lists."""
        result = {}
        for key, value in self.__dict__.items():
            if value is None:
                continue
            if hasattr(value, 'to_dict'):
                result[key] = value.to_dict()
            elif isinstance(value, list):
                result[key] = [item.to_dict() if hasattr(item, 'to_dict') else item for item in value]
            else:
                result[key] = value
        return result

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)

    def __repr__(self):
        return json.dumps(self.to_dict(), indent=4)


class Pattern:
    def __init__(self, operations, afterMatchSkipStrategy="SKIP_PAST_LAST_EVENT"):
        if isinstance(operations, list) and all(isinstance(item, Operation) for item in operations):
            self.operations = operations
        else:
            self.operations = [Operation(**item) if isinstance(item, dict) else item for item in operations]
        self.afterMatchSkipStrategy = afterMatchSkipStrategy

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        """Convert the object to a dictionary, filtering out None values and handling nested objects and lists."""
        result = {}
        for key, value in self.__dict__.items():
            if value is None:
                continue
            if hasattr(value, 'to_dict'):
                result[key] = value.to_dict()
            elif isinstance(value, list):
                result[key] = [item.to_dict() if hasattr(item, 'to_dict') else item for item in value]
            else:
                result[key] = value
        return result

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)

    def __repr__(self):
        return json.dumps(self.to_dict(), indent=4)


class Operation:
    def __init__(self, operationType, touched=True, isOutOfBoxRule=False, blockType=None, logObserved=None,
                 countThresholdObserved=None, countUniqueValuesObserved=None,
                 ruleTuningOperation=None, seconds=None, ruleElementKey=None):
        self.touched = touched
        self.operationType = operationType
        self.isOutOfBoxRule = isOutOfBoxRule
        self.blockType = blockType
        self.logObserved = logObserved if isinstance(logObserved, LogObserved) else LogObserved(**logObserved) if logObserved else None
        self.countThresholdObserved = countThresholdObserved if isinstance(countThresholdObserved, CountThresholdObserved) else CountThresholdObserved(**countThresholdObserved) if countThresholdObserved else None
        self.countUniqueValuesObserved = countUniqueValuesObserved if isinstance(countUniqueValuesObserved, CountUniqueValuesObserved) else CountUniqueValuesObserved(**countUniqueValuesObserved) if countUniqueValuesObserved else None
        self.ruleTuningOperation = ruleTuningOperation if isinstance(ruleTuningOperation, RuleTuningOperation) else RuleTuningOperation(**ruleTuningOperation) if ruleTuningOperation else None
        self.seconds = seconds
        self.ruleElementKey = ruleElementKey

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        """Convert the object to a dictionary, filtering out None values and handling nested objects and lists."""
        result = {}
        for key, value in self.__dict__.items():
            if value is None:
                continue
            if hasattr(value, 'to_dict'):
                result[key] = value.to_dict()
            elif isinstance(value, list):
                result[key] = [item.to_dict() if hasattr(item, 'to_dict') else item for item in value]
            else:
                result[key] = value
        return result

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)

    def __repr__(self):
        return json.dumps(self.to_dict(), indent=4)


class LogObserved:
    def __init__(self, filter, groupByFields):
        self.filter = filter
        self.groupByFields = groupByFields

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        """Convert the object to a dictionary, filtering out None values and handling nested objects and lists."""
        result = {}
        for key, value in self.__dict__.items():
            if value is None:
                continue
            if hasattr(value, 'to_dict'):
                result[key] = value.to_dict()
            elif isinstance(value, list):
                result[key] = [item.to_dict() if hasattr(item, 'to_dict') else item for item in value]
            else:
                result[key] = value
        return result

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)

    def __repr__(self):
        return json.dumps(self.to_dict(), indent=4)


class CountUniqueValuesObserved:
    def __init__(self, filter, threshold, groupByFields, windowSeconds, uniqueValueFields):
        self.filter = filter
        self.threshold = threshold
        self.groupByFields = groupByFields
        self.windowSeconds = windowSeconds
        self.uniqueValueFields = uniqueValueFields

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        """Convert the object to a dictionary, filtering out None values and handling nested objects and lists."""
        result = {}
        for key, value in self.__dict__.items():
            if value is None:
                continue
            if hasattr(value, 'to_dict'):
                result[key] = value.to_dict()
            elif isinstance(value, list):
                result[key] = [item.to_dict() if hasattr(item, 'to_dict') else item for item in value]
            else:
                result[key] = value
        return result

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)

    def __repr__(self):
        return json.dumps(self.to_dict(), indent=4)


class CountThresholdObserved:
    def __init__(self, filter, threshold, groupByFields, windowSeconds):
        self.filter = filter
        self.threshold = threshold
        self.groupByFields = groupByFields
        self.windowSeconds = windowSeconds

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        """Convert the object to a dictionary, filtering out None values and handling nested objects and lists."""
        result = {}
        for key, value in self.__dict__.items():
            if value is None:
                continue
            if hasattr(value, 'to_dict'):
                result[key] = value.to_dict()
            elif isinstance(value, list):
                result[key] = [item.to_dict() if hasattr(item, 'to_dict') else item for item in value]
            else:
                result[key] = value
        return result

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)

    def __repr__(self):
        return json.dumps(self.to_dict(), indent=4)


class RuleTuningOperation:
    def __init__(self, threshold, windowSeconds, inclusionFilter):
        self.threshold = threshold
        self.windowSeconds = windowSeconds
        self.inclusionFilter = inclusionFilter

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        """Convert the object to a dictionary, filtering out None values and handling nested objects and lists."""
        result = {}
        for key, value in self.__dict__.items():
            if value is None:
                continue
            if hasattr(value, 'to_dict'):
                result[key] = value.to_dict()
            elif isinstance(value, list):
                result[key] = [item.to_dict() if hasattr(item, 'to_dict') else item for item in value]
            else:
                result[key] = value
        return result

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)

    def __repr__(self):
        return json.dumps(self.to_dict(), indent=4)


class SuppressionConfig:
    def __init__(self, enabled, groupByFields, windowSeconds):
        self.enabled = enabled
        self.groupByFields = groupByFields
        self.windowSeconds = windowSeconds

    @staticmethod
    def from_milliseconds(suppression_milliseconds, group_by_fields):
        """
        Create a SuppressionConfig object from a suppression value in milliseconds.
        """
        if suppression_milliseconds == 0:
            return SuppressionConfig(enabled=False, groupByFields=group_by_fields, windowSeconds=0)
        else:
            window_seconds = suppression_milliseconds // 1000  # Convert milliseconds to seconds
            return SuppressionConfig(enabled=True, groupByFields=group_by_fields, windowSeconds=window_seconds)

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        """Convert the object to a dictionary, filtering out None values and handling nested objects and lists."""
        result = {}
        for key, value in self.__dict__.items():
            if value is None:
                continue
            if hasattr(value, 'to_dict'):
                result[key] = value.to_dict()
            elif isinstance(value, list):
                result[key] = [item.to_dict() if hasattr(item, 'to_dict') else item for item in value]
            else:
                result[key] = value
        return result

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)

    def __repr__(self):
        return json.dumps(self.to_dict(), indent=4)


# Classes needed for the Axon List Management API
class ListColumnType(Enum):
    STRING = "STRING",
    LONG_TEXT = "LONG_TEXT",
    INTEGER = "INTEGER",
    DATE = "DATE",
    GEO_POINT = "GEO_POINT",
    IP = "IP"


class ListColumn:
    def __init__(self, title, description, type_value):
        self.title = title
        self.description = description
        self.type = type_value
        self.id = str(uuid.uuid4())

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        """Convert the object to a dictionary, filtering out None values and handling nested objects and lists."""
        result = {}
        for key, value in self.__dict__.items():
            if value is None:
                continue
            if hasattr(value, 'to_dict'):
                result[key] = value.to_dict()
            elif isinstance(value, list):
                result[key] = [item.to_dict() if hasattr(item, 'to_dict') else item for item in value]
            else:
                result[key] = value
        return result

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)

    def __repr__(self):
        return json.dumps(self.to_dict(), indent=4)


class ListDefinition:
    def __init__(self, title, description, columns: list[ListColumn]):
        self.title = title
        self.description = description
        self.columns = columns

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        """Convert the object to a dictionary, filtering out None values and handling nested objects and lists."""
        result = {}
        for key, value in self.__dict__.items():
            if value is None:
                continue
            if hasattr(value, 'to_dict'):
                result[key] = value.to_dict()
            elif isinstance(value, list):
                result[key] = [item.to_dict() if hasattr(item, 'to_dict') else item for item in value]
            else:
                result[key] = value
        return result

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)

    def __repr__(self):
        return json.dumps(self.to_dict(), indent=4)


class ListItem:
    def __init__(self, column_id, value, operationType="ADD"):
        self.value = {column_id: value}
        self.operationType = operationType

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        """Convert the object to a dictionary, filtering out None values and handling nested objects and lists."""
        result = {}
        for key, value in self.__dict__.items():
            if value is None:
                continue
            if hasattr(value, 'to_dict'):
                result[key] = value.to_dict()
            elif isinstance(value, list):
                result[key] = [item.to_dict() if hasattr(item, 'to_dict') else item for item in value]
            else:
                result[key] = value
        return result

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)

    def __repr__(self):
        return json.dumps(self.to_dict(), indent=4)


class AxonListPayload:
    def __init__(self, listDefinition: ListDefinition, listItems: list[ListItem]):
        self.listDefinition = listDefinition
        self.listItems = listItems

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        """Convert the object to a dictionary, filtering out None values and handling nested objects and lists."""
        result = {}
        for key, value in self.__dict__.items():
            if value is None:
                continue
            if hasattr(value, 'to_dict'):
                result[key] = value.to_dict()
            elif isinstance(value, list):
                result[key] = [item.to_dict() if hasattr(item, 'to_dict') else item for item in value]
            else:
                result[key] = value
        return result

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)

    def __repr__(self):
        return json.dumps(self.to_dict(), indent=4)
