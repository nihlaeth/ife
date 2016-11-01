"""Everything to do with furniture."""

from ife.description import DescType, add_desc
from ife.semantics import parse_kwargs

# chairs
def long_chair(**kwargs):
    """Really look at that chair."""
    info = parse_kwargs(**kwargs)
    tokens = [info['object']['color'], info['object']['material'], "chair"]
    if info['object']['broken']:
        tokens.insert(0, "broken")
    if info['object']['dirty'] > 50:
        tokens.insert(0, "dirty")
    return tokens

add_desc("chair", DescType.long_, long_chair)

def short_chair(**kwargs):
    """Glance at chair."""
    info = parse_kwargs(**kwargs)
    tokens = ["chair"]
    if info['object']['broken']:
        tokens.insert(0, "broken")
    return tokens


add_desc("chair", DescType.short, short_chair)

def far_chair(**kwargs):
    """Something with a chair shaped blob."""
    return ["chair"]

add_desc("chair", DescType.far, far_chair)
