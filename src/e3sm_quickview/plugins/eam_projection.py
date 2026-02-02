import time as time_module

from paraview.simple import *
from paraview.util.vtkAlgorithm import *
from vtkmodules.numpy_interface import dataset_adapter as dsa
from vtkmodules.vtkCommonCore import vtkPoints
from vtkmodules.vtkCommonDataModel import (
    vtkPolyData,
    vtkCellArray,
    vtkPlane,
)
from vtkmodules.vtkCommonTransforms import vtkTransform
from vtkmodules.vtkFiltersCore import vtkAppendFilter
from vtkmodules.vtkFiltersGeneral import (
    vtkTransformFilter,
    vtkTableBasedClipDataSet,
)

try:
    from paraview.modules.vtkPVVTKExtensionsFiltersGeneral import vtkPVClipDataSet
    from paraview.modules.vtkPVVTKExtensionsMisc import vtkPVBox
except Exception as e:
    print(e)
from vtkmodules.util import vtkConstants, numpy_support
from vtkmodules.util.vtkAlgorithm import VTKPythonAlgorithmBase
from paraview import print_error

import math

try:
    import numpy as np
    import warnings
    from pyproj import Proj, Transformer

    warnings.filterwarnings("ignore", category=FutureWarning, module="pyproj")
    _has_deps = True
except ImportError as ie:
    print_error(
        "Missing required Python modules/packages. Algorithms in this module may "
        "not work as expected! \n {0}".format(ie)
    )
    _has_deps = False


def ProcessPoint(point, radius):
    # theta = math.radians(point[0] - 180.)
    # phi   = math.radians(point[1])
    # rho   = 1.0
    theta = point[0]
    phi = 90 - point[1]
    rho = (1000 - point[2]) + radius if not point[2] == 0 else radius
    x = rho * math.sin(math.radians(phi)) * math.cos(math.radians(theta))
    y = rho * math.sin(math.radians(phi)) * math.sin(math.radians(theta))
    z = rho * math.cos(math.radians(phi))
    return [x, y, z]


@smproxy.filter()
@smproperty.input(name="Input")
@smdomain.datatype(
    dataTypes=["vtkUnstructuredGrid", "vtkPolyData"], composite_data_supported=False
)
class EAMSphere(VTKPythonAlgorithmBase):
    def __init__(self):
        super().__init__(
            nInputPorts=1, nOutputPorts=1, outputType="vtkUnstructuredGrid"
        )
        self.__Dims = -1
        self.isData = False
        self.radius = 2000

    @smproperty.intvector(name="Data Layer", default_values=[0])
    @smdomain.xml(
        """<BooleanDomain name="bool"/>
        """
    )
    def SetDataLayer(self, isData_):
        if not self.isData == isData_:
            self.isData = isData_
            self.Modified()

    def RequestDataObject(self, request, inInfo, outInfo):
        inData = self.GetInputData(inInfo, 0, 0)
        outData = self.GetOutputData(outInfo, 0)
        assert inData is not None
        if outData is None or (not outData.IsA(inData.GetClassName())):
            outData = inData.NewInstance()
            outInfo.GetInformationObject(0).Set(outData.DATA_OBJECT(), outData)
        return super().RequestDataObject(request, inInfo, outInfo)

    def RequestData(self, request, inInfo, outInfo):
        inData = self.GetInputData(inInfo, 0, 0)
        outData = self.GetOutputData(outInfo, 0)

        if inData.IsA("vtkPolyData"):
            afilter = vtkAppendFilter()
            afilter.AddInputData(inData)
            afilter.Update()
            afilter.GetOutput()
            outData.DeepCopy(afilter.GetOutput())
        else:
            outData.DeepCopy(inData)

        inWrap = dsa.WrapDataObject(inData)
        outWrap = dsa.WrapDataObject(outData)

        inPoints = np.array(inWrap.Points)
        pRadius = (self.radius + 1) if self.isData else self.radius
        outPoints = np.array(list(map(lambda x: ProcessPoint(x, pRadius), inPoints)))

        _coords = numpy_support.numpy_to_vtk(
            outPoints, deep=True, array_type=vtkConstants.VTK_FLOAT
        )
        vtk_coords = vtkPoints()
        vtk_coords.SetData(_coords)
        outWrap.SetPoints(vtk_coords)

        return 1


