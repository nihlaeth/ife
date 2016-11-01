"""Dreamscape stables."""

from bson.objectid import ObjectId

from ife.init import init_regions, init_locations

init_regions.append({
    '_id': ObjectId(),
    'name': 'dreamscape stables',
    'connected_to': ['home'],
    'region': None,
    })

init_locations.append(
    {
        '_id': ObjectId(),
        'name': 'yard',
        'region': 'dreamscape stables',
        'anchors': 'standard directions',
        'inside': False,
        },
    {
        '_id': ObjectId(),
        'name': 'pasture',
        'region': 'dreamscape stables',
        'anchors': 'standard directions',
        'inside': False,
        },
    )

