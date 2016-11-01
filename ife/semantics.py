"""Tools for processing sentence fragments."""

def parse_kwargs(**kwargs) -> dict:
    """Store sentence fragments in dict for action callables."""
    result = {}
    sentence_fragments = [
        'subject',
        'verb',
        'object',
        ]
    for fragment in sentence_fragments:
        result[fragment] = None if fragment not in kwargs else kwargs[fragment]

    return result
