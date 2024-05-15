import pathlib

import compas
from compas.colors import Color
from compas.datastructures import Mesh
from compas.geometry import Brep
from compas.geometry import Point
from compas.geometry import Vector
from compas.geometry import offset_polygon
from compas.itertools import pairwise
from compas.tolerance import Tolerance
from compas_viewer import Viewer

# ==============================================================================
# Define the data files
# ==============================================================================

here = pathlib.Path(__file__).parent
sessionpath = here / "data" / "session.json"

# ==============================================================================
# Import the session
# ==============================================================================

session = compas.json_load(sessionpath)

# ==============================================================================
# Load the cablemesh from the work session
# ==============================================================================

cablemesh: Mesh = session["cablemesh"]
shell: Mesh = session["shell"]

params = session["params"]

cablemesh.scale(1e3)
shell.scale(1e3)

# ==============================================================================
# Make an intrados
# ==============================================================================

idos: Mesh = cablemesh.copy()

for vertex in idos.vertices():
    point = cablemesh.vertex_point(vertex)
    normal = cablemesh.vertex_normal(vertex)
    idos.vertex_attributes(vertex, "xyz", point + normal * (-params["shell"] * 1e3))

# =============================================================================
# Blocks
# =============================================================================

boxes = []

for face in idos.faces():
    # vertices of the face
    vertices = idos.face_vertices(face)

    # coordinates and normals of the face vertices
    points = [Point(*idos.vertex_coordinates(vertex)) for vertex in vertices]
    normals = [Vector(*idos.vertex_normal(vertex)) for vertex in vertices]

    # bottom face of the box as an inward offset of the face polygon
    bottom = [Point(*point) for point in offset_polygon(points, distance=0.5 * params["ribs"] * 1e3)]

    # additional offset to create tapering
    inset = [Point(*point) for point in offset_polygon(points, distance=1.0 * params["ribs"] * 1e3)]

    # top face of the box
    top = [point + normal * params["thickness"] * 1e3 for point, normal in zip(inset, normals)]

    # box sides
    bottomloop = bottom + bottom[:1]
    toploop = top + top[:1]
    sides = []
    for (a, b), (aa, bb) in zip(pairwise(bottomloop[::-1]), pairwise(toploop[::-1])):
        sides.append([a, aa, bb, b])

    # box mesh from polygons
    polygons = [bottom[::-1], top] + sides
    box = Mesh.from_polygons(polygons)
    brep = Brep.from_mesh(box)
    boxes.append(brep)

# ==============================================================================
# Waffle
# ==============================================================================

A = Brep.from_mesh(shell)
A = A - boxes[:220]

waffle = A

filepath = here / "data" / "waffle.stp"
waffle.to_step(filepath)

# ==============================================================================
# Add the intrados to the session
# ==============================================================================

# ==============================================================================
# Export
# ==============================================================================

# compas.json_dump(session, sessionpath)

# ==============================================================================
# Viz
# ==============================================================================

tolerance = Tolerance()
tolerance.lineardeflection = 1

viewer = Viewer()

viewer.renderer.camera.near = 1e0
viewer.renderer.camera.far = 1e5
viewer.renderer.camera.pan_delta = 100
viewer.renderer.config.gridsize = (20000, 20, 20000, 20)
viewer.renderer.camera.target = [0, 0, 2000]
viewer.renderer.camera.position = [3000, -7000, 3000]

# viewer.scene.add(session["shell"])
# viewer.scene.add(idos, facecolor=Color.blue().lightened(50), linecolor=Color.blue())

# for box in boxes:
#     viewer.scene.add(box, facecolor=Color.red().lightened(50), linecolor=Color.red())

viewer.scene.add(waffle)

viewer.show()
