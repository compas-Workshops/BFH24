import pathlib

import compas
from compas.datastructures import Mesh
from compas_gmsh.models import MeshModel
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

cablemesh = session["cablemesh"]

# ==============================================================================
# Mesh Model
# ==============================================================================

# Create a model directly from the STEP file
filepath = str(here / "data" / "waffle.stp")
model = MeshModel.from_step(filepath)

# Set the maximum mesh size
model.options.mesh.meshsize_max = 100

# ==============================================================================
# Surface Mesh
# ==============================================================================

# Generate and optimize a mesh
model.generate_mesh(2)
# model.optimize_mesh(niter=10)

# Convert to a COMPAS mesh
meshmodel = model.mesh_to_compas()

# ==============================================================================
# volumetric Mesh
# ==============================================================================

# # Generate and optimize a mesh
# model.generate_mesh(3)

# # Convert to COMPAS tets
# tets = model.mesh_to_tets()

# # This is a temp hack
# tetmesh = Mesh()
# for tet in tets:
#     tetmesh.join(Mesh.from_vertices_and_faces(tet.vertices, tet.faces), weld=False)

# ==============================================================================
# Export
# ==============================================================================

# compas.json_dump(session, sessionpath)

# ==============================================================================
# Viz
# ==============================================================================

viewer = Viewer()

viewer.renderer.camera.near = 1e0
viewer.renderer.camera.far = 1e5
viewer.renderer.camera.pan_delta = 100
viewer.renderer.config.gridsize = (20000, 20, 20000, 20)
viewer.renderer.camera.target = [0, 0, 2000]
viewer.renderer.camera.position = [3000, -7000, 3000]

viewer.scene.add(meshmodel)
# viewer.scene.add(tetmesh)

viewer.show()
