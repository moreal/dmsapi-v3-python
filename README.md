# Python DMS-API

DSM-DMS api server wrapping library

## Example

```python
# Make user stay :)
from dmsapi import DMSSession
from dmsapi.api.stay import StayType

session = DMSSession('<user-id>', '<user-password>')
session.stay.apply(StayType.STAY)
```

## License

MIT

## Contribution

Welcome!!