@smproxy.filter()
@smproperty.input(name="Input")
@smdomain.datatype(
    dataTypes=["vtkUnstructuredGrid", "vtkPolyData"], composite_data_supported=False
)
class EAMVTSSphere(VTKPythonAlgorithmBase):
    def __init__(self):
        super().__init__(nInputPorts=1, nOutputPorts=1)
        self.__Dims = -1
        self.isData = False
        self.radius = 2000

    @smproperty.intvector(name="Data Layer", default_values=[0])
    @smdomain.xml(
        """<BooleanDomain name="bool"/>
        """
    )
    def SetDataLayer(self, isData_):
        if not self.isData == isData_:
            self.isData = isData_
            self.Modified()

    def RequestDataObject(self, request, inInfo, outInfo):
        inData = self.GetInputData(inInfo, 0, 0)
        outData = self.GetOutputData(outInfo, 0)
        assert inData is not None
        if outData is None or (not outData.IsA(inData.GetClassName())):
            outData = inData.NewInstance()
            outInfo.GetInformationObject(0).Set(outData.DATA_OBJECT(), outData)
        return super().RequestDataObject(request, inInfo, outInfo)

    def RequestData(self, request, inInfo, outInfo):
        inData = self.GetInputData(inInfo, 0, 0)
        outData = self.GetOutputData(outInfo, 0)
        outData.DeepCopy(inData)

        inWrap = dsa.WrapDataObject(inData)
        outWrap = dsa.WrapDataObject(outData)

        inPoints = np.array(inWrap.Points)
        pRadius = (self.radius + 1) if self.isData else self.radius
        outPoints = np.array(list(map(lambda x: ProcessPoint(x, pRadius), inPoints)))
        # outPoints   = np.array(list(map(ProcessPoint,inPoints)))

        _coords = numpy_support.numpy_to_vtk(
            outPoints, deep=True, array_type=vtkConstants.VTK_FLOAT
        )
        vtk_coords = vtkPoints()
        vtk_coords.SetData(_coords)
        outWrap.SetPoints(vtk_coords)

        return 1


@smproxy.source(name="EAMLineSource")
@smproperty.xml(
    """
                <IntVectorProperty name="longitude"
                    command="SetLongitude"
                    number_of_elements="1"
                    default_values="0">
                </IntVectorProperty>
                """
)
class EAMLineSource(VTKPythonAlgorithmBase):
    def __init__(self):
        VTKPythonAlgorithmBase.__init__(
            self, nInputPorts=0, nOutputPorts=1, outputType="vtkPolyData"
        )
        self.longitude = 0

    def RequestInformation(self, request, inInfo, outInfo):
        return super().RequestInformation(request, inInfo, outInfo)

    def RequestUpdateExtent(self, request, inInfo, outInfo):
        return super().RequestUpdateExtent(request, inInfo, outInfo)

    def SetLongitude(self, long_):
        self.longitude = long_
        self.Modified()

    def RequestData(self, request, inInfo, outInfo):
        x = self.longitude
        y = list(range(-90, 91, 1))
        points = vtkPoints()
        for i in y:
            # Add points to the vtkPoints object
            points.InsertNextPoint(x, i, 0)
        # Create a vtkCellArray to define the connectivity of the polyline
        line = vtkCellArray()
        line.InsertNextCell(len(y))  # 4 is the number of points in the polyline
        for i in range(len(y)):
            line.InsertCellPoint(i)
        # Create a vtkPolyData object to hold the points and the polyline
        polyData = vtkPolyData.GetData(outInfo, 0)
        polyData.SetPoints(points)
        polyData.SetLines(line)
        return 1


