"""Your home."""

from bson.objectid import ObjectId

from ife.init import init_regions, init_locations

init_regions.append({
    '_id': ObjectId(),
    'name': 'home',
    'connected_to': ['dreamscape stables'],
    'region': None,
    })

init_locations.append({
    '_id': ObjectId(),
    'name': 'living room',
    'region': 'home',
    'anchors': 'standard inside directions',
    'inside': True,
    })
