class OperationConflictError(Exception):
	"""Raise when both URL and JSON params are passed"""
	pass


class SpecificURLError(Exception):
	"""Raised with the specified URL isn't passed"""
	pass

