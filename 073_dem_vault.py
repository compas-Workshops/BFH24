import pathlib

import compas
from compas_assembly.geometry import Arch
from compas_model.algorithms import blockmodel_interfaces

# from compas_model.analysis import cra_penalty_solve
from compas_model.elements import BlockElement
from compas_model.models import Model
from compas_model.viewers import BlockModelViewer

# =============================================================================
# Block model
# =============================================================================

template = Arch(rise=3, span=10, thickness=0.12, depth=0.5, n=30)

model = Model()

for block in template.blocks():
    model.add_element(BlockElement(shape=block))

# =============================================================================
# Interfaces
# =============================================================================

blockmodel_interfaces(model, amin=0.01)

# =============================================================================
# Boundary Conditions
# =============================================================================

elements: list[BlockElement] = sorted(model.elements(), key=lambda e: e.geometry.centroid().z)[:2]

for element in elements:
    element.is_support = True

# =============================================================================
# Equilibrium
# =============================================================================

# cra_penalty_solve(model)

# =============================================================================
# Export
# =============================================================================

here = pathlib.Path(__file__).parent
compas.json_dump(model, here / "blockmodel_arch.json")

# =============================================================================
# Viz
# =============================================================================

viewer = BlockModelViewer()
viewer.scene.add(model, show_blockfaces=False, show_interfaces=True, show_contactforces=True)
viewer.show()
