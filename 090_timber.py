import pathlib

import compas
from compas_timber.connections import LMiterJoint
from compas_timber.connections import TButtJoint
from compas_timber.connections import THalfLapJoint
from compas_timber.elements import Beam
from compas_timber.model import TimberModel
from compas_viewer.viewer import Viewer

here = pathlib.Path(__file__).parent
LINES = here / "data" / "lines.json"

# Load centerlines from file
lines = compas.json_load(LINES)

model = TimberModel()

# Add beams to model
HEIGHT = 120
WIDTH = 60
for line in lines:
    model.add_beam(Beam.from_centerline(centerline=line, height=HEIGHT, width=WIDTH))

beams = model.beams

# Assign joints - Frame - Frame
LMiterJoint.create(model, beams[5], beams[3])
LMiterJoint.create(model, beams[3], beams[4])
LMiterJoint.create(model, beams[4], beams[0])
LMiterJoint.create(model, beams[0], beams[5])

# Assign joints - Inner - Inner
THalfLapJoint.create(model, beams[2], beams[1])


# Assign joints - Frame - Inner
TButtJoint.create(model, beams[1], beams[0])
TButtJoint.create(model, beams[1], beams[3])
TButtJoint.create(model, beams[2], beams[4])

# =============================================================================
# Visualisation
# =============================================================================

viewer = Viewer()

viewer.renderer.camera.near = 1e0
viewer.renderer.camera.far = 1e5
viewer.renderer.camera.pan_delta = 100
viewer.renderer.config.gridsize = (20000, 20, 20000, 20)
viewer.renderer.camera.target = [0, 0, 1000]
viewer.renderer.camera.position = [-3000, -7000, 3000]

# draw center lines
for beam in model.beams:
    viewer.scene.add(beam.centerline, linewidth=5, show_points=True)

# draw blanks (including joinery extensions)
# for beam in model.beams:
#     viewer.scene.add(beam.blank)

# draw geometry (with features)
for beam in model.beams:
    viewer.scene.add(beam.geometry, opacity=0.3)


viewer.show()
