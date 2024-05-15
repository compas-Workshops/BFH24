import compas
import compas_assembly
import compas_cra
import compas_dr
import compas_fd
import compas_fea2
import compas_ifc
import compas_model
import compas_notebook
import compas_occ
import compas_viewer


def check_version(package, version):
    return f"{version} => {package.__version__}  {'OK' if package.__version__ == version else 'ERROR'}"


print(f"compas          : {check_version(compas, '2.1.1')}")
print(f"compas_assembly : {check_version(compas_assembly, '0.7.1')}")
print(f"compas_cra      : {check_version(compas_cra, '0.4.0')}")
print(f"compas_dr       : {check_version(compas_dr, '0.3.1')}")
print(f"compas_fd       : {check_version(compas_fd, '0.5.1')}")
print(f"compas_fea2     : {check_version(compas_fea2, '0.2.0')}")
print(f"compas_ifc      : {check_version(compas_ifc, '0.4.0')}")
print(f"compas_model    : {check_version(compas_model, '0.4.3')}")
print(f"compas_notebook : {check_version(compas_notebook, '0.6.1')}")
print(f"compas_occ      : {check_version(compas_occ, '1.1.0')}")
print(f"compas_viewer   : {check_version(compas_viewer, '1.1.4')}")
