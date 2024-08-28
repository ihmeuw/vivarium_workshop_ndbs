from pathlib import Path

import vivarium_workshop_ndbs
from vivarium_workshop_ndbs.constants import metadata

BASE_DIR = Path(vivarium_workshop_ndbs.__file__).resolve().parent

ARTIFACT_ROOT = Path(
    f"/mnt/team/simulation_science/pub/models/{metadata.PROJECT_NAME}/artifacts/"
)
