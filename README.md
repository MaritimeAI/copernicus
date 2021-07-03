# ESA Copernicus Open Access Hub module

## Install

```shell
pip install git+https://github.com/MaritimeAI/copernicus
```

## Examples

### Search

```python
import os

from copernicus import Config
from copernicus import DataHub
from copernicus import Polygons

os.environ['COPERNICUS_USERNAME'] = "i-am-the-user"
os.environ['COPERNICUS_PASSWORD'] = "it's-a-secret"

# Load config from file and initialize DataHub instance
config = Config.load('config.yaml')
data_hub = DataHub(config, limit=1000)

# Load region of interest from GeoJSON as polygon
polygon, properties = Polygons.read_geojson('area_of_interest.geojson')

# Search for products using the area polygon
snapshots = data_hub.search(config.search, area=polygon)

# Sort search results by snapshot start time
snapshots = sorted(snapshots,
                   key=lambda item: item.begin_position)

# Print each snapshot by its name (title)
for snapshot in snapshots:
    print(snapshot.title) 
```

### Download

```python
from copernicus import Config
from copernicus import DataHub
from copernicus import download

# Load config from file and initialize DataHub instance
config = Config.load('config.yaml', username="i-am-the-user",
                     password="it's-a-secret")
data_hub = DataHub(config)

# Search for products using the area polygon
snapshots = data_hub.search(config.search)

# Set output directory to dwonload snapshots to
config.output = 'snapshots'

# Download the first found snapshot
download(snapshots[0].link)
```
