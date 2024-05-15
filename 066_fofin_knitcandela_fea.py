import pathlib

import compas
import compas_fea2
from compas.geometry import Plane
from compas_fea2.model import DeformablePart
from compas_fea2.model import ElasticIsotropic
from compas_fea2.model import Model
from compas_fea2.model import SolidSection
from compas_fea2.problem import FieldOutput
from compas_fea2.problem import LoadCombination
from compas_fea2.units import units
from compas_viewer import Viewer

compas_fea2.set_backend("compas_fea2_opensees")

units = units(system="SI_mm")

# ==============================================================================
# Define the data files
# ==============================================================================

here = pathlib.Path(__file__).parent
sessionpath = here / "data" / "session.json"

# ==============================================================================
# Import the session
# ==============================================================================

session = compas.json_load(sessionpath)

# =============================================================================
# Model
# =============================================================================

model = Model()

material = ElasticIsotropic(E=30 * units("GPa"), v=0.17, density=2350 * units("kg/m**3"))
section = SolidSection(material=material)

filepath = str(here / "waffle.stp")
part = DeformablePart.from_step_file(filepath, section=section, meshsize_max=600)
model.add_part(part)

nodes = model.find_nodes_on_plane(plane=Plane.worldXY(), tolerance=1)
model.add_pin_bc(nodes=nodes)

model.summary()

# =============================================================================
# Problem
# =============================================================================

problem = model.add_problem(name="SLS")

step = problem.add_static_step()
step.combination = LoadCombination.SLS()

step.add_gravity_load_pattern([part], g=9.81 * units("m/s**2"), load_case="DL")

step.add_output(FieldOutput(node_outputs=["U", "RF"], element_outputs=["S3D"]))

# =============================================================================
# Analysis
# =============================================================================

tmp = str(here / "__temp/tmp")

model.analyse_and_extract(problems=[problem], path=tmp, VERBOSE=True)

disp_sls = problem.displacement_field
stress_sls = problem.stress_field
reactions_sls = problem.reaction_field

for result in stress_sls.results():
    point = result.location.reference_point
    for item in result.principal_stresses:
        vector = item[1]
        print(vector)

# Show Results
# cmap = ColorMap.from_palette("davos")
# problem.show_stress_contours(
#     stress_type="smax",
#     draw_reactions=0.01,
#     draw_loads=0.05,
#     draw_bcs=0.5,
#     cmap=cmap,
#     bound=[-0.5, 3.5],
# )
# problem.show_elements_field_vector(stress_sls, vector_sf=100, draw_bcs=0.5)
# problem.show_nodes_field_vector(disp_sls, scale_factor=500, draw_bcs=0.5, draw_loads=1)
# problem.show_deformed(scale_factor=100, draw_bcs=0.5, draw_loads=1)

# ==============================================================================
# Export
# ==============================================================================

# compas.json_dump(session, sessionpath)

# ==============================================================================
# Viz
# ==============================================================================

# viewer = Viewer()

# viewer.renderer.camera.near = 1e0
# viewer.renderer.camera.far = 1e5
# viewer.renderer.camera.pan_delta = 100
# viewer.renderer.config.gridsize = (20000, 20, 20000, 20)
# viewer.renderer.camera.target = [0, 0, 2000]
# viewer.renderer.camera.position = [3000, -7000, 3000]

# # viewer.scene.add(meshmodel)

# viewer.show()
