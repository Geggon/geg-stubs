import clr

clr.AddReference("DLLs/AML.Engine")

import Aml.Engine
import Aml.Engine.CAEX
from Aml.Engine.CAEX import CAEXDocument

amldoc = CAEXDocument.New_CAEXDocument()
ih = amldoc.CAEXFile.InstanceHierarchy.Append("IH1")