@smproxy.filter()
@smproperty.input(name="Input")
@smdomain.datatype(
    dataTypes=["vtkPolyData", "vtkUnstructuredGrid"], composite_data_supported=False
)
@smproperty.xml(
    """
                <IntVectorProperty name="Translate"
                      command="SetTranslation"
                      number_of_elements="1"
                      default_values="0">
                    <BooleanDomain name="bool"/>
                 </IntVectorProperty>
                 <IntVectorProperty
                    name="Projection"
                    command="SetProjection"
                    number_of_elements="1"
                    default_values="0">
                    <EnumerationDomain name="enum">
                        <Entry value="0" text="Cyl. Equidistant"/>
                        <Entry value="1" text="Robinson"/>
                        <Entry value="2" text="Mollweide"/>
                    </EnumerationDomain>
                </IntVectorProperty>
                """
)
class EAMProject(VTKPythonAlgorithmBase):
    def __init__(self):
        super().__init__(
            nInputPorts=1, nOutputPorts=1, outputType="vtkUnstructuredGrid"
        )
        self.__Dims = -1
        self.project = 0
        self.translate = False

    def SetTranslation(self, translate):
        if self.translate != translate:
            self.translate = translate
            self.Modified()

    def SetProjection(self, project):
        if self.project != int(project):
            self.project = int(project)
            self.Modified()

    def RequestData(self, request, inInfo, outInfo):
        t_start = time_module.perf_counter()
        inData = self.GetInputData(inInfo, 0, 0)
        outData = self.GetOutputData(outInfo, 0)
        
        t0 = time_module.perf_counter()
        if inData.IsA("vtkPolyData"):
            afilter = vtkAppendFilter()
            afilter.AddInputData(inData)
            afilter.Update()
            outData.DeepCopy(afilter.GetOutput())
        else:
            outData.DeepCopy(inData)
        print(f"    [EAMProject] DeepCopy: {time_module.perf_counter() - t0:.2f}s")

        if self.project == 0:
            print(f"    [EAMProject] Total (no proj): {time_module.perf_counter() - t_start:.2f}s")
            return 1

        inWrap = dsa.WrapDataObject(inData)
        outWrap = dsa.WrapDataObject(outData)
        inPoints = np.array(inWrap.Points)

        t0 = time_module.perf_counter()
        flat = inPoints.flatten()
        x = flat[0::3] - 180.0 if self.translate else flat[0::3]
        y = flat[1::3]

        try:
            # Use proj4 string for WGS84 instead of EPSG code to avoid database dependency
            latlon = Proj(proj="latlong", datum="WGS84")
            if self.project == 1:
                proj = Proj(proj="robin")
            elif self.project == 2:
                proj = Proj(proj="moll")
            else:
                # Should not reach here, but return without transformation
                return 1

            xformer = Transformer.from_proj(latlon, proj, always_xy=True)
            res = xformer.transform(x, y)
        except Exception as e:
            print(f"Projection error: {e}")
            # If projection fails, return without modifying coordinates
            return 1
        print(f"    [EAMProject] Transform: {time_module.perf_counter() - t0:.2f}s")
        
        t0 = time_module.perf_counter()
        flat[0::3] = np.array(res[0])
        flat[1::3] = np.array(res[1])

        outPoints = flat.reshape(inPoints.shape)
        _coords = numpy_support.numpy_to_vtk(
            outPoints, deep=True, array_type=vtkConstants.VTK_FLOAT
        )
        vtk_coords = vtkPoints()
        vtk_coords.SetData(_coords)
        outWrap.SetPoints(vtk_coords)
        print(f"    [EAMProject] SetPoints: {time_module.perf_counter() - t0:.2f}s")
        print(f"    [EAMProject] Total: {time_module.perf_counter() - t_start:.2f}s")

        return 1


# =============================================================================
# OPTIMIZATION: INITIAL_CLIP_ON controls whether lat/lon clipping is enabled.
# Set to False to completely disable crop feature (always skip clipping).
# Set to True to enable clipping when user crops (full range still skips).
# =============================================================================
INITIAL_CLIP_ON = True


@smproxy.filter()
@smproperty.input(name="Input")
@smdomain.datatype(
    dataTypes=["vtkPolyData", "vtkUnstructuredGrid"], composite_data_supported=False
)
@smproperty.xml(
    """
                <DoubleVectorProperty name="Longitude Range"
                      command="SetLongitudeRange"
                      number_of_elements="2"
                      default_values="-180 180">
                 </DoubleVectorProperty>
                <DoubleVectorProperty name="Latitude Range"
                      command="SetLatitudeRange"
                      number_of_elements="2"
                      default_values="-90 90">
                 </DoubleVectorProperty>
                """
)
class EAMTransformAndExtract(VTKPythonAlgorithmBase):
    def __init__(self):
        super().__init__(
            nInputPorts=1, nOutputPorts=1, outputType="vtkUnstructuredGrid"
        )
        self.project = 0
        self.longrange = [-180.0, 180.0]
        self.latrange = [-90.0, 90.0]

    def SetLongitudeRange(self, min, max):
        if self.longrange[0] != min or self.longrange[1] != max:
            self.longrange = [min, max]
            self.Modified()

    def SetLatitudeRange(self, min, max):
        if self.latrange[0] != min or self.latrange[1] != max:
            self.latrange = [min, max]
            self.Modified()

    # =========================================================================
    # OPTIMIZATION: Helper to check if clipping should be skipped
    # =========================================================================
    def _should_skip_clipping(self):
        """Returns True if clipping should be skipped (pass-through mode).
        
        Logic (Option 2):
        - Full range → always skip (fast, no clipping needed)
        - Cropped range + INITIAL_CLIP_ON=True → perform clipping
        - Cropped range + INITIAL_CLIP_ON=False → skip (disables crop feature)
        """
        # Always skip if using full range (no clipping needed)
        if (self.longrange == [-180.0, 180.0] and 
            self.latrange == [-90.0, 90.0]):
            return True
        # Only skip non-full-range if clipping is globally disabled
        if not INITIAL_CLIP_ON:
            return True
        return False

    def RequestData(self, request, inInfo, outInfo):
        t_start = time_module.perf_counter()
        inData = self.GetInputData(inInfo, 0, 0)
        outData = self.GetOutputData(outInfo, 0)
        ncells = inData.GetNumberOfCells()
        print(f"    [EAMTransformAndExtract] Input cells: {ncells:,}")

        # =====================================================================
        # OPTIMIZATION: Skip all clipping if disabled or using full range
        # This saves ~6 seconds per pipeline update on large datasets
        # =====================================================================
        if self._should_skip_clipping():
            outData.ShallowCopy(inData)
            print(f"    [EAMTransformAndExtract] SKIPPED (clip disabled or full range)")
            print(f"    [EAMTransformAndExtract] Total: {time_module.perf_counter() - t_start:.2f}s (output cells: {outData.GetNumberOfCells():,})")
            return 1

        # =====================================================================
        # CLIPPING ENABLED: Perform meridian wrap handling and lat/lon extract
        # =====================================================================
        t0 = time_module.perf_counter()
        planeL = vtkPlane()
        planeL.SetOrigin([180.0, 0.0, 0.0])
        planeL.SetNormal([-1, 0, 0])
        clipL = vtkTableBasedClipDataSet()
        clipL.SetClipFunction(planeL)
        clipL.SetInputData(inData)
        clipL.Update()
        print(f"    [EAMTransformAndExtract] clipL: {time_module.perf_counter() - t0:.2f}s")

        t0 = time_module.perf_counter()
        planeR = vtkPlane()
        planeR.SetOrigin([180.0, 0.0, 0.0])
        planeR.SetNormal([1, 0, 0])
        clipR = vtkTableBasedClipDataSet()
        clipR.SetClipFunction(planeR)
        clipR.SetInputData(inData)
        clipR.Update()
        print(f"    [EAMTransformAndExtract] clipR: {time_module.perf_counter() - t0:.2f}s")

        t0 = time_module.perf_counter()
        transFunc = vtkTransform()
        transFunc.Translate(-360, 0, 0)
        transform = vtkTransformFilter()
        transform.SetInputData(clipR.GetOutput())
        transform.SetTransform(transFunc)
        transform.Update()
        print(f"    [EAMTransformAndExtract] transform: {time_module.perf_counter() - t0:.2f}s")

        t0 = time_module.perf_counter()
        append = vtkAppendFilter()
        append.AddInputData(clipL.GetOutput())
        append.AddInputData(transform.GetOutput())
        append.Update()
        print(f"    [EAMTransformAndExtract] append: {time_module.perf_counter() - t0:.2f}s")

        t0 = time_module.perf_counter()
        box = vtkPVBox()
        box.SetReferenceBounds(
            self.longrange[0],
            self.longrange[1],
            self.latrange[0],
            self.latrange[1],
            -1.0,
            1.0,
        )
        box.SetUseReferenceBounds(True)
        extract = vtkPVClipDataSet()
        extract.SetClipFunction(box)
        extract.InsideOutOn()
        extract.ExactBoxClipOn()
        extract.SetInputData(append.GetOutput())
        extract.Update()
        print(f"    [EAMTransformAndExtract] extract: {time_module.perf_counter() - t0:.2f}s")

        outData.ShallowCopy(extract.GetOutput())
        print(f"    [EAMTransformAndExtract] Total: {time_module.perf_counter() - t_start:.2f}s (output cells: {outData.GetNumberOfCells():,})")
        return 1


@smproxy.filter()
@smproperty.input(name="Input")
@smdomain.datatype(
    dataTypes=["vtkPolyData", "vtkUnstructuredGrid"], composite_data_supported=False
)
@smproperty.xml(
    """
                <IntVectorProperty name="Center Meridian"
                      command="SetCentralMeridian"
                      number_of_elements="1"
                      default_values="0">
                 </IntVectorProperty>
                """
)
class EAMCenterMeridian(VTKPythonAlgorithmBase):
    def __init__(self):
        super().__init__(
            nInputPorts=1, nOutputPorts=1, outputType="vtkUnstructuredGrid"
        )
        self.project = 0
        self.cmeridian = 0.0

    def SetCentralMeridian(self, meridian):
        if self.cmeridian != meridian:
            self.cmeridian = meridian
            self.Modified()

    def RequestData(self, request, inInfo, outInfo):
        inData = self.GetInputData(inInfo, 0, 0)
        outData = self.GetOutputData(outInfo, 0)

        if self.cmeridian == 0:
            outData.ShallowCopy(inData)
            return 1

        split = (self.cmeridian - 180) if self.cmeridian > 0 else (self.cmeridian + 180)

        planeL = vtkPlane()
        planeL.SetOrigin([split, 0.0, 0.0])
        planeL.SetNormal([-1, 0, 0])
        clipL = vtkTableBasedClipDataSet()
        clipL.SetClipFunction(planeL)
        clipL.SetInputData(inData)
        clipL.Update()

        planeR = vtkPlane()
        planeR.SetOrigin([split, 0.0, 0.0])
        planeR.SetNormal([1, 0, 0])
        clipR = vtkTableBasedClipDataSet()
        clipR.SetClipFunction(planeR)
        clipR.SetInputData(inData)
        clipR.Update()

        transFunc = vtkTransform()
        transFunc.Translate(360, 0, 0)
        transform = vtkTransformFilter()
        transform.SetInputData(clipL.GetOutput())
        transform.SetTransform(transFunc)
        transform.Update()

        append = vtkAppendFilter()
        append.AddInputData(clipR.GetOutput())
        append.AddInputData(transform.GetOutput())
        append.Update()

        transFunc = vtkTransform()
        transFunc.Translate(-(180 + split), 0, 0)
        transform = vtkTransformFilter()
        transform.SetInputData(append.GetOutput())
        transform.SetTransform(transFunc)
        transform.Update()

        outData.ShallowCopy(transform.GetOutput())
        return 1